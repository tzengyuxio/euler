#!/usr/bin/python
# -*- coding: utf-8 -*-

size = 20

g = [] # grid
for i in range(22):
    r = [0 for x in range(22)]
    g.append(r)

g[0][0] = 1

for step in range(1, size*2+1):
    for y in range(min(step, size)+1):
        x = step - y
        # here is some redundent calculation, 
        # the lower-left half side is needless to calculate.
        if x > size or y > size:
            continue
        if y == 0 and x != 0:
            g[x][y] = g[x-1][y]
            g[y][x] = g[x-1][y]
        elif x != 0 and y != 0:
            g[x][y] = g[x-1][y] + g[x][y-1]
            g[y][x] = g[x-1][y] + g[x][y-1]

print g[size][size]
