# Volummetric-rendering
<img src="assets/output.png" width="400" ></img>

## Methodology
We render the color of any ray passing through the scene using principles from classical volume rendering. The volume density σ(x) can be interpreted as the differential probability of a ray terminating at an infinitesimal particle at location x. We numerically estimate this continuous integral using quadrature. Deter- ministic quadrature, which is typically used for rendering discretized voxel grids, would effectively limit our representation’s resolution because the MLP would only be queried at a fixed discrete set of locations. Instead, we use a stratified sampling approach where we partition [tn, tf ] into N evenly-spaced bins and then draw one sample uniformly at random from within each bin

## Metal support for ARM chips on MacOS ('mps')

Change device='mps' from device='cpu' to run this on your GPU. The tensors are especially transformed into float32 dtype from float64 to enable functioning on Metal GPUs

## How to run

```
pip install torch matplotlib numpy
```