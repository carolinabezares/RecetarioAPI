from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:carolinabezares06@localhost:3306/recetario")

meta = MetaData()

conn = engine.connect()
