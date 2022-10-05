def rotations(t):
    # Return list of rotations of input string t
    tt = t * 2
    return [ tt[i:i+len(t)] for i in range(0, len(t)) ]

def bwm(t):
    # Return lexicographically sorted list of t’s rotations
    return sorted(rotations(t))

def bwtViaBwm(t):
    # Given T, returns BWT(T) by way of the BWM
    return ''.join(map(lambda x: x[-1], bwm(t)))

def expand_bwt(compressed_bwt): 
    expanded_txt = ''
    i = 0
    this_run_char = ''
    this_run_len = 0
    while i < len(compressed_bwt): 
        if compressed_bwt[i] == ' ': 
            i += 1
            continue
        this_run_char = compressed_bwt[i]
        this_run_len = int(compressed_bwt[i + 2])
        this_run_str = this_run_char * this_run_len
        expanded_txt += this_run_str
        i += 3
    return expanded_txt

from io import StringIO
import sys
import numpy as np

# get command line inputs
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)

compressed_bwt = arguments[0]
expanded_bwt = expand_bwt(compressed_bwt)
print(expanded_bwt)