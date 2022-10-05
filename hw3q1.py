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

def get_bwm_stats(t): 
    longest_run = t[0]
    longest_run_len = 0
    num_runs = 0
    prev_char = t[0]
    this_run_len = 1
    for i in range(1, len(t), 1): 
        if t[i] == prev_char: 
            this_run_len += 1
            longest_run += t[i]
        else: 
            if (this_run_len > longest_run_len): 
                longest_run_len = this_run_len
            prev_char = t[i]
            num_runs += 1
            this_run_len = 1

    num_runs += 1 # account for final run
    return longest_run_len, num_runs


from io import StringIO
import sys
import numpy as np

# get command line inputs
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)

s1 = arguments[0]
s2 = arguments[1]

s1_bwm = bwm(s1)
s2_bwm = bwm(s2)

s1_bwt = bwtViaBwm(s1)
s2_bwt = bwtViaBwm(s2)

s1_max_run_len, s1_len_in_runs = get_bwm_stats(s1_bwt)
s2_max_run_len, s2_len_in_runs = get_bwm_stats(s2_bwt)

# IN THE CASE OF TIES ??
if s1_len_in_runs < s2_len_in_runs: 
    print(s1_bwt + ' ' + str(s1_len_in_runs) + ' ' + str(s1_max_run_len))
else: 
    print(s2_bwt + ' ' + str(s2_len_in_runs) + ' ' + str(s2_max_run_len))







