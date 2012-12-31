#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

factors = []

def large_prime_factor(n):
    n = int(n)
    p = 2
    maxp = p
    while p <= n:
        if (n%p)==0:
            n /= p
            maxp = p
        else:
            p += 1

    return maxp

print large_prime_factor(sys.argv[1])
