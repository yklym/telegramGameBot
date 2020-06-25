from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from data.config import DB_CONF

Base = declarative_base()

engine = create_engine(
    f'postgresql://{DB_CONF["user"]}:{DB_CONF["password"]}@{DB_CONF["host"]}:{DB_CONF["port"]}/{DB_CONF["database"]}',
    echo=False)

Session = sessionmaker(bind=engine)
session = Session()
