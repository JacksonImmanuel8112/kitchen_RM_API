from pydantic import BaseModel
from typing import Optional

class IngredientBase(BaseModel):
    name: str
    code : str
    uom: Optional[str] = None
    price: Optional[float] = None

class IngredientCreate(IngredientBase):
    pass

class IngredientUpdate(IngredientBase):
    id: int
    pass

class IngredientResponse(IngredientBase):
    id: int

    class Config:
        from_attributes = True