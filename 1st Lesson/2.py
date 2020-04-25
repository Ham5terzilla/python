from math import *
t=float(input())
x=float(input())
print(round(((9*pi*t + 10*cos(x)) / (t**0.5 - abs(sin(t))) * e**x), 2))