from matr import matr_mult
import scipy.linalg as la
import math


def matr_transposed(A):
    result = [[0]*len(A) for x in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[j][i] = A[i][j]
    return result


def matr_svd(A):
    At = matr_transposed(A)  # Transposed A
    AAt = matr_mult(A, At)  # A multiplied by transposed A
    AtA = matr_mult(At, A)  # Transposed A multiplied by A
    U_val, U = la.eig(AAt)
    V_val, V = la.eig(AtA)
    Vt = matr_transposed(V)
    S = math.sqrt(U_val[0].real)
    # print(U_val)
    # print(V_val)
    return U, Vt, S


if __name__ == '__main__':
    A = [[1, 2, 3],
         [4, 5, 6]]
    print(matr_svd(A))
