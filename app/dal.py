import asyncpg
from app.database import get_pool
from app.schemas.schemas import ProductCreate, Product, Category, CategoryCreate

# All functions below should use async with pool.acquire(...) for DB ops

async def create_product(product: ProductCreate):
    pool = await get_pool()
    async with pool.acquire() as conn:
        row = await conn.fetchrow(
            """
            INSERT INTO products (name, sku, quantity, price, category_id)
            VALUES ($1, $2, $3, $4, $5)
            RETURNING id, name, sku, quantity, price, category_id
            """,
            product.name, product.sku, product.quantity, product.price, product.category_id)
        return dict(row) if row else None

async def list_products():
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT id, name, sku, quantity, price, category_id FROM products ORDER BY id ASC;")
        return [dict(row) for row in rows]

async def get_product(product_id: int):
    pool = await get_pool()
    async with pool.acquire() as conn:
        row = await conn.fetchrow("SELECT id, name, sku, quantity, price, category_id FROM products WHERE id=$1;", product_id)
        return dict(row) if row else None

async def list_categories():
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT id, name FROM categories ORDER BY id ASC;")
        return [dict(row) for row in rows]

async def get_products_by_category(category_id: int):
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch(
            "SELECT id, name, sku, quantity, price, category_id FROM products WHERE category_id=$1 ORDER BY id ASC;",
            category_id)
        return [dict(row) for row in rows]
