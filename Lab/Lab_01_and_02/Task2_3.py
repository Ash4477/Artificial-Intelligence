from math import *

def func(x, h):
    return (sin(x + h) - sin(x)) / h


x_values = [i * 0.001 for i in range(int(-pi * 1000), int(pi * 1000))]
h_values = [0.001, 0.01, 0.1]



for h in h_values:
    print(f"--- h = {h} ---")
    for x in x_values:
        f1 = func(x, h)
        f2 = cos(x)
        print(f"x = {x:.3f}, d/dx sin(x) = {f1:.6f}, cos(x) = {f2:.6f}, Difference = {abs(f1 - f2):.6f}")
