'''
The karmarker karp algorithm, run on standard input.
'''
import numpy as np
from utils import *

def kk_n(inputfile, max_iter, verbose=False):
    '''
    KK algorithm on normal data representation.
    '''
    A = np.loadtxt(inputfile)
    if verbose:
        print(A)
    size = A.shape[0]
    
    return None, None

if __name__ == "__main__":
    # unit test the KK algorithm
    pass