from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:1824@localhost:5432/energy_db"

engine = create_engine(DATABASE_URL)