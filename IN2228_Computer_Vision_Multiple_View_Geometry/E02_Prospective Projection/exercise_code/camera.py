import numpy as np
from math import tan, atan
from abc import ABC, abstractmethod

def compute_relative_pose(pose_1,pose_2):
    '''
    Inputs:
    - pose_i transform from cam_i to world coordinates, matrix of shape (3,4)
    Outputs:
    - pose transform from cam_1 to cam_2 coordinates, matrix of shape (3,4)
    '''

    ########################################################################
    # TODO:                                                                #
    # Compute the relative pose, which transform from cam_1 to cam_2       #
    # coordinates.                                                         #
    ########################################################################

    R1, T1 = pose_1[:, :3], pose_1[:, 3:4]
    R2, T2 = pose_2[:, :3], pose_2[:, 3:4]
    
    R_real = R2.T @ R1 
    T_real = R2.T @ (T1 - T2)
    
    pose = np.hstack((R_real, T_real))    

    ########################################################################
    #                           END OF YOUR CODE                           #
    ########################################################################

    return pose


class Camera(ABC):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    @abstractmethod
    def project(self, pt):
        """Project the point pt onto a pixel on the screen"""
        
    @abstractmethod
    def unproject(self, pix, d):
        """Unproject the pixel pix into the 3D camera space for the given distance d"""


class Pinhole(Camera):

    def __init__(self, w, h, fx, fy, cx, cy):
        Camera.__init__(self, w, h)
        self.K = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])

    def project(self, pt):
        '''
        Inputs:
        - pt, vector of size 3
        Outputs:
        - pix, projection of pt using the pinhole model, vector of size 2
        '''
        ########################################################################
        # TODO:                                                                #
        # project the point pt, considering the pinhole model.                 #
        ########################################################################

        X, Y, Z = pt[0], pt[1], pt[2]
        
        ## Perspective projection
        x_norm = X / Z
        y_norm = Y / Z
        
        ## apply intrinsic matrix
        u = self.K[0, 0] * x_norm + self.K[0, 2]
        v = self.K[1, 1] * y_norm + self.K[1, 2]

        pix = np.array([u, v])

        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################

        return pix

    def unproject(self, pix, d):
        '''
        Inputs:
        - pix, vector of size 2
        - d, scalar 
        Outputs:
        - final_pt, obtained by unprojecting pix with the distance d using the pinhole model, vector of size 3
        '''
        ########################################################################
        # TODO:                                                                #
        # Unproject the pixel pix using the distance d, considering the pinhole#
        # model. Be careful: d is the distance between the camera origin and   #
        # the desired point, not the depth.                                    #
        ########################################################################

        u, v = pix[0], pix[1]
        
        f_x, f_y = self.K[0, 0], self.K[1, 1]
        c_x, c_y = self.K[0, 2], self.K[1, 2]
        
        # Compute normalized coordinates
        x_norm = (u - c_x) / f_x
        y_norm = (v - c_y) / f_y
        
        direction = np.array([x_norm, y_norm, 1.0])
        
        direction_nrom = np.linalg.norm(direction)
        direction = direction / direction_nrom
        
        final_pt = d * direction
        
        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################
        return final_pt


class Fov(Camera):

    def __init__(self, w, h, fx, fy, cx, cy, W):
        Camera.__init__(self, w, h)
        self.K = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])
        self.W = W

    def project(self, pt):
        '''
        Inputs:
        - pt, vector of size 3
        Outputs:
        - pix, projection of pt using the Fov model, vector of size 2
        '''
        ########################################################################
        # TODO:                                                                #
        # project the point pt, considering the Fov model.                     #
        ########################################################################

        X, Y, Z = pt[0], pt[1], pt[2]
        
        # Step 1: Convert to normalized coordinates (divide by Z)
        x_n = X / Z
        y_n = Y / Z
        
        # Step 2: Calculate undistorted radius in normalized coordinates
        ru = np.sqrt(x_n**2 + y_n**2)
        
        # Step 3: Apply FOV distortion model
        # Based on Devernay-Faugeras FOV model: rd = (1/ω) * arctan(2 * ru * tan(ω/2))
        omega = self.W / 2.0  # W is the full FOV, omega is half-angle
        
        if abs(omega) < 1e-8:
            # When W ≈ 0, use pinhole model
            rd = ru
        else:
            # FOV distortion equation
            if ru < 1e-8:
                rd = 0.0
            else:
                rd = (1.0 / self.W) * np.arctan(2.0 * ru * np.tan(omega))
        
        # Step 4: Apply distortion to normalized coordinates
        if ru > 1e-8:
            scale = rd / ru
            x_d = x_n * scale
            y_d = y_n * scale
        else:
            x_d = 0.0
            y_d = 0.0
        
        # Step 5: Apply intrinsic matrix to get pixel coordinates
        fx, fy = self.K[0, 0], self.K[1, 1]
        cx, cy = self.K[0, 2], self.K[1, 2]
        
        u = fx * x_d + cx
        v = fy * y_d + cy
        
        pix = np.array([u, v])
        
        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################

        return pix

    def unproject(self, pix, d):
        '''
        Inputs:
        - pix, vector of size 2
        - d, scalar 
        Outputs:
        - final_pt, obtained by unprojecting pix with the distance d using the Fov model, vector of size 3
        '''
        ########################################################################
        # TODO:                                                                #
        # Unproject the pixel pix using the distance d, considering the FOV    #
        # model. Be careful: d is the distance between the camera origin and   #
        # the desired point, not the depth.                                    #
        ########################################################################

        u, v = pix[0], pix[1]
        
        # Extract intrinsic parameters
        fx, fy = self.K[0, 0], self.K[1, 1]
        cx, cy = self.K[0, 2], self.K[1, 2]
        
        # Step 1: Convert to normalized coordinates
        x_d = (u - cx) / fx
        y_d = (v - cy) / fy
        
        # Step 2: Calculate distorted radius
        rd = np.sqrt(x_d**2 + y_d**2)
        
        # Step 3: Apply inverse FOV distortion
        # Based on Devernay-Faugeras FOV model: ru = tan(rd * ω) / (2 * tan(ω/2))
        omega = self.W / 2.0  # W is the full FOV, omega is half-angle
        
        if abs(omega) < 1e-8:
            # When W ≈ 0, use pinhole model
            ru = rd
        else:
            # Inverse FOV distortion equation
            if abs(rd) < 1e-8:
                ru = 0.0
            else:
                ru = np.tan(rd * self.W) / (2.0 * np.tan(omega)) # Use self.W in numerator's tan, omega in denominator's tan
        
        # Step 4: Convert back to undistorted normalized coordinates
        if rd > 1e-8:
            scale = ru / rd
            x_n = x_d * scale
            y_n = y_d * scale
        else:
            x_n = 0.0
            y_n = 0.0
        
        # Step 5: Create 3D ray direction vector
        # For pinhole model: ray = [x_n, y_n, 1]
        direction = np.array([x_n, y_n, 1.0])
        
        # Step 6: CRITICAL - Normalize the ray direction before scaling
        direction_norm = np.linalg.norm(direction)
        if direction_norm > 1e-8:
            unit_direction = direction / direction_norm
        else:
            unit_direction = np.array([0.0, 0.0, 1.0])
        
        # Step 7: Scale the normalized direction by the specified distance
        final_pt = d * unit_direction
        

        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################        
        return final_pt
