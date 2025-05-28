import numpy as np
from math import tan, atan
from abc import ABC, abstractmethod

def get_relative_pose(pose_1,pose_2):
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

    
    pass

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

        pass

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

        pass

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

        pass

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


        pass

        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################        
        return final_pt
