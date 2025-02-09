from sqlalchemy import create_engine, MetaData

# Definir los parámetros de conexión
user = 'DiosdelSexo'
password = 'chup0p3n3'
host = 'LocalHost'  
port = '5432'  
db = 'P2P'
connectionUrl = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}?client_encoding=UTF8'

engine = create_engine(connectionUrl)
meta = MetaData()
conn = engine.connect()