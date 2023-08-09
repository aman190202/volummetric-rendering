import numpy as np
import torch

def return_rays (H=400,W=400,f=1200):
    

    rays_o = np.zeros((H*W, 3))
    rays_d = np.zeros((H*W, 3))
    u = np.arange(W)
    v = np.arange(H)
    u, v = np.meshgrid(u, v)

    dirs = np.stack((u - W / 2,
                    -(v - H / 2),
                    - np.ones_like(u) * f), axis=-1)
    rays_d = dirs / np.linalg.norm(dirs, axis=-1, keepdims=True)
    rays_d = rays_d.reshape(-1, 3)


    return rays_o, rays_d