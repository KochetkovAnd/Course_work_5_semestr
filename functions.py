from sympy import *

def method_chord(fn, x0, e):

    expr = sympify(fn)
    f = lambdify("x", expr)

    x, xPrev = x0, x0 + e * 2
    Xs = []
    i = 0 
    while abs(x - xPrev) > e and i < 500: 
        x, xPrev =  x - f(x) * (x - xPrev) / (f(x) - f(xPrev)), x   
        Xs.append((i, x, abs(xPrev - x)))   
        i += 1 
    if(i == 500):
        return "Корней нет или задана слишком малая погрешность", []
    return x, Xs  