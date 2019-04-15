import sys
from sympy import latex, sympify, diff

f = sys.argv[1]

print(latex(sympify(f)))
