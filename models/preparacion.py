from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

preparacion = Table(
    "preparacion",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("preparacion",String(255),),
    Column("id_receta",Integer, ForeignKey("recetas.id")),
)

meta.create_all(engine)