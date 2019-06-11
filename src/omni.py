# coding=utf-8
#
#   Copyright 2019, Guilherme Felipe Zabot, all rights reserved.
#   This code is under GNU General Public License v3.0.
#   zabot.gui@gmail.com
#
# Verified on June 10th, 2019.

from scipy.spatial import distance
from utils import read_archives

import random
import numpy as np
import sys


# This code is an implementation of the Omni Technique proposed by: Traina Jr. C. (2017)

# ------------------------------------------------
# Algorithm to find a good foci base
# ------------------------------------------------
def hull_of_foci(data_fem, n_focis=1):
    result = []

    # Randomly chooses an object and get a object row
    random_object = random.randint(0, len(data_fem)-1)
    object_row = data_fem.iloc[random_object]

    #Find first focus and second focus.
    for i in range(2):
        greater_distance = [-1, -1] #[Great distance, index]

        for row in data_fem.iterrows():
            dist = distance.euclidean(object_row, row[1])
            if dist > greater_distance[1]:
                greater_distance = [row[0], dist]

        if greater_distance[0] not in result:
            result.append(greater_distance[0])
            object_row = data_fem.iloc[greater_distance[0]]
    if n_focis == 1:
        result = [result[0]]

    # Find three or more elements
    if n_focis > 3:
        edge = distance.euclidean(data_fem.iloc[result[0]], data_fem.iloc[result[1]])
        while n_focis-2 > 0:
            smaller = [np.inf, 0]

            for row in data_fem.iterrows():

                if row[0] not in result:  # ok
                    error = 0
                    for i in result:
                        dist = distance.euclidean(data_fem.iloc[i], row[1])
                        error = error + np.abs(edge - dist)  # Minimum error check
                    if error < smaller[0]:
                        smaller = [error, row[0]]

            result.append(smaller[1])
        n_focis = n_focis-1
    return result


def list_distances(search_object, data_fem):
    result = []
    for row in data_fem.iterrows():
        dist = distance.euclidean(data_fem.iloc[search_object], row[1])
        result.append([row[0], dist])
    return result


def omni_candidates_generate(data, focis, radius, search_object):
    result = []
    for focus in focis:
        result_temp = []
        distances = list_distances(focus, data)
        for dst in distances:
            if dst[0] != search_object:
                if distances[search_object][1] - radius <= dst[1] <= distances[search_object][1] + radius:
                    result_temp.append(dst[0])
        result.append(set(result_temp))
    result = list(set.intersection(*result))
    return result


def omni_candidates_refinement(candidates, data_fem, radius, search_object):
    result = []
    for candidate in candidates:
        dst = distance.euclidean(data_fem.iloc[search_object], data_fem.iloc[candidate])
        if dst <= radius:
            result.append(candidate)
    return result


def normalization_radius(radius, data_fem1, data_fem2, focis_fem1, focis_fem2):  # For two data spaces
    max_distance_fem1 = distance.euclidean(data_fem1.iloc[focis_fem1[0]], data_fem1.iloc[focis_fem1[1]])
    max_distance_fem2 = distance.euclidean(data_fem2.iloc[focis_fem2[0]], data_fem2.iloc[focis_fem2[1]])

    return max_distance_fem1*radius, max_distance_fem2*radius


def main(argv):
    path_fem1 = sys.argv[1]
    path_fem2 = sys.argv[2]

    data_fem1 = read_archives(path_fem1)
    data_fem2 = read_archives(path_fem2)

    print(hull_of_foci(data_fem1, 1))
    print(hull_of_foci(data_fem2, 2))

if __name__ == "__main__":
    main(sys.argv[1:])