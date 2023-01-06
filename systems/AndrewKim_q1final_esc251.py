import numpy as np
import matplotlib.pyplot as plt
from control.matlab import ss, pole # MATLAB-like control toolbox functionality

# Close all figures
plt.close('all')

# Parameters
k1 = -1
k2 = 0.5
m = 1

# Set state space model
A = np.array([
[0, 1],
[2*k1/m, 0]
])
B = np.array([
[0],
[0]
])
C = np.eye(2)
D = 0
sys = ss(A, B, C, D)

# poles
p = pole(sys)
fig, ax = plt.subplots()
ax.plot(np.real(p), np.imag(p),'x')
ax.grid()
print(p)
ax.set_title('1d.) Pole Plot ($x_e$ = $\sqrt{k1/k2}$)')
plt.show()
