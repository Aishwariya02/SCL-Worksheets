import numpy as np

x = [1,2,3,4]
y = [1,2,5,11]
unknown = float(input("Enter the value of x:"))

#Solving by System of Linear Equations

A = np.array([[4,1],[1,4]])
B = np.array([ 6*(y[0]-2*y[1]+y[2]), 6*(y[1]-2*y[2]+y[3]) ])
X2 = np.linalg.solve(A,B)

m = [None]*4
a=0
b=0

for i in range(4):
    if i==0 or i==3:
        m[i]=0
    else :
        m[i]=X2[i-1]
 
i=0
for i in range(1,len(x)):
    if unknown > x[i-1] and unknown < x[i]:
        a = x[i-1]
        b = x[i]
        break

value = ((1/6)*((b- unknown)**3*m[i-1]))+((1/6)*((unknown- a)**3*m[i]))+(x[i]-unknown)*(y[i-1]-(1/6)*m[i-1])+((unknown-x[i-1])*(y[i]-(1/6)*m[i]))

print("The value is:",value)
