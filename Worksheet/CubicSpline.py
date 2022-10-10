import re
from sympy import Symbol

# Gauss Jordan Elimination
import math
def non_zero(row):
  for i in range(len(row)):
    if row[i] != 0:
      return i

def rref(matrix):
  rows = len(matrix)
  columns = len(matrix[0])
  non_zero_index = -1

  # Arrange the rows by leftmost non-zero entry
  matrix.sort(key = non_zero)
  for i in range(0, rows):
  # Making the first non-zero element 1
    for j in range(columns):
      if not math.isclose(matrix[i][j], 0.0):
        non_zero_index = j
        matrix[i] = [x / matrix[i][j] for x in matrix[i]]
        break

  # Making leading coefficient column corresponding values 0
    for j in range(rows):
      if j == i:
        continue
      else:
        ratio = matrix[j][non_zero_index] / matrix[i][non_zero_index]
        row = [x * ratio for x in matrix[i]]
        matrix[j] = [x - y for x, y in zip(matrix[j], row)]
  print("The given matrix in RREF is:")
  for row in matrix:
    print(row)
  return matrix

# Finding the augmented matrix
def augmented_matrix(eqn_list,eqn_count):
    aug_matrix=[]
    for i in eqn_list:
         val = re.findall(r'[\d\.\-\+]+',i)
         #print(val)
         val = [int(x) for x in val]
         aug_matrix.append(val)
    #print(aug_matrix)
    del aug_matrix[0][0]
    del aug_matrix[eqn_count-1][eqn_count]
    #print(aug_matrix)
    return aug_matrix



def eq(x,y,v,n):
  l=[]
  for i in range(1,n):
    temp=''
    temp+=str(1)
    temp+=str(v[i-1])
    temp+='+'
    temp+=str(4)
    temp+=str(v[i])
    temp+='+'
    temp+=str(1)
    temp+=str(v[i+1])
    temp+='='
    temp+=str(6*y[i-1]-12*y[i]+6*y[i+1])
    #print(temp)
    l.append(temp)
  return l





x_val=[1,2,3,4]
y=[1,2,5,11]
n=len(x_val)-1
v=['x','y','z','a','b']
eq_list=eq(x_val,y,v,n)
aug=augmented_matrix(eq_list,len(eq_list))
aug = rref(aug)
rank = len(aug)
zeros = [0] * len(aug[0])
solution = []
for row in aug:
  if row == zeros:
    rank -= 1
# Unique Solution
if rank == len(aug[0]) - 1:
  for i in range(len(aug) - 1, -1, -1):
    for j in range(len(aug[0]) - 1):
      if math.isclose(aug[i][j], 0.0):
        continue
      else:
        solution.insert(0, aug[i][len(aug[0]) - 1])
  print("Unique Solution:", solution)
# Infinite Solutions
elif rank < len(aug[0]) - 1:
  print("Infinite Solutions")
# No solution
else:
  print("No Solution")
solution.insert(0,0)
solution.append(0)
print(solution)
x = Symbol('x')
p=1.5
final_eq=[]
dif=[]
print('The equations are: ')
for i in range(n):
  d=1/6*(x_val[i+1]-x)**3*solution[i]+1/6*(x-x_val[i])**3*solution[i+1]+(x_val[i+1]-x)*(y[i]-(1/6*solution[i]))+(x-x_val[i])*(y[i+1]-(1/6*solution[i+1]))
  final_eq.append(str(d))
  print(d)
  dif.append(abs(i-int(p-1)))
f_eq_index=dif.index(min(dif))
x=p
f_value=eval(final_eq[f_eq_index])
print('The value using cubic spline is: ',end=' ')
print(f_value)
