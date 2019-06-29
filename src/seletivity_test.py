# coding=utf-8
#
#   Copyright 2019, Guilherme Felipe Zabot, all rights reserved.
#   This code is under GNU General Public License v3.0.
#   zabot.gui@gmail.com
#
# Verified on June 11th, 2019.
# This code is an implementation of the Omni Technique proposed by: Traina Jr. C. (2017)

from utils import read_archives
from omni import *
import sys

# ------------------------------------------------
# Read Combinations
# ------------------------------------------------
def read_combinations(path):
    text_file = open(path, 'r')
    combinations = [line.replace('\n', '').split(',') for line in text_file.readlines()]
    text_file.close()
    return combinations

# ------------------------------------------------
# Traditional Approach
# ------------------------------------------------
def traditional_approach(data_fem1, data_fem2, search_element, radius, dist1, dist2):
   # Find foci to data_fem and data_fem2
   # By default, the number of foci n_foci=2
   foci_fem1 = hull_of_foci(data_fem1, n_focis=2, dist=dist1)
   foci_fem2 = hull_of_foci(data_fem2, n_focis=2, dist=dist2)

   # Radius normalization for both data_fem
   radius_fem1, radius_fem2 = normalization_radius(radius, data_fem1, data_fem2, foci_fem1, foci_fem2)

   # Generation of candidates using the focis
   candidates_fem1 = omni_candidates_generation(data_fem1, foci_fem1, radius_fem1, search_element)
   candidates_fem2 = omni_candidates_generation(data_fem2, foci_fem2, radius_fem2, search_element)

   # Intersect candidates
   candidates_intersection = list(set(candidates_fem1).intersection(set(candidates_fem2)))

   # Refines the intersection of candidates generated
   refinement_fem1 = omni_candidates_refinement(candidates_intersection, data_fem1, radius_fem1, search_element, dist=dist1)
   refinement_fem2 = omni_candidates_refinement(candidates_intersection, data_fem2, radius_fem2, search_element, dist=dist2)

   # Final query resulta
   return list(set(refinement_fem1).intersection(set(refinement_fem2)))

# ------------------------------------------------
# Proposal Approach
# ------------------------------------------------
def proposal_approach(data_fem1, data_fem2, search_element, radius, dist1, dist2):
   # Find foci to data_fem and data_fem2
   # By default, the number of foci n_foci=2
   foci_fem1 = hull_of_foci(data_fem1, n_focis=2, dist=dist1)
   foci_fem2 = hull_of_foci(data_fem2, n_focis=2, dist=dist2)

   # Radius normalization for both data_fem
   radius_fem1, radius_fem2 = normalization_radius(radius, data_fem1, data_fem2, foci_fem1, foci_fem2)

   # Generation of candidates using the focis
   candidates_fem1 = omni_candidates_generation(data_fem1, foci_fem1, radius_fem1, search_element)
   candidates_fem2 = omni_candidates_generation(data_fem2, foci_fem2, radius_fem2, search_element)

   # Refines the intersection of candidates generated
   refinement_fem1 = omni_candidates_refinement(candidates_fem1, data_fem1, radius_fem1, search_element, dist1)
   refinement_fem2 = omni_candidates_refinement(candidates_fem2, data_fem2, radius_fem2, search_element, dist2)

   # Final query resulta
   return list(set(refinement_fem1).intersection(set(refinement_fem2)))


def main():
   data_fem1 = read_archives('/home/zabot/Documents/Datasets/Lung-HCRP/Features/LBP.csv')
   data_fem2 = read_archives('/home/zabot/Documents/Datasets/Lung-HCRP/Features/colorLayout.csv')
   distances_combinations = read_combinations('/home/zabot/Documents/Documents/Codes/Mestrado/Spectra/archives/spatialdistances.txt')

   search_element = 15
   radius = 0.4

   for dist1, dist2 in distances_combinations:
      print(dist1, dist2)
      result_traditional = traditional_approach(data_fem1, data_fem2, search_element, radius, dist1, dist2)
      result_proposal = proposal_approach(data_fem1, data_fem2, search_element, radius, dist1, dist2)
      print(result_traditional)
      print(result_proposal)

if __name__ == "__main__":
    main()