'''
ESC251 - Take Home Exam - Question 3

Andy Kim
'''

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from control.matlab import sys, ss, step

# Close all plots
plt.close('all')

# Parameters
R1 = 1.32 * (10^9)                 # kg
R2 = 10 * R1
g = 9.8
pg = g * 13.5 * (10^3)
A = 5*(10^(-4))
j = A*R1
k = pg/A
patm = 10e4

# Step
A = [[k*((1/R1)+(1/R2)), -k/R2],
    [-k/R2, k/R2]]
B = [[-1/(j)], [0]]
C = np.eye(2)
D = [[0],[0]]

t = np.linspace(0,100,500)
sys = ss(A, B, C, D)
y, t = step(sys, t, 0)

# Plot q, theta (t)
fig = plt.figure(1)
plt.subplot(1,1,1)                                                                  # simulation 1
plt.title('Fluid Levels versus Time')
plt.plot(t, patm * y[:,0], label='h1')
plt.plot(t, patm * y[:,1], label='h2')
plt.xlabel('Time [s]')
plt.ylabel('Fluid Height')
plt.legend(loc = 'upper right')
#plt.ylim(0, 1.2)

#fig.subplots_adjust(wspace=0.4, hspace = 0.4)
plt.show()                                                                          # show plots
