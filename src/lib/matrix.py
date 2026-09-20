"""ЛР2: операции над матрицами (переиспользуемый модуль)."""

import numpy as np


def check(mat: list[list[float]]) -> None:
    """Проверить, что матрица не рваная.

    Raises:
        ValueError: если строки разной длины.
    """
    if len(mat) == 0:
        return

    first_length = len(mat[0])
    for i in mat:
        if len(i) != first_length:
            raise ValueError("матрица рваная")


def transpose(mat: list[list[float]]) -> list[list[float]]:
    """Транспонировать матрицу.

    transpose([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]
    """
    check(mat)
    if len(mat) == 0:
        return []
    return np.array(mat).T.tolist()


def row_sums(mat: list[list[float]]) -> list[float]:
    """Суммы элементов по строкам.

    row_sums([[1, 2, 3], [4, 5, 6]])
    [6, 15]
    """
    check(mat)
    if len(mat) == 0:
        return []
    return np.array(mat).sum(axis=1).tolist()


def col_sums(mat: list[list[float]]) -> list[float]:
    """Суммы элементов по столбцам.

    col_sums([[1, 2, 3], [4, 5, 6]])
    [5, 7, 9]
    """
    check(mat)
    if len(mat) == 0:
        return []
    return np.array(mat).sum(axis=0).tolist()
