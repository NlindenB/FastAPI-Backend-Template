# Alembic Database Migration

## 1. Auto-Generated Tables

- Create a revision: `alembic revision --autogenerate -m "Initial migration"`

## 2. Update Tables

- Update 1 table: `alembic update head`
- Update more than 1 table: `alembic update head``

## 3. Alembic + Docker

- Revision via Docker: `docker exec CONTAINER_NAME alembic revision --autogenerate -m "Initial migration"`
- Update 1 table via Docker: `docker exec CONTAINER_NAME alembic update head`
- Update more than 1 table via Docker: `docker exec CONTAINER_NAME alembic update heads`
