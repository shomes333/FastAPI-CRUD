from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:windruh420@localhost:3306/basededatos")


conn = engine.connect()

meta_data = MetaData()