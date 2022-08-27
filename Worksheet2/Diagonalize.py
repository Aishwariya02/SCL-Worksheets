import sympy as sp
import numpy as np
x=sp.var('x')

def eigen_vector(mat,l):
    length=mat.shape[0]
    I=sp.eye(length)
    Z=I.multiply(l)
    H=mat-Z
    J=H.nullspace()
    return J
    
def eigen_value(mat):
    length=mat.shape[0]
    I=sp.eye(length)
    Z=I.multiply(x)
    H=mat-Z
    Det=H.det()
    print("Diagonlisation of {} is \n".format(mat.tolist()))
    L=sp.solve(Det,x)
    l=[]
    for i in L:
        k=eigen_vector(mat,i)

        for j in range(len(k)):
            l.append(k[j].tolist()) 
    M=np.empty((mat.shape[0],len(l)))
    for i in range(len(l)):
        for j in range(mat.shape[0]):
            M[j][i]=l[i][j][0]
    
    Mi=np.linalg.inv(M)
    print(M)
    K=Mi.dot(mat)
    K=K.dot(M)
    print(K)
       
A = sp.Matrix([[1,0],[6,-1]])
eigenvalue(A)
p,d = A.diagonalize()
print(p)
