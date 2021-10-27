from re import X
from sympy import *

def method_chord(fn, x0, x1, e):

    expr = sympify(fn)
    f = lambdify("x", expr)
    
    Xs = []
    Xs.append(( x1, f(x1),  x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))))
    x, xPrev = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0)), x1
    Xs.append(( x, f(x),  x - f(x) * (x - x1) / (f(x) - f(x1))))
    i = 1 
    while abs(x - xPrev) > e and i < 50000: 
        x, xPrev =  x - f(x) * (x - x1) / (f(x) - f(x1)), x
        Xs.append((x, f(x), x - f(x) * (x - x1) / (f(x) - f(x1))))   
        i += 1 
    if(i == 50000):
        return "Корней нет или задана слишком малая погрешность", []
    return x, Xs

def checkFor(fn, x0, x1):
    expr = sympify(fn)
    f = lambdify("x", expr)
    return f(x0) >= 0 and f(x1) < 0 or f(x1) >= 0 and f(x0) < 0