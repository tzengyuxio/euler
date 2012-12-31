#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import math

linenum = 0
max_linenum = 0
max_value = 0.0

with open('data/base_exp.txt', 'r') as csvfile:
    baseexp_reader = csv.reader(csvfile, delimiter=',')
    for row in baseexp_reader:
        linenum += 1
        value = int(row[1]) * math.log(int(row[0]))
        if value > max_value:
            max_value = value
            max_linenum = linenum

csvfile.close()

print max_linenum
