import numpy as np
import matplotlib.pyplot as plt
from control.matlab import initial, sys, ss # MATLAB-like control toolbox functionality

# Close all figures
plt.close('all')

# Parameters
Cc = 1722 # J/K
Cm = 292 # J/K
Rc = 0.014 # K/W
Rm = 1.2 # K/W# ICs
Ta = 20 # C
Tc0 = 90 # C
Tm0 = Ta # C

Te = (Cc*Tc0 + Cm*Tm0)/(Cc + Cm)
print('Te = ', Te)# Set up model


# Input: heat energy J/s, Output: Delta Temperature (above ambient)
A = np.array([
[-1/(Rc*Cc), 1/(Rc*Cc)],
[ 1/(Rc*Cm), (-1/Cm)*(1/Rc + 1/Rm)]
])
B = np.array([
[1/Cc],
[0]
])
C = np.eye(2)
D = np.zeros((2, 1))

sys = ss(A, B, C, D)


# IC response
x0 = np.array([
[Tc0 - Ta], # Delta Tc = Tc0 - Ta
[0] # Delta Tm = Tm - Ta0 = 0
])
t = np.linspace(0, 1000, 500)
y, t = initial(sys, t, x0)

Tc = y[:,0] + Ta
Tm = y[:,1] + Ta
fig, ax = plt.subplots()
ax.plot(t, Tc)
ax.plot(t, Tm)
ax.plot(t, Te*np.ones(len(t)), 'k--')
ax.set_xlabel('Time [s]')
ax.set_ylabel('Temperature [C]')
ax.legend(('Tc','Tm'))

plt.show()
