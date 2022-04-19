'''
A set of helper functions for doing basic, common
things across the other algorithms.
'''
import numpy as np
import random
import sys
from kk import *

def compute_residue_n(A, S):
    '''
    Compute residue from the standard (i.e sign list)
    representation of a solution.
        - A: list of integers
        - S: list of signs (the "solution")
    '''
    res = 0
    try:
        for (a, s) in zip(A, S):
            res += a*s
    except:
        import pdb; pdb.set_trace();
    return abs(res)

def pp_conversion(A, G):
    '''
    Convert a solution in prepartitioned form to standard form.
        - A: list of integers that have been assigned groups
        - G: list of group IDs for each of the integers
    '''
    seen_gids = []
    res = []
    for i in range(len(A)):
        if G[i] in seen_gids:
            Aind = G.index(G[i]) # find first instance of this gid
            res[Aind] += A[i]
            res.append(0)
        else:
            res.append(A[i])
            seen_gids.append(G[i])
    return res

def compute_residue_p(A, G):
    '''
    Compute the residue for a prepartitioned solution 
    representation.
    '''
    standardform = pp_conversion(A,G)
    return kk_n(standardform)

def getNeighborN(S):
    '''
    Returns the neighbor of a state as defined on this
    statespace in normal form.
    - S: a solution represented in normal form
    '''
    size = len(S)
    tind = np.random.choice(np.arange(size), size=2, replace=False)
    Sn = S.copy()
    Sn[tind[0]] *= -1
    if random.random() < 0.5:
        Sn[tind[1]] *= -1
    return Sn

def getNeighborP(G):
    '''
    Returns the neighbor of a state as defined on this statespace
    in prepartitioned form.
    - G: int list, group IDs for all integers
    '''
    size = len(G)
    all_indices = set(np.arange(size).tolist())
    tind = np.random.choice(np.arange(size), size=1, replace=False)
    other_inds = list(all_indices.difference(set(G[tind])))
    new_gid = np.random.choice(np.asarray(other_inds))
    Gn = G.copy() 
    Gn[tind[0]] = new_gid
    return Gn

# notes on why prepartitioned better: kk is deterministic
# partitioning: just run kk, each element has a specific way in
# which it can be grouped with other elements
# smallest element never paired up with first element in first iteration?
# partitioning: group elements beforehand, make it so there are more different
# groups that we can obtain
# each element as own partition, the same as kk
# when put these together, always get strictly more possible results
# gives more options, then when run randomized algos, more likely to go towards
# actual optimum

# other notes: should time these and discuss the runtime

class MaxBinHeap:
    '''
    A binary heap implementation that supports retrieving
    maximum elements, insertions, and deletions.
    The binary heap is implemented as an array.
    Thank you to this source: https://www.geeksforgeeks.org/max-heap-in-python/
    '''
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.sysmaxsize = -sys.maxsize - 1
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = -1 * self.sysmaxsize
        self.FRONT = 1

    def parent(self, pos):
        '''
        Return the parent index of pos.
        '''
        return pos//2

    def leftChild(self, pos):
        '''
        Return index of the left child of pos.
        '''
        return 2 * pos

    def rightChild(self, pos):
        '''
        Return index of the right child of pos.
        '''
        return (2 * pos) + 1

    def isLeaf(self, pos):
        '''
        Returns true if pos represents a leaf node.
        '''
        return pos*2 > self.size

    def swap(self, fpos, spos):
        '''
        Swap two nodes in the heap.
        '''
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def maxHeapify(self, pos):
 
        # If the node is a non-leaf node and smaller
        # than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
                self.Heap[pos] < self.Heap[self.rightChild(pos)]):
  
                # Swap with the left child and heapify
                # the left child
                if (self.Heap[self.leftChild(pos)] > 
                    self.Heap[self.rightChild(pos)]):
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))
  
                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

    def insert(self, element):
        '''
        Insert an element into the heap.
        '''
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element
  
        current = self.size
  
        while (self.Heap[current] > 
               self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def getMax(self):
        '''
        Get the max element from the heap.
        '''
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-= 1
        self.maxHeapify(self.FRONT)
        return popped

    def maxHeap(self):
        for pos in range(self.size//2, 0, -1):
            self.maxHeapify(pos)

    def Print(self):
        for i in range(1, (self.size//2)+1):
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1]))

if __name__ == "__main__":
    # unit test the compute_residue_n function
    print("---------Unit Testing Normal Residue Calculations-----------")
    numarr = np.loadtxt('data/instance1.txt')
    numarr = numarr[:3]
    randsol = np.asarray([1 if random.random() < 0.5 else -1 for i in range(100)])
    randsol = randsol[:3]
    print(numarr)
    print(randsol)
    print(compute_residue_n(numarr, randsol))

    # unit test the max_heap
    print("---------------Unit Testing Max Heap----------------")
    print('The maxHeap is ')
    maxHeap = MaxBinHeap(15)
    maxHeap.insert(5)
    maxHeap.insert(3)
    maxHeap.insert(17)
    maxHeap.insert(10)
    maxHeap.insert(84)
    maxHeap.insert(19)
    maxHeap.insert(6)
    maxHeap.insert(22)
    maxHeap.insert(9)
    maxHeap.maxHeap()
 
    maxHeap.Print()
    print("The Max val is " + str(maxHeap.getMax()))

    # unit test the conversion from prepartitioned
    print("---------------Unit Testing Prepartition Conversion----------------")
    print(numarr)
    print(pp_conversion(numarr, [1,2,2]))