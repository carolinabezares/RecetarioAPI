from typing import Optional
from pydantic import BaseModel

class Tipo(BaseModel):
    id: Optional[int]
    tipo: str