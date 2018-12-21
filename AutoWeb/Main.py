#!/usr/bin/python3
#-*- coding:utf-8 -*-
import req
import readcsv
import store
import time
##explain##
'''
replace ./test.csv with your filename
It will store in Output.csv
'''

##initial
req.init()
rs = readcsv.openCsv("./fake_or_real_news.csv")
if rs==-1:
    print("ERROR 1!")
store.writeCsv("./Output1.csv")
store.setTitle(["id","label","title_decision","title_score","content_decision","content_score"])

rs = readcsv.getNext()
while rs != -1:
    res = -1
    maxtry = 10
    try:
        while res==-1 and maxtry>0:
            res = req.sendRequest(rs)
            maxtry = maxtry - 1
    except :
        print("Internet Error!Sleep 3 sec！",res,maxtry)
        time.sleep(3)
        continue
    record = [rs[0],rs[3],res["title_decision"],\
    res["title_score"],res["content_decision"],\
    res["content_score"]]
    store.insert(record)
    store.fflush()
    rs = readcsv.getNext()
    print(record)

print("Done")
readcsv.closeCsv()
store.closeCsv()
