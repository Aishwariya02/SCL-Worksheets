n = int(input("Enter the number of rows of matrix: "))
m = int(input("Enter the number of cols of matrix: "))

a = []
final = []
for i in range(n):
    b = []
    for j in range(m):
        num = int(input("Enter matrix entry ["+str(i)+"]["+str(j)+"]: "))
        b.append(num)
    a.append(b);
    
    
print("Input Matrix :")
for i in range(len(a)):
    print(a[i])

flag = 1;
iternum = 0
zero = [0]*m
b=[]
while flag:
    c = 0
    b = []
    for i in a:
        if i != zero:
            b.append(i)
        else:
            c +=1
    j=0
    while j<c:
        b.append(zero)
        j+=1
    
    pos = m+1;
    value = -1000
    swap = 0;
    for i in range(n-c):
        for j in range(m):
            if b[i][j] != 0:
                if j<=pos and value<b[i][j]:
                    value = b[i][j]
                    pos = j
                    swap = i
                    
            break;
    if pos == m+1:
        pos = 0
    
    c_ = b[swap]
    b[swap] = b[0]
    b[0] = c_
    
    #print(b[0])
    
    scalar = b[0][pos]
    
    if scalar!=0:
        for i in range(m):
            b[0][i] /=scalar
    
    print("After Iteration " + str(iternum) + " : ")
    for i in range(len(b)):
        print(b[i])
    
    for i in range(1,n):
        scalar = b[i][pos]
        if scalar != 0:
            for j in range(m):
                b[i][j] -= scalar*b[0][j]
     
    #print("After making all the values in the column of leading 1 zero : ",b)
    
    if len(b) == 1:
        flag = 0
        d = [0]*iternum + b[0]
        final.append(d)
        
    else:
        d = [0]*iternum + b[0]
        final.append(d)
        a = []
        for i in range(1,n):
            a_ = []
            for j in range(1,m):
                a_.append(b[i][j])
            a.append(a_)
        
        #print("Matrix for next iteration : ",a)
        n = n-1
        m = m-1
        iternum +=1 
        
        
        
print("Final matrix after performing Gauss Jordan Elimination : ")
for i in range(len(final)):
    print(final[i])
