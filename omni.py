# coding=utf-8
#
#   Copyright 2019, Guilherme Felipe Zabot, all rights reserved.
#   This code is under GNU General Public License v3.0.
#   zabot.gui@gmail.com
#
# Verified on June 10th, 2019.

from scipy.spatial import distance
import numpy as np

import random

"""
This code is an implementation of the Omni Technique proposed by: Traina Jr. C. in
The Omni-family of all-purpose access methods: a simple and effective way to make
similarity search more efficient, (2007).  
"""

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
            dist = distance.euclidean(element_row, row[1])
            
            if dist > greater_distance[1]:
                greater_distance = [row[0], dist]

        if greater_distance[0] not in result:
            result.append(greater_distance[0])
            element_row = data_fem.iloc[greater_distance[0]]
        
    if n_focis == 1:
        result = list(result[0])

    # Find three or more elements
    if n_focis > 3:
        edge = distance.euclidean(data_fem.iloc[result[0]], data_fem.iloc[result[1]])
        for focus in range(n_focis - 2):
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

    return result


