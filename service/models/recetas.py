from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import Integer, String
from ..config.db import meta, engine

recetas = Table(
    "recetas",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("nombre_receta",String(255),),
    Column("id_tipo",Integer, ForeignKey("tipo_receta.id")),
)

meta.create_all(engine)