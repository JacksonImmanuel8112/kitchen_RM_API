from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from app.core.database import Base, AuditMixin

class ProductType(Base, AuditMixin):
    __tablename__ = "product_type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    code = Column(String(100))
    solution_type_id = Column(Integer,  ForeignKey("solution_type.id"))
