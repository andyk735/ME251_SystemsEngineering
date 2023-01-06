'''
ESC251 - Homework 3
"Analysis of a (quarter) bus suspension"
Andy Kim
'''

import numpy as np
import matplotlib.pyplot as plt
from control.matlab import ss, lsim

# Close all plots
plt.close('all')

# Parameters
m1 = 2500           # 1/4 bus body mass, kg
m2 = 320            # suspension mass, kg
k1 = 80e3           # spring constant of suspension system, N/m
k2 = 500e3          # spring constant of wheel and tire, N/m
b1 = 350            # damping constant of suspension system, N.s/m
b2 = 15e3           # damping constant of wheel and tire, N.s/m

a = 0.1             # amplitude, m
v = 7.5             # car velocity, m/s
lam = 6             # wavelength, m
omega = (2*np.pi*v)/lam

# State Space
A = np.array([
    [       0,        1,           0,           0],
    [-(k1/m1), -(b1/m1),     (k1/m1),     (b1/m1)],
    [       0,        0,           0,           1],
    [ (k1/m2),  (b1/m2), -(k1+k2)/m2, -(b1+b2)/m2],])
B = np.array([
    [0],
    [(b1*b2)/(m1*m2)],
    [b2/m2],
    [k2/m2 - (b2/m2)*(b1+b2)/m2],])
C = np.eye(4)
D = np.array([
    [0],
    [0],
    [0],
    [b2/m2],])

# Solutions
t = np.linspace(0, 10, 1000)
sys = ss(A, B, C, D)

u1 = 0.1                                # 10 cm step input
x0_1 = np.array([0, 0, 0, -(b2/m2)*u1])
yresp1, t, xresp1 = lsim(sys, u1, t, x0_1)

u2 = np.array(a*np.sin(omega*t))
x0_2 = np.array([0, 0, 0, 0])
yresp2, t, xresp2 = lsim(sys, u2, t, x0_2)

u3 = np.array(a*np.sin(omega*t/(7.5)))
yresp3, t, xresp3 = lsim(sys, u3, t, x0_2)

u4 = np.array(a*np.sin(2*omega*t))
yresp4, t, xresp4 = lsim(sys, u4, t, x0_2)

# Plots
fig = plt.figure(1)
plt.suptitle('ESC251 Homework 3')

plt.subplot(2,2,1)
plt.title('10 cm Step Response')
plt.plot(t, yresp1[:, 0], label='x1')
plt.plot(t, yresp1[:, 1], label='v1')
plt.plot(t, yresp1[:, 2], label='x2')
plt.plot(t, yresp1[:, 3], label='v2')
plt.xlabel('Time [s]')
plt.ylabel('y response')
plt.legend(loc = 'upper right')

plt.subplot(2,2,2)
plt.title('Frequency Response, v = 7.5')
plt.plot(t, yresp2[:, 0], label='x1')
plt.plot(t, yresp2[:, 1], label='v1')
plt.plot(t, yresp2[:, 2], label='x2')
plt.plot(t, yresp2[:, 3] + (b2/m2)*u2, label='v2')
plt.xlabel('Time [s]')
plt.ylabel('y response')
plt.legend(loc = 'upper right')

plt.show()
