from sympy import symbols, sympify
x = symbols('x')

def func(val,k): 
    return k.subs(x,val).evalf()

def regulaFalsi(k,a,b):
 
    if (func(a,k) * func(b,k) >= 0):
        print("Invalid values of a and b")
        return
  
    c = a 
    for i in range(1000):
        c = (a*func(b,k)-b*func(a,k))/(func(b,k)-func(a,k))
        if (func(c,k) == 0.0):
            break
        if (func(c,k)*func(a,k) < 0):
            b = c
        else:
            a = c
             
    print("The value of root is : ","%.4f"%c)
     
k = input("Enter the equation : ")
k = sympify(k)
print(k)

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
regulaFalsi(k,a,b)
