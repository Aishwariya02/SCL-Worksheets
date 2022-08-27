from sympy import var,Matrix,shape,eye,solve,multiply,det

x = var('x')


A = Matrix([[4,0,1],[-1,2,0],[2,0,1]])
l = shape(A)
I = eye(l[0])
H = A-(I*x)
det = det()
eigenvalues = solve(det,x)
print("Eigen values of A are ",eigenvalues)
for e in eigenvalues:
    H = A - (I.multiply(e))
    J=H.nullspace()
    for i in range(len(J)):
        print("Eigen vector for eigen value ",e," is: ",J[i].tolist())
