from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://admin:carolinabezares06@reccetario.cajbapsm5aqx.us-west-1.rds.amazonaws.com:3306/recetario")

meta = MetaData()

conn = engine.connect()
