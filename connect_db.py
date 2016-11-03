#coding:utf-8
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import CHAR,Integer,String,VARCHAR,Text
from contextlib import contextmanager

class User(object):
    pass

BaseModel=declarative_base()

class SetSupport(BaseModel):
    __tablename__ = "SetSupport"
    startdate = Column(DATETIME,primary_key=True)
    transset = Column(VARCHAR(100), primary_key=True)
    support  = Column(Integer, index=True, nullable=False)

class Rules(BaseModel):
    __tablename__ = "Rules"
    startdate = Column(DATETIME, primary_key=True)
    LHS  = Column(VARCHAR(255), index=True, primary_key=True,nullable=False)
    RHS  = Column(VARCHAR(255), index=True, primary_key=True,nullable=False)
    conf = Column(FLOAT)

class SH600000(BaseModel):
    __tablename__ = "SH600001"
    id = Column(Integer, primary_key=True, autoincrement=True)
    stockID = Column(VARCHAR(8),nullable=true)
    Date = Column(DATETIME)
    Trend = Column(Integer,nullable=true)

class SH600001(BaseModel):
    __tablename__ = "SH600002"
    id = Column(Integer, primary_key=True, autoincrement=True)
    stockID = Column(VARCHAR(8),nullable=true)
    Date = Column(DATETIME)
    Trend = Column(Integer,nullable=true)

class SH600002(BaseModel):
    __tablename__ = "SH600003"
    id = Column(Integer, primary_key=True, autoincrement=True)
    stockID = Column(VARCHAR(8),nullable=true)
    Date = Column(DATETIME)
    Trend = Column(Integer,nullable=true)

class SH600003(BaseModel):
    __tablename__ = "SH600004"
    id = Column(Integer, primary_key=True, autoincrement=True)
    stockID = Column(VARCHAR(8),nullable=true)
    Date = Column(DATETIME)
    Trend = Column(Integer,nullable=true)

class Stock(BaseModel):
    __tablename__ = "STOCK"
    id = Column(Integer,primary_key=True,autoincrement=True)
    chWindCode = Column(VARCHAR(255))
    chCode = Column(VARCHAR(255))
    nDate = Column(VARCHAR(255))
    nTime = Column(VARCHAR(255))
    nOpen = Column(VARCHAR(255))
    nHigh = Column(VARCHAR(255))
    nlow = Column(VARCHAR(255))
    nClose = Column(VARCHAR(255))
    iVolume = Column(VARCHAR(255))
    iTurover = Column(VARCHAR(255))
    iMarchItems = Column(VARCHAR(255))
    nIntesest = Column(VARCHAR(255))
    nTrend = Column(VARCHAR(255))

engine = create_engine(
            "mysql://root:123456@localhost:3306/platelinkage?charset=utf8")
metadata = MetaData(engine)

def init_db():
    BaseModel.metadata.create_all(engine)

init_db()

@contextmanager
def open_session():
    session = sessionmaker(engine)()
    try:
        yield session
    finally:
        session.close()


