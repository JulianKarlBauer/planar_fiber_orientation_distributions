#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import scipy.optimize

###########################################################
ORDER = 720


class IntegrationSchemeCircle:
    def __init__(self, order=ORDER):
        self.length = 2.0 * np.pi * 1.0
        self.angles = self.length * np.arange(order) / order
        self.weights = np.full(order, 1.0 / order)
        self.weights_incl_length = self.length * self.weights


class ReconstructionProblemPlanar2DFast:
    def __init__(self, la0=0.5, d0=0.0, d7=0.0, order=ORDER):
        self.la0 = la0
        self.d0 = d0
        self.d7 = d7
        self.default_initial_x = [0.8378770664093456] + 4 * [0.0]

        self.order = order

        scheme = IntegrationSchemeCircle(order=order)
        self.length = scheme.length
        self.angles = scheme.angles
        self.weights_incl_length = scheme.weights_incl_length

    def odf(self, L, f1, f2, g1, g2, phi):
        return np.exp(
            -1
            - L
            - f1 * np.cos(2.0 * phi)
            - f2 * np.sin(2.0 * phi)
            + g1 * np.cos(4.0 * phi)
            - g2 * np.sin(4.0 * phi)
        )

    def integrate(self, vector):
        weights = self.weights_incl_length
        return np.tensordot(vector, weights, 1)

    def residuum(self, x_vector):
        angles = self.angles
        odf_values = self.odf(*x_vector, phi=angles)

        sqrt = np.sqrt(2)

        res = np.array(
            [
                self.integrate(odf_values) - 1.0,
                self.integrate(odf_values * 1.0 / 2.0 * np.cos(2.0 * angles))
                - (self.la0 - 1.0 / 2.0),
                self.integrate(odf_values * 1.0 / 2.0 * np.sin(2.0 * angles)) - 0.0,
                self.integrate(odf_values * -1.0 / 8.0 * np.cos(4.0 * angles))
                - (self.d0 - 3.0 / 280.0),
                self.integrate(odf_values * sqrt / 8.0 * np.sin(4.0 * angles))
                - (sqrt * self.d7),
            ]
        )
        return res


def get_reconstructed_fodf_planar_fast(
    la0, d0, d7, order=ORDER, solver_kwargs=None, tolerance=1e-9
):
    problem = ReconstructionProblemPlanar2DFast(la0, d0, d7, order)

    if solver_kwargs is None:
        solver_kwargs = dict(method="lm", options=dict(ftol=tolerance, factor=0.1))
        # solver_kwargs = dict(method="krylov", options=dict())

    result = scipy.optimize.root(
        fun=problem.residuum,
        x0=problem.default_initial_x,
        tol=tolerance,
        **solver_kwargs,
    )
    return result
