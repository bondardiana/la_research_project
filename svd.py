from matr import matr_mult
import scipy.linalg as la
import math
import numpy as np


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
    S = np.sqrt(U_val.real)
    # print(U_val)
    # print(V_val)
    U = matr_transposed(U)
    U.reverse()
    S = list(S)
    S.reverse()
    Vtt = [list(Vt[0])]
    Vtt += [[-x for x in Vt[i]] for i in range(1, len(Vt))]
    return U, Vtt, S


if __name__ == '__main__':
    A = [[1, 2, 4],
         [4, 5, 6]]
    U, Vt, S = matr_svd(A)
    # U2, D2, V2 = np.linalg.svd(A)
    # print(U2)
    print('A=', end='')
    for i in A:
        print(i)
    print()
    print('U=', end='')
    for i in U:
        print(i)
    print()
    # print(V2)
    print('Vt=', end='')
    for i in Vt:
        print(i)
    print()
    # print(D2)
    print()
    At = matr_transposed(A)
    print('At=', end='')
    for i in At:
        print(i)
    print()
