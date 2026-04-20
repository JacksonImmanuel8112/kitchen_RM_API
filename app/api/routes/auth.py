from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.schemas.user import UserCreate, UserLogin, TokenResponse
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/signup")
def signup(data: UserCreate, db: Session = Depends(get_db)):
    user = auth_service.signup(db, data.email, data.password)

    if not user:
        raise HTTPException(status_code=400, detail="Email already exists")

    return {"message": "User created successfully"}


@router.post("/login", response_model=TokenResponse)
def login(data: UserLogin, db: Session = Depends(get_db)):
    token = auth_service.login(db, data.email, data.password)

    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"access_token": token}