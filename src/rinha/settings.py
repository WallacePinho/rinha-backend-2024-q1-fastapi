import os
from fastapi import FastAPI

app = FastAPI()

DATABASE_HOST = os.getenv("DATABASE_HOST", "postgres")
DATABASE_PASS = os.getenv("DATABASE_PASS", "rinha")
DATABASE_PORT = os.getenv("DATABASE_PORT", "5432")
DATABASE_NAME = os.getenv("DATABASE_NAME", "rinha")
DATABASE_USER = os.getenv("DATABASE_USER", "rinha")