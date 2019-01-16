# TSP Local Solver

Python implementation of different local heuristics for the TSP.

	- Current Implementation has 2-opt Algorithm 
	- Multiple Adj Matrices are being used as a single matrix with all almost 200k points causes a memory error
	- Implemented 2-opt (n^2) on top 1000 points got from optimized set
	- Current implementation is more focused on not using a distance matrix but only make sure entire dataset is used
	- Will be Adding c++ code with better algorithms to this to make it more robust and optimized

## Installation

 * This is a standalone library, better included directly in large scale datasets. Works with Python 3 (3.7xx)
 * The input to this needs to be a .csv files with the coordinates of the cities
 * I am working on to make it more generic as a package

### Optional

 * [Doctest][doctest] for running tests.
 * [Pytest][pytest] for test integration.
 * [Yapf][yapf] for code formatting.


## TODO

 * Improve by adding LKH, and k-opt Algorithms
 * Verify with more test cases

[doctest]: https://docs.python.org/2/library/doctest.html
[pytest]: https://docs.pytest.org/en/latest/
[yapf]: https://github.com/google/yapf


## Travis-Build
[![Build Status](https://api.travis-ci.org/sananand007/genTspsolver.png?branch=master)](https://travis-ci.org/sananand007/genTspsolver)
