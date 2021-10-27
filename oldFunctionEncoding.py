from math import *
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
plusMinus = ['+',"-"]

def f(x, fn):
    fn= fn.replace(' ' ,'')
    return float(recFunction(x, fn))  

def findBrackets(func):
    start = func.find("(")
    i = start + 1
    n = 1
    while n != 0:
        if func[i] == "(":
            n += 1
        elif func[i] == ")":
            n -= 1
        i += 1 
    end = i
    return start, end

def findRight(fn, pos):
    start = pos + 1
    n = start
    while fn[n] in numbers and n < len(fn) - 1 or n == start and fn[n] == "-":
        n += 1
    if n == len(fn) - 1:
        end = n + 1
    else:
        end = n
    return start, end

def findLeft(fn, pos):
    end = pos
    n = end - 1 
    while fn[n] in numbers and n >= 0:
        n -= 1
    if n != -1 and fn[n] in plusMinus:
        start = n
    else:
        start = n + 1
    return start, end

def findLeftRight(func, pos):
    startRight, endRight = findRight(func, pos)
    startLeft, endLeft = findLeft(func, pos)
    return startLeft, endLeft, startRight, endRight

def updateStr(fn, start, end, n):
    if n < 0:
        if start != 0 and fn[start - 1] == "+":
            fn = fn[: start - 1] + strDeleteE(n) + fn[end :]
        elif start != 0 and fn[start - 1] == "-":
            fn = fn[: start - 1] +"+"+ strDeleteE(abs(n)) + fn[end :]
        else:
            fn = fn[: start] + strDeleteE(n) + fn[end :]
    else:
        fn = fn[: start] + strDeleteE(n) + fn[end :] 
    return strDeleteE(fn)  

def updateStr2(fn, start, end, n):
    if n > 0 and (fn[start] == "+" or fn[start] == "-"):
        fn = fn[: start] +"+"+ strDeleteE(n) + fn[end :]
    else:
        fn = fn[: start] + strDeleteE(n) + fn[end :]      
    return strDeleteE(fn)  

def strDeleteE(x):
    x = str(x)
    if x.find("e") != -1:        
        nE = x.find("e")
        if x[nE + 1] == "+":
            st = int(x[nE + 2 :]) - 12
            nDot = x.find(".")
            x = x[: nDot] + x[nDot + 1 : nE]
            for i in range(0, st):
                x = x + "0"
        elif x[nE + 1] == "-":
            st = int(x[nE + 2 :])
            nDot = x.find(".")
            ss = "0."
            for i in range(1, st):
                ss = ss + "0"
            if x[0] == "-":
                x = "-" + ss + x[nDot - 1] + x[nDot + 1 : nE]
            else:
                x = ss + x[nDot - 1] + x[nDot + 1 : nE]

    return x 

def recFunction(x, fn):
    while fn.find("(") != -1:
        start, end = findBrackets(fn)
        insideBracets = fn[start + 1 : end - 1]
        fn = fn[: start] + recFunction(x, insideBracets) + fn[end :]

    while fn.find("x^") != -1:
        start, end = findRight(fn, fn.find("x^") + 1)
        n = float(fn[start : end])
        pw = pow(x, n)
        fn = updateStr(fn, start - 2, end, pw)   
    
    while fn.find("x*") != -1:
        start, end = findRight(fn, fn.find("x*") + 1)
        n = float(fn[start : end])
        s = x * n 
        fn = updateStr(fn, start - 2, end, s)

    while fn.find("*x") != -1:
        start, end = findLeft(fn, fn.find("*x"))
        n = float(fn[start : end])
        s = x * n 
        fn = updateStr2(fn, start, end + 2, s)  

    while fn.find("x") != -1:
        start  = fn.find("x")
        fn = updateStr(fn, start, start + 1, x)

    while fn.find("e^") != -1:
        start, end = findRight(fn, fn.find("e^") + 1)
        n = float(fn[start : end])
        pw = pow(exp(1), n)
        fn = updateStr(fn, start - 2, end, pw)     

    while fn.find("*") != -1 or fn.find("/") != -1:
        if fn.find("*") != -1 and fn.find("/") != -1:
            if fn.find("*") < fn.find("/"):
                startLeft, endLeft, startRight, endRight  = findLeftRight(fn, fn.find("*"))
                a = float(fn[startLeft : endLeft])
                b = float(fn[startRight : endRight])        
                s = a * b
            else:
                startLeft, endLeft, startRight, endRight  = findLeftRight(fn, fn.find("/"))
                a = float(fn[startLeft : endLeft])
                b = float(fn[startRight : endRight])        
                s = a / b
        elif fn.find("*") != -1:
            startLeft, endLeft, startRight, endRight  = findLeftRight(fn, fn.find("*"))
            a = float(fn[startLeft : endLeft])
            b = float(fn[startRight : endRight])        
            s = a * b
        else:
            startLeft, endLeft, startRight, endRight  = findLeftRight(fn, fn.find("/"))
            a = float(fn[startLeft : endLeft])
            b = float(fn[startRight : endRight])        
            s = a / b
        fn = updateStr2(fn, startLeft, endRight, s)

    if fn[0]=="+":
             fn = fn[1:] 

    while fn.find("+") != -1 or fn.find("-") != -1 and fn.rfind("-") != 0:     
        if fn.find("+") != -1 and fn.find("-") != -1 and fn.rfind("-") != 0:
            if fn.find("+") <  fn[1:].find("-"):
                startLeft, endLeft, startRight, endRight,  = findLeftRight(fn, fn.find("+"))
                a = float(fn[startLeft : endLeft])
                b = float(fn[startRight : endRight])        
                s = a + b                
            else:
                if fn.find("-") == 0:
                    startLeft, endLeft, startRight, endRight,  = findLeftRight(fn, fn[1 :].find("-"))
                else:
                    startLeft, endLeft, startRight, endRight,  = findLeftRight(fn, fn.find("-"))        
                a = float(fn[startLeft : endLeft])
                b = float(fn[startRight : endRight])        
                s = a - b
        elif fn.find("+") != -1:                
            startLeft, endLeft, startRight, endRight,  = findLeftRight(fn, fn.find("+"))
            a = float(fn[startLeft : endLeft])
            b = float(fn[startRight : endRight])        
            s = a + b
        else:
            if fn.find("-") == 0:
                    startLeft, endLeft, startRight, endRight,  = findLeftRight(fn, fn[1 :].find("-"))
                    endLeft += 1
                    startRight += 1
            else:
                startLeft, endLeft, startRight, endRight,  = findLeftRight(fn, fn.find("-"))        
            a = float(fn[startLeft : endLeft])
            b = float(fn[startRight : endRight])        
            s = a - b

        fn = fn[: startLeft] + strDeleteE(s) + fn[endRight :]
     

    return fn