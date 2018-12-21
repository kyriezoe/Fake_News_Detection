#!/usr/bin/python3
#-*- coding:utf-8 -*-
import csv

def __init__(self):
    pass

def openCsv(filename):
    try:
        global csv_file
        csv_file = open(filename)
        global reader
        reader = csv.reader(csv_file)
        return next(reader)
    except:
        return -1

def closeCsv():
    global csv_file
    csv_file.close()

def getNext():
    try:
        header_row = next(reader)
        return header_row
    except StopIteration as e:
        return -1
    except:
        return -1

def Test():
    rs = openCsv("./test.csv")
    while rs!=-1:
        #print(rs)
        rs = getNext()
    return 0

# print(Test())