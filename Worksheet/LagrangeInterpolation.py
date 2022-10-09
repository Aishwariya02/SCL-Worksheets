def lagrange_interpolation(x:list,y:list,xi:int):
    result=0.0
    for i in range(len(x)):
        term=y[i]
        #print(term)
        for j in range(len(x)):
            if j!=i:
                term=term*(xi-x[j])/(x[i]-x[j])
        result=result+term
    return result


x=[5,6,9,11]
y=[12,13,14,16]

x1 = int(input("Enter the point to be interpolated: "))
print("Value of y at x = ",x1," is ",lagrange_interpolation(x, y, x1))
