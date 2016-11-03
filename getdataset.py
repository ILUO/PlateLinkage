#coding:utf-8
from connect_db import *
import MySQLdb
from datetime import *


class GetDataset(object):
    def __init__(self):
        self.dataset = {}

    def getdata(self, start, end, stock):
        starttime = start.split('-')
        endtime = end.split('-')
        startdate = date(int(starttime[0]),int(starttime[1]),int(starttime[2]))
        enddate = date(int(endtime[0]),int(endtime[1]),int(endtime[2]))
        days = (enddate-startdate).days
        for i in range(0, len(stock)):
            self.dataset[stock[i]] = {}
            for j in range(0, days):
                self.dataset[stock[i]][str(j)] = 0

        try:
            conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', port=3306, db='platelinkage')
            cursor = conn.cursor()
            for i in range(0, len(stock)):
                sql = "select * from " + stock[i] + " where date>='" + start + "' and  date<='" + end + "'  and Trend=1;"
                result = cursor.execute(sql)
                data = cursor.fetchmany(result)
                for d in data:
                    self.dataset[stock[i]][str(d[2])] = 1
            return self.dataset

        except Exception as e:
            print e


if __name__ == '__main__':
    getdataset = GetDataset()
    getdataset.getdata('2001-02-02', '2001-03-01', ['sh600001', 'sh600002'])
    print getdataset.dataset

























