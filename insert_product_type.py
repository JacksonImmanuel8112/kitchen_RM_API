from sqlalchemy import create_engine, text
from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

# ─── Config ───────────────────────────────────────────
created_by = "lakshman@indent.com"

solution_map = {
    "FG": 1,
    "SFG": 2
}

raw_data = """
FG	VCHP001	Ghee Pongal
FG	VCHP002	Ghee Rava Kichadi
FG	VCHP003	Tomato Chutney
FG	VCHP004	Cauliflower Chops
FG	VCHP005	Kadalai Curry
FG	VCHP006	Poori Dal
FG	VCHP007	Chole Channa
FG	VCHP008	White Veg Kurma
FG	VCHP009	Tiffin Sambar
FG	VCHP010	Kaara Dosa Masala
FG	VCHP011	Paneer Masala
FG	VCHP012	Potato Masala
FG	VCHP018	Sundals
FG	VCHP020	Adai Pradhaman
FG	VCHP020	Payasam
FG	VCHP021	Ghee Ravakesari
FG	VCHP022	Sweet pongal
FG	VCHP023	Boiled Basmathi Rice
FG	VCHP025	Boiled Noodles
FG	VCHP026	Cooked Boiled Rice
FG	VCHP027	Kathirika Gravy
FG	VCHP028	Chapathi Side dishes
FG	VCHP029	Saravana Special Biryani
FG	VCHP030	Aviyal
FG	VCHP031	Kootu
FG	VCHP032	Curd Rice
FG	VCHP033	Sambar Rice
FG	VCHP034	Poriyal
FG	VCHP035	Kuzhambu
FG	VCHP036	Meals Sambar
FG	VCHP037	Rasam
FG	VCHP046	Phulka/Naan Sidedish
SFG	VCHP013	Appam Batter
SFG	VCHP014	Vada Batters
SFG	VCHP016	Roasted Coconut Chutney Masala
SFG	VCHP017	Roasted Malli Chutney Masala
SFG	VCHP039	Soups
SFG	VCHP040	Butter gravy
SFG	VCHP041	Yellow Gravy
SFG	VCHP042	Onion Masala
SFG	VCHP043	Masala Vada Batter
SFG	VCHP044	Bonda Batter
SFG	VCHP045	Meals Vada Batters
"""

# ─── Build values list ────────────────────────────────
seen = set()
values_list = []

for line in raw_data.strip().split("\n"):
    parts = line.strip().split("\t")
    if len(parts) < 3:
        continue

    solution, code, name = parts[0].strip(), parts[1].strip(), parts[2].strip()

    if code in seen:
        print(f"⚠️  Skipping duplicate: {code} - {name}")
        continue
    seen.add(code)

    solution_id = solution_map.get(solution)
    if solution_id is None:
        print(f"⚠️  Unknown solution type '{solution}' for {code}, skipping")
        continue

    values_list.append({
        "name": name,
        "code": code,
        "solution_type_id": solution_id,
    })

# ─── Insert ───────────────────────────────────────────
if len(values_list) == 0:
    print("❌ No values to insert, exiting.")
    exit()

query = text("""
    INSERT INTO product_type (name, code, solution_type_id)
    VALUES (:name, :code, :solution_type_id)
""")

with engine.connect() as conn:
    conn.execute(query, values_list)
    conn.commit()
    print(f"✅ {len(values_list)} rows inserted successfully!")