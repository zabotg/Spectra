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
    file = open("result-correlation.txt","w")

    for metric1, metric2 in comb_dist:
        for name_fem1, name_fem2 in comb_fem:
            data_fem1 = read_archives(dataset_path.format(name_fem1))
            data_fem2 = read_archives(dataset_path.format(name_fem2))

            corr = correlation(data_fem1, data_fem2, percentage=1, metric1=metric1, metric2=metric2)
            print(metric1, metric2, name_fem1, name_fem2, corr)
            file.write("{};{};{};{};{}\n".format(metric1,metric2,name_fem1,name_fem2,corr))
    file.close()


if __name__ == "__main__":
    main()