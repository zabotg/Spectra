# coding=utf-8
#
#   Copyright 2019, Guilherme Felipe Zabot, all rights reserved.
#   This code is under GNU General Public License v3.0.
#   zabot.gui@gmail.com
#
# Verified on June 10th, 2019.

from sklearn.neighbors import KDTree
from scipy.stats import pearsonr
from utils import read_archives

import sys
import numpy as np
import random

import warnings
warnings.filterwarnings('ignore')


# This code describe the implementation of the correlation tecnique PCMS

# ------------------------------------------------
# Calculates the correlation between FEM1 and FEM2
# ------------------------------------------------
def correlation(data_fem1, data_fem2, percentage=0.10, metric1='euclidean', metric2='euclidean'):
    size_fem1 = len(data_fem1.index)
    size_fem2 = len(data_fem2.index)

    if size_fem1 != size_fem2:
        sys.exit("Diferent number os elements in FEM1 and FEM2")

    elements_total = round(size_fem1 * percentage) # Elements percentage
    list_elements = random.sample(range(0, size_fem1), elements_total)

    # Geting the values in list_elements and
    data_fem1 = data_fem1.iloc[list_elements]
    data_fem2 = data_fem2.iloc[list_elements]

    # See the documentation of the DistanceMetric class for a list of available metrics
    tree_fem1 = KDTree(data_fem1, leaf_size=2, metric=metric1)
    tree_fem2 = KDTree(data_fem2, leaf_size=2, metric=metric2)

    # Calculate distances between all elements in data_fem1 and data_fem2
    distances_fem1, elements_fem1 = tree_fem1.query(data_fem1, k=len(data_fem1))
    distances_fem2, elements_fem2 = tree_fem2.query(data_fem2, k=len(data_fem2))

    # Ordered lists by element index
    for i in range(elements_total):
        a_data1, b_data1 = list(elements_fem1[i]), list(distances_fem1[i])
        a_data2, b_data2 = list(elements_fem2[i]), list(distances_fem2[i])

        elements_fem1[i], distances_fem1[i] = zip(*sorted(zip(a_data1, b_data1)))
        elements_fem2[i], distances_fem2[i] = zip(*sorted(zip(a_data2, b_data2)))

    # Calculates the correlation and an average over the pearson vectors
    value_corr = []
    for elem in range(elements_total):
        distances_data1 = distances_fem1[elem]
        distances_data2 = distances_fem2[elem]
        value_corr.append(pearsonr(distances_data1, distances_data2)[0])
    value_corr = np.mean(value_corr)
    return value_corr

def main(argv):
    if len(argv) != 3:
        sys.exit("ERROR Number of arguments is different from three.")

    path_fem1 = sys.argv[1]
    path_fem2 = sys.argv[2]
    percentage = float(sys.argv[3])

    data_fem1 = read_archives(path_fem1)
    data_fem2 = read_archives(path_fem2)

    metric1 = 'euclidean'
    metric2 = 'euclidean'

    value_corr = correlation(data_fem1, data_fem2, percentage, metric1, metric2)

    print(value_corr)

if __name__ == "__main__":
    main(sys.argv[1:])