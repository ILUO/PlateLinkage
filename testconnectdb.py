from connect_db import *
import datetime
import random
sh600001 = []
sh600002 = []
sh600003 = []
sh600004 = []
date = datetime.date(2001,02,01)
for i in range(0,60):
    DICT = {}
    id = 'SH600001'
    Trend = random.randint(0,1)
    DICT['stockID'] = id
    DICT['Date'] = date + datetime.timedelta(days=i+1)
    DICT['Trend'] = Trend
    sh600001.append(DICT)
for i in range(0,60):
    DICT = {}
    id = 'SH600002'
    DATE = str(i)
    Trend = random.randint(0,1)
    DICT['stockID'] = id
    DICT['Date'] = date + datetime.timedelta(days=i+1)
    DICT['Trend'] = Trend
    sh600002.append(DICT)
for i in range(0,60):
    DICT = {}
    id = 'SH600003'
    Trend = random.randint(0,1)
    DICT['stockID'] = id
    DICT['Date'] = date + datetime.timedelta(days=i+1)
    DICT['Trend'] = Trend
    sh600003.append(DICT)
for i in range(0,60):
    DICT = {}
    id = 'SH600004'
    Trend = random.randint(0,1)
    DICT['stockID'] = id
    DICT['Date'] = date + datetime.timedelta(days=i+1)
    DICT['Trend'] = Trend
    sh600004.append(DICT)


with open_session() as s:
  s.execute(
      SH600000.__table__.insert(),sh600001
  )
  s.execute(
      SH600001.__table__.insert(),sh600002
  )
  s.execute(
      SH600002.__table__.insert(),sh600003
  )
  s.execute(
      SH600003.__table__.insert(),sh600004
  )
  s.commit()