import sys

from sympy import sympify, sign, diff

def func(F, var, x):

    return sympify(F, {var: x}).evalf()

def newton(x0, F, Tol, N, var):

    Df = diff(F, var)

    k = 0

    print("%d %.10f" % (k, x0))

    while k < N:

        x = x0 - (func(F, var, x0) / Df.evalf(subs={var: x0}))

        print("%d %.10f" % (k + 1, x))

        if abs(x - x0) < Tol:

            return x

        k += 1

        x0 = x

    print("Max iterations reached")

x0 = eval(sys.argv[1])

F = sys.argv[2]
tol = eval(sys.argv[3])
N = eval(sys.argv[4])

var = sys.argv[5]

newton(x0, F, tol, N, var)
