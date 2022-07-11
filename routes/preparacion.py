from fastapi import APIRouter
from config.db import conn
from models.preparacion import preparacion as pre
from schemas.preparacion import Preparacion


preparaciones = APIRouter()

@preparaciones.get("/preparacion")
def get_all_preparaciones():
    return conn.execute(pre.select()).fetchall() 