from pydantic import BaseModel

class IngredientBase(BaseModel):
    name: str
    uom: str
    cost_per_unit: float

class IngredientCreate(IngredientBase):
    pass

class IngredientUpdate(IngredientBase):
    pass

class IngredientResponse(IngredientBase):
    id: int

    class Config:
        from_attributes = True