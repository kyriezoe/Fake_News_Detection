#!/usr/bin/python3
#-*- coding:utf-8 -*-

import csv

def __init__(self):
    pass

def closeCsv():
    global csv_file
    csv_file.close()

def writeCsv(filename):
    global csv_file,csv_writer
    csv_file = open(filename,"w",newline="")
    csv_writer = csv.writer(csv_file,dialect=("excel"))

def setTitle(_tuple):
    csv_writer.writerow(_tuple)

def insert(_tuple):
    global csv_writer
    csv_writer.writerow(_tuple)

def fflush():
    global csv_file
    csv_file.flush()