#!/usr/bin/python
# -*- coding: utf-8 -*-

def power(n):
    p = 1
    for i in range(n):
        p = p * n % 10000000000
    return p

s = []
for i in range(1,1001):
    s.append(power(i))

print sum(s)%10000000000
