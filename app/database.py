import asyncpg

class Database:
    def __init__(self):
        self.pool = None

    async def init(self):
        self.pool = await asyncpg.create_pool(dsn="postgresql://inventory_user:inventorypass123@db:5432/inventory_db", min_size=1, max_size=10)

    async def close(self):
        await self.pool.close()

db = Database()

async def get_pool():
    return db.pool
