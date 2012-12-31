#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def is_prime(n):
    mid = int(n ** 0.5)
    
    if n == mid * mid:
        return False

    for i in range(3, mid+1, 2):
        if n % i == 0:
            return False

    return True

c = 1 # count
s = 3 # start

#while c < 10001:
print '[1] 2'
while c < 10001:
    if is_prime(s):
        c += 1
        print '[%d] %d' % (c, s)

    s += 2
