# author: JHR 10/04/22

import time
import math

eq1 = time.process_time ()
print(eq1)
eq2 = math.pow(2,2)
print(eq2)
eq3 = time.process_time ()
print(eq3)
eq4 = 2**2
print(eq4)
eq5 = time.process_time ()
print(eq5)

# 0.031555, 0.031616, 0.031623
# More time passes as more lines are ran, number is less than 0.1

eq6 = time.perf_counter ()
print(eq6)
eq7 = math.pow(2,2)
print(eq7)
eq8 = time.perf_counter ()
print(eq8)
eq9 = 2**2
print(eq9)
eq10 = time.perf_counter ()
print(eq10)

# 6129848.560275029, 6129848.560283808, 6129848.560290184
# More time still passes as more lines are ran but number is in the millions 