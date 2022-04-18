'''
Implements simulated annealing for finding optimal partition
of integers.
'''
import numpy as np
import argparse
from utils import *

def sim_ann_n(inputfile, max_iter):
    '''
    Simulated annealing with normal solution representation.
        - inputfile: string, path in integers to partition
        - max_iter: int, maximum number of iterations for
                    which to run the algorithm. 
    '''
    return None, None

def sim_ann_p(inputfile, max_iter):
    '''
    Simulated annealing with prepartitioned solution representation.
    '''
    return None, None

if __name__ == "__main__":
    # unit testing
    print("------Beginning Unit Tests of the Normal Sim Annealing function-------------")
    parser = argparse.ArgumentParser(description="hill climbing unit tests")
    parser.add_argument('inputfile')
    parser.add_argument('max_iter', type=int)
    args = parser.parse_args()

    print(sim_ann_n(args.inputfile, args.max_iter, verbose=True))