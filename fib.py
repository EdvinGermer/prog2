from numba import njit

def fib_py(n):
        """ Recursive fibonacci function from instructions """
        if n <= 1:
                return n
        else:
                return(fib_py(n-1) + fib_py(n-2))


@njit
def fib_numba(n):
        """ Recursive fibonacci function from instructions with numba decorator """
        if n <= 1:
                return n
        else:
                return(fib_numba(n-1) + fib_numba(n-2))
