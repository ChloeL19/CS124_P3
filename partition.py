'''
Main program for running the various number parition 
algorithms.
'''
from repeated_random import *
from hill_climbing import *
from simulated_annealing import *
import time
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="partition script")
    parser.add_argument('flag', type=int)
    parser.add_argument('algorithm', type=int)
    parser.add_argument('inputfile')
    args = parser.parse_args()
    res=None
    if (args.algorithm == 0):
        start_time = time.time()
        res = kk_n(np.loadtxt(args.inputfile))
        end_time = time.time()
    if (args.algorithm == 1):
        start_time = time.time()
        res = normal_rr(args.inputfile, 25000)
        end_time = time.time()
    if (args.algorithm == 2):
        start_time = time.time()
        res = hill_climb_n(args.inputfile, 25000)
        end_time = time.time()
    if (args.algorithm == 3):
        start_time = time.time()
        res = sim_ann_n(args.inputfile, 25000)
        end_time = time.time()
    if (args.algorithm == 11):
        start_time = time.time()
        res = prepartitioned_rr(args.inputfile, 25000)
        end_time = time.time()
    if (args.algorithm == 12): pass
        #res = None
        # start_time = time.time()
        # res =  hill_climb_p(args.inputfile, 25000)
        # end_time = time.time()
    if (args.algorithm == 13): pass
        #res = None
        # start_time = time.time()
        # res = sim_ann_p(args.inputfile, 25000)
        # end_time = time.time()
    if res is not None:
        print(int(res))
        #print("Elapsed time: {}".format(end_time - start_time))
    else:
        print("eh")