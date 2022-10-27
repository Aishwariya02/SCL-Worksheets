import numpy as np

# Define parameters
f = lambda t, s: np.exp(-t) # ODE
h = 0.1 # Step size
t = np.arange(0, 1 + h, h) # Numerical grid
s0 = -1 # Initial Condition

s = np.zeros(len(t))
sp= np.zeros(len(t))
s[0] = s0
sp[0] = s0

for i in range(0, len(t) - 1):
    s[i + 1] = s[i] + h*f(t[i], s[i])
    sp[i+1]= s[i] + h*0.5*(f(t[i],s[i]) + f(t[i+1], s[i+1]))

print(sp)
