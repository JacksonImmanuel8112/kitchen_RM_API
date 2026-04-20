import pandas as pd
import io
import os

data = [
    {"Solution Type": "ST1", "Product Type": "PT1", "Product Name": "P1", "Qty": None},
    {"Solution Type": "ST2", "Product Type": "PT2", "Product Name": "P2", "Qty": None}
]
df = pd.DataFrame(data)
output = io.BytesIO()
try:
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Products')
    
    excel_data = output.getvalue()
    print(f"Generated Excel size: {len(excel_data)} bytes")
    
    with open("test_template.xlsx", "wb") as f:
        f.write(excel_data)
    print("Saved test_template.xlsx locally.")
except Exception as e:
    print(f"Error: {e}")
