""" Procrustes Aligment for point clouds """
import numpy as np
from pathlib import Path


def procrustes_align(pc_x, pc_y):
    """
    calculate the rigid transform to go from point cloud pc_x to point cloud pc_y, assuming points are corresponding
    :param pc_x: Nx3 input point cloud
    :param pc_y: Nx3 target point cloud, corresponding to pc_x locations
    :return: rotation (3, 3) and translation (3,) needed to go from pc_x to pc_y
    """
    R = np.zeros((3, 3), dtype=np.float32)
    t = np.zeros((3,), dtype=np.float32)

    # TODO: Your implementation starts here ###############
    # 1. get centered pc_x and centered pc_y
    # 2. create X and Y both of shape 3XN by reshaping centered pc_x, centered pc_y
    # 3. estimate rotation
    # 4. estimate translation
    # R and t should now contain the rotation (shape 3x3) and translation (shape 3,)
    # TODO: Your implementation ends here ###############
    
    centroid_x = np.mean(pc_x, axis=0)
    centroid_y = np.mean(pc_y, axis=0)
    
    centered_x = pc_x - centroid_x
    centered_y = pc_y - centroid_y
    
    # 2. create X and Y both of shape 3XN by reshaping centered pc_x, centered pc_y
    X = centered_x.T  # Shape: 3 x N
    Y = centered_y.T  # Shape: 3 x N
    
    # 3. estimate rotation using SVD
    # Compute cross-covariance matrix H = X * Y^T
    H = np.dot(X, Y.T)  # Shape: 3 x 3
    
    # Perform SVD: H = U * S * V^T
    U, S, Vt = np.linalg.svd(H)
    
    # Compute rotation matrix: R = V * U^T
    R = np.dot(Vt.T, U.T)
    
    # Ensure proper rotation (determinant = 1, not reflection)
    if np.linalg.det(R) < 0:
        Vt[-1, :] *= -1
        R = np.dot(Vt.T, U.T)
    
    # 4. estimate translation
    # t = centroid_y - R * centroid_x
    t = centroid_y - np.dot(R, centroid_x)
    
    # Convert to correct data types
    R = R.astype(np.float32)
    t = t.astype(np.float32)
    
    # R and t should now contain the rotation (shape 3x3) and translation (shape 3,)
    # TODO: Your implementation ends here ###############
    
    t_broadcast = np.broadcast_to(t[:, np.newaxis], (3, pc_x.shape[0]))
    print('Procrustes Aligment Loss: ', np.abs((np.matmul(R, pc_x.T) + t_broadcast) - pc_y.T).mean())
    
    return R, t


def load_correspondences():
    """
    loads correspondences between meshes from disk
    """

    load_obj_as_np = lambda path: np.array(list(map(lambda x: list(map(float, x.split(' ')[1:4])), path.read_text().splitlines())))
    path_x = (Path(__file__).parent / "resources" / "points_input.obj").absolute()
    path_y = (Path(__file__).parent / "resources" / "points_target.obj").absolute()
    return load_obj_as_np(path_x), load_obj_as_np(path_y)
