from tkinter import Image
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

imagenes = Table(
    "imagenes",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("imagen",String(255)),
    Column("id_tipo",Integer, ForeignKey("tipo_receta.id")),
)

meta.create_all(engine)