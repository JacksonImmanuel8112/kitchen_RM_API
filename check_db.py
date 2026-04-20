from sqlalchemy import create_engine, text
import json
import logging

# Set up logging to stdout
logging.basicConfig(level=logging.INFO)

# Assuming DATABASE_URL might not be readily importable if config implies other things, let's just use the same strategy as SessionLocal
from app.core.database import SessionLocal

db = SessionLocal()
try:
    print("Total recipes:", db.execute(text("SELECT COUNT(*) FROM recipe_master")).scalar())
    print("Recipes with yield NOT NULL:", db.execute(text("SELECT COUNT(*) FROM recipe_master WHERE yield_qty IS NOT NULL")).scalar())
    print("Recipes with qty NOT NULL:", db.execute(text("SELECT COUNT(*) FROM recipe_master WHERE qty IS NOT NULL")).scalar())
    print("Recipes with is_deleted=0:", db.execute(text("SELECT COUNT(*) FROM recipe_master WHERE is_deleted=0")).scalar())
    
    # Try fetching 1 sample
    res = db.execute(text("""
        SELECT pm.name as product_name, im.name as ingredient_name, rm.yield_qty, rm.qty as ingredient_qty 
        FROM recipe_master rm
        JOIN product_master pm ON rm.product_id = pm.id
        JOIN ingredient_master im ON rm.ingredient_id = im.id
        WHERE rm.is_deleted = 0
        LIMIT 5
    """)).fetchall()
    
    print("Sample joins:")
    for r in res:
        print(dict(r._mapping))
finally:
    db.close()
