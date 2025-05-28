import numpy as np
def get_null_vector(D):
    '''
    Inputs:
    - D: numpy.ndarray, matrix of shape (m,n)
    Outputs:
    - null_vector: numpy.ndarray, matrix of shape (dim_kern,n)
    '''

    ########################################################################
    # TODO:                                                                #
    # Get the kernel of the matrix D.                                      #
    # the kernel should consider the numerical errors.                     #
    ########################################################################

    # The kernel of a matrix D is the set of all vectors x such that D*x = 0.
    # The kernel is also a subspace of the vector space.
    # The null space corresponds to the 0 singular values of the matrix D.
    
    u, sigma, vt = np.linalg.svd(D, full_matrices=True)
    rank = np.sum(sigma > 1e-10)
    null_vector = vt[rank:, :]
    
   
    # As alternaltive, we can use the null space function from scipy
    # from scipy.linalg import null_space
    # null_vector = linalg.null_space(D)
    pass

    ########################################################################
    #                           END OF YOUR CODE                           #
    ########################################################################
    return null_vector
