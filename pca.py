import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from matr import matr_mult


def matr_pca(A):
    # Take the whole dataset consisting of d+1 dimensions, scale it
    # and ignore the labels such that our new dataset becomes d dimensional.

    A_scaled = StandardScaler().fit_transform(np.array(A))

    # Compute the mean for every dimension of the whole dataset.
    A_mean = np.mean(A, axis=0)

    # Compute the covariance matrix of the whole dataset.
    A_scaled_tr = A_scaled.T
    covariance_matrix = np.cov(A_scaled_tr)
    # Compute eigenvectors and the corresponding eigenvalues.
    eig_vals, eig_vecs = np.linalg.eig(covariance_matrix)
    # k eigenvectors with the largest eigenvalues to form a d × k dimensional matrix
    zipped_lists = zip(eig_vals.real, eig_vecs)
    sorted_zipped_lists = sorted(zipped_lists)
    W = [element for _, element in sorted_zipped_lists]
    # Use this d × k eigenvector matrix to transform the samples onto the new subspace.
    result = pd.DataFrame(columns=['PC1', 'PC2'])
    result['PC1'] = A_scaled.dot(np.array(W).T[0])
    result['PC2'] = A_scaled.dot(np.array(W).T[1])
    return result


if __name__ == '__main__':
    A = [[1, 2, 5],
         [3, 5, 6],
         [7, 8, 10]]
    print(matr_pca(A))
