def f(x):
    return x * x * x - x * x + 2

def df(x):
    return 3 * x * x - 2 * x

def newtonRaphson( x ):
    h = f(x) / df(x)
    while abs(h) >= 0.0001:
        h = f(x)/df(x)
        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h
    print("The value of the root is : ", "%.4f"% x)
 
x0 = 0.1 # Initial value
newtonRaphson(x0)
