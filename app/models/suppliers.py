from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from app.core.database import Base, AuditMixin

class Ingredient(Base, AuditMixin):
    __tablename__ = "supplier_master"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)