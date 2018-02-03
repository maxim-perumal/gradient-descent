import random
from math_function import *

scale = 10

f1 = polynomial_deg4(1,1,-13,-1,12)
x1 = random.randint(-3*scale,-1*scale)
x2 = random.randint(1*scale,3*scale)

step = 1000
accuracy = 0.01

while (step > accuracy):
    if (f1.derivative(x1) > 0):
        x1 -= step
    elif (f1.derivative(x1) < 0):
        x1 += step
    if (f1.derivative(x2) > 0):
        x2 -= step
    elif (f1.derivative(x2) < 0):
        x2 += step
    step -= accuracy

if (f1.y(x1) - f1.y(x2) < 0):
    print(x1)
else:
    print(x2)
