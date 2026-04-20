from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from app.core.database import Base, AuditMixin

class Products(Base, AuditMixin):
    __tablename__ = "product_master"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    code = Column(String(100))
    shelf_life_mins = Column(Integer, nullable=True)
    product_type_id = Column(Integer, ForeignKey("product_type.id"))