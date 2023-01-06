'''
ESC251 - Homework 4
"Frequency response of mass-spring system"
Andy Kim
'''

import numpy as np
import matplotlib.pyplot as plt
from control.matlab import ss, lsim

# Close all plots
plt.close('all')

# Parameters
m1 = 2500                       # 1/4 bus body mass, kg
k1 = 80e3                       # spring constant of suspension system, N/m
b1 = 350                        # damping constant of suspension system, N.s/m
omegaN = np.sqrt(k1/m1)         # natural frequency, rad
zeta = b1/(2*np.sqrt(m1*k1))    # damping ratio

# Frequency Solutions
omega = np.linspace(0, 20, 4000)

denom = (((omegaN**2)-(omega**2))**2)+((2*zeta*omegaN*omega)**2)
f = ((omegaN**2) * ((omegaN**2)-(omega**2))) / denom
g = ((-1) * (omegaN**2) * (2*zeta*omegaN*omega)) / denom

M = np.sqrt((f**2)+(g**2))                       # magnitude of output signal
phi = np.arctan2(g, f)                           # phase shift of output signal

# Plots
fig = plt.figure(1)
plt.suptitle('ESC251 Homework 4 - Andrew Kim')

plt.subplot(2,1,1)
plt.title('Magnitude of Output Signal')
plt.plot(omega, M, label='Magnitude: $M = B/A$')
plt.xlabel('$\omega$ [rad/s]')
plt.ylabel('Magnitude: $M = B/A$')
plt.legend(loc = 'upper right')
M_max = M.max()
#print(M_max)

plt.subplot(2,1,2)
plt.title('Phase of Output Signal')
plt.plot(omega, phi*180/np.pi, label='Phase')
plt.xlabel('$\omega$ [rad/s]')
plt.ylabel('Phase [rad]')
plt.legend(loc = 'upper right')

fig.subplots_adjust(wspace=0.4, hspace = 0.4)

plt.show()

# Simulate response due to sinusoidal input at omega_max #1
omega_max = 5.656

A = np.array([ [0, 1], [-k1/m1, -b1/m1] ])
B = np.array([ [1/m1], [0] ])
C = np.array([1,0]) # get y
D = 0
sys = ss(A, B, C, D)

t = np.linspace(0, 40, 2000)
u = 2*np.cos(omega_max*t)
x0 = np.zeros((2,1))
y, t, x = lsim(sys, u, t, x0)

# Sinusoidal Input Solution #1
denom2 = (((omegaN**2)-(omega_max**2))**2)+((2*zeta*omegaN*omega_max)**2)
f2 = ((omegaN**2) * ((omegaN**2)-(omega_max**2))) / denom2
g2 = ((-1) * (omegaN**2) * (2*zeta*omegaN*omega_max)) / denom2
M2 = np.sqrt((f2**2)+(g2**2))
phi2 = np.arctan2(g2, f2)
#print(M2)                                           # magnitude of output signal due to sinusoidal input at omega_max
#print(phi2*180/np.pi)                               # phase shift of output signal due to sinusoidal input at omega_max

# Plot
fig, ax = plt.subplots()
ax.plot(t, u, label='u')
ax.plot(t, y, label='y')
ax.grid()
ax.legend()
#ax.set_ylim(-30, 30)
ax.set_ylabel('u, y')
ax.set_xlabel('Time (s)')
plt.title('Sinusoidal Input - 2cos($\omega$t)')
plt.show()

# Sinusoidal Input Solution #2
omega6 = 20
denom3 = (((omegaN**2)-(omega6**2))**2)+((2*zeta*omegaN*omega6)**2)
f3 = ((omegaN**2) * ((omegaN**2)-(omega6**2))) / denom3
g3 = ((-1) * (omegaN**2) * (2*zeta*omegaN*omega6)) / denom3
M3 = np.sqrt((f3**2)+(g3**2))
phi3 = np.arctan2(g3, f3)
print(M3)
print(phi3*180/np.pi)

t = np.linspace(0, 10, 1000)
u = 5*np.cos(20*t)
x0 = np.zeros((2,1))
y, t, x = lsim(sys, u, t, x0)

# Plot
fig, ax = plt.subplots()
ax.plot(t, u, label='u')
ax.plot(t, y, label='y')
ax.grid()
ax.legend()
#ax.set_ylim(-30, 30)
ax.set_ylabel('u, y')
ax.set_xlabel('Time (s)')
plt.title('Sinusoidal Input - 5cos(20t)')
plt.show()
