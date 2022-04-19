'''
Implements simulated annealing for finding optimal partition
of integers.
'''
import numpy as np
import argparse
import math
from utils import *

def T(iter):
    '''
    Temperature function for simulated anealing.
        - iter: int
    '''
    return 10**10*(0.8)**(math.floor(iter/300))

def sim_ann_n(inputfile, max_iter, verbose=False):
    '''
    Simulated annealing with normal solution representation.
        - inputfile: string, path in integers to partition
        - max_iter: int, maximum number of iterations for
                    which to run the algorithm. 
    '''
    A = np.loadtxt(inputfile)
    if verbose:
        print(A)
    size = A.shape[0]
    randsol = np.asarray([1 if random.random() < 0.5 else -1 for i in range(size)])
    randsol2 = randsol.copy()
    for i in range(max_iter):
        randsol1 = getNeighborN(randsol)
        if compute_residue_n(A, randsol1) < compute_residue_n(A, randsol):
            randsol = randsol1 # confirm!
        else:
            prob = math.exp((-1*compute_residue_n(A, randsol1)\
                -compute_residue_n(A, randsol))/T(i))
            if random.random() < prob:
                randsol = randsol1
        #import pdb; pdb.set_trace();
        if compute_residue_n(A, randsol) < \
            compute_residue_n(A, randsol2):
            randsol2 = randsol
    # time saver: stop when residue is zero!
    return compute_residue_n(A, randsol2), randsol2

def sim_ann_p(inputfile, max_iter, verbose=False):
    '''
    Simulated annealing with prepartitioned solution representation.
    '''
    A = np.loadtxt(inputfile)
    if verbose:
        print(A)
    size = A.shape[0]
    randsol = np.arange(size)
    np.random.shuffle(randsol)
    randsol2 = randsol.copy()
    for i in range(max_iter):
        randsol1 = getNeighborP(randsol)
        if compute_residue_p(A, randsol1) < compute_residue_p(A, randsol):
            randsol = randsol1 # confirm!
        else:
            prob = math.exp((-1*compute_residue_p(A, randsol1)\
                -compute_residue_p(A, randsol))/T(i))
            if random.random() < prob:
                randsol = randsol1
        #import pdb; pdb.set_trace();
        if compute_residue_p(A, randsol) < \
            compute_residue_p(A, randsol2):
            randsol2 = randsol
    # time saver: stop when residue is zero!
    return compute_residue_p(A, randsol2), randsol2

if __name__ == "__main__":
    # unit testing
    print("------Beginning Unit Tests of the Normal Sim Annealing function-------------")
    parser = argparse.ArgumentParser(description="hill climbing unit tests")
    parser.add_argument('inputfile')
    parser.add_argument('max_iter', type=int)
    args = parser.parse_args()

    print(sim_ann_n(args.inputfile, args.max_iter, verbose=True))