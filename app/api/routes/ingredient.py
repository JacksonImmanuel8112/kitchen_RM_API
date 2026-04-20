from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.schemas.ingredient import (
    IngredientCreate,
    IngredientUpdate,
    IngredientResponse
)
from app.services import ingredient_service

router = APIRouter(prefix="/ingredients", tags=["Ingredients"])


@router.get("/", response_model=list[IngredientResponse])
def get_all(db: Session = Depends(get_db)):
    return ingredient_service.get_all(db)


@router.get("/{id}", response_model=IngredientResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    item = ingredient_service.get_by_id(db, id)
    if not item:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return item


@router.post("/", response_model=IngredientResponse)
def create(data: IngredientCreate, db: Session = Depends(get_db)):
    return ingredient_service.create(db, data)


@router.put("/{id}", response_model=IngredientResponse)
def update(id: int, data: IngredientUpdate, db: Session = Depends(get_db)):
    item = ingredient_service.update(db, id, data)
    if not item:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return item


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    success = ingredient_service.delete(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return {"message": "Deleted successfully"}