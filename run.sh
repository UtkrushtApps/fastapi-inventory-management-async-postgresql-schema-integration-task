#!/bin/bash
set -e

cd /root/task

echo "Starting Docker containers..."
docker-compose up -d

echo "Waiting for PostgreSQL to be ready..."
for i in {1..30}
do
  docker exec -it inventory_postgres pg_isready -U inventory_user && break
  sleep 2
done
sleep 5

echo "Creating database schema..."
docker exec -i inventory_postgres psql -U inventory_user -d inventory_db < /root/task/schema.sql

echo "Loading sample data..."
docker exec -i inventory_postgres psql -U inventory_user -d inventory_db < /root/task/data/sample_data.sql

echo "Validating FastAPI is responding..."
for i in {1..12}
do
  curl -s http://localhost:8000/health && echo "API is up!" && break
  sleep 2
done

exit 0
