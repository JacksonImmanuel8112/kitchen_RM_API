from fastapi import FastAPI
from app.api.router import router
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine, test_db_connection
from app.models import ingredient, user

app = FastAPI(title="RM Tool API")

test_db_connection()

# Create tables
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://127.0.0.1:4200"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)