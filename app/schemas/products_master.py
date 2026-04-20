from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductMasterBase(BaseModel):
    name: str
    code: str
    product_type_id : int

class ProductCreate(ProductMasterBase):
    pass

class ProductUpdate(ProductMasterBase):
    id : int
    pass

class ProductResponse(ProductMasterBase):
    id: int
    created_by: Optional[str]
    created_date: Optional[datetime]

    modified_by: Optional[str]
    modified_date: Optional[datetime]

    deleted_by: Optional[str]
    deleted_date: Optional[datetime]

    is_active: bool
    is_deleted: bool

    class Config:
        from_attributes = True