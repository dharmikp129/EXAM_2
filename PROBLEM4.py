# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 17:42:29 2022

@author: dharm
"""

def discharge():
    n = float(input("n = Manning's value = "))
    S = float(input("S = Channel's slope = "))
    u = input("unit of width/height (m or ft)= ")
    b = float(input("b = bottom width = "))
    h = float(input("h = water depth = "))
    k = 1
    u1 = "Cumecs"
    if u.lower() == "ft":
        u1 = "cfs"
    if u.lower() == "ft":
        k = 1.49

    Q = (k/n) * (b * h) * (b * h / (2.0 * h + b)) ** (2.0 / 3.0) * S ** (0.5)
    Q = round(Q,3)
    print(f' Q = {Q} {u1}')
    return Q
print('''
    Manning's Formula for discharge in rectangular channel Q = (k * A * R^(2/3) * S^0.5) / n
        Q = Flow Rate, (in cfs, or m)
        k = 1.49 for discharge in cfs, and 1 for in cumecs
        A = Area of section = b*h , b = bottom width, h = water depth
        R = hydraulic Radius = Area/Wetted Perimeter = bh/(2h+b)
        n = Manning's Roughness coefficient
        ''')

print(f'Inputs needed to calculate the discharge Q')
discharge()