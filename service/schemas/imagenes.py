from ast import Str
from typing import Optional
from pydantic import BaseModel

class Imagenes(BaseModel):
    id: Optional[int]
    imagen: Optional[str]
    id_tipo : int