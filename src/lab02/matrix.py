
import numpy as np
#общая функция на рваность
def check(mat):
    if len(mat) == 0:
        return 
    
    first_length = len(mat[0])
    for i in mat:
        if len(i) != first_length:
            raise ValueError("матрица рваная")
#1 
def transpose(mat):
    check(mat)
    if len(mat) == 0:
        return []
    return np.array(mat).T.tolist()

print(transpose([[1, 2, 3]]))    
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))  
print(transpose([])) 
print(transpose([[1, 2], [3]]))

#2
def row_sums(mat):
    check(mat)
    if len(mat) == 0:
        return []
    return np.array(mat).sum(axis=1).tolist()

print(row_sums([[1, 2, 3], [4, 5, 6]]))   
print(row_sums([[-1, 1], [10, -10]]))  
print(row_sums([[0, 0], [0, 0]]))     
print(row_sums([[1, 2], [3]]))      

#3
def col_sums(mat):
    check(mat)
    if len(mat) == 0:
        return []
    return np.array(mat).sum(axis = 0).tolist()

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))  
print(col_sums([[0, 0], [0, 0]]))     
print(col_sums([[1, 2], [3]]))      



