import numpy as np
import matplotlib.pyplot as plt
from control.matlab import ss, pole, lsim # MATLAB-like control toolbox functionality

# Close all figures
plt.close('all')

# Parameters
m = 0.002
c = 0
k = 4e5
R = 12
L = 1e-3
Kf = 16
Kb = 13

# Set state space model
A = np.array([
[0, 1, 0],
[-k/m, -c/m, Kf/m],
[0, Kb/L, -R/L]
])
B = np.array([
[0],
[0],
[1/L]
])
C = np.array([1, 0, 0])
D = 0
sys = ss(A, B, C, D)

# poles
p = pole(sys)
fig, ax = plt.subplots()
plt.suptitle("Andrew Kim Exam Question 1")
ax.plot(np.real(p), np.imag(p),'x')
ax.grid()
ax.set_title('1a.) Pole plot')
plt.show()

# Sinusoidal Responses

# 10 Hz
t = np.linspace(0, 50, 100)
f = 10
T = 1/f
lamb = 3e8/f
omega = (2*np.pi)/T

u0 = 0
u = np.sin(omega*t)

q0 = np.array([
              [0],
              [0],
              [0],
              ])

y, t, q = lsim(sys, u, t, q0)
y = y*lamb

fig, ax = plt.subplots()
ax.plot(t, y, label='y')
ax.plot(t, u, label='u')
ax.set_xlabel('Time [s]')
ax.set_ylabel('u, y')
plt.title('10 Hz')
ax.legend()

# 5000 Hz
t = np.linspace(0, 30, 300)
f = 5000
T = 1/f
lamb = 3e8/f
omega = (2*np.pi)/T

u0 = 0
u = np.sin(omega*t)

q0 = np.array([
              [0],
              [0],
              [0],
              ])

y, t, q = lsim(sys, u, t, q0)
y = y*lamb

fig, ax = plt.subplots()
ax.plot(t, y, label='y')
ax.plot(t, u, label='u')
ax.set_xlabel('Time [s]')
ax.set_ylabel('u, y')
plt.title('5000 Hz')
ax.legend()

# 20000 Hz
t = np.linspace(0, 30, 300)
f = 20000
T = 1/f
lamb = 3e8/f
omega = (2*np.pi)/T

u0 = 0
u = np.sin(omega*t)

q0 = np.array([
              [0],
              [0],
              [0],
              ])

y, t, q = lsim(sys, u, t, q0)
y = y*lamb

fig, ax = plt.subplots()
ax.plot(t, y, label='y')
ax.plot(t, u, label='u')
ax.set_xlabel('Time [s]')
ax.set_ylabel('u, y')
plt.title('30000 kHz)')
ax.legend()
plt.show()