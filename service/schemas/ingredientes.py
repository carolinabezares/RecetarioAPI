from typing import Optional
from pydantic import BaseModel

class Ingredientes(BaseModel):
    id: Optional[int]
    ingredientes: str
    id_receta : int