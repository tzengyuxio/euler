#!/usr/bin/python
# -*- coding: utf-8 -*-

def is_palindromic(n):
    sn = str(n)
    sz = len(sn)
    if sz%2:   # odd
        half = sz/2
        return sn[:half] == sn[half+1:][::-1] 
    else:           # even
        half = sz/2
        return (sn[:half] == sn[half:][::-1])

max_palindromic = 0
for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        m = x * y
        if m < max_palindromic:
            break
        if is_palindromic(m):
            max_palindromic = m
            print '%d x %d = %d' % (x, y, m)
            break
