"""
1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

1 2    -->    3 1
3 4           4 2

123     741
456 --> 852
789     963

"""
import numpy as np
import copy

def rotate_matrix(M):
    N = len(M)
    n_layers = int(N/2)
    for l in range(n_layers):
        start = l
        last = N - start - 1
        for i in range(start, last):
            # top M[start][i]
            # right M[i][last]
            # bottom M[last][last - (i - start)]
            # left M[last - (i - start)][start]
            temp = copy.deepcopy(M[start][i])
            print(temp)
            # left to top
            M[start][i] = copy.deepcopy(M[last - (i - start)][start])
            # bottom to left
            M[last - (i - start)][start] = copy.deepcopy(M[last][last - (i - start)])
            # right to bottom
            M[last][last - (i - start)] = copy.deepcopy(M[i][last])
            # top to right
            M[i][last] = copy.deepcopy(temp)

    return M

inputs = [[[1,2],[3,4]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]]

for M in inputs:
    print(np.array(rotate_matrix(M)))