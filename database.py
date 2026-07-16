from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv("postgresql://postgres:1824@localhost:5432/energy_db")

engine = create_engine(DATABASE_URL)
