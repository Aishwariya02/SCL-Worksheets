import numpy as np

def RK4_step(f,y,t,dt, N=1):
    dt /= N;
    for k in range(N):
        k1=f(y,t)*dt; k2=f(y+k1/2,t+dt/2)*dt; k3=f(y+k2/2,t+dt/2)*dt; k4=f(y+k3,t+dt)*dt;
        y, t = y+(k1+2*(k2+k3)+k4)/6, t+dt        
    return y

def Adams_Moulton_4th(function, y_matrix, time):
    y = np.zeros((np.size(time), np.size(y_matrix)))
    y[0] = y_matrix
### bootstrap steps with 4th order one-step method
    dt = time[1] - time[0]
    y[1] = RK4_step(function,y[0], time[0], dt, N=4)
    y[2] = RK4_step(function,y[1], time[1], dt, N=4)
    y[3] = RK4_step(function,y[2], time[2], dt, N=4)

    f_m2 = function(y[0], time[0])
    f_m1 = function(y[1], time[1])
    f_0 = function(y[2], time[2])
    f_1 = function(y[3], time[3])
    for i in range(3,len(time) - 1):
    ### first shift the "virtual" function value array so that
    ### [f_m3, f_m2, f_m1, f_0] corresponds to [ f[i-3], f[i-2], f[i-1], f[i] ]
        f_m3, f_m2, f_m1, f_0 = f_m2, f_m1, f_0, f_1
    ### predictor formula 4th order [ 55/24, -59/24, 37/24, -3/8 ]
        y[i+1] = y[i] + (dt/24) * (55*f_0 - 59*f_m1 + 37*f_m2 - 9*f_m3)
        f_1 = function(y[i+1], time[i+1])
    ### Corrector formula 4th order [ 3/8, 19/24, -5/24, 1/24 ]
        y[i+1] = y[i] + (dt/24) * (9*f_1 + 19*f_0 - 5*f_m1 + f_m2)
        f_1 = function(y[i+1], time[i+1])
    return y
