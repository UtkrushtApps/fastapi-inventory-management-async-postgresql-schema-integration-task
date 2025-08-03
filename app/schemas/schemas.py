from pydantic import BaseModel, condecimal, PositiveInt
from typing import Optional

class Category(BaseModel):
    id: int
    name: str

class CategoryCreate(BaseModel):
    name: str

class Product(BaseModel):
    id: int
    name: str
    sku: str
    quantity: int
    price: float
    category_id: int

class ProductCreate(BaseModel):
    name: str
    sku: str
    quantity: int
    price: float
    category_id: int
