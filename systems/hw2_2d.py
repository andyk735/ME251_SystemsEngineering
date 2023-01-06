'''
ESC251 - Homework 2
"Two Containers Connected by a Pipe"
Andy Kim
'''
from scipy import signal
#from scipy.integrate import odeint
#import numpy as np
import matplotlib.pyplot as plt

# Close all plots
plt.close('all')

# Parameters
R = 100000
C = 2*(0.05)/R

# Step
A = [(-2/(R*C))]
B = [1/(R*C)]
C = [1]
D = [0]

sys = signal.StateSpace(A, B, C, D)
t, y = signal.step(sys)

# Plot q, theta (t)
fig = plt.figure(1)
plt.suptitle('ESC251 Homework 2 (Andy Kim)')                               # main title

plt.subplot(1,1,1)                                                                  # simulation 1
plt.title('RC Filter Step Response')
plt.plot(t, y)
plt.xlabel('Time [s]')
plt.ylabel('Vout [V]')
#plt.legend(loc = 'upper left')
#plt.ylim(0, 1.2)

#fig.subplots_adjust(wspace=0.4, hspace = 0.4)
plt.show()                                                                          # show plots
