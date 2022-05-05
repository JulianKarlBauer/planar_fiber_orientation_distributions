#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import planarfiberdist
import matplotlib.pyplot as plt

order = 720

#############
# Get Reconstruction
reconstruction = planarfiberdist.reconstruction.get_reconstructed_fodf_planar_fast(
    la0=2 / 3, d0=-1 / 315, d7=1 / 18, order=order, solver_kwargs=None, tolerance=1e-9
)

assert reconstruction.success
lagrange_multipliers = reconstruction.x

#############
# Plot Reconstruction

angles = planarfiberdist.reconstruction.IntegrationSchemeCircle(order=order).angles
values = planarfiberdist.reconstruction.ReconstructionProblemPlanar2DFast().odf(
    *lagrange_multipliers, angles
)

fig, axs = plt.subplots(
    figsize=(9, 15), ncols=1, nrows=1, subplot_kw={"projection": "polar"}
)
ax = axs
ax.plot(angles, values, label="reconstructed fodf")
# # plt.show()

