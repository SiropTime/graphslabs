import scipy
import numpy as np

from random import randint

if __name__ == '__main__':
    n = int(input("Введите размерность матрицы: "))
    row = np.array([randint(1, n-1) for i in range(n-1)])
    col = np.array([randint(1, n-1) for j in range(n-1)])
    data = np.array([randint(1, 1000) for k in range(n-1)])
    sparse_matrix: scipy.sparse.csc_matrix = scipy.sparse.csc_matrix((data, (row, col)), shape=(n, n)).toarray()
    print(sparse_matrix)
    pre = [sparse_matrix[i,j] if (i + j) % 2 == 0 else 0 for i, j in zip(*sparse_matrix.nonzero())]
    res = sum(pre)
    print(res)
