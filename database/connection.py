import os
from sqlalchemy import create_engine, Engine, event
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv



load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

engine = create_engine(f'mysql+pymysql://{os.getenv('DATABASE_USER')}:{os.getenv("DATABASE_PASS")}@localhost:3306/{os.getenv("DATABASE_NAME")}')

session = scoped_session(sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
))

@event.listens_for(Engine, 'connect')
def set_mysql_program(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("SET SESSION sql_mode='TRADITIONAL'")
    cursor.close()
