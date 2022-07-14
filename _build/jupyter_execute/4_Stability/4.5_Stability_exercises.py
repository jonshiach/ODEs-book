#!/usr/bin/env python
# coding: utf-8

# # Stability Exercises
# 
# `````{admonition} Exercise 4.1
# :class: note
# :name: ex4.1
# 
# Determine the stability function of the following Runge-Kutta method
# \begin{align*}
#     \begin{array}{c|ccccc}
#         0 &  &  &  &  & \\
#         \frac{1}{4} & \frac{1}{4} &  &  &  & \\
#         \frac{1}{2} & \frac{1}{2} & 0 &  &  & \\
#         \frac{3}{4} & 0 & \frac{1}{2} & \frac{1}{4} &  &    \\
#         0 & 0 & \frac{1}{6} & -\frac{1}{3} & \frac{1}{6} & \\ \hline
#         & -1 & \frac{2}{3} & -\frac{1}{3} & \frac{2}{3} & 1
#     \end{array}
# \end{align*}
# 
# ````{dropdown} Solution (click to show)
# 
# \begin{align*}
#     \mathbf{b} A^0 \mathbf{e} &= 
#     \begin{pmatrix} -1 \\ \frac{2}{3} \\ -\frac{1}{3} \\ \frac{2}{3} \\ 1 \end{pmatrix}
#     \begin{pmatrix} 
#         1 & 0 & 0 & 0 & 0 \\
#         0 & 1 & 0 & 0 & 0 \\
#         0 & 0 & 1 & 0 & 0 \\
#         0 & 0 & 0 & 1 & 0 \\
#         0 & 0 & 0 & 0 & 1 
#     \end{pmatrix}
#     \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \\ 1 \end{pmatrix}
#     = 1, \\
#     \mathbf{b} A^1 \mathbf{e} &= 
#     \begin{pmatrix} -1 \\ \frac{2}{3} \\ -\frac{1}{3} \\ \frac{2}{3} \\ 1 \end{pmatrix}
#     \begin{pmatrix} 
#         0 & 0 & 0 & 0 & 0 \\
#         \frac{1}{4} & 0 & 0 & 0 & 0 \\
#         \frac{1}{2} & 0 & 0 & 0 & 0 \\
#         0 & \frac{1}{2} & \frac{1}{4} & 0 & 0 \\
#         0 & \frac{1}{6} & -\frac{1}{3} & \frac{1}{6} & 0
#     \end{pmatrix}
#     \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \\ 1 \end{pmatrix}
#     = \frac{1}{2}, \\
#     \mathbf{b} A^2 \mathbf{e} &= 
#     \begin{pmatrix} -1 \\ \frac{2}{3} \\ -\frac{1}{3} \\ \frac{2}{3} \\ 1 \end{pmatrix}
#     \begin{pmatrix} 
#         0 & 0 & 0 & 0 & 0 \\
#         0 & 0 & 0 & 0 & 0 \\
#         0 & 0 & 0 & 0 & 0 \\
#         \frac{1}{4} & 0 & 0 & 0 & 0 \\
#         -\frac{1}{8} & \frac{1}{12} & \frac{1}{24} & 0 & 0
#     \end{pmatrix}
#     \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \\ 1 \end{pmatrix}
#     = \frac{1}{6}, \\
#     \mathbf{b} A^3 \mathbf{e} &= 
#     \begin{pmatrix} -1 \\ \frac{2}{3} \\ -\frac{1}{3} \\ \frac{2}{3} \\ 1 \end{pmatrix}
#     \begin{pmatrix} 
#         0 & 0 & 0 & 0 & 0 \\
#         0 & 0 & 0 & 0 & 0 \\
#         0 & 0 & 0 & 0 & 0 \\
#         0 & 0 & 0 & 0 & 0 \\
#         \frac{1}{24} & 0 & 0 & 0 & 0
#     \end{pmatrix}
#     \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \\ 1 \end{pmatrix}
#     = \frac{1}{24}, \\
#     \mathbf{b} A^4 \mathbf{e} &= 
#     \begin{pmatrix} -1 \\ \frac{2}{3} \\ -\frac{1}{3} \\ \frac{2}{3} \\ 1 \end{pmatrix}
#     \begin{pmatrix} 
#         0 & 0 & 0 & 0 & 0 \\
#         0 & 0 & 0 & 0 & 0 \\
#         0 & 0 & 0 & 0 & 0 \\
#         0 & 0 & 0 & 0 & 0 \\
#         0 & 0 & 0 & 0 & 0
#     \end{pmatrix}
#     \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \\ 1 \end{pmatrix}
#     = 0, \\
# \end{align*}
# 
# So the stability function is $R(z) = 1 + z + \frac{1}{2} z^2 + \frac{1}{6} z^3 + \frac{1}{24} z^4$
# ````
# `````

# In[1]:


from sympy import *
init_printing()

A = Matrix([[0, 0, 0, 0, 0], 
            [Rational(1,4), 0, 0, 0, 0], 
            [Rational(1,2), 0, 0, 0, 0], 
            [0, Rational(1,2), Rational(1,4), 0, 0], 
            [0, Rational(1,6), -Rational(1,3), Rational(1,6), 0]])
b = Matrix([[-1], [Rational(2,3)], [-Rational(1,3)], [Rational(2,3)], [1]])
e = ones(5, 1)

# Calculate coefficents
for k in range(1, len(b) + 1):
    pprint(b.T * A ** (k - 1) * e)


# `````{admonition} Exercise 4.2
# :class: note
# :name: ex4.2
# 
# Determine the stability function of the following Runge-Kutta method. Is this an A-stable method?
# \begin{align*}
#     \begin{array}{c|cc}
#         \frac{1}{4} & \frac{7}{24} & -\frac{1}{24}\\
#         \frac{3}{4} & \frac{13}{24} & \frac{5}{24}\\ \hline
#         & \frac{1}{2} & \frac{1}{2}
#     \end{array}
# \end{align*}
# 
# ````{dropdown} Solution
# \begin{align*}
#     R(z) &= \frac{\det \left( 
#     \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - z
#     \begin{pmatrix} \frac{7}{24} & -\frac{1}{24} \\ \frac{13}{24} & \frac{5}{24} \end{pmatrix} + z
#     \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & \frac{1}{2} \end{pmatrix} \right)}{\det \left(
#     \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - z
#     \begin{pmatrix} \frac{7}{24} & -\frac{1}{24} \\ \frac{13}{24} & \frac{5}{24} \end{pmatrix} \right)} \\
#     &= \frac{\det 
#     \begin{pmatrix} 1 + \frac{5}{24} z & \frac{1}{24} z \\ -\frac{13}{24} z & 1 + \frac{7}{24} z \end{pmatrix}}{\det
#     \begin{pmatrix} 1 - \frac{7}{24} z & \frac{1}{24} z \\ -\frac{13}{34} z & 1 - \frac{5}{24} z \end{pmatrix}}
#     = \frac{1 + \frac{1}{2} z + \frac{1}{12} z^2}{1 - \frac{1}{2} z + \frac{1}{12} z^2}.
# \end{align*}
# 
# Check the roots of $Q(z)$
# \begin{align*}
#     0 &= 1 - \frac{1}{2} z + \frac{1}{12} z^2, \\
#     \therefore z &= \frac{\frac{1}{2} \pm \sqrt{-\frac{1}{3}}}{\frac{1}{6}}
#     = 3 \pm \sqrt{3}i,
# \end{align*}
# so the roots of $Q(z)$ have positive real parts so the first condition for A-stability is satisfied.
# 
# Check that $E(y) \geq 0$
# 
# \begin{align*}
#     E(y) &= \left( 1 - \frac{1}{2} i y - \frac{1}{12} y^2 \right)
#     \left( 1 + \frac{1}{2} i y - \frac{1}{12} y^2 \right) \\
#     & \qquad -
#     \left( 1 - \frac{1}{2} i y - \frac{1}{12} y^2 \right)
#     \left( 1 + \frac{1}{2} i y - \frac{1}{12} y^2 \right) = 0
# \end{align*}
# 
# so $E(y) \geq 0$ and the second condition for A-stability is satisfied. Since both conditions are satisfied then this method is A-stable
# 
# ````
# 
# `````

# In[2]:


from sympy import *
init_printing()

# Define RK method
A = Matrix([[Rational(7,24), -Rational(1,24)],
            [Rational(13,24), Rational(5,24)]])
ebT = Matrix([[Rational(1,2), 0], [0, Rational(1,2)]])
I = eye(2)

z = Symbol('z')

# Calculate R(z)
z, y = symbols('z, y')

def P(z):
    return (I - z * A + z * ebT).det()

def Q(z):
    return (I - z * A).det()

Rz = P(z) / Q(z)
print("R(z) = ")
display(nsimplify(Rz))

# Check roots of Q have positive real parts
print('roots of Q(z) = ')
display(solve(Q(z) - 0))

# Check E(y) >= 0
E = Q(1j * y) * Q(-1j * y) - P(1j * y) * P(-1j * y)
print('E(y) = ')
display(simplify(nsimplify(E)))


# `````{admonition} Exercise 4.3
# :class: note
# :name: ex4.3
# 
# Plot the region of absolute stability for the following Runge-Kutta method.
# 
# \begin{align*}
#     \begin{array}{c|cc}
#         \frac{1}{3} & \frac{1}{3} & 0\\
#         1 & 1 & 0\\ \hline
#         & \frac{3}{4} & \frac{1}{4}
#     \end{array}
# \end{align*}
# 
# ````{dropdown} Solution
# 
# Determine the stability function
# \begin{align*}
#     R(z) &= \frac{\left( 
#     \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - z
#     \begin{pmatrix} \frac{1}{3} & 0 \\ 1 & 0 \end{pmatrix} - z
#     \begin{pmatrix} \frac{3}{4} & 0 \\ 0 & \frac{1}{4} \end{pmatrix} \right)}{ \det \left(
#     \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - z
#     \begin{pmatrix} \frac{1}{3} & 0 \\ 1 & 0 \end{pmatrix} \right)} \\
#     &= \frac{\det
#     \begin{pmatrix} 1 - \frac{13}{12} z & 0 \\ -z & 1 - \frac{1}{4} z \end{pmatrix}}{\det
#     \begin{pmatrix} 1 - \frac{1}{3} z & 0  \\ -z & 1 \end{pmatrix}}
#     = \frac{1 + \frac{2}{3} z + \frac{5}{48} z^2}{1 - \frac{1}{3} z}
# \end{align*}
# 
# Plot 
# 
# ```{glue:} ex4.3_plot
# ```
# 
# Code 
# 
# ```python
# import numpy as np
# import matplotlib.pyplot as plt
# 
# # Generate z values
# X, Y = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))
# Z = X + Y * 1j
# 
# # Define stability function
# R = (1 + 2 / 3 * Z + 5 / 48 * Z ** 2) / (1 - 1 / 3 * Z)
# 
# # Plot stability region
# fig = plt.figure(figsize=(8, 6))
# plt.contourf(X, Y, abs(R), levels=[0, 1], colors="#99ccff")
# plt.contour(X, Y, abs(R), colors= "k", levels=[0, 1])
# plt.axhline(0, color="k", linewidth=2)
# plt.axvline(0, color="k", linewidth=2)
# plt.axis("equal")
# plt.axis([-15, 5, -1.5, 1.5])
# plt.xlabel("$\mathrm{Re}(z)$", fontsize=14)
# plt.ylabel("$\mathrm{Im}(z)$", fontsize=14)
# plt.show()
# ```
# ````
# 
# `````

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
from sympy import *
init_printing()

# Define RK method
A = Matrix([[Rational(1,3), 0],
            [1, 0]])
ebT = Matrix([[Rational(3,4), 0], [0, Rational(1,4)]])
I = eye(2)

# Calculate R(z)
z, y = symbols('z, y')

def P(z):
    return (I - z * A + z * ebT).det()

def Q(z):
    return (I - z * A).det()

Rz = P(z) / Q(z)
print("R(z) = ")
display(nsimplify(Rz))

# Generate z values
X, Y = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))
Z = X + Y * 1j

# Define stability function
R = (1 + 2 / 3 * Z + 5 / 48 * Z ** 2) / (1 - 1 / 3 * Z)

# Plot stability region
fig = plt.figure(figsize=(8, 6))
plt.contourf(X, Y, abs(R), levels=[0, 1], colors="#99ccff")
plt.contour(X, Y, abs(R), colors= "k", levels=[0, 1])
plt.axhline(0, color="k", linewidth=2)
plt.axvline(0, color="k", linewidth=2)
plt.axis("equal")
plt.axis([-15, 5, -1.5, 1.5])
plt.xlabel("$\mathrm{Re}(z)$", fontsize=14)
plt.ylabel("$\mathrm{Im}(z)$", fontsize=14)
plt.show()

from myst_nb import glue
glue("ex4.3_plot", fig, display=False)


# `````{admonition} Exercise 4.4
# :class: note
# :name: ex4.4
# 
# Calculate the stiffness ratio for the following system of ODEs. 
# 
# \begin{align*}
#     y_1' &= -80.6 y_1 + 119.4 y_2,\\
#     y_2' &= 79.6 y_1 - 120.4 y_2.
# \end{align*}
# 
# What are the maximum step lengths that the Euler method is stable for solving each equation?
#     
# ````{dropdown} Solution
# 
# Calculate the eigenvalues of the coefficient matrix
# 
# \begin{align*}
#     0 &= \begin{vmatrix} -80.6 - \lambda & 119.4 \\ 79.6 & -120.4 - \lambda \end{vmatrix}
#     = \lambda^2 + 201 \lambda + 200, \\
#     \therefore \lambda &= \frac{-201 \pm 199}{2} = -200, -1
# \end{align*}
# 
# so the stiffness ratio is $S = 200$. The Euler method is stable for $h\lambda \in [-2, 0]$ so the maximum step length is 
# 
# $$h = \frac{-2}{\min(-200, -1)} = \frac{-2}{-200} = 0.01.$$
# ````
# `````
