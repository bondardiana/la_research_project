import numpy as np
from svd import matr_transposed
from matr import matr_mult

import scipy.linalg as la


def matr_pca(A):
    # 1.Take the whole dataset consisting of d+1 dimensions
    # and ignore the labels such that our new dataset becomes d dimensional.

    # 2.Compute the mean for every dimension of the whole dataset.
    A_mean = np.mean(A, axis=0)
    # print(A_mean)
    # 3.Compute the covariance matrix of the whole dataset.
    A_covMatrix = np.cov(A, bias=True)
    # print(A_covMatrix)
    # 4.Compute eigenvectors and the corresponding eigenvalues.
    A_val, A_vec = la.eig(A)
    A_val_real = A_val.real
    # 5.Sort the eigenvectors by decreasing eigenvalues and choose
    # k eigenvectors with the largest eigenvalues to form a d × k dimensional matrix W.
    zipped_lists = zip(A_val_real, A_vec)
    sorted_zipped_lists = sorted(zipped_lists)[:2]
    W = [element for _, element in sorted_zipped_lists]
    # 6.Use this d × k eigenvector matrix to transform the samples onto the new subspace.
    Wt = matr_transposed(W)
    # print(W)
    return matr_mult(A, Wt)


if __name__ == '__main__':
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    print(matr_pca(A))
