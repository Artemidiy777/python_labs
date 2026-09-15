import numpy as np

def check(mat):
    if len(mat) == 0:
        return 
    
    first_length = len(mat[0])
    for i in mat:
        if len(i) != first_length:
            raise ValueError("матрица рваная")


def transpose(mat):
    check(mat)
    if len(mat) == 0:
        return []
    return np.array(mat).T.tolist()

def row_sums(mat):
    check(mat)
    if len(mat) == 0:
        return []
    return np.array(mat).sum(axis=1).tolist()

def col_sums(mat):
    check(mat)
    if len(mat) == 0:
        return []
    return np.array(mat).sum(axis = 0).tolist()