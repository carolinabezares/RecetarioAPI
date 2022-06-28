from fastapi import APIRouter
from config.db import conn
from models.ingredientes import ingredientes as ingre
from schemas.ingredientes import Ingredientes


ingredientes = APIRouter()

@ingredientes.get("/ingredientes")
def get_all_ingredientes():
    return conn.execute(ingre.select()).fetchall() 