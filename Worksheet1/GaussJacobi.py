from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

def jacobi(A, b, N=25, x=None):
    if x is None:
        x = zeros(len(A[0]))
    D = diag(A)
    R = A - diagflat(D)
    for i in range(N):
        x = (b - dot(R, x)) / D
    return x


n = int(input("Enter the number of equations: "))
m = int(input("Enter the number of unknowns: "))
a = []
c=[]
for i in range(n):
    b = []
    for j in range(m+1):
        if j == m:
            num = int(input("Enter constant term: "))
            c.append(num)
        else:
            num = int(input("Enter matrix entry ["+str(i)+"]["+str(j)+"]: "))
            b.append(num)
    a.append(b)
# print(a)
# print(c)
print("Input Matrix :")
for i in range(len(a)):
    print(a[i])
    
A = array(a)
b = array(c)
guess = array([1.0]*n)
sol = jacobi(A, b, N=25, x=guess)
print("A: ")
pprint(A)
print("B: ")
pprint(b)
print("x = ")
pprint(sol)
