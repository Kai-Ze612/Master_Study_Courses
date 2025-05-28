
import numpy as np

def meeting_point_linear(pts_list):
    '''
    Inputs:
    - pts_list: List[numpy.ndarray], list of each persons points in the space
    Outputs:
    - numpy.ndarray, meeting point or vectors spanning the possible meeting points of shape (m, dim_intersection)
    '''
    A = pts_list[0] # person A's points of shape (m,num_pts_A)
    B = pts_list[1] # person B's points of shape (m,num_pts_B)

    ########################################################################
    # TODO:                                                                #
    # Implement the meeting point algorithm.                               #
    #                                                                      #
    # As an input, you receive                                             #
    # - for each person, you receive a list of landmarks in their subspace.#
    #   It is guaranteed that the landmarks span each person’s whole       #
    #   subspace.                                                          #
    #                                                                      #
    # As an output,                                                        #
    # - If such a point exist, output it.                                  #
    # - If there is more than one such point,                              # 
    #   output vectors spanning the space.                                 #
    ########################################################################
    
    ## We need to find the intersection of the two subspaces.
    ## The intersection of two subspaces is the set of all vectors that belong to both subspaces. It is also a subspace.
    ## In the other words, we need to find v = linear_combination(basis_A) = linear_combination(basis_B)
    
    u_A, sigma_A, Vt_A = np.linalg.svd(A, full_matrices=False)
    u_B, sigma_B, Vt_B = np.linalg.svd(B, full_matrices=False)
    
    ## To find the basis of A and B, we need to find the non-zero singular values
    ## The non-zero singular values are the ones that correspond to the non-zero singular vectors, which are the basis vectors.
    rank_A = np.sum(sigma_A > 1e-10)
    rank_B = np.sum(sigma_B > 1e-10)
    
    ## columns of u_A and u_B are the basis vectors of A and B respectively
    basis_A = u_A[:, :rank_A]
    basis_B = u_B[:, :rank_B]
    
    ## The orthogonal complement of a subspace S is the set of all vectors that are perpendicular (orthogonal) to every vector in S
    ## Given a subspace S, the orthonormal basis contains in the columns of the materix A
    ## The projection matrix P of a subspace S is given by P = A * A^T
    ## The orthogonal complement of a subspace S is given by P_orth = I - P
    ## We need to find the intersection of the two subspaces.
    orth_A = np.eye(A.shape[0]) - np.dot(basis_A, basis_A.T)
    orth_B = np.eye(B.shape[0]) - np.dot(basis_B, basis_B.T)
    
    stacked = np.vstack((orth_A, orth_B))

    ## Find the null space of the stacked matrix
    u, sigma, Vt = np.linalg.svd(stacked, full_matrices=True)
    rank_stacked = np.sum(sigma > 1e-10)
    null_basis = Vt[rank_stacked:, :].T
    
    # Check dimension of intersection
    null_dim = null_basis.shape[1]
    
    # For zero-dimensional intersection (only the origin)
    # Return an array with correct shape for empty intersection
    if null_dim == 0:
        return np.zeros((A.shape[0], 1))  # Empty array with m rows and 0 columns
    
    # If the intersection is 1-dimensional, return a single point
    if null_dim == 1:
        point = null_basis.flatten()
        norm = np.linalg.norm(point)
        if norm > 1e-10:
            point = point / norm
        return point.reshape(-1, 1)
    
    # Otherwise return the basis for the intersection
    return null_basis

    ########################################################################
    #                           END OF YOUR CODE                           #
    ########################################################################
