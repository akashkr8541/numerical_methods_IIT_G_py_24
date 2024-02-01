# Write a code to generate a 10 × 10 random matrix and find out its trace

import numpy


def transpose_matrix(mat):
    row = len(mat)
    col = len(mat[0])
    transpose_mat = numpy.random.randint(0,1, size=(col,row))
    for i in range(0,row,1):
        for j in range(0,col,1):
            transpose_mat[j][i] = mat[i][j]
    return transpose_mat


m = 10
n = 10
mat = numpy.random.randint(0, 10, size=(m, n))
print(mat)
print()
print(transpose_matrix(mat))

# print(numpy.transpose(mat))


