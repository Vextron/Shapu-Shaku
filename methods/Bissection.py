import sys

from sympy import sympify, sign

def func(F, var, x):

    return sympify(F, {var: x}).evalf()

def bissect(a, b, F, Tol, N, var):

    k = 1

    Pn = (a + b)/2
    Fn = func(F, var, Pn)

    print("%d %.10f %.10f %.10f %.10f" % (k, a, b, Pn, Fn))

    while k < N and abs(a - b) / 2 > Tol:

        if sign(func(F, var, a)) == sign(Fn):

            a = Pn

        else:

            b = Pn

        Pn = (a + b)/2
        Fn = func(F, var, Pn)

        k += 1

        print("%d %.10f %.10f %.10f %.10f" % (k, a, b, Pn, Fn))

    if k >= N:

        print('Max iterations reached')

a = eval(sys.argv[1])
b = eval(sys.argv[2])

F = sys.argv[3]
tol = eval(sys.argv[4])
N = eval(sys.argv[5])
var = sys.argv[6]

bissect(a, b, F, tol, N, var)


