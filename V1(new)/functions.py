from re import X
from sympy import *

def method_chord(fn, xStart, xFinish, e):

    expr = sympify(fn)
    f = lambdify("x", expr)

    K = 10000 # число итераций после которых выходит 
    
    Xs = []

    printE = numberSigns(e) + 1

    x0, x1, x2 = xStart, xFinish, xFinish - f(xFinish) * (xFinish - xStart) / (f(xFinish) - f(xStart))
    Xs.append((1, round(x0, printE), round(x1, printE), round(x2, printE), round(f(x2), printE)))
    i = 2 
    while abs(f(x2)) > e:
        s = x2 - f(x2) * (x2 - x1) / (f(x2) - f(x1))
        x0, x1, x2 = x1, x2, x2 - f(x2) * (x2 - x1) / (f(x2) - f(x1))
        Xs.append((i, round(x0, printE), round(x1, printE), round(x2, printE), round(f(x2), printE)))  
        i += 1 
    if(i == K):
        return "Корней нет или задана слишком малая погрешность\nили задан слишком большой интервал", []
    return round(x2, printE), Xs

def checkFor(fn, x0, x1):
    expr = sympify(fn)
    f = lambdify("x", expr)
    return f(x0) >= 0 and f(x1) < 0 or f(x1) >= 0 and f(x0) < 0

def numberSigns(e):
    s = str(e)
    if '.' in s:
        return len(s[s.find('.') + 1 :])
    else:
        return 0 
