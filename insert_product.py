from sqlalchemy import create_engine, text
from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

created_by = "system"

# PD_ID -> product_type_id
pd_to_product_type_id = {
    "VCHP001": 1,   "VCHP002": 2,   "VCHP003": 3,   "VCHP004": 4,
    "VCHP005": 5,   "VCHP006": 6,   "VCHP007": 7,   "VCHP008": 8,
    "VCHP009": 9,   "VCHP010": 10,  "VCHP011": 11,  "VCHP012": 12,
    "VCHP018": 13,  "VCHP020": 14,  "VCHP021": 15,  "VCHP022": 16,
    "VCHP023": 17,  "VCHP025": 18,  "VCHP026": 19,  "VCHP027": 20,
    "VCHP028": 21,  "VCHP029": 22,  "VCHP030": 23,  "VCHP031": 24,
    "VCHP032": 25,  "VCHP033": 26,  "VCHP034": 27,  "VCHP035": 28,
    "VCHP036": 29,  "VCHP037": 30,  "VCHP046": 31,  "VCHP013": 32,
    "VCHP014": 33,  "VCHP016": 34,  "VCHP017": 35,  "VCHP039": 36,
    "VCHP040": 37,  "VCHP041": 38,  "VCHP042": 39,  "VCHP043": 40,
    "VCHP044": 41,  "VCHP045": 42,
}

raw_data = """
1	FG	VCHP001	Ghee Pongal	VCH001	Ghee Pongal
2	FG	VCHP002	Ghee Rava Kichadi	VCH002	Ghee Rava Kichadi
3	FG	VCHP003	Tomato Chutney	VCH003	Tomato Chutney
4	FG	VCHP004	Cauliflower Chops	VCH004	Cauliflower Chops
5	FG	VCHP005	Kadalai Curry	VCH005	Kadalai Curry
6	FG	VCHP006	Poori Dal	VCH006	Poori Dal
7	FG	VCHP007	Chole Channa	VCH007	Chole Channa
8	FG	VCHP008	White Veg Kurma	VCH008	White Veg Kurma
9	FG	VCHP009	Tiffin Sambar	VCH009	Tiffin Sambar
10	FG	VCHP010	Kaara Dosa Masala	VCH010	Kaara Dosa Masala
11	FG	VCHP011	Paneer Masala	VCH011	Paneer Masala
12	FG	VCHP012	Potato Masala	VCH012	Potato Masala
13	FG	VCHP018	Sundals	VCH022	Black Channa Sundal
14	FG	VCHP018	Sundals	VCH023	White Channa Sundal
15	FG	VCHP020	Adai Pradhaman	VCH024	Adai Pradhaman
16	FG	VCHP020	Payasam	VCH025	Parupu Payasam
17	FG	VCHP020	Payasam	VCH026	Semiya Pal Payasam
18	FG	VCHP021	Ghee Ravakesari	VCH027	Ghee Ravakesari
19	FG	VCHP022	Sweet pongal	VCH028	Sweet pongal
20	FG	VCHP023	Boiled Basmathi Rice	VCH029	Boiled Basmathi Rice
21	FG	VCHP025	Boiled Noodles	VCH030	Boiled Noodles
22	FG	VCHP026	Cooked Boiled Rice	VCH031	Cooked Boiled Rice
23	FG	VCHP027	Kathirika Gravy	VCH032	Kathirika Gravy
24	FG	VCHP028	Chapathi Side dishes	VCH037	Tadka Dal
25	FG	VCHP028	Chapathi Side dishes	VCH038	Vegetable Kurma
26	FG	VCHP029	Saravana Special Biryani	VCH039	Saravana Special Biryani
27	FG	VCHP030	Aviyal	VCH040	Aviyal
28	FG	VCHP031	Kootu	VCH041	Turnip Cabbage_Kootu
29	FG	VCHP031	Kootu	VCH042	Ash gourd _Karamani Kootu
30	FG	VCHP031	Kootu	VCH043	Ash Gourd Kootu
31	FG	VCHP031	Kootu	VCH044	Ash Gourd_Ridge Gourd Kootu
32	FG	VCHP031	Kootu	VCH045	Bottle Gourd_Channa kootu
33	FG	VCHP031	Kootu	VCH046	Brinjal Kootu
34	FG	VCHP031	Kootu	VCH047	Cabbage kootu
35	FG	VCHP031	Kootu	VCH048	Cabbage_Channa Kootu
36	FG	VCHP031	Kootu	VCH049	Chow Chow_Channa Kootu
37	FG	VCHP031	Kootu	VCH050	Chow-Chow_Kootu
38	FG	VCHP031	Kootu	VCH051	Kathirikai_Kootu
39	FG	VCHP031	Kootu	VCH052	Keerai Kootu
40	FG	VCHP031	Kootu	VCH053	Knol khol Kootu
41	FG	VCHP031	Kootu	VCH054	Malabar Vellari Kootu
42	FG	VCHP031	Kootu	VCH055	Multivegies Kootu
43	FG	VCHP031	Kootu	VCH056	Potato kootu curry
44	FG	VCHP031	Kootu	VCH057	Red Pumpkin Kootu
45	FG	VCHP031	Kootu	VCH058	Senai eriseri kootu
46	FG	VCHP031	Kootu	VCH059	Senai Vazhai Potato kootu
47	FG	VCHP031	Kootu	VCH060	Snake gourd_Peanut Kootu
48	FG	VCHP031	Kootu	VCH061	Surakkai_Kootu
49	FG	VCHP032	Curd Rice	VCH062	Curd Rice
50	FG	VCHP033	Sambar Rice	VCH063	Sambar Rice
51	FG	VCHP034	Poriyal	VCH064	Avarakai Poriyal
52	FG	VCHP034	Poriyal	VCH065	Beans Poriyal
53	FG	VCHP034	Poriyal	VCH066	Beetroot- Gean Peas Poriyal
54	FG	VCHP034	Poriyal	VCH067	Cabbage - Dum Poriyal
55	FG	VCHP034	Poriyal	VCH068	Cabbage -Capsicum Poriyal
56	FG	VCHP034	Poriyal	VCH069	Cabbage -Green Peas Poriyal
57	FG	VCHP034	Poriyal	VCH070	Carrot - Beans- Cabbage Poriyal
58	FG	VCHP034	Poriyal	VCH071	Carrot - Beans Poriyal
59	FG	VCHP034	Poriyal	VCH072	Carrot - Grean Peas Poriyal
60	FG	VCHP034	Poriyal	VCH073	Lady's Finger- Poriyal
61	FG	VCHP034	Poriyal	VCH074	Scarlet Gourds( Kovakai) Poriyal
62	FG	VCHP034	Poriyal	VCH075	Snake Gourd Kadala parupu Poriyal
63	FG	VCHP034	Poriyal	VCH076	Beans Kara Curry
64	FG	VCHP034	Poriyal	VCH077	Cluster Beans Kara Curry
65	FG	VCHP034	Poriyal	VCH078	Karamani-Kara Curry
66	FG	VCHP034	Poriyal	VCH079	Plaintain - Green Peas Poriyal
67	FG	VCHP034	Poriyal	VCH080	Potato - Green Peas Poriyal
68	FG	VCHP034	Poriyal	VCH081	Potato Bun Roast
69	FG	VCHP034	Poriyal	VCH082	Sennai-Pattani - Poriyal
70	FG	VCHP034	Poriyal	VCH083	Vellai Kathiri Mochchai- Kara Curry
71	FG	VCHP035	Kuzhambu	VCH084	Buttermilk Kuzhambu - Chow Chow
72	FG	VCHP035	Kuzhambu	VCH085	Buttermilk Kuzhambu - Colocasia
73	FG	VCHP035	Kuzhambu	VCH086	Buttermilk Kuzhambu - Okra
74	FG	VCHP035	Kuzhambu	VCH087	Buttermilk Kuzhambu -White Pumpkin
75	FG	VCHP035	Kuzhambu	VCH106	Appalam Vathakuzhambu
76	FG	VCHP035	Kuzhambu	VCH107	Avarakai Vathakuzhambu
77	FG	VCHP035	Kuzhambu	VCH108	Brinjal Vathakuzhambu
78	FG	VCHP035	Kuzhambu	VCH109	Chinna vengayam Vathakuzhambu
79	FG	VCHP035	Kuzhambu	VCH110	Drum Stick Vathakuzhambu
80	FG	VCHP035	Kuzhambu	VCH111	Fenugreek Vathakuzhambu
81	FG	VCHP035	Kuzhambu	VCH112	Karunai Kizhangu Vathakuzhambu
82	FG	VCHP035	Kuzhambu	VCH113	Kovakai Vathakuzhambu
83	FG	VCHP035	Kuzhambu	VCH114	Lady's Finger Vathakuzhambu
84	FG	VCHP035	Kuzhambu	VCH115	Manathakali Vathakuzhambu
85	FG	VCHP035	Kuzhambu	VCH116	Senbu Vathakuzhambu
86	FG	VCHP035	Kuzhambu	VCH117	Sennai Vathakuzhambu
87	FG	VCHP035	Kuzhambu	VCH118	Sundakai Vathakuzhambu
88	FG	VCHP035	Kuzhambu	VCH119	Sungakai Vathakuzhambu
89	FG	VCHP036	Meals Sambar	VCH088	Okra Sambar
90	FG	VCHP036	Meals Sambar	VCH089	Avarai Capsicum Mango Sambar
91	FG	VCHP036	Meals Sambar	VCH090	Avarai Murungai Manga Sambar
92	FG	VCHP036	Meals Sambar	VCH091	Avarai Murungai Sambar
93	FG	VCHP036	Meals Sambar	VCH092	Chow - Chow Murungai Sambar
94	FG	VCHP036	Meals Sambar	VCH093	Kadhamba Sambar
95	FG	VCHP036	Meals Sambar	VCH094	Kathiri Capsicum Manga Sambar
96	FG	VCHP036	Meals Sambar	VCH095	Kathiri Murungai Manga Sambar
97	FG	VCHP036	Meals Sambar	VCH096	Kathiri Murungai Sambar
98	FG	VCHP036	Meals Sambar	VCH097	Mulangi Sambar
99	FG	VCHP036	Meals Sambar	VCH098	Urulai Murungai Sambar
100	FG	VCHP036	Meals Sambar	VCH099	Vellai Poosani Murungai Sambar
101	FG	VCHP036	Meals Sambar	VCH100	Vellai-Kathiri Murungai Sambar
102	FG	VCHP037	Rasam	VCH101	Cauli Flower Rasam
103	FG	VCHP037	Rasam	VCH102	Garlic Rasam
104	FG	VCHP037	Rasam	VCH103	Paruppu Rasam
105	FG	VCHP037	Rasam	VCH104	Pine apple Rasam
106	FG	VCHP037	Rasam	VCH105	Tomato Rasam
107	FG	VCHP046	Phulka/Naan Sidedish	VCH033	Baby Corn Masala
108	FG	VCHP046	Phulka/Naan Sidedish	VCH034	Gobi Mutter
109	FG	VCHP046	Phulka/Naan Sidedish	VCH035	Green peas Masala
110	FG	VCHP046	Phulka/Naan Sidedish	VCH036	Veg Jaipuri
111	SFG	VCHP013	Appam Batter	VCH013	Appam Batter
112	SFG	VCHP014	Vada Batters	VCH016	Medhu Vadai Batter
113	SFG	VCHP016	Roasted Coconut Chutney Masala	VCH020	Roasted Coconut Chutney Masala
114	SFG	VCHP017	Roasted Malli Chutney Masala	VCH021	Roasted Malli Chutney Masala
115	SFG	VCHP039	Soups	VCH120	Tomato Soup
116	SFG	VCHP039	Soups	VCH121	Vegetable Soup
117	SFG	VCHP040	Butter gravy	VCH122	Butter Gravy
118	SFG	VCHP041	Yellow Gravy	VCH123	Yellow Gravy
119	SFG	VCHP042	Onion Masala	VCH124	Onion Masala
120	SFG	VCHP043	Masala Vada Batter	VCH125	Masala Vada Batter
121	SFG	VCHP044	Bonda Batter	VCH126	Bonda Batter
122	SFG	VCHP045	Meals Vada Batters	VCH014	Cabbage Vada Batter
123	SFG	VCHP045	Meals Vada Batters	VCH015	Keerai Vada Batter
124	SFG	VCHP045	Meals Vada Batters	VCH017	Onion Medhu Vada Batter
125	SFG	VCHP045	Meals Vada Batters	VCH018	Spl Vada Batter
"""

# ─── Parse — one product per VCH (PV_ID) row ──────────
# PD_ID is only used to resolve product_type_id
# PV_ID = code, variant name = product name

product_insert_list = []
seen_pv_ids = set()

for line in raw_data.strip().split("\n"):
    parts = [p.strip() for p in line.strip().split("\t")]
    if len(parts) < 6:
        continue

    _, solution_type, pd_id, _, pv_id, product_name = parts[:6]

    if pv_id in seen_pv_ids:
        print(f"⚠️  Duplicate PV_ID skipped: {pv_id} - {product_name}")
        continue
    seen_pv_ids.add(pv_id)

    product_type_id = pd_to_product_type_id.get(pd_id)
    if product_type_id is None:
        print(f"⚠️  No product_type_id for PD_ID={pd_id}, skipping {pv_id} - {product_name}")
        continue

    product_insert_list.append({
        "code": pv_id,
        "name": product_name,
        "product_type_id": product_type_id,
        "is_active": 1,
        "is_deleted": 0,
        "created_by": created_by,
    })

if not product_insert_list:
    print("❌ No products to insert, exiting.")
    exit()

print(f"📋 Total products to insert: {len(product_insert_list)}")  # should print 125

# ─── Insert ───────────────────────────────────────────
product_query = text("""
    INSERT INTO product_master (code, name, product_type_id, is_active, is_deleted, created_by)
    VALUES (:code, :name, :product_type_id, :is_active, :is_deleted, :created_by)
""")

with engine.connect() as conn:
    conn.execute(product_query, product_insert_list)
    conn.commit()
    print(f"✅ {len(product_insert_list)} products inserted into product_master.")