#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

# according to the fact:
#
#    F(n+1)/(Fn) will approach 1.618
#
# calculate the x of 'F(n) * 1.618^x > 10^100'

fib = []
fib.append(0) # fib(0)
fib.append(1) # fib(1)
fib.append(1) # fib(2)

# generate some fib numbers
for i in range(20):
    fib.append(fib[-1]+fib[-2])

# find a better start point than fib(1)
si = 0 # start index
sn = 0 # start num
sd = 0 # start digits
for i in range(len(fib)):
    if i > 3:
        d = float(fib[i]) / fib[i-1]
        if abs(d - 1.618034) < 0.000001:
            si, sn, sd = i, fib[i], len(str(sn))
            break

#print 'fib(%d) = %d (%d digits)' % (si, sn, sd)
# the start point is fib[17]=1597

# transform sn to a float between [1-10)
sn = sn / 10.0**(sd-1)

while sd < 1000:
    sn *= 1.618034
    si += 1
    if sn > 10:
        sn /= 10
        sd += 1

print si
