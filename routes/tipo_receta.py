from fastapi import APIRouter
from config.db import conn
from models.tipo_receta import tipo_receta
from schemas.tipo_receta import Tipo


tipo_recetas = APIRouter()

@tipo_recetas.get("/tipos")
def get_all_tipos_de_recetas():
    return conn.execute(tipo_receta.select()).fetchall() 