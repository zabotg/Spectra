# coding=utf-8
#
#   Copyright 2019, Guilherme Felipe Zabot, all rights reserved.
#   This code is under GNU General Public License v3.0.
#   zabot.gui@gmail.com
#
# Verified on June 29th, 2019.

from scipy.spatial import distance
from utils import get_all_combinations
from omni import *
import sys

def main():
    a = [1,2,3,4,5]
    b = [2,3,4,6,8]
    result = distance.canberra(a,b)

    # list_elem = ['canberra','chebyshev','cityblock','euclidean','jaccard','hamming']
    # print(get_all_combinations(list_elem))
    print(result)


if __name__ == "__main__":
    main()