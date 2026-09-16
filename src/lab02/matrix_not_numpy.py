# общая функция на рваность
def check(mat):
    if len(mat) == 0:
        return
    first_length = len(mat[0])
    for i in mat:
        if len(i) != first_length:
            raise ValueError("матрица рваная")

# 1 — транспонирование
def transpose(mat):
    check(mat)
    if len(mat) == 0:
        return []
    rows = len(mat)
    cols = len(mat[0])
    result = []
    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(mat[row][col])
        result.append(new_row)
    return result


print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))

# 2 — сумма по строкам
def row_sums(mat):
    check(mat)
    result = []
    for row in mat:
        total = 0
        for number in row:
            total += number
        result.append(total)
    return result

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))

# 3 — сумма по столбцам
def col_sums(mat):
    check(mat)
    if len(mat) == 0:
        return []
    cols = len(mat[0])
    result = []
    for col in range(cols):
        total = 0
        for row in mat:
            total += row[col]
        result.append(total)
    return result

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))