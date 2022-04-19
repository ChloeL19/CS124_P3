'''
The karmarker karp algorithm, run on standard input.
'''
import numpy as np
from utils import *

def kk_n(A, verbose=False):
    '''
    KK algorithm on normal data representation.
    '''
    if verbose:
        print(A)
    size = A.shape[0]
    maxHeap = MaxBinHeap(size + 1)
    for i in range(size):
        maxHeap.insert(A[i])
    maxHeap.maxHeap()
    while maxHeap.size > 1: # include max_iter here??
        n1 = maxHeap.getMax()
        n2 = maxHeap.getMax()
        maxHeap.insert(abs(n1-n2))
    residue = maxHeap.getMax()
    return residue

if __name__ == "__main__":
    # unit test the KK algorithm
    pass