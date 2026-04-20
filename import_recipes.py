import pandas as pd
from sqlalchemy import create_engine, text
from app.core.config import DATABASE_URL
import os

# Database connection
engine = create_engine(DATABASE_URL)

def get_mapping(table_name):
    query = text(f"SELECT id, name FROM {table_name}")
    with engine.connect() as conn:
        result = conn.execute(query)
        return {row.name.strip().lower(): row.id for row in result}

def import_recipes():
    file_path = "only_recipe_master.xlsx"
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    print(f"Loading data from {file_path}...")
    df = pd.read_excel(file_path)
    
    # Replace NaN with None for database compatibility
    df = df.astype(object).where(pd.notnull(df), None)

    print("Fetching product and ingredient mappings...")
    product_map = get_mapping("product_master")
    ingredient_map = get_mapping("ingredient_master")

    recipes_to_insert = []
    missing_products = set()
    missing_ingredients = set()

    for _, row in df.iterrows():
        product_name = str(row['Product']).strip().lower()
        ingredient_name = str(row['ingredient']).strip().lower()

        product_id = product_map.get(product_name)
        ingredient_id = ingredient_map.get(ingredient_name)

        if not product_id:
            missing_products.add(row['Product'])
            continue
        
        if not ingredient_id:
            missing_ingredients.add(row['ingredient'])
            continue

        recipes_to_insert.append({
            "product_id": product_id,
            "ingredient_id": ingredient_id,
            "yield_qty": row['Yield_qty'],
            "yield_uom": row['yield_UOM'],
            "qty": row['Qty'],
            "qty_uom": row['UOM'],
            "created_by": "system",
            "is_active": 1,
            "is_deleted": 0
        })

    if missing_products:
        print(f"Warning: Missing products in database: {missing_products}")
    if missing_ingredients:
        print(f"Warning: Missing ingredients in database: {missing_ingredients}")

    if not recipes_to_insert:
        print("No recipes found to insert.")
        return

    print(f"Inserting {len(recipes_to_insert)} recipe records...")
    query = text("""
        INSERT INTO recipe_master (product_id, ingredient_id, yield_qty, yield_uom, qty, qty_uom, created_by, is_active, is_deleted)
        VALUES (:product_id, :ingredient_id, :yield_qty, :yield_uom, :qty, :qty_uom, :created_by, :is_active, :is_deleted)
    """)

    with engine.connect() as conn:
        conn.execute(query, recipes_to_insert)
        conn.commit()
    
    print("Import completed successfully.")

if __name__ == "__main__":
    import_recipes()
