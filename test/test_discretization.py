#!/usr/bin/env python
# -*- coding: utf-8 -*-
from planarfibers import discretization


class Test_execute_without_error:
    def test_default(self):
        df = discretization.get_points_on_slices()

    def test_no_one(self):
        df = discretization.get_points_on_slices(
            radii=["0", "1/2", "9/10"],
            la0s=["1/2", "4/6", "5/6"],
            numeric=False,
        )

    def test_only_one(self):
        df = discretization.get_points_on_slices(
            radii=["0", "1/2", "9/10"],
            la0s=["1"],
            numeric=False,
        )

    def test_random(self):
        df = discretization.get_points_on_slices(
            radii=["0", "1/2", "9/10", "2/3"],
            la0s=["1/2", "1"],
            numeric=False,
        )
