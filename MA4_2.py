#!/usr/bin/env python3.9

from person import Person
from fib import fib_py, fib_numba
import matplotlib.pyplot as plt
from time import perf_counter as pc

def main():
	print()
	print('Initial test of fib functions:')
	print('Python fib: ', fib_py(10))
	print('Numba fib: ', fib_numba(10))
	f = Person(10)
	print('C++ fib: ', f.fib())



	# Calculations
	x_axis = []
	python_time = []
	numba_time = []
	cpp_time = []
	for n in range(20,31):
		x_axis.append(n)

		# Python
		start = pc()
		fib_py(n)
		end = pc()
		python_time.append(end-start)

		# Numba
		start = pc()
		fib_numba(n)
		end = pc()
		numba_time.append(end-start)

		# C++
		start = pc()
		f = Person(n)
		f.fib()
		end = pc()
		cpp_time.append(end-start)

	
	# Plot for 3 calculations
	# plt.plot(x_axis, python_time, 'red', label='python')
	# plt.plot(x_axis, numba_time, 'blue', label='Numba')
	# plt.plot(x_axis, cpp_time, 'green', label='C++')
	# plt.legend(loc="upper left")
	# plt.xlabel("nth fibonacci number")
	# plt.ylabel("Calculation time")
	# plt.title("Fibonacci comparison")
	# plt.savefig('fib_plot.png')
	# print()

	# Plot for 2 calculations
	# plt.plot(x_axis, python_time, 'red', label='python')
	# plt.plot(x_axis, numba_time, 'blue', label='Numba')
	# plt.legend(loc="upper left")
	# plt.xlabel("nth fibonacci number")
	# plt.ylabel("Calculation time")
	# plt.title("Fibonacci comparison")
	# plt.savefig('fib_plot_2.png')
	# print()


	print('\nCalculating the 47th fib number')
	#Calculate 47th fib number with numba
	start = pc()
	fib = fib_numba(47)
	end = pc()
	print(f'Numba 47th fib number: {fib} in {end-start} seconds')

	#Calculate 47th fib number with C++
	start = pc()
	f = Person(47)
	fib = f.fib()
	end = pc()
	print(f'C++ 47th fib number: {fib} in {end-start} seconds')
	print()


	# The 46th fib number is 1836311903  and is fine for a 32bit system
	# The 47th fib number is 2971215073 and is to big for a 32bit system
	# Too big numbers are limited by "Integer overflow".

	# Calculating the 46th fib number works well with both Numba and C++
	 
	# Calculating the 47th fib number does not work for C++ but it does
	# work for Numba. C++ returns a negative value.

	# This suggests that C++ runs 32bit and Numba possible
	# runs 64bit? 

	
if __name__ == '__main__':
	main()
