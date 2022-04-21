'''
Implements both normal representation and prepartioned 
representation for repeated random.
'''
import numpy as np
import argparse
from utils import *

def normal_rr(inputfile, max_iter, verbose=False):
    '''
    Repeated random algorithm on normal representation.
    (i.e. list of signs)
        - max_iter: int, the maximum number of iterations to
                    perform
        - inputfile: string, path to the matrix of random
                    integer values to partition
    Returns the list of signs with the smallest residue.
    '''
    A = np.loadtxt(inputfile)
    if verbose:
        print(A)
    size = A.shape[0]
    randsol = np.asarray([1 if random.random() < 0.5 else -1 for i in range(size)])
    for i in range(max_iter):
        randsol2 = np.asarray([1 if random.random() < 0.5 else -1 for i in range(size)])
        if (compute_residue_n(A, randsol2.tolist()) < \
        compute_residue_n(A, randsol.tolist())):
            randsol = randsol2
        if (compute_residue_n(A, randsol) == 0):
            break
    return compute_residue_n(A, randsol)

def prepartitioned_rr(inputfile, max_iter, verbose=False):
    '''
    Repeated random algorithm on prepartitioned representation.
    (i.e. list of group IDs.)
    Arguments same as above.
    '''
    A = np.loadtxt(inputfile)
    if verbose:
        print(A)
    size = A.shape[0]
    randsol = np.random.randint(0, size, size=size)
    for i in range(max_iter):
        randsol2 = np.random.randint(0, size, size=size)
        if compute_residue_p(A, randsol2.tolist()) < \
            compute_residue_p(A, randsol.tolist()):
            randsol = randsol2
        if compute_residue_p(A, randsol.tolist()):
            break
    return compute_residue_p(A, randsol.tolist())

if __name__ == "__main__":
    # do some testing here
    print("------Beginning Unit Tests of the Normal Repeated Random function-------------")
    parser = argparse.ArgumentParser(description="repeated random unit tests")
    parser.add_argument('inputfile')
    parser.add_argument('max_iter', type=int)
    args = parser.parse_args()
    
    print(normal_rr(args.inputfile, args.max_iter, verbose=True))