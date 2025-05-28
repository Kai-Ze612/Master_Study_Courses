"""Creating an SDF grid"""
import numpy as np


def sdf_grid(sdf_function, resolution):
    """
    Create an occupancy grid at the specified resolution given the implicit representation.
    :param sdf_function: A function that takes in a point (x, y, z) and returns the sdf at the given point.
    Points may be provides as vectors, i.e. x, y, z can be scalars or 1D numpy arrays, such that (x[0], y[0], z[0])
    is the first point, (x[1], y[1], z[1]) is the second point, and so on
    :param resolution: Resolution of the occupancy grid
    :return: An SDF grid of specified resolution (i.e. an array of dim (resolution, resolution, resolution) with positive values outside the shape and negative values inside.
    """

    # ###############
    # TODO: Implement
    coordinates = np.linspace(-1, 1, resolution)
    x, y, z = np.meshgrid(coordinates, coordinates, coordinates, indexing='ij')
    
    # Flatten the coordinate grids to 1D arrays
    x_flat = x.flatten()
    y_flat = y.flatten()
    z_flat = z.flatten()
    
    # Call SDF function with flattened coordinates
    sdf_values_flat = sdf_function(x_flat, y_flat, z_flat)
    
    # Reshape back to 3D grid
    sdf_values = sdf_values_flat.reshape(resolution, resolution, resolution)
    
    return sdf_values
    # ###############
