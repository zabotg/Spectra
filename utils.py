# coding=utf-8
#
#   Copyright 2019, Guilherme Felipe Zabot, all rights reserved.
#   This code is under GNU General Public License v3.0.
#   zabot.gui@gmail.com
#
# Verified on June 10th, 2019.

import warnings
import pandas as pd

# ------------------------------------------------
#               Read the FEMs archives
# ------------------------------------------------
def read_archives(path_fem1, path_fem2):
    try:
        data_fem1 = pd.read_csv(path_fem1, sep=';', header=None)
        data_fem2 = pd.read_csv(path_fem2, sep=';', header=None)
        return data_fem1, data_fem2
    except NameError:
        return NameError