import random
from math_function import *

f1 = polynomial_deg4(1,1,-13,-1,12)

z = 10000
a = 0

while (z  > 1):
    if (f1.derivative(a) > 0):
        a -= z
    elif (f1.derivative(a) < 0):
        a += z
    z -= 0.001

print(a)
