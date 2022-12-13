import scipy
import numpy as np

from random import randint

if __name__ == '__main__':
    n = int(input("Введите размерность матрицы: "))
    row = np.array([randint(0, 100) for i in range(n)])
    col = np.array([randint(0, 100) for j in range(n)])
    data = np.array([randint(0, 100) for k in range(n)])
    sparse_matrix: scipy.sparse.csc_matrix = scipy.sparse.csc_matrix((data, (row, col)), (n, n)).toarray()

    print(sparse_matrix)
