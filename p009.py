#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# --------------------------------------
#
#    a^2 + b^2 = c^2
#    a + b + c = 1000
#
# => a * b = 1000 * (500 - c)
# => a + b > c
# => c < 500

for c in range(499, 0, -1):
    aandb = 1000 - c
    for a in range(1, aandb/2+1):
        b = aandb - a
        if a + c < b:
            continue
        if a * b % 1000 != 0:
            continue
        if a*a + b*b == c*c:
            print '(a, b, c) = (%d, %d, %d)' % (a, b, c)
            print 'a*b*c = %d' % (a*b*c)
            break
