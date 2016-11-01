#!/usr/bin/python

import sys
from math_funcs import *

param = []

for p in sys.argv:
    param.append(p)

param.remove(param[0])

print param

for p in param:
    print primeFactors(p)
