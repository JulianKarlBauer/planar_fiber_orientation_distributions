#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import planarfibers
import pandas as pd
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)

df = planarfibers.discretization.get_points_on_slices(
    radii=["0", "1/2", "9/10"],
    la0s=["1/2", "4/6", "5/6", "1"],
    numeric=False,
)

print(df)
