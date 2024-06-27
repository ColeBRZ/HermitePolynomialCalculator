import sympy as smp
import math

def nDerivatives(fx, n):
    x = smp.symbols('x', real=True)
    derivatives = []
    for i in range(1, n+1):
        d_o_f = smp.diff(fx, x, i)
        derivatives.append(d_o_f)
    return derivatives

def hermiteExtractor(fx, n):
    x = smp.symbols('x', real=True)
    derivatives = nDerivatives(fx, n)
    for i in range(n):
        thereturn = (-1)**i * smp.exp(x**2) * derivatives[i]
        print(f"H_{i+1} = {thereturn}")

x = smp.symbols('x', real=True)
function = smp.exp(-x**2)
hermiteExtractor(function, 100)