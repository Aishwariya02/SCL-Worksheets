n2 = int(input("Enter number of equations:"))
n1 = int(input("Enter number of unknowns:"))
augmatrix = []
for i in range(n2):
    print("Equation "+str(i+1)+": ")
    a = []
    for j in range(n1):
        n = int(input("Enter coefficient of x"+str(j+1)+": "))
        a.append(n)
    b = int(input("Enter RHS of the eqn: "))
    a.append(b)
    augmatrix.append(a)
print("The augmented matrix is:")
for i in range(n2):
    print(augmatrix[i])

pos = -1;
flag = 0;
zero = [0]*(n1+1);
for i in range(n2):
    if augmatrix[i] == zero:
        for k in range(i+1,n2):
            if augmatrix[k] != zero:
                print("Not a REF")
                flag = 1
    else:
        for index in range(0,n1+1):
            if augmatrix[i][index] != 0:
                if index > pos:
                    pos = index                    
                    break;
                else:
                    print("Neither REF nor RREF");
                    flag = 1
                    break;

                    
        for k in range(i+1,n2):
            if augmatrix[k][pos] != 0:
                print("Neither REF nor RREF");
                flag = 1;
                break;
    
    if flag == 1:
        break;
        
        
    else:
        if augmatrix[i][pos] != 1:
            print(pos)
            print('The matrix is in REF but not in RREF')
            break;
        
        for k in range(0,n2):
            if k!=i:
                print(pos)
                if augmatrix[k][pos] !=0:
                    flag = 1;
                    print("The matrix is in REF but not in RREF");
                    break;
         
    if flag == 1:
        break;
