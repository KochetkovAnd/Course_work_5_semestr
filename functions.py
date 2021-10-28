from re import X
from sympy import *

def method_chord(fn, x0, x1, e):

    expr = sympify(fn)
    f = lambdify("x", expr)

    K = 100000 # число итераций после которых выходит 
    
    Xs = []
    Xs.append((0, x1, f(x1)))
    x, xPrev = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0)), x1
    Xs.append((1, x, f(x)))
    i = 2 
    while abs(x - xPrev) > e and i < K:
        x, xPrev =  x - f(x) * (x - x1) / (f(x) - f(x1)), x
        Xs.append((i, x, f(x)))   
        i += 1 
    if(i == K):
        return "Корней нет или задана слишком малая погрешность", []
    return x, Xs

def checkFor(fn, x0, x1):
    expr = sympify(fn)
    f = lambdify("x", expr)
    return f(x0) >= 0 and f(x1) < 0 or f(x1) >= 0 and f(x0) < 0