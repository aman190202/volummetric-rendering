from camera import return_rays
from existing import Sphere_duo
from render import rendering
import torch
import matplotlib.pyplot as plt

H = 400
W = 400

rays_o, rays_d = return_rays()

model = Sphere_duo(torch.tensor([0.0,0.0,-1.]),.1,torch.tensor([1.,1.,1.]), torch.tensor([0.,0.,-4.]),.05,torch.tensor([1.,0.,0.]))
px_colors = rendering(model, torch.from_numpy(rays_o), torch.from_numpy(rays_d), 0.8, 1.2)

img = px_colors.reshape(H, W, 3).cpu().numpy()
plt.figure(dpi=200)
plt.imshow(img)
plt.savefig("assets/concurrent.png")
