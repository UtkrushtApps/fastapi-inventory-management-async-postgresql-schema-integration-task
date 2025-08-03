# Inventory Management Platform – FastAPI & Async PostgreSQL Task

## Task Overview

This company’s inventory management tool is critical for tracking available products and keeping operations efficient. You are tasked with enabling the API endpoints for adding, listing, and searching products by building a robust database foundation and implementing all asynchronous PostgreSQL access logic. Business growth depends on managing products and categories efficiently and updating systems in near real time.

## Guidance

You have a pre-built FastAPI app with all routers, middleware, and endpoint stubs in place. The only missing pieces are the actual PostgreSQL table definitions and the backend logic that interacts asynchronously with the database (the `dal.py` file). Focus your work on:
- Creating a functional, normalized schema in `schema.sql` so every API route requiring products and categories can operate
- Implementing async/await-compatible database interaction code in `app/dal.py` (which your endpoints will call)
- Reviewing `app/database.py` for async PostgreSQL connection handling
- No need to modify or add API endpoints; your work powers them underneath

## Database Access

- Host: `localhost` (or from containers, `db`)
- Port: `5432`
- Database: `inventory_db`
- Username: `inventory_user`
- Password: `inventorypass123`

Use any tool like psql, DBeaver, or pgAdmin to inspect, test, and validate the database schema directly as you work.

## Objectives

- Define a PostgreSQL schema with tables for `products` and `categories`, with a foreign key linking products to categories
- Ensure basic attributes such as product name, SKU, quantity, and price (use appropriate data types and constraints)
- Insert sample data (5 categories, at least 10 products, distributed among these categories)
- In `app/dal.py`, implement async CRUD logic using asyncpg for all required product and category operations
- Make sure all API endpoints (add product, get product(s), search by category) function correctly using your schema and DAL code

## How to Verify

- Using the API, confirm products can be created and retrieved; validate category information joins correctly
- List all categories and confirm product/category mappings by testing GET endpoints
- Search for products within a specific category and confirm the result set is accurate
- Validate that your schema enforces constraints (e.g., products must belong to a valid category, unique SKUs, prices cannot be negative)
- Manually check the database for data correctness and relationships involved
