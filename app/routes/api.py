from fastapi import APIRouter, HTTPException, status
from app.dal import list_products, create_product, list_categories, get_products_by_category, get_product
from app.schemas.schemas import ProductCreate, Product, Category
from typing import List

router = APIRouter()

@router.get("/products", response_model=List[Product])
async def get_all_products():
    return await list_products()

@router.get("/products/{product_id}", response_model=Product)
async def get_one_product(product_id: int):
    prod = await get_product(product_id)
    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")
    return prod

@router.get("/categories", response_model=List[Category])
async def get_all_categories():
    return await list_categories()

@router.get("/categories/{category_id}/products", response_model=List[Product])
async def get_products_in_category(category_id: int):
    return await get_products_by_category(category_id)

@router.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
async def add_product(product: ProductCreate):
    item = await create_product(product)
    if not item:
        raise HTTPException(status_code=400, detail="Product creation failed")
    return item
