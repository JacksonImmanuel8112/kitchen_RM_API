from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from app.core.database import Base, AuditMixin

class SolutionCategoryInput(Base, AuditMixin):
    __tablename__ = "IP_Solution_Category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)