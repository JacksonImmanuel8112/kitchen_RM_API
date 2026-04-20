import os
import datetime
import pymysql

from sqlalchemy import create_engine, Column, String, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# 🔥 IMPORTANT: allow PyMySQL to act like MySQLdb
pymysql.install_as_MySQLdb()

# 🔹 Load .env (only works locally, safe for production)
load_dotenv()

# 🔹 Get DATABASE URL
DATABASE_URL = os.getenv("DATABASE_URL")

print("🚀 DATABASE_URL:", DATABASE_URL)

if not DATABASE_URL:
    raise Exception("❌ DATABASE_URL is not set")

# 🔹 Create engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # 🔥 avoids stale connections
    pool_recycle=300,
    echo=False            # set True for SQL debug
)

# 🔹 Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 🔹 Base model
Base = declarative_base()

# 🔹 Audit Mixin (common columns)
class AuditMixin:
    created_by = Column(String(255), nullable=True)
    created_date = Column(
        DateTime(timezone=True),
        default=lambda: datetime.datetime.now(datetime.timezone.utc)
    )
    modified_by = Column(String(255), nullable=True)
    modified_date = Column(
        DateTime(timezone=True),
        default=lambda: datetime.datetime.now(datetime.timezone.utc),
        onupdate=lambda: datetime.datetime.now(datetime.timezone.utc)
    )
    deleted_by = Column(String(255), nullable=True)
    deleted_date = Column(DateTime(timezone=True), nullable=True)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)


# 🔹 DB dependency (for FastAPI)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🔹 Optional: test connection on startup
def test_db_connection():
    try:
        with engine.connect() as conn:
            print("✅ Database connected successfully")
    except Exception as e:
        print("❌ Database connection failed:", e)
        raise e