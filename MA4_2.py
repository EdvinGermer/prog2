#!/usr/bin/env python3.9

from person import Person
from fib import fib_py, fib_numba
import matplotlib.pyplot as plt
from time import perf_counter as pc

def main():
	print('Initial test of fib functions:')
	print('Python fib: ', fib_py(10))
	print('Numba fib: ', fib_numba(10))
	f = Person(10)
	print('C++ fib: ', f.fib())

if __name__ == '__main__':
	main()
