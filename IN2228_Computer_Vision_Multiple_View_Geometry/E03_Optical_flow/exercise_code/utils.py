
from scipy.signal import convolve2d as conv2
import numpy as np
import cv2

def getGaussiankernel(sigma):
    """
    Compute the 2D Gaussian kernel
    
    Args:
        sigma (float): Standard deviation of Gaussian
        
    Returns:
        G (numpy.ndarray): Gaussian kernel of shape (4*sigma+1, 4*sigma+1)
    """
    k = int(np.ceil(4 * sigma + 1))
    # Ensure odd kernel size
    if k % 2 == 0:
        k += 1
    
    # Create coordinate arrays centered at origin
    half_k = k // 2
    x = np.arange(-half_k, half_k + 1)
    y = np.arange(-half_k, half_k + 1)
    
    # Create 2D coordinate grids
    X, Y = np.meshgrid(x, y)
    
    # Compute 2D Gaussian kernel using separability
    # G(x,y) = exp(-(x^2 + y^2)/(2*sigma^2))
    G = np.exp(-(X**2 + Y**2) / (2 * sigma**2))
    
    # Normalize so sum equals 1
    G = G / np.sum(G)
    
    return G

def getGradients(I, sigma=2):
    """
    Compute spatial gradients - CORRECTED VERSION
    """
    I_ = I.copy().astype(np.float64)
    I_ = I_ / 255.0
    
    if sigma > 0:
        k = int(np.ceil(4 * sigma + 1))
        if k % 2 == 0:
            k += 1
        I_ = cv2.GaussianBlur(I_, (k, k), sigmaX=sigma, sigmaY=sigma, borderType=cv2.BORDER_REFLECT)

    # FIXED: Flip the kernel signs
    kernel_x = np.array([[1, 0, -1]]) / 2.0  # Changed from [-1, 0, 1]
    kernel_y = np.array([[1], [0], [-1]]) / 2.0  # Changed from [[-1], [0], [1]]
    
    Ix = conv2(I_, kernel_x, mode='same', boundary='symm')
    Iy = conv2(I_, kernel_y, mode='same', boundary='symm')

    return Ix, Iy


def getTemporalPartialDerivative(I1, I2, sigma=2):
    """
    Compute temporal gradient - CHECK SIGN
    """
    I1_ = I1.copy().astype(np.float64)
    I2_ = I2.copy().astype(np.float64)
    I1_ = I1_ / 255.0
    I2_ = I2_ / 255.0
    
    if sigma > 0:
        k = int(np.ceil(4 * sigma + 1))
        if k % 2 == 0:
            k += 1
        I1_ = cv2.GaussianBlur(I1_, (k, k), sigmaX=sigma, sigmaY=sigma, borderType=cv2.BORDER_REFLECT)
        I2_ = cv2.GaussianBlur(I2_, (k, k), sigmaX=sigma, sigmaY=sigma, borderType=cv2.BORDER_REFLECT)

    # Standard temporal gradient
    It = I2_ - I1_

    return It

def getM(Ix, Iy, sigma=7):
    """
    Compute structure tensor M for Lucas-Kanade method
    
    Args:
        Ix (numpy.ndarray): Image gradient in x-direction of shape (H, W)
        Iy (numpy.ndarray): Image gradient in y-direction of shape (H, W)
        sigma (float): Standard deviation for Gaussian weighting
        
    Returns:
        M (numpy.ndarray): Structure tensor of shape (H, W, 2, 2)
    """
    G = getGaussiankernel(sigma)
    
    # Compute elements of structure tensor
    # M = [Ix*Ix  Ix*Iy]
    #     [Ix*Iy  Iy*Iy]
    
    # Element-wise products
    IxIx = Ix * Ix
    IxIy = Ix * Iy
    IyIy = Iy * Iy
    
    # Convolve with Gaussian kernel to get local weighted sums
    M11 = conv2(IxIx, G, mode='same', boundary='symm')
    M12 = conv2(IxIy, G, mode='same', boundary='symm')
    M22 = conv2(IyIy, G, mode='same', boundary='symm')

    # Stack into 2x2 matrix for each pixel
    # Note: M21 = M12 due to symmetry
    M = np.stack((M11, M12, M12, M22), axis=-1)
    M = M.reshape(M.shape[0], M.shape[1], 2, 2)
    
    assert(np.allclose(M[:,:,0,1], M12))
    assert(np.allclose(M[:,:,1,0], M12))
    assert(np.allclose(M[:,:,0,0], M11))
    assert(np.allclose(M[:,:,1,1], M22))

    return M

def getq(It, Ix, Iy, sigma=7):
    """
    Compute q vector for Lucas-Kanade method
    
    Args:
        It (numpy.ndarray): Temporal gradient of shape (H, W)
        Ix (numpy.ndarray): Image gradient in x-direction of shape (H, W)
        Iy (numpy.ndarray): Image gradient in y-direction of shape (H, W)
        sigma (float): Standard deviation for Gaussian weighting
        
    Returns:
        q (numpy.ndarray): q vector of shape (H, W, 2)
    """
    G = getGaussiankernel(sigma)
    
    # Compute elements of q vector
    # q = [Ix*It]
    #     [Iy*It]
    
    # Element-wise products
    IxIt = Ix * It
    IyIt = Iy * It
    
    # Convolve with Gaussian kernel to get local weighted sums
    q1 = conv2(IxIt, G, mode='same', boundary='symm')
    q2 = conv2(IyIt, G, mode='same', boundary='symm')

    # Create vector for each pixel
    q = np.stack((q1, q2), axis=-1)
    
    assert(np.allclose(q[:,:,0], q1))
    assert(np.allclose(q[:,:,1], q2))

    return q