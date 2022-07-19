from fastapi import APIRouter
from ..config.db import conn
from ..models.imagenes import imagenes as img
from ..schemas.imagenes import Imagenes


imagenes = APIRouter()

@imagenes.get("/imagenes")
def get_all_imagenes():
    return conn.execute(img.select()).fetchall() 