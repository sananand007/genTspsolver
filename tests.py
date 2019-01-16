'''
Tests to Run on TRAVIS CI
'''
import sys, os
import pandas as pd
from glob import glob
import numpy as np
from itertools import combinations_with_replacement, combinations, permutations
from haversine import haversine
import time
from find_dist import Calculate_dist
sys.path.append(os.path.join(os.path.dirname(__file__), "tsp-local_2opt"))

if __name__=="__main__":
	csv_input = os.getcwd()
	Obj = Two_opt(csv_input)