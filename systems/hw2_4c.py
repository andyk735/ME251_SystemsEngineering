'''
ESC251 - Homework 2
"Two Containers Connected by a Pipe"
Andy Kim
'''
#from scipy import signal
#from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Close all plots
plt.close('all')

t = np.linspace(0, 30, 100)
y = 4*np.exp((-1/2)*t)*np.sin((1/2)*t)

# Plot q, theta (t)
fig = plt.figure(1)
plt.suptitle('ESC251 Homework 2 (Andy Kim)')                               # main title

plt.subplot(1,1,1)                                                                  # simulation 1
plt.title('Exercise 4c')
plt.plot(t, y)
plt.xlabel('Time [s]')
plt.ylabel('y')
#plt.legend(loc = 'upper left')
#plt.ylim(0, 1.2)

#fig.subplots_adjust(wspace=0.4, hspace = 0.4)
plt.show()                                                                          # show plots
