from fastapi import FastAPI
from .routes.tipo_receta  import tipo_receta
from .routes.recetas import recetas
from .routes.ingredientes import ingredientes
from .routes.imagenes import imagenes
from .routes.preparacion import preparaciones

app = FastAPI()
app.include_router(tipo_receta)
app.include_router(recetas)
app.include_router(ingredientes)
app.include_router(imagenes)
app.include_router(preparaciones)

@app.get('/')
def home():
    return ("Nuevo Cambio")

