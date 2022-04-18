'''
A set of helper functions for doing basic, common
things across the other algorithms.
'''
import numpy as np
import random

def compute_residue_n(A, S):
    '''
    Compute residue from the standard (i.e sign list)
    representation of a solution.
        - A: list of integers
        - S: list of signs (the "solution")
    '''
    res = 0
    for (a, s) in zip(A, S):
        res += a*s
    return abs(res)

if __name__ == "__main__":
    # unit test the compute_residue_n function
    numarr = np.loadtxt('data/instance1.txt')
    numarr = numarr[:3]
    randsol = np.asarray([1 if random.random() < 0.5 else -1 for i in range(100)])
    randsol = randsol[:3]
    print(numarr)
    print(randsol)
    print(compute_residue_n(numarr, randsol))