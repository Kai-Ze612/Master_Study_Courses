import numpy as np

def swap_rows(A, i, j):
    '''
    Inputs:
    - A: numpy.ndarray, matrix
    - i: int, index of the first row
    - j: int, index of the second row

    Outputs:
    - numpy.ndarray, matrix with swapped rows
    '''
    A[[i, j]] = A[[j, i]]
    return A

def multiply_row(A, i, scalar):
    '''
    Inputs:
    - A: numpy.ndarray, matrix
    - i: int, index of the row
    - scalar: float, scalar to multiply the row with

    Outputs:
    - numpy.ndarray, matrix with multiplied row
    '''
    A[i] = A[i] * scalar
    return A

def add_row(A, i, j, scalar=1):
    '''
    Inputs:
    - A: numpy.ndarray, matrix
    - i: int, index of the row to be added to
    - j: int, index of the row to be added

    Outputs:
    - numpy.ndarray, matrix with added rows
    '''
    A[i] = A[i] + A[j]*scalar
    return A

def perform_gaussian_elemination(A):
    '''
    Inputs:
    - A: numpy.ndarray, matrix of shape (dim, dim)

    Outputs:
    - ops: List[Tuple[str,int,int]], sequence of elementary operations
    - A_inv: numpy.ndarray, inverse of A
    '''
    dim = A.shape[0]
    A_inv = np.eye(dim)
    ops = []
    ########################################################################
    # TODO:                                                                #
    # Implement the Gaussian elemination algorithm.                        #
    # Return the sequence of elementary operations and the inverse matrix. #
    #                                                                      #
    # The sequence of the operations should be in the following format:    #
    # • to swap to rows                                                    #
    #   ("S",<row index>,<row index>)                                      #
    # • to multiply the row with a number                                  #
    #   ("M",<row index>,<number>)                                         #
    # • to add multiple of one row to another row                          #
    #   ("A",<row index i>,<row index j>, <number>)                        #
    # Be aware that the rows are indexed starting with zero.               #
    # Output sufficient number of significant digits for numbers.          #
    # Output integers for indices.                                         #
    #                                                                      #
    # Append to the sequence of operations                                 #
    # • "DEGENERATE" if you have successfully turned the matrix into a     #
    #   form with a zero row.                                              #
    # • "SOLUTION" if you turned the matrix into the $[I|A −1 ]$ form.     #
    #                                                                      #
    # If you found the inverse, output it as a second element,             #
    # otherwise return None as a second element                            #
    ########################################################################

    A_aug = np.hstack((A.copy(), np.eye(dim)))
   
    # Forward elimination
    for i in range(dim):
        # Find pivot row
        max_row = i
        for k in range(i + 1, dim):
            if abs(A_aug[k, i]) > abs(A_aug[max_row, i]):
                max_row = k
        
        # Check if the pivot is approximately zero (matrix is singular)
        if abs(A_aug[max_row, i]) < 1e-10:
            ops.append("DEGENERATE")
            return ops, None
        
        # Swap rows if needed
        if max_row != i:
            A_aug = swap_rows(A_aug, i, max_row)
            ops.append(("S", i, max_row))
        
        # Scale the pivot row to make the pivot element 1
        pivot = A_aug[i, i]
        A_aug = multiply_row(A_aug, i, 1.0 / pivot)
        ops.append(("M", i, 1.0 / pivot))
        
        # Eliminate other rows
        for j in range(dim):
            if j != i:
                factor = -A_aug[j, i]
                A_aug = add_row(A_aug, j, i, factor)
                ops.append(("A", j, i, factor))
    
    # Extract the inverse matrix from the augmented matrix
    A_inv = A_aug[:, dim:2*dim]
    
    # Verify the solution
    # Check if A * A_inv is close to the identity matrix
    product = np.dot(A, A_inv)
    identity = np.eye(dim)
    if np.allclose(product, identity, rtol=1e-10, atol=1e-10):
        ops.append("SOLUTION")
    else:
        ops.append("DEGENERATE")
        A_inv = None
    
    return ops, A_inv
    pass

    ########################################################################
    #                           END OF YOUR CODE                           #
    ########################################################################
