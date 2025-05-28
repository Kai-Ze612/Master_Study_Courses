import numpy as np

def solve_linear_equation_SVD(D, b):
    '''
    Inputs:
    - D: numpy.ndarray, matrix of shape (m,n)
    - b: numpy.ndarray, vector of shape (m,)
    Outputs:
    - x: numpy.ndarray, solution of the linear equation D*x = b
    - D_inv: numpy.ndarray, pseudo-inverse of D of shape (n,m)
    '''

    ########################################################################
    # TODO:                                                                #
    # Solve the linear equation D*x = b using the pseudo-inverse and SVD.  #
    # Your code should be able to tackle the case where D is singular.     # 
    ########################################################################

    # The pseudo-inverse of a matrix D is defined as:
    # D_inv = V * S_inv * U^T
    
    u, sigma, vt = np.linalg.svd(D, full_matrices=True)
    
    ## Get dim of D
    m, n = D.shape

    ## S_inv is the pseudo-inverse of sigma
    S_inv = np.zeros((n, m))
    for i in range(min(m, n)):
        if sigma[i] > 1e-10:
            S_inv[i, i] = 1/sigma[i]
    
    ## Calculate the pseudo-inverse of D
    D_inv = vt.T @ S_inv @ u.T
    x = D_inv @ b

    ########################################################################
    #                           END OF YOUR CODE                           #
    ########################################################################

    return x, D_inv

