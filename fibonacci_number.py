# Assignment 1    question 2
# Write a small code in to print first 20 Fibonacci numbers.

a = 0        # storing first number of Fibonacci series.
b = 1        # storing second number of Fibonacci series.
print(a)
print(b)
n = 3      # starting initial counter from 3 as two terms of series are already printed
while (n <= 20):      # while loop with for printig 20 fibonacci numbers
    c = a+b          # storing next number to be printed in variable 'c'
    print(c)
    a = b         # storing the number before the currently printed number in the series in variable 'a'.
    b = c         # storing the printed number in current loop in variable 'b'.
    n = n+1       # increasing conter by 1.
