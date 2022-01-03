#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sympy as sp
import pandas as pd

two = sp.S(2)
zero = sp.S(0)
base = sp.sympify("-4 / 35")
pi = sp.pi


def radius_circle_d7_d0_plane(la0):
    return (la0 - la0 ** sp.S(2)) / sp.S(2)


def r_max(la0):
    return radius_circle_d7_d0_plane(la0)


def get_d_0(radius_factor, beta, la0):
    radius = radius_circle_d7_d0_plane(la0)
    return radius_factor * radius * sp.sin(beta) + radius + base


def get_d_7(radius_factor, beta, la0):
    radius = radius_circle_d7_d0_plane(la0)
    return radius_factor * radius * sp.cos(beta)


def d0_hat_by_la0_d0(la0, d0):
    return d0 - base - radius_circle_d7_d0_plane(la0)


def r_by_la0_d0_d7(la0, d0, d7):
    d0_hat = d0_hat_by_la0_d0(la0=la0, d0=d0)
    return sp.sqrt(d0_hat ** sp.S(2) + d7 ** sp.S(2))


def beta_by_la0_d0_d7(la0, d0, d7):
    return sp.atan2(d0_hat_by_la0_d0(la0=la0, d0=d0), d7)


def points_view00(la0s, radius_almost):
    angle_upper = pi / two
    angle_mid = zero
    angle_lower = -pi / two

    one_is_on_board = sp.S(1) in la0s

    nbr_la0s = len(la0s)
    if one_is_on_board:
        nbr_la0s -= 1
    tmp = {
        **{
            f"v00-upper-{index}": {
                "la0": la0s[index],
                "radius_factor": radius_almost,
                "beta": angle_upper,
            }
            for index in range(nbr_la0s)
        },
        **{
            f"v00-mid-{index}": {
                "la0": la0s[index],
                "radius_factor": zero,
                "beta": angle_mid,
            }
            for index in range(nbr_la0s)
        },
        **{
            f"v00-lower-{index}": {
                "la0": la0s[index],
                "radius_factor": radius_almost,
                "beta": angle_lower,
            }
            for index in range(nbr_la0s)
        },
    }
    if one_is_on_board:
        tmp["ud"] = {
            "la0": la0s[-1],
            "radius_factor": zero,
            "beta": zero,
        }
    return tmp


def points_view_shaped_half_circle(la0, angles, angles_names, radii, key_extension=""):
    points = {
        "vshc-central": {
            "la0": la0,
            "radius_factor": zero,
            "beta": zero,
        },
        **{
            f"vshc-{angles_names[index_angle]}-{index_radius}": {
                "la0": la0,
                "radius_factor": radius,
                "beta": angles[index_angle],
            }
            for index_angle in range(len(angles))
            for index_radius, radius in enumerate(radii[1:])
        },
    }
    return {key + key_extension: val for key, val in points.items()}


def get_points_on_slices(
    radii=["0", "1/2", "9/10"], la0s=["1/2", "4/6", "5/6", "1"], numeric=False
):

    la0s = list(map(sp.sympify, la0s))
    radii = list(map(sp.sympify, radii))

    angles_raw = ["-90", "-45", "0", "45", "90"]
    angles = list(map(sp.rad, map(sp.sympify, angles_raw)))
    angles_names = list(map(lambda x: x.replace("-", "m"), angles_raw))

    radius_almost = radii[-1]

    points = points_view00(la0s=la0s, radius_almost=radius_almost)
    for index, la0 in enumerate(la0s[:-1]):
        points = {
            **points,
            **points_view_shaped_half_circle(
                la0=la0,
                angles=angles,
                angles_names=angles_names,
                radii=radii,
                key_extension=f"-la0-{index}",
            ),
        }

    df = pd.DataFrame(points).T

    df["r"] = df.apply(
        lambda row: sp.simplify(row["radius_factor"] * r_max(la0=row["la0"])),
        axis=1,
    )

    df["d_0"] = df.apply(
        lambda row: sp.simplify(
            get_d_0(
                radius_factor=row["radius_factor"], beta=row["beta"], la0=row["la0"]
            )
        ),
        axis=1,
    )

    df["d_7"] = df.apply(
        lambda row: sp.simplify(
            get_d_7(
                radius_factor=row["radius_factor"], beta=row["beta"], la0=row["la0"]
            )
        ),
        axis=1,
    )

    # if False:
    #     df_sorted = df.sort_values(
    #         by=["la0", "beta", "r"], ascending=(True, True, True)
    #     )

    if numeric:
        return df.applymap(lambda x: float(sp.N(x)))
    return df
