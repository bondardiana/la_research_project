import numpy as np
from sklearn.decomposition import PCA
import pandas as pd


def pca1(A, n_components=2):
    # Compute the mean for every dimension of the whole dataset, mean centering
    A_mean = np.mean(A, axis=0)
    A = A - A_mean
    # Compute the covariance matrix of the whole dataset.
    cov_matrix = np.cov(A.T)
    # Compute eigenvectors and the corresponding eigenvalues.
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    eigenvectors = eigenvectors.T
    # sort and take n eigenvectors with the largest eigenvalues to form a d × n dimensional matrix
    idxs = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idxs]
    eigenvectors = eigenvectors[idxs]
    # store first n eigenvectors
    components = eigenvectors[0:n_components]

    return np.dot(A, components.T)


if __name__ == '__main__':
    A = [[1, 2, 5],
         [3, 5, 6],
         [7, 8, 10]]
    print(pca1(A))
    X = np.array(A)
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(X)
    principalDf = pd.DataFrame(data=principalComponents, columns=[
                               'principal component 1', 'principal component 2'])
    print(principalDf)
