# coding=utf-8
#
#   Copyright 2019, Guilherme Felipe Zabot, all rights reserved.
#   This code is under GNU General Public License v3.0.
#   zabot.gui@gmail.com
#
# Verified on June 10th, 2019.

import pandas as pd
from itertools import combinations

# ------------------------------------------------
#               Read the FEMs archives
# ------------------------------------------------
def read_archives(path_fem):
    try:
        data_fem1 = pd.read_csv(path_fem, sep=';', header=None)
        return data_fem1
    except NameError:
        return NameError


# ------------------------------------------------
# Get all combinations of a list without repetitions
# ------------------------------------------------
def get_all_combinations(list_elem):
    return list(combinations(list_elem, 2))
