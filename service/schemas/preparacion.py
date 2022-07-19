from typing import Optional
from pydantic import BaseModel

class Preparacion(BaseModel):
    id: Optional[int]
    preparacion: str
    id_receta : int