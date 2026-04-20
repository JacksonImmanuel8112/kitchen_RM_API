from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.schemas.products_master import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)
from app.services import product_master_service

router = APIRouter(prefix="/Products", tags=["Products"])


@router.get("/", response_model=list[ProductResponse])
def get_all(db: Session = Depends(get_db)):
    return product_master_service.get_all(db)


@router.get("/{id}", response_model=ProductResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    item = product_master_service.get_by_id(db, id)
    if not item:
        raise HTTPException(status_code=404, detail="Product not found")
    return item


@router.post("/", response_model=ProductResponse)
def create(data: ProductCreate, db: Session = Depends(get_db)):
    return product_master_service.create(db, data)


@router.put("/{id}", response_model=ProductResponse)
def update(id: int, data: ProductUpdate, db: Session = Depends(get_db)):
    item = product_master_service.update(db, id, data)
    if not item:
        raise HTTPException(status_code=404, detail="Product not found")
    return item


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    success = product_master_service.delete(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Deleted successfully"}