import math

def f(x):
    return 3*x + math.cos(x) - x
  
def bisection(a,b):
 
    if (f(a) * f(b) >= 0):
        print("You have not assumed right a and b\n")
        return
  
    c = a
    while ((b-a) >= 0.01):
        c = (a+b)/2
        if (f(c) == 0.0):
            break
        if (f(c)*f(a) < 0):
            b = c
        else:
            a = c
             
    print("The value of root is : ","%.4f"%c)
     
# Driver code
# Initial values assumed
a =-1
b = 0
bisection(a, b)
