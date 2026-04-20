from fastapi import APIRouter
from app.api.routes import ingredient, auth, products_master, conversion

router = APIRouter()

router.include_router(ingredient.router)
router.include_router(auth.router)
router.include_router(products_master.router)
router.include_router(conversion.router)