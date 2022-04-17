'''
Generates a list of 100 integers chosen uniformly
in the range [1,10^12].
'''

import numpy as np
import argparse

if __name__ == "__main__":
    # parse arguments
        # inputfile

    parser = argparse.ArgumentParser(description="data gen")
    parser.add_argument('inputfile')
    args = parser.parse_args()

    np.savetxt(args.inputfile, np.random.uniform(1, 10**12, size=100))