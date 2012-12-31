#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def gcd(a, b):
    if a == 1 or b == 1:
        return 1
    if a == b:
        return a
    else:
        aa = max(a, b)
        bb = min(a, b)
        c = aa%bb
        if c==0:
            return bb
        else:
            return gcd(c, bb)

def smallest_multiple(n):
    m = 1
    for i in range(1,n+1):
        if (m % i):
            g = gcd(m, i)
            m = m * (i / g)
        print 'f(%d) = %d' % (i, m)

    return m

print smallest_multiple(int(sys.argv[1]))
