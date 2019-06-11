from utils import read_archives
from correlation import read_archives
from omni import *
import sys
import numpy as np


def candidates_generation(data_fem1, data_fem2, search_element, radius):
    # Find foci to data_fem1 and data_fem2
    # By default, the number of foci n_focis=2
    foci_fem1 = hull_of_foci(data_fem1, n_focis=2)
    foci_fem2 = hull_of_foci(data_fem2, n_focis=2)

    # Radius normalization for both data_fem
    radius_fem1, radius_fem2 = normalization_radius(radius, data_fem1, data_fem2, foci_fem1, foci_fem2)
    
    # Generate candidates
    candidates_fem1 = omni_candidates_generation(data_fem1, foci_fem1, radius_fem1, search_element)
    candidates_fem2 = omni_candidates_generation(data_fem2, foci_fem2, radius_fem2, search_element)
    
    # Intersect candidates
    candidates_intersection = list(set(candidates_fem1).intersection(set(candidates_fem2)))

    return candidates_intersection, candidates_fem1, candidates_fem2


def main(argv):
    if len(argv) != 4:
        sys.exit("ERROR Number of arguments is different from three.")

    data_fem1 = read_archives(sys.argv[1])
    data_fem2 = read_archives(sys.argv[2])

    search_element = int(sys.argv[3])
    radius = float(sys.argv[4])

    a,_,_ = candidates_generation(data_fem1, data_fem2, search_element, radius)
    print(a)

if __name__ == "__main__":
    main(sys.argv[1:])