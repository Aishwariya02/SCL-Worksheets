from sympy import symbols,sympify,diff

x = symbols('x')

def func(equation,k):
    return equation.subs(x,k).evalf()

def diff_eval(equation,k):
    return func(diff(equation,x),k)

def fixed_point(equation,a,b,f):
    if func(equation,a)*func(equation,b)>0:
        print("Give a correct value for a and b")
    else:
        difa = abs(diff_eval(f,a));
        difb = abs(diff_eval(f,b));

        print(difa,"\n");
        print(difb,"\n");

        if max(difa,difb)>=1:
            print("Convergence criteria not satisfied");
        else:
            while abs(func(f,a)-a) > 0.0001:
                a = func(f,a)
            print("The root is :", "%.4f"%a)

def main():
    equation = input("Enter the equation")
    equation = sympify(equation)

    print(equation)

    a = int(input("Enter A : "))
    b = int(input("Enter B : "))

    f = sympify(input("Enter an iteration function"));

    fixed_point(equation,a,b,f);

main()
