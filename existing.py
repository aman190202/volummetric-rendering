import torch
import numpy as np

class Sphere_duo():
    # position, radius and color
    def __init__(self, p1 , r1 ,c1, p2, r2, c2):
        self.p1 = p1
        self.r1 = r1
        self.c1 = c1
        self.p2 = p2
        self.r2 = r2
        self.c2 = c2

        
    def intersect(self, x1 , x2):
        """
        :param x: points [batch_size, 3]
        """
        
        # (x- xc)^2 + (y-yc)^2 + (z-zc)^2 <= r^2 
        
        cond = (x1[:, 0] - self.p1[0])**2 + (x1[:, 1] - self.p1[1])**2 + (x1[:, 2] - self.p1[2])**2 <= self.r1**2
        
                
        num_rays = x1.shape[0]
        colors = torch.zeros((num_rays, 3))
        density = torch.zeros((num_rays, 1))
        
        colors[cond] = self.c1
        density[cond] = 10

        cond = (x2[:, 0] - self.p2[0])**2 + (x2[:, 1] - self.p2[1])**2 + (x2[:, 2] - self.p2[2])**2 <= self.r2**2
        colors[cond]= colors[cond] + self.c2
        density[cond] = 20
        
        return colors, density
    

class Sphere():

    def __init__(self, p ,r ,c): # position , radius and color
        self.p = p
        self.r = r
        self.c = c

    def intersect(self, o ,d):

        # Equation of the sphere : (x-xc)^2 + (y-yc)^2 + (z-zc)^2 = r^2
        
        a = d[:,0]**2 + d[:,1]**2 + d[:,2]**2
        b = 2 * ((d[:,0]* (o[:,0]-self.p[0])) + (d[:,1]* (o[:,1]-self.p[1])) + (d[:,2]* (o[:,2]-self.p[2])))
        c = (o[:,0] - self.p[0])**2 + (o[:,1] - self.p[1])**2 + (o[:,2] - self.p[2])**2 - self.r** 2

        pho = b**2 - 4*a*c

        cond = pho >= 0
        num_rays = o.shape[0]
        colors = np.zeros((num_rays,3))

        colors[cond] = self.c
        print(cond.shape)
        return colors
        
