#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# note: sieve to filter all the non-prime numbers, may be faster.

def is_prime(n):
    mid = int(n ** 0.5)
    
    if n == mid * mid:
        return False

    for i in range(3, mid+1, 2):
        if n % i == 0:
            return False

    return True

primes = [2]
s = 3 # start

while s < 2000000:
    if is_prime(s):
        primes.append(s)
    s += 2

print sum(primes)
