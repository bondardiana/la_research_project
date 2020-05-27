def matr_mult(A, B):
    if len(A[0]) != len(B):
        print(A)
        print(B)
        return 'Error, not suitable matrices'

    result = [[0]*len(B[0]) for x in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


if __name__ == '__main__':
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    B = [[1, 2, 3, 4],
         [8, 7, 6, 5],
         [9, 10, 11, 12]]
    M = matr_mult(A, B)
    print('A=', end='')
    for i in A:
        print(i)
    print()
    print('B=', end='')
    for i in B:
        print(i)
    print()
    print('M=', end='')
    for i in M:
        print(i)
