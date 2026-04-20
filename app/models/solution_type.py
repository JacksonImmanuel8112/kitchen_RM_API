from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from app.core.database import Base, AuditMixin

class SolutionType(Base, AuditMixin):
    __tablename__ = "solution_type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)