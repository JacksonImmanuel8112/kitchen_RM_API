from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from app.core.database import Base, AuditMixin

class RecipeMaster(Base, AuditMixin):
    __tablename__ = "recipe_master"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product_master.id"))
    ingredient_id = Column(Integer, ForeignKey("ingredient_master.id"))
    price = Column(DECIMAL(10,2), nullable=True)
    qty_uom = Column(String(20))
    price = Column(DECIMAL(10,2), nullable=True)
    yield_uom = Column(String(20))