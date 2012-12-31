#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# b = number of blue disc 
# t = total disc number of blue and red
#
# when t is large enough, b is near (and greater than) t * 0.5^0.5
import math

c = .5**.5
t = 10      # total
tsb = 0     # t-b
tpbs1 = 0   # t+b-1
while t < 1000000000000:
    if tsb == 0:
        b = int(math.ceil(t * c))
        if t * (t-1) == b * (b-1) * 2:
            print 'blue/total = %d / %d (first)' % (b,t)
            tsb = t-b
            tpbs1 = t+b-1
        else:
            t += 1

    else:
        t = int(math.floor(tpbs1 / (1-c)))
        b = int(math.ceil(t * c))
        while t-b != tpbs1:
            t += 1
            b = int(math.ceil(t * c))
        print 'blue/total = %d / %d' % (b,t)
        tsb = t-b
        tpbs1 = t+b-1
