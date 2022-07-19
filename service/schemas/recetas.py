from typing import Optional
from pydantic import BaseModel

class Recetas(BaseModel):
    id: Optional[int]
    nombre_receta: str
    id_tipo : int