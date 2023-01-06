'''
ESC251 - Homework 2
"Two Containers Connected by a Pipe"
Andy Kim
'''

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Close all plots
plt.close('all')

# Parameters
R = 100                 # kg
C1 = 2                  # kg
C2 = 1
pg = 1
K = R/pg
Qin = 0

def water(h,t):
    '''
    water
    '''
    dhdt1 = -(h[0]-h[1])/(R*C1) + (K/R*C1)*Qin
    dhdt2 = (h[0]-h[1])/(R*C2)
    dhdt = [dhdt1, dhdt2]
    return dhdt

# ICs
h0 = [125, 50]
t = np.linspace(0, 500, 2000)
y = odeint(water, h0, t)

# Plot q, theta (t)
fig = plt.figure(1)
plt.suptitle('ESC251 Homework 2 (Andy Kim)')                               # main title

plt.subplot(1,1,1)                                                                  # simulation 1
plt.title('Fluid Levels versus Time')
plt.plot(t, y[:,0], label='h1')
plt.plot(t, y[:,1], label='h2')
plt.xlabel('Time [s]')
plt.ylabel('Fluid Height')
plt.legend(loc = 'upper left')
#plt.ylim(0, 1.2)

#fig.subplots_adjust(wspace=0.4, hspace = 0.4)
plt.show()                                                                          # show plots
