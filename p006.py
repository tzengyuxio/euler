#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def sum_of_sq(n):
    l = []
    for i in range(1, n+1):
        l.append(i**2)

    return sum(l)

def sq_of_sum(n):
    s = (1+n)*n/2
    return s**2

n = int(sys.argv[1])
print abs(sum_of_sq(n) - sq_of_sum(n))
