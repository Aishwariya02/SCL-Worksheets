def inverse_lagrange_interpolation(x,y,yi):
       result=0.0
       for i in range(len(x)):
         term = x[i]
         print(term)
         for j in range(len(x)):
             if j!=i:
                 term=term*(yi-y[j])/(y[i]-y[j])
         result=result+term
       return result

x=[5,6,9,11]
y=[12,13,14,16]

y1 = float(input("Enter y to be interpolated: "))
print('Value of x at y = ',y1,'is ',inverse_lagrange_interpolation(x, y, y1))
