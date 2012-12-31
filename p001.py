#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

x = int(sys.argv[1])

def f1(x):
    m = []
    for i in range(x):
        if not(i%3) or not(i%5):
            m.append(i)

    return sum(m)

def f2(x):
    x -= 1
    max3 = x - (x % 3)
    max5 = x - (x % 5)
    max15 = x - (x % 15)
    sum3 = (3 + max3) * max3 / 3 / 2
    sum5 = (5 + max5) * max5 / 5 / 2
    sum15 = (15 + max15) * max15 / 15 / 2

    return sum3 + sum5 - sum15

print 'brute force: %d' % f1(x)
print 'tricky calc: %d' % f2(x)
