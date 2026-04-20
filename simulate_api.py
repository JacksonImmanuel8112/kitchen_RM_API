import requests
import pandas as pd
import io

# 1. Download template
r_template = requests.get('http://127.0.0.1:8000/conversion/template')
if r_template.status_code != 200:
    print("Failed to get template")
    exit(1)

# 2. Modify template in pandas
df = pd.read_excel(io.BytesIO(r_template.content))
print("Original head:\n", df.head())

# Fill first 2 rows with Qty=5
df.loc[0, "Qty"] = 5
df.loc[1, "Qty"] = 10
print("\nModified head:\n", df.head())

# Save to bytes
output = io.BytesIO()
with pd.ExcelWriter(output, engine='openpyxl') as writer:
    df.to_excel(writer, index=False)
output.seek(0)

# 3. Post to calculate
files = {'file': ('test.xlsx', output.read(), 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
r_calc = requests.post('http://127.0.0.1:8000/conversion/calculate', files=files)

print("\nCalculate Status:", r_calc.status_code)
print("Calculate Response:", r_calc.text)
