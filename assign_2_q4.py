# Write a code to compute matrix-vector multiplication of any given size.
import numpy


def vector_multiplication(a, b):
    # n = len(vector1[0])
    multiplication_result = 0
    for i in range(0, n, 1):
        multiplication_result = multiplication_result + a[0][i]*b[i][0]
    return multiplication_result


n = int(input('enter the size of vector '))
vector1 = numpy.random.randint(1, 10, size=(1, n))
vector2 = numpy.random.randint(1, 10, size=(n, 1))

print(vector1)
print()
print(vector2)
print()
print('The vector multiplication result is ', vector_multiplication(vector1, vector2))
