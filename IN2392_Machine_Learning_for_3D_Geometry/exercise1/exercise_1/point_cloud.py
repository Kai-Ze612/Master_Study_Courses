"""Triangle Meshes to Point Clouds"""
import numpy as np


def sample_point_cloud(vertices, faces, n_points):
    """
    Sample n_points uniformly from the mesh represented by vertices and faces
    :param vertices: Nx3 numpy array of mesh vertices
    :param faces: Mx3 numpy array of mesh faces
    :param n_points: number of points to be sampled
    :return: sampled points, a numpy array of shape (n_points, 3)
    """

    # ###############
    # TODO: Implement
    v_0 = vertices[faces[:, 0]]
    v_1 = vertices[faces[:, 1]]
    v_2 = vertices[faces[:, 2]]
    
    cross_product = np.cross(v_1 - v_0, v_2 - v_0)
    triangle_areas = 0.5 * np.linalg.norm(cross_product, axis=1)
    
    triangle_probabilities = triangle_areas / np.sum(triangle_areas)
    triangle_indices = np.random.choice(len(faces), size=n_points, p=triangle_probabilities)
    
    r1 = np.random.random(n_points)
    r2 = np.random.random(n_points)
    sqrt_r1 = np.sqrt(r1)
    u = 1 - sqrt_r1
    v = sqrt_r1 * (1 - r2)
    w = sqrt_r1 * r2
    
    selected_v0 = vertices[faces[triangle_indices, 0]]
    selected_v1 = vertices[faces[triangle_indices, 1]]
    selected_v2 = vertices[faces[triangle_indices, 2]]
    
    sampled_points = u[:, np.newaxis] * selected_v0 + v[:, np.newaxis] * selected_v1 + w[:, np.newaxis] * selected_v2
    
    return sampled_points
    # ###############
