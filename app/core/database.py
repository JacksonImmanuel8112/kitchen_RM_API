from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import DATABASE_URL
import datetime
from sqlalchemy import Column, String, DateTime, Boolean

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

class AuditMixin:
    created_by = Column(String(255), nullable=True)
    created_date = Column(DateTime(timezone=True), default=lambda: datetime.datetime.now(datetime.timezone.utc))
    modified_by = Column(String(255), nullable=True)
    modified_date = Column(DateTime(timezone=True), default=lambda: datetime.datetime.now(datetime.timezone.utc), onupdate=lambda: datetime.datetime.now(datetime.timezone.utc))
    deleted_by = Column(String(255), nullable=True)
    deleted_date = Column(DateTime(timezone=True), nullable=True)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)