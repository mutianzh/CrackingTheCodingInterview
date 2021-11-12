"""
1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""
import numpy as np


def zero_matrix(M):

    if not M or len(M) == 0 or len(M[0]) == 0:
        return None

    row_has_zero = False
    col_has_zero = False
    num_row = len(M)
    num_col = len(M[0])

    for i in range(num_row):
        if M[0][i] == 0:
            row_has_zero = True
    for i in range(num_col):
        if M[i][0] == 0:
            col_has_zero = True

    for i in range(1, num_row):
        for j in range(1, num_col):
            if M[i][j] == 0:
                M[i][0] = 0
                M[0][j] = 0

    for c in range(num_col):
        if M[0][c] == 0:
            for r in range(num_row):
                M[r][c] = 0

    for r in range(num_row):
        if M[r][0] == 0:
            for c in range(num_col):
                M[r][c] = 0

    if row_has_zero:
        for i in range(num_col):
            M[0][i] = 0

    if col_has_zero:
        for i in range(num_row):
            M[i][0] = 0

    return M


    return


inputs = [[[1,0,3,4], [0,6,7,8],[9,10,11,0],[13,14,15,16]]]



for input in inputs:
    print(np.array(input))
    print(np.array(zero_matrix(input)))



