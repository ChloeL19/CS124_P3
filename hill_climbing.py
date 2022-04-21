'''
Implements a hill climbing algorithm for both
normal and prepartitioned solution representations.
'''
import numpy as np
import argparse
import time
from utils import *

def hill_climb_n(inputfile, max_iter, verbose=False):
    '''
    Hill climbing algorithm for solutions in normal form.
        - inputfile: string, path to the input file where
                    the integers that need to be partitioned
                    are stored.
        - max_iter: int, the number of algorithm iterations
                    to perform before returning the optimal
                    solution.
    '''
    A = np.loadtxt(inputfile)
    if verbose:
        print(A)
    size = A.shape[0]
    randsol = np.asarray([1 if random.random() < 0.5 else -1 for i in range(size)])
    for i in range(max_iter):
        randsol2 = getNeighborN(randsol)
        #Time improvement: remove to get a better time!
        assert((randsol2 != randsol).any())
        if (compute_residue_n(A, randsol2.tolist()) < \
        compute_residue_n(A, randsol.tolist())):
            randsol = randsol2.copy()
        # could save time by stopping when reach 0
        if compute_residue_n(A, randsol) == 0:
            break
    return compute_residue_n(A, randsol)

def hill_climb_p(inputfile, max_iter, verbose=False):
    '''
    Hill climbing algorithm for solutions in prepartitioned form.
    '''
    A = np.loadtxt(inputfile)
    if verbose:
        print(A)
    size = A.shape[0]
    randsol = np.random.randint(0, size, size=size)
    for i in range(max_iter):
        randsol2 = getNeighborP(randsol)
        #Time improvement: remove to get a better time!
        assert((randsol2 != randsol).any())
        if (compute_residue_p(A, randsol2.tolist()) < \
        compute_residue_p(A, randsol.tolist())):
            randsol = randsol2.copy()
        # could save time by stopping when reach 0
        if compute_residue_p(A, randsol.tolist()) == 0:
            break
    return compute_residue_p(A, randsol.tolist())

if __name__ == "__main__":
    # unit testing
    print("------Beginning Unit Tests of the Normal Hill Climbing function-------------")
    parser = argparse.ArgumentParser(description="hill climbing unit tests")
    parser.add_argument('inputfile')
    parser.add_argument('max_iter', type=int)
    args = parser.parse_args()

    print(hill_climb_n(args.inputfile, args.max_iter, verbose=True))