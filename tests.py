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
from concorde.tsp import TSPSolver
from find_dist import Calculate_dist
from tsp-local_2opt import Two_opt

if __name__=="__main__":
	csv_input = os.getcwd()
	print(f'path - {csv_input}')
	Obj = Two_opt(csv_input)