import pandas as pd
from sqlalchemy import create_engine, text

# 🔹 DB connection
# DATABASE_URL = "mysql+pymysql://root:12345@localhost:3306/rm_tool"

DATABASE_URL = "mysql+pymysql://root:gQeXWYcOmzuOQPIgkZrEyoRyMxODzAYK@shinkansen.proxy.rlwy.net:46699/railway"

engine = create_engine(DATABASE_URL)

# 🔹 Read Excel
file_path = "Kitchen_RM_Tool_ingredient.xlsx"  # change path
df = pd.read_excel(file_path)

# 🔹 Clean data (important)
df = df[['Code', 'Price']].dropna()
df['Code'] = df['Code'].astype(str).str.strip()
df['Price'] = df['Price'].astype(float)

# 🔹 Update query
query = text("""
    UPDATE ingredient_master
    SET price = :price
    WHERE code = :code
""")

# 🔹 Execute updates
with engine.begin() as conn:
    for _, row in df.iterrows():
        print(row['Code'])
        conn.execute(query, {
            "code": row['Code'],
            "price": row['Price']
        })

print("✅ Prices updated from Excel successfully")