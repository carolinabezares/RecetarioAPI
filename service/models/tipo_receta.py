from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from ..config.db import meta, engine

tipo_receta = Table(
    "tipo_receta",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("tipo",String(255),),
)

meta.create_all(engine)