import sys

from sympy import sympify
from numpy import arange

start = eval(sys.argv[1])
end = eval(sys.argv[2])
step = eval(sys.argv[3])

X = arange(start, end + step, step)

var = sys.argv[5]
F = sympify(sys.argv[4])

def getPair(F, var, X):

    for i in X:

        y = F.evalf(subs={var: i})

        print("%.10f %.10f" % (i, y))

getPair(F, var, X)

