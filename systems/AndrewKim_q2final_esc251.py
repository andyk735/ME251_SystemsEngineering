import numpy as np
import matplotlib.pyplot as plt
from control.matlab import sys, ss, step, lsim, pole # MATLAB-like control toolbox functionality

# Close all figures
plt.close('all')

# Parameters
Ra = 0.02           # (C/W)
Rb = 2
Rc = 2.2
Rd = 0.2
Re = 0.02

C1 = 8700           # (J/C)
C2 = 6200
C3 = 6600
C4 = 20000

# State Space
A = np.array([
[   (-1/(C1*Ra)) - (1/(C1*Rb)), 1/(C1*Rb),  0,  0],
[   1/(C2*Rb), (-1/(C2*Rb)) - (1/(C2*Rc)),  1/(C2*Rc),  0],
[   0,  1/(C3*Rc),  (-1/(C3*Rc)) - (1/(C3*Rd)),  1/(C3*Rd)],
[   0,  0,  1/(C4*Rd),  (-1/(C4*Rd)) - (1/(C4*Re))]
])

B = np.array([
[0],
[0],
[0],
[1/(C4*Re)]
])
C = np.eye(4)
D = 0

sys = ss(A, B, C, D)

x0 = np.array([
              [0],
              [0],
              [0],
              [0],
              ])

# Step Response
t = np.linspace(0, 3600, 2000)
y_step, t = step(sys, t, x0)

fig, ax = plt.subplots()
ax.plot(t, y_step[:, 0], label='$T_1$ - $T_i$')
ax.plot(t, y_step[:, 1], label='$T_2$ - $T_i$')
ax.plot(t, y_step[:, 2], label='$T_3$ - $T_i$')
ax.plot(t, y_step[:, 3], label='$T_4$ - $T_i$')
ax.set_xlabel('Time [s]')
ax.set_ylabel('Temperatures [\u2103]')
plt.title('2d.) Temperature Step Response')
ax.legend()

# IC response (varying outside temperature)
Tw = 15
Ti = 20
To = 5 - (15*t)
x1 = np.array([
[Tw - Ti],
[Tw - Ti],
[Tw - Ti],
[Tw - Ti]
])

y_ic, t, x = lsim(sys, To, t, x1)

fig, ax = plt.subplots()
ax.plot(t, y_ic[:, 0], label='$T_1$')
ax.plot(t, y_ic[:, 1], label='$T_2$')
ax.plot(t, y_ic[:, 2], label='$T_3$')
ax.plot(t, y_ic[:, 3], label='$T_4$')
ax.plot(t, To, label='$T_0$')
plt.axhline(y = Ti, label='$T_i$')
ax.set_xlabel('Time [s]')
ax.set_ylabel('Temperature [\u2103]')
plt.title('2e.) Initial Temperature Response')
ax.legend()

# Poles
p = pole(sys)
fig, ax = plt.subplots()
ax.plot(np.real(p), np.imag(p),'x')
ax.grid()
print(p)
ax.set_title('2f.) Pole Plot')
plt.show()
