import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

server = 'DIAMOND\\NHOM5CSDLPT'
database = 'QLCH_QN'
username = 'sa'
password = '123'
driver = '{ODBC Driver 17 for SQL Server}'

connectDB = pyodbc.connect(f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}")


SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://sa:123@DIAMOND\\NHOM5CSDLPT/QLCH_QN?driver=ODBC+Driver+17+for+SQL+Server"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()