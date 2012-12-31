#!/usr/bin/python
# -*- coding: utf-8 -*-

f = []
f.append(1)
f.append(2)

n = f[-1] + f[-2]
while n < 4000000:
    f.append(n)
    n = f[-1] + f[-2]

even_f = [x for x in f if (x%2)==0]

print sum(even_f)
