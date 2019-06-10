#!interpreter [optional-arg]
# -*- coding: utf-8 -*-

"""
{This class describe the implementation of the Omni-Technique}
"""

# Futures
from __future__ import print_function
# […]

# Built-in/Generic Imports
import os
import sys
# […]

# Libs
import pandas as pd # Or any other
# […]

# Own modules
#from {path} import {class}
# […]

__author__ = '{Guilherme Zabot}'
__copyright__ = 'Copyright {2019}, {Spectra}'
__credits__ = ['{Guilherme Zabot}']
__version__ = '{0}.{0}.{1}'
__email__ = '{zabot.gui@gmail.com}'

class Omni(object):

    def hull_of_foci(data, n_foci=1):
        foci = []
        random_elem =  random.randint(0, len(data) - 1)  # Find for a random element
        elem_row = data.iloc[random_elem]  # Get element row

        for i in n_foci:




        random_element = ()
    

def hull_of_foci(data, n_focis=1):
    result = []

    random_element = random.randint(0, len(data) - 1)  # Fisrt, find for a random element
    element_row = data.iloc[random_element]  # Get element row

    # Find first and second focus O(n)
    for focus in range(2):
        greater_distance = [-1, -1]  # Great distance and index
        for row in data.iterrows():
            dst = distance.euclidean(element_row, row[1])
            if dst > greater_distance[1]:
                greater_distance = [row[0], dst]

        if greater_distance[0] not in result:
            result.append(greater_distance[0])
            element_row = data.iloc[greater_distance[0]]

    if n_focis == 1:
        return [result[0]]

    elif n_focis == 2:
        return result

    # Find three or more elements
    edge = distance.euclidean(data.iloc[result[0]], data.iloc[result[1]])
    for focus in range(n_focis - 2):
        smaller = [np.inf, 0]
        for row in data.iterrows():
            if row[0] not in result:  # ok
                error = 0
                for i in result:
                    dst = distance.euclidean(data.iloc[i], row[1])
                    error = error + np.abs(edge - dst)  # Minimum error check
                if error < smaller[0]:
                    smaller = [error, row[0]]
        result.append(smaller[1])

    return result