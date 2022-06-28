from datetime import datetime
from turtle import st, title
from typing import Text
from fastapi import FastAPI
from routes.tipo_receta import tipo_recetas
from routes.recetas import recetas
from routes.ingredientes import ingredientes
from routes.imagenes import imagenes
from routes.preparacion import preparaciones

app = FastAPI()
app.include_router(tipo_recetas)
app.include_router(recetas)
app.include_router(ingredientes)
app.include_router(imagenes)
app.include_router(preparaciones)

@app.get('/')
def read_root():
    return ("Welcome: Welcome to my REST API")

