def f(x):
    return x ** 3 + x - 1

def method_chord2(x0, e):
    xPrev,x = x0, x0 + 2 * e
    while abs(x - xPrev) > e:   
        x, xPrev =  x - f(x) * (x - xPrev) / (f(x) - f(xPrev)), x       
    return x

#print(method_chord2(-10, 0.001))

f ="0"
print(f.isdigit())