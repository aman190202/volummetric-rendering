import torch
import numpy as np


def compute_accumulated_transmittance(betas):
    device = 'cpu'
    betas = betas.cpu().numpy()
    accumulated_transmittance = np.cumprod(betas,1)
    accumulated_transmittance = (torch.from_numpy(accumulated_transmittance)).to(device)
    accumulated_transmittance[:, 0] = 1.
    return accumulated_transmittance

def rendering(model, rays_o, rays_d, tn, tf, nb_bins=500, device='cpu'):
    
    rays_o = rays_o.to(torch.float32).to(device)
    rays_d = rays_d.to(torch.float32).to(device)
    t = torch.linspace(tn, tf, nb_bins).to(device) # [nb_bins]
    delta = torch.cat((t[1:] - t[:-1], torch.tensor([1e10]).to(device))) 
    
    x = rays_o.unsqueeze(1) + t.unsqueeze(0).unsqueeze(-1) * rays_d.unsqueeze(1) # [nb_rays, nb_bins, 3]
    
    colors, density = model.intersect(x.reshape(-1, 3),x.reshape(-1, 3))
    colors = colors.to(torch.float32).to(device)
    
    
    colors = colors.reshape((x.shape[0], nb_bins, 3)) # [nb_rays, nb_bins, 3]
    density = density.reshape((x.shape[0], nb_bins)).to(torch.float32).to(device)

    
    alpha = 1 - torch.exp(- density * delta.unsqueeze(0)) # [nb_rays, nb_bins, 1]
    T = compute_accumulated_transmittance(1 - alpha) # [nb_rays, nb_bins, 1]
    c = (T.unsqueeze(-1) * alpha.unsqueeze(-1) * colors).sum(1) # [nb_rays, 3]
    
    return c