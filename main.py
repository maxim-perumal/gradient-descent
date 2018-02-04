import random
from math_function import *

f1 = polynomial_deg4(1,1,-13,-1,12)

random_point = [-5,0,5]
j = 0

while (j < len(random_point)):
    step = 1
    previous_state = -1 # -1 mean no previous state

    i = 0

    while(step > 0.01) :
        if (f1.derivative(random_point[j]) > 0):
            if (previous_state == 0):
                step -= step/10
            random_point[j] -= step
            previous_state = 1
        elif (f1.derivative(random_point[j]) < 0):
            if (previous_state == 1):
                step += step/10
            random_point[j] += step
            previous_state = 0
    j += 1

print (random_point)
