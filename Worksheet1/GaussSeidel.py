import re 
n = int(input("Enter the number of equations: "))
eq = []
for i in range(n):
    s = input("Enter equation " + str(i+1) + ":")
    eq.append(s)

a = []

for x in eq:
    x = re.findall("(-?[\d]+)", x)
    x = [int(i) for i in x]
    a.append(x)
    
print("Matrix form: ")
for i in range(len(a)):
    print(a[i])

i = 0
initail  = [0]*n
values = [0]*n
maxiter = 25
while i < maxiter:
    for j in range(len(a)):
        k =0
        values[j] = a[j][-1]
        while k < (len(a[j])-1):
            if k!=j:
                values[j] -= values[k]*a[j][k]
            k+=1      
        values[j] /= a[j][j];
    print(values)
    i+=1;
