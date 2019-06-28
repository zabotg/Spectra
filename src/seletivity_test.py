# coding=utf-8
#
#   Copyright 2019, Guilherme Felipe Zabot, all rights reserved.
#   This code is under GNU General Public License v3.0.
#   zabot.gui@gmail.com
#
# Verified on June 17th, 2019.

from utils import read_archives
from correlation import correlation
import random

def read_combinations(path):
   text_file = open(path, 'r')
   combinations = [line.replace('\n', '').split(',') for line in text_file.readlines()]
   text_file.close()
   return combinations

def main():
   comb_fem_path = "/home/zabot/Documents/Documents/Codes/Mestrado/Spectra/archives/combinations_fem.txt"
   comb_dist_path = "/home/zabot/Documents/Documents/Codes/Mestrado/Spectra/archives/combinations_distances.txt"

   # Read combinations FEMs and Distances in order
   comb_fem = read_combinations(comb_fem_path)
   comb_dist = read_combinations(comb_dist_path)

   #Writing output to a single file
   file = open("result-selectivity-Lung.txt","w")
   file.close

   #Generating a list of 20 random elements
   random.seed(123)
   list_elements = random.sample(range(0, 50), 20)
   print(list_elements)

   # #Get combinations of FEMs
   # for fem1, fem2 in comb_fem:
   #    print(fem1, fem2)

   #    for dist1, dist2 in comb_dist:
   #       print(dist1, dist2)

if __name__ == "__main__":
    main()