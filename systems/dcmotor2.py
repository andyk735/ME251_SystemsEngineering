import numpy as np
import matplotlib.pyplot as plt
from control.matlab import ss, pole, tf, step, bode # MATLAB-like control toolbox functionality

# Close all figures
plt.close('all')

# Parameters
J = 0.01
b = 0.1
Ke = 0.01
Kt = 0.01
R = 1
L = 0.5

# Set state space model
A = np.array([
[-b/J, Kt/J],
[-Ke/L, -R/L]
])
B = np.array([
[0],
[1/L]
])
C = np.array([1, 0])
D = 0
sys = ss(A, B, C, D)

# poles
p = pole(sys)
fig, ax = plt.subplots()
ax.plot(np.real(p), np.imag(p),'x')
ax.grid()
ax.set_title('Pole plot')

# TF
s = tf('s') # transfer function
G = Kt/((J*s + b)*(R + L*s) + Ke*Kt)    # our TF equation
p_ = pole(G)
fig, ax = plt.subplots()
ax.plot(np.real(p_), np.imag(p_),'x')
ax.grid()
ax.set_title('Pole plot')

# State-space to transfer function
G_ = tf(sys) # compute TF from ss(sys)
print('G-G_ = ', G-G_)

# Transfer function to state space
sys_ = ss(G)

# Step Response
t = np.linspace(0, 10, 1000)
y_step, t = step(sys, t)     # can replace sys with G
y1, t = step(G,t)

fig, ax = plt.subplots()
ax.plot(t, y_step, t[::10] ,y1[::10], 's')
ax.set_xlabel('Time [s]')
ax.set_ylabel('Angular Velocity [rad/s]')
ax.set_title('Second Order Step Response')

# Approximate Step Response
dom_pole = p[1]
J=0
G_app = Kt/((J*s + b)*(R + L*s) + Ke*Kt)
y_app, t = step(G_app,t)
y_approx = b*(1-np.e**(dom_pole * t))
fig, ax1 = plt.subplots()
ax1.plot(t, y_app, t, y_step, "--")
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Angular Velocity [rad/s]'),
ax1.set_title('1st Order Step Response Approximation')

# Frequency Response
# sys_app = ss(G_app)
# bode(sys_app)
# bode(sys)
# plt.show()
mag, phase, omega = bode(sys)
fig, axs = plt.subplots(2)
axs[0].plot(omega, mag)
axs[1].plot(omega, phase)
axs[0].set_xlabel('Frequency [rad/s]')
axs[0].set_ylabel('mag = output/input amp')
axs[1].set_ylabel('phase')
plt.show()
