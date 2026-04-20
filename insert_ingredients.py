from sqlalchemy import create_engine, text
from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

created_by = "system"

# Solution Category ID map
category_map = {
    "AGRO": 1,
    "Dairy": 2,
    "Horeca": 3,
    "Pantry": 4,
}

raw_data = """
AGRO	1P02	Garlic 
AGRO	P063	Cauliflower_Cleaned
AGRO	P064	Shallots_Cleaned
AGRO	P065	Corriendar_Cleaned
AGRO	P067	Lemon
AGRO	P072	Pineapple
AGRO	P075	Baby Corn
AGRO	P076	Beans
AGRO	P077	Beetroot
AGRO	P078	Bitter Gourd (Paaharkai)
AGRO	P079	Broad Beans (Avarakkai)
AGRO	P080	Cabbage
AGRO	P081	Carrot
AGRO	P082	Cluster Beans (Kothavarangai)
AGRO	P083	Coconut
AGRO	P084	Drumstick
AGRO	P085	Gherkins (Kovakkai)
AGRO	P086	Ginger
AGRO	P087	Green Chilli 
AGRO	P088	Green Peas (Frozen)
AGRO	P090	Okra
AGRO	P091	Mango(Mangai)
AGRO	P092	Onion
AGRO	P093	Plantain (Valaikkai)
AGRO	P094	Potato
AGRO	P095	Redkidney Beans (Karamani)
AGRO	P096	Colacasia
AGRO	P097	Sweet Potato
AGRO	P098	Yam (Chenai)
AGRO	P100	Celery
AGRO	P101	Curry Leaves (Karuvepillai)
AGRO	P102	Green Leaves (Sirukeerai)
AGRO	P103	Leeks
AGRO	P104	Mint Leaves
AGRO	P106	Bottle Gourd ( Suraikkai )
AGRO	P107	Brinjal - Blue
AGRO	P108	Green -Capsicum
AGRO	P109	Chow Chow
AGRO	P110	Cucumber
AGRO	P111	Peerkangai
AGRO	P112	Raddish (Mullangi)
AGRO	P114	Red Pumpkin
AGRO	P115	Snake-Guard(Pudalankai)
AGRO	P116	Tomato (Country)
AGRO	P117	Brinjal - White
AGRO	P118	Ash Gourd
AGRO	V_IP_014	Turnip
AGRO	V_IP_019	Mochchai
AGRO	V_IP_022	Mushroom
AGRO	V_IP003	Coconut Water
Dairy	1P06	Milk
Dairy	1P07	Ghee
Dairy	P001	Curd
Dairy	R_IP_004	Paneer
Dairy	R_IP_005	Butter
Horeca	P012	Briyani Masala
Horeca	P013	Brinjal gravy masala
Horeca	P014	Buttermilk Kuzhambu - Masala
Horeca	P015	Chops Masala
Horeca	P018	Kadalai Curry Masala
Horeca	P021	Meals Sambar Masala
Horeca	P022	Poori Dal Masala
Horeca	P023	Rasam Podi
Horeca	P024	Sambar Sadham Masala
Horeca	P025	Tiffin Sambar Masala
Horeca	P026	Vathakuzhambu Masala
Horeca	P027	Veg Kurma Masala
Horeca	P028	Yellow Gravy Masala
Horeca	P029	Butter Gravy Masala
Horeca	P031	Tomato Chutney Masala
Horeca	P032	Adai pradhaman paste
Horeca	P033	Briyani Paste
Horeca	P034	Brinjal gravy paste
Horeca	P035	Chops Paste
Horeca	P036	Garlic Paste
Horeca	P037	Ginger paste
Horeca	P038	Green Chilli Paste
Horeca	P039	Kadalai Curry Paste
Horeca	P040	Kesari Paste
Horeca	P041	Malli Paste
Horeca	P042	Malli Pudhina Paste
Horeca	P043	Meals Sambar Paste
Horeca	P044	Onion Paste
Horeca	P045	Parupu Payasam Paste
Horeca	P046	Poori dal Paste
Horeca	P047	Rasam Paste
Horeca	P049	Sambar Sadham Paste
Horeca	P051	Tamarind paste
Horeca	P052	Tiffin Sambar Paste
Horeca	P053	Tomato paste
Horeca	P054	Vathakuzhambu Paste
Horeca	P055	Yellow Gravy Paste
Horeca	P056	Sweet Pongal Paste
Horeca	P057	Vellam Paagu
Horeca	P120	Coconut Chutney Masala
Horeca	P121	Potato Masala Paste
Horeca	P124	Parupu Rasam Podi
Pantry	1P08	RO Water
Pantry	1P13	Javvarusi
Pantry	1P15	Raisins
Pantry	1P20	Cashew Nut - Full
Pantry	1P23	Long Red Chilli
Pantry	1P27	Raw Rice Flour
Pantry	1P29	Asafoetida Powder
Pantry	1P33	Coriander Powder
Pantry	1P34	Garam Masala
Pantry	1P37	Pepper powder
Pantry	1P38	Chilli Powder
Pantry	1P39	Tandoori Masala
Pantry	1P41	Turmeric Powder
Pantry	1P44	Maida
Pantry	1P46	Salt
Pantry	1P48	Coconut Oil
Pantry	1P49	Gingelly Oil
Pantry	1P50	Mustard Seeds
Pantry	1P51	Refined Oil
Pantry	1P53	Bengal Gram Dal
Pantry	1P56	Toor Dal
Pantry	1P57	Urad Dal
Pantry	1P58	Urad Dal Split
Pantry	1P60	Bay Leaf
Pantry	1P61	Black Pepper
Pantry	1P66	Coriander seeds
Pantry	1P67	Cumin Seeds
Pantry	1P68	Fennel Seeds
Pantry	1P69	Fenugreek
Pantry	1P71	Jeera Seeds
Pantry	R_IP_006	Appalam
Pantry	R_IP_011	Asafoetida
Pantry	R_IP_012	Jeera Powder
Pantry	R_IP_013	Kasoori Methi
Pantry	R_IP_015	Refined Sugar
Pantry	R_IP_017	White Channa
Pantry	V_IP_0011	Rava
Pantry	V_IP_005	Basmathi Rice
Pantry	V_IP_006	Boiled Rice
Pantry	V_IP_007	Raw Rice
Pantry	V_IP_009	Moong Dal
Pantry	V_IP_012	Black Channa
Pantry	V_IP_024	Bread
Pantry	V_IP_013	Red Chilly (Round)
Pantry	V_IP_015	Sundried- Manathakalli
Pantry	V_IP_016	Sundried- Sungakai
Pantry	V_IP_017	Sundried- Sundakai
Pantry	V_IP_018	Fenugreek Powder
Pantry	V_IP_020	Noodles
Pantry	V_IP_021	Peanut
Pantry	V_IP_023	Saffron Jeera
Pantry	V_IP001	Adai
Pantry	V_IP002	Elachi Powder
Pantry	V_IP004	Vermicelli
"""

# ─── Parse ────────────────────────────────────────────
insert_list = []
seen_codes = set()

for line in raw_data.strip().split("\n"):
    parts = [p.strip() for p in line.strip().split("\t")]
    if len(parts) < 3:
        continue

    category, code, name = parts[0], parts[1], parts[2]

    # ⚠️  Duplicate code warning (V_IP_013 appears twice in your data)
    if code in seen_codes:
        print(f"⚠️  Duplicate code skipped: {code} - {name}")
        continue
    seen_codes.add(code)

    solution_category_id = category_map.get(category)
    if solution_category_id is None:
        print(f"⚠️  Unknown category '{category}' for {code}, skipping")
        continue

    insert_list.append({
        "code": code,
        "name": name,
        "solution_category_id": solution_category_id,
        "is_active": 1,
        "is_deleted": 0,
        "created_by": created_by,
    })

if not insert_list:
    print("❌ No ingredients to insert, exiting.")
    exit()

print(f"📋 Total ingredients to insert: {len(insert_list)}")

# ─── Insert ───────────────────────────────────────────
query = text("""
    INSERT INTO ingredient_master (code, name, solution_category_id, is_active, is_deleted, created_by)
    VALUES (:code, :name, :solution_category_id, :is_active, :is_deleted, :created_by)
""")

with engine.connect() as conn:
    conn.execute(query, insert_list)
    conn.commit()
    print(f"✅ {len(insert_list)} ingredients inserted into ingredients_master.")
# ```

# One thing to flag — your raw data has **`V_IP_013` used twice** with two different names:
# ```
# Pantry	V_IP_013	Bread
# Pantry	V_IP_013	Red Chilly (Round)   ← duplicate code, will be skipped