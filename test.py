from connect_db import *
import itertools
# import time
# import MySQLdb
#
# enddate = '2015-10-14'
# Stocklist = ['000001','000005','000006']
# with open_session() as s:
#     start = time.time()
#     for i in range(0,len(Stocklist)):
#         result = s.query(Stock.chCode).filter(Stock.nDate==enddate, Stock.nTrend==1, Stock.chCode == Stocklist[i]).all()
#         print result
#     end = time.time()
#     print end - start
#
# start = time.time()
# sqlpart = ''
# for i in range(0,len(Stocklist)):
#     if i != len(Stocklist)-1:
#         sqlpart = sqlpart + "chCode = '" + Stocklist[i] + "' or "
#     else:
#         sqlpart = sqlpart + "chCode = '" + Stocklist[i]+"');"
#
# sql = "select chCode from Stock where nDate = '" + enddate + "' and " + "nTrend = 1 " + " and (" + sqlpart
# print sql
# try:
#     conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', port=3306, db='platelinkage')
#     cursor = conn.cursor()
#     result = cursor.execute(sql)
#     stockid = cursor.fetchmany(result)
#     print stockid
# except Exception as e:
#     print e.args
# end = time.time()
# print end - start
# with open_session() as s:
#         result = s.query(SetSupport).all()
#         print result[0].transset
#         supportdata = {}
# with open_session() as s:
#     result = s.query(SetSupport).all()
#     for trans in  result:
#         stocklist = eval(trans.transset)
#         stockset = frozenset(stocklist)
#         supportdata[stockset] = trans.support
#     print supportdata
def getnewsupportdata(self,stock1,stock2,supportdata):
        for i in range(1,len(stock1)):
            for a in itertools.chain(itertools.combinations(stock1,i)):
                print a

getnewsupportdata(1,[1,2,3,4],5,6)