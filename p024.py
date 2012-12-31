#!/usr/bin/python
# -*- coding: utf-8 -*-

def fac(n):
    a = range(1, n+1)
    return reduce(lambda x,y : x*y, a)

d = range(0, 10) # digits list
c = 1000000      # millionth count
r = ''           # result

while d:
    if len(d) == 1:
        r += str(d[i])
    else:
        p = fac(len(d)-1)
        i = c / p
        if c % p == 0:
            i -= 1
        r += str(d[i])
        c = c % p 
    del d[i]

print r
