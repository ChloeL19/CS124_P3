'''
Main program for running the various number parition 
algorithms.
'''
from repeated_random import *
from hill_climbing import *
from simulated_annealing import *
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="partition script")
    parser.add_argument('flag', type=int)
    parser.add_argument('algorithm', type=int)
    parser.add_argument('inputfile')
    args = parser.parse_args()
    
    if (args.algorithm == 0):
        pass
    if (args.algorithm == 1):
        res, _ = normal_rr(args.inputfile, 25000)
    if (args.algorithm == 2):
        res, _ = hill_climb_n(args.inputfile, 25000)
    if (args.algorithm == 3):
        res, _ = sim_ann_n(args.inputfile, 25000)
    if (args.algorithm == 11):
        res, _ = prepartitioned_rr(args.inputfile, 25000)
    if (args.algorithm == 12):
        res, _ =  hill_climb_p(args.inputfile, 25000)
    if (args.algorithm == 13):
        res, _ = sim_ann_p(args.inputfile, 25000)
    print(res)