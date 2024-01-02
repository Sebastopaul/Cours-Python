# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 12:42:25 2024

@author: sebay
"""

import math

def sin(x):
    sin = 0
    for n in range(60):
        sin += ((-1)**n * x**(2*n + 1)) / (math.factorial(2*n + 1))
    return sin

def cos(x):
    cos = 0
    for n in range(60):
        cos += ((-1)**n * x**(2*n)) / (math.factorial(2*n))
    return cos

def pi():
    pi = 0
    for n in range(190000000):
        pi += 4 * (((-1)**n)/(2*n+1))
    return pi

x = math.radians(100)

print('sin')
print(sin(x))
print(math.sin(x))

print('\ncos')
print(cos(x))
print(math.cos(x))

print('\npi')
print(pi())
print(math.pi)
