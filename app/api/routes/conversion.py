from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.database import SessionLocal
import pandas as pd
import io

router = APIRouter(prefix="/conversion", tags=["conversion"])


# 🔹 DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =====================================================
# 🟢 1. DOWNLOAD TEMPLATE (FIXED - NO CORRUPTION)
# =====================================================
@router.get("/template")
def get_template(db: Session = Depends(get_db)):
    """
    Generate Excel template with Product list and empty Qty
    """

    query = text("""
        SELECT 
            st.name as solution_type,
            pt.name as product_type,
            pm.name as product_name
        FROM product_master pm
        JOIN product_type pt ON pm.product_type_id = pt.id
        JOIN solution_type st ON pt.solution_type_id = st.id
        WHERE pm.is_deleted = 0 AND pm.is_active = 1
        ORDER BY st.name, pt.name, pm.name
    """)

    results = db.execute(query).fetchall()

    data = []
    for row in results:
        data.append({
            "Solution Type": row.solution_type,
            "Product Type": row.product_type,
            "Product Name": row.product_name,
            "Qty": ""
        })

    df = pd.DataFrame(data)

    # 🔥 IMPORTANT: Use BytesIO (no temp files)
    output = io.BytesIO()

    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name="Products")

    output.seek(0)

    return StreamingResponse(
        output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition": "attachment; filename=conversion_template.xlsx"
        }
    )


# =====================================================
# 🟢 2. CALCULATE INGREDIENT REQUIREMENTS
# =====================================================
@router.post("/calculate")
async def calculate_requirements(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Upload filled Excel → Calculate ingredient requirements
    """

    # 🔹 Validate file
    if not file.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(status_code=400, detail="Upload Excel file only")

    contents = await file.read()

    try:
        df = pd.read_excel(io.BytesIO(contents))
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Excel file")

    # 🔹 Validate columns
    required_cols = ["Product Name", "Qty"]
    for col in required_cols:
        if col not in df.columns:
            raise HTTPException(status_code=400, detail=f"Missing column: {col}")

    # 🔹 Filter valid rows
    df["Qty"] = pd.to_numeric(df["Qty"], errors="coerce")
    df = df[df["Qty"].notnull() & (df["Qty"] > 0)]

    if df.empty:
        return {"ingredients": [], "message": "No valid quantities provided"}

    # 🔹 Map input
    input_products = df.set_index("Product Name")["Qty"].to_dict()
    product_names = list(input_products.keys())

    # 🔹 Fetch recipes
    query = text("""
        SELECT 
            pm.name as product_name,
            im.name as ingredient_name,
            im.code as ig_code,
            sc.name as solution_category,
            rm.yield_qty,
            rm.qty as ingredient_qty,
            rm.qty_uom as uom
        FROM recipe_master rm
        JOIN product_master pm ON rm.product_id = pm.id
        JOIN ingredient_master im ON rm.ingredient_id = im.id
        LEFT JOIN ip_solution_category sc ON im.solution_category_id = sc.id
        WHERE pm.name IN :names AND rm.is_deleted = 0
    """)

    recipes = db.execute(query, {"names": tuple(product_names)}).fetchall()

    ingredient_totals = {}

    # 🔹 Calculate
    for row in recipes:
        input_qty = input_products.get(row.product_name, 0)

        if row.yield_qty is not None and float(row.yield_qty) > 0 and row.ingredient_qty is not None:
            required_qty = float(input_qty) * (
                float(row.ingredient_qty) / float(row.yield_qty)
            )

            if row.ingredient_name in ingredient_totals:
                ingredient_totals[row.ingredient_name]["qty"] += required_qty
            else:
                ingredient_totals[row.ingredient_name] = {
                    "qty": required_qty,
                    "uom": row.uom,
                    "ig_code": row.ig_code,
                    "solution_category": row.solution_category
                }

    # 🔹 Format response
    result_list = [
        {
            "solution_category": info["solution_category"] or "N/A",
            "ig_code": info["ig_code"] or "N/A",
            "ingredient_name": name,
            "quantity": round(info["qty"], 2),
            "uom": info["uom"]
        }
        for name, info in ingredient_totals.items()
    ]

    return {"ingredients": result_list}