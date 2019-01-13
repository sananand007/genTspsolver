# TSP Local Solver

Python implementation of different local heuristics for the TSP.

	- Current Implementation has 2-opt Algorithm 
	- Multiple Adj Matrices are being used as a single matrix with all almost 200k points causes a memory error
	- Implemented 2-opt (n^2) on top 1000 points got from optimized set

## Installation

This is a standalone library, better included directly in projects. Works with Python 3 (3.7xx)

### Optional

 * [Doctest][doctest] for running tests.
 * [Pytest][pytest] for test integration.
 * [Yapf][yapf] for code formatting.


## TODO

 * Improve LKH, some of Helsgaun work is in there but more can be added.
 * Verify that 3 works

[doctest]: https://docs.python.org/2/library/doctest.html
[pytest]: https://docs.pytest.org/en/latest/
[yapf]: https://github.com/google/yapf


## Travis-Build
[![Build Status](https://travis-ci.org/{sananand007}/{genTspsolver}.png?branch=master)](https://travis-ci.org/{sananand007}/{genTspsolver})


## Travis-Docs
[![Inline docs](http://inch-ci.org/github/{ORG-or-sananand007}/{genTspsolver}.svg?branch=master)](http://inch-ci.org/github/{ORG-or-sananand007}/{genTspsolver})
