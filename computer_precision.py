# Assignment 1  question 1
# Write a small code in to find the machine precession of your personal computer.

import numpy    # importing required library
# Machine precision for single precision
single_precision = numpy.finfo(numpy.float32).eps   # finfo = floating point info
print(f"Single precision machine epsilon: {single_precision}")
# Machine precision for double precision
double_precision = numpy.finfo(numpy.float64).eps
print(f"Double precision if this computer is : {double_precision}")
