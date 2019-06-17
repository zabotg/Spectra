# coding=utf-8
#
#   Copyright 2019, Guilherme Felipe Zabot, all rights reserved.
#   This code is under GNU General Public License v3.0.
#   zabot.gui@gmail.com
#
# Verified on June 17th, 2019.

from utils import read_archives
from correlation import correlation

def read_combinations(path):
   text_file = open(path, 'r')
   combinations = [line.replace('\n', '').split(',') for line in text_file.readlines()]
   text_file.close()
   return combinations

def main():
   dataset_path = "/home/zabot/Datasets/Lung-HCRP/Features/{}.csv"
   comb_fem_path = "/home/zabot/Documents/Codes/Mestrado/Spectra/archives/combinations_fem.txt"
   comb_dist_path = "/home/zabot/Documents/Codes/Mestrado/Spectra/archives/combinations_distances.txt"

   # Read combinations FEMs and Distances in order
   comb_fem = read_combinations(comb_fem_path)
   comb_dist = read_combinations(comb_dist_path)

if __name__ == "__main__":
   main()