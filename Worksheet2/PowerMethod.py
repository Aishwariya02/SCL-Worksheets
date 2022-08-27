import numpy as np


def power(a,x):
    for i in range(10):
        x = np.dot(a, x)
        x_n = x / x.min()
    print('Power method:')
    print('Eigentvector of matrix')
    for i in range(len(a)):
        print(a[i])
    print("is ", x_n)
    find_ray(a,x_n)
    
def find_ray(a,x_n):
    h=np.dot(a,x_n)
    m=np.dot(h,x_n)
    
    x_2=np.dot(x_n,x_n)
    dom_eival=m/x_2
    print('Reyleigh quotient method:')
    print('The dominant eigen value for matrix {} is {:.2f}'.format(a.tolist(),dom_eival))    


ab = np.array([[2, -12], 
              [1, -5]])   
x=np.array([1,1]) 
power(ab,x)
