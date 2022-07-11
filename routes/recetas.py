from fastapi import APIRouter
from config.db import conn
from models.recetas import recetas as rc
from schemas.recetas import Recetas


recetas = APIRouter()

@recetas.get("/recetas")
def get_all_recetas():
    return conn.execute(rc.select()).fetchall() 