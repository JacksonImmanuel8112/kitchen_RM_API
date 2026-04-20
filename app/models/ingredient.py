from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from app.core.database import Base, AuditMixin

class Ingredient(Base, AuditMixin):
    __tablename__ = "ingredient_master"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    code = Column(String(20))
    price = Column(DECIMAL(10,2), nullable=True)
    shelf_life_mins = Column(Integer, nullable=True)
    uom = Column(String(20))
    specification = Column(String(150), nullable=True)
    brand = Column(String(150), nullable=True)
    supplier_id = Column(Integer, ForeignKey("supplier_master.id"), nullable=True)

    solution_category_id = Column(Integer, ForeignKey("IP_Solution_Category.id"))