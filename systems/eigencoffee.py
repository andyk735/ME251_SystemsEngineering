# The final plot is the same as coffeeheat.py, but instead we use eigenvalues.

import numpy as np
import matplotlib.pyplot as plt
from control.matlab import sys, ss, pole # MATLAB-like control toolbox functionality

# Close all figures
plt.close('all')

# Parameters
Cc = 1722 # J/K
Cm = 292 # J/K
Rc = 0.014 # K/W
Rm = 1.2 # K/W

# ICs
Ta = 20 # C
Tc0 = 90 # C
Tm0 = Ta

#
Te = (Cc*Tc0 + Cm*Tm0)/(Cc + Cm)
print('Te = ', Te)

# Set up model
# Input: heat energy J/s, Output: Delta Temperature (above ambient)
A = np.array([[-1/(Rc*Cc), 1/(Rc*Cc)],
               [1/(Rc*Cm), (-1/Cm)*(1/Rc + 1/Rm)]])
B = np.array([[1/Cc],
              [0]])
C = np.eye(2)
D = np.zeros((2, 1))
sys = ss(A, B, C, D)

# Compute Poles / Eigenvalues
p = pole(sys)
print('p = ', p)
evals, evecs = np.linalg.eig(A)
print('evals = ', evals)

# Check evals/evecs
c1 = evecs[:,0]
c2 = evecs[:,1]
s1, s2 = p  # short for s1 = p[0], s2 = p[1]
zc = A @ c1 - s1 * c1
print('eval/evec check, zc =', zc)


# Solve for coefficients d1, d2
x0 = np.array([
            [Tc0 - Ta], # Delta Tc = Tc0 - Ta
            [Tm0 - Ta] ]) # Delta Tm = Tm0 - Ta

b = x0
x = np.linalg.solve(evecs, b)
d1 = x[0]
d2 = x[1]


# x(t) = d1*e^{s1*t}*c1 + d2*e^{s2*t}*c2
t = np.linspace(0, 1000, 500)
xsol = np.zeros((len(t), 2))
for i in range(len(t)):
    xsol[i, :] = d1*np.exp(s1*t[i])*c1 + d2*np.exp(s2*t[i])*c2   # solution at t = i, filling each row of size [i,2]

# Solutions
Tc_sol = xsol[:, 0] + Ta
Tm_sol = xsol[:, 1] + Ta

# Solution Plots
fig, ax = plt.subplots()
ax.plot(t, Tc_sol)
ax.plot(t, Tm_sol)
ax.plot(t, Te*np.ones(len(t)), 'k--')
ax.set_xlabel('Time [s]')
ax.set_ylabel('Temperature [C]')
ax.legend(('Tc','Tm'))
ax.set_title('Solution using evals/evecs')

# Pole Plot
fig, ax = plt.subplots()
ax.plot(p, np.zeros(2), 'x')
ax.set_xlabel('Re{p}')
ax.set_ylabel('Im{p}')

plt.show()
