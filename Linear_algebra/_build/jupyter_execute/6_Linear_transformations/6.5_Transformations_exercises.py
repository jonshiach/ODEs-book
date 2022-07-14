#!/usr/bin/env python
# coding: utf-8

# (transformations-exercises-section)=
# # Transformations exercises
# 
# :::::{admonition} Exercise 6.1
# :class: note
# :name: ex6.1
# 
# Which of the following transformations are linear transformations?
# 
# (a) &emsp; $T: (x, y) \mapsto (0, y)$;
# 
# :::{dropdown} Solution
# Let $(x_1, y_1), (x_2, y_2) \in \mathbb{R}^2$ and $\alpha \in \mathbb{R}$
# 
# \begin{align*}
#     T\left( \begin{pmatrix} x_1 \\ y_1\end{pmatrix} + \alpha \begin{pmatrix} x_2 \\ y_2 \end{pmatrix} \right)
#     &= T\begin{pmatrix} x_1 + \alpha x_2 \\ y_1 + \alpha y_2 \end{pmatrix} \\
#     &= \begin{pmatrix} 0 \\ y_1 + \alpha y_2 \end{pmatrix} \\
#     &= \begin{pmatrix} 0 \\ y_1 \end{pmatrix} + \alpha \begin{pmatrix} 0 \\ y_2 \end{pmatrix}\\
#     &= T\begin{pmatrix} x_1 \\ y_1 \end{pmatrix} + \alpha T\begin{pmatrix} x_2 \\ y_2 \end{pmatrix},
# \end{align*}
# 
# therefore $T$ is a linear transformation.
# :::
#         
# (b) &emsp; $T: (x, y) \mapsto (x, 5)$;
# 
# :::{dropdown} Solution
# $T$ is not a linear transformation since 
# 
# \begin{align*}
#     T\left( \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \begin{pmatrix} 1 \\ 1 \end{pmatrix} \right) = \begin{pmatrix} 2 \\ 5 \end{pmatrix}, \\
#     T\begin{pmatrix} 1 \\ 0 \end{pmatrix} + T\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 \\ 10 \end{pmatrix}.
# \end{align*}
# :::
# 
# (c) &emsp; $T: (x, y) \mapsto (x, x - y)$;
# 
# :::{dropdown} Solution
# Let $(x_1, y_1), (x_2, y_2) \in \mathbb{R}^2$ and $\alpha \in \mathbb{R}$
# 
# \begin{align*}
#     T\left(\begin{pmatrix} x_1 \\ y_1 \end{pmatrix} + \alpha \begin{pmatrix} x_2 \\ y_2 \end{pmatrix} \right) 
#     &= T\begin{pmatrix} x_1 + \alpha x_2 \\ y_1 + \alpha y_2 \end{pmatrix} \\
#     &= \begin{pmatrix} x_1 + \alpha x_2 \\ x_1 - y_1 + \alpha x_2 - \alpha y_2 \end{pmatrix} \\
#     &= \begin{pmatrix} x_1 \\ x_1 - y_1 \end{pmatrix} + \alpha \begin{pmatrix} x_2 \\ x_2 - y_2 \end{pmatrix} \\
#     &= T\begin{pmatrix} x_1 \\ y_1 \end{pmatrix} + \alpha T\begin{pmatrix} x_2 \\ y_2 \end{pmatrix},
# \end{align*}
# 
# therefore $T$ is a linear transformation.
# :::
# 
# (d) &emsp; $T: (x, y, z) \mapsto (x + y, z)$;
# 
# :::{dropdown} Solution
# Let $(x_1, y_1, z_2) \in \mathbb{R}^3$, $(x_2, y_2) \in \mathbb{R}^2$ and $\alpha \in \mathbb{R}$
# 
# \begin{align*}
#     T\left( \begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} + \alpha \begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix} \right) &= T\begin{pmatrix} x_1 + \alpha x_2 \\ y_1 + \alpha y_2 \\ z_1 + \alpha z_2 \end{pmatrix} \\
#     &= \begin{pmatrix} x_1 + y_1 + \alpha x_2 + \alpha y_2 \\  z_1 + \alpha z_2 \end{pmatrix} \\
#     &= \begin{pmatrix} x_1 + y_1 \\ z_1 \end{pmatrix} + \alpha \begin{pmatrix} x_2 + y_2 \\ z_2 \end{pmatrix} \\
#     &= T\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} + \alpha T\begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix},
# \end{align*}
# 
# therefore $T$ is a linear transformation.
# :::
# 
# (e) &emsp; $T: (x, y) \mapsto (3x + 1, y)$;
# 
# :::{dropdown} Solution
# $T$ is not a linear transformation since
# 
# \begin{align*}
#     T\left( \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \begin{pmatrix} 1 \\ 1 \end{pmatrix} \right)
#     &= T \begin{pmatrix} 2 \\ 1 \end{pmatrix} 
#     = \begin{pmatrix} 7 \\ 1 \end{pmatrix}, \\
#     T\begin{pmatrix} 1 \\ 0 \end{pmatrix} + T \begin{pmatrix} 1 \\ 1 \end{pmatrix} 
#     &= \begin{pmatrix} 4 \\ 0 \end{pmatrix} + \begin{pmatrix} 4 \\ 1 \end{pmatrix} 
#     = \begin{pmatrix} 8 \\ 1 \end{pmatrix},
# \end{align*}
# :::
# 
# (f) &emsp; $T: f(x) \mapsto \dfrac{\mathrm{d}}{\mathrm{d}x} f(x)$;
# 
# :::{dropdown} Solution
# Let $f(x),g(x) \in P(\mathbb{R})$ and $\alpha \in \mathbb{R}$:
# 
# \begin{align*}
#     T(f(x) + \alpha g(x)) &= f'(x) + \alpha g'(x) \\
#     &= f'(x) + g'(x) \\ 
#     &=  T(f(x)) + \alpha T(g(x))
# \end{align*}
# 
# therefore $T$ is a linear transformation.
# :::
# 
# (g) &emsp; $T: f(x) \mapsto xf(x)$.
# :::{dropdown} Solution
# Let $f(x),g(x) \in P(\mathbb{R})$ and $\alpha \in \mathbb{R}$:
# 
# \begin{align*}
#     T(f(x) + \alpha g(x)) &= x f(x) + \alpha x g(x) \\
#     &= T(f(x)) + \alpha T(g(x))
# \end{align*}
# 
# therefore $T$ is a linear transformation.
# :::
# 
# (h) &emsp; $T: \mathbb{C}^2 \to \mathbb{C}$ where $T: (x, y) \mapsto x + y$;
# 
# :::{dropdown} Solution
# Let $(x_1 + i y_1, x_2 + i y_2), (x_3 + i y_3, x_4 + i y_4) \in \mathbb{C}$ and $\alpha \in \mathbb{R}$
# 
# \begin{align*}
#     &T \left( \begin{pmatrix} x_1 + i y_1 \\ x_2 + i y_2 \end{pmatrix} + \alpha \begin{pmatrix} x_3 + i y_3 \\ x_4 + i y_4 \end{pmatrix} \right)  \\ 
#     &\qquad = T \begin{pmatrix} x_1 + i y_1 + \alpha(x_3 + i y_3) \\ x_2 + i y_2 + \alpha(x_4 + i y_4) \end{pmatrix} \\
#     &\qquad = x_1 + i y_1 + x_2 + i y_2 + \alpha(x_3 + i y_3 + x_4 + i y_4) \\
#     &\qquad = T \begin{pmatrix} x_1 + i y_1 \\ x_2 + i y_2 \end{pmatrix} + \alpha T\begin{pmatrix} x_3 + i y_3 \\ x_4 + i y_4 \end{pmatrix},
# \end{align*}
# 
# therefore $T$ is a linear transformation.
# :::
# 
# (i) &emsp; $T: \mathbb{C}^2 \to \mathbb{C}$ where $T: (x, y) \mapsto x y$;
# 
# :::{dropdown} Solution
# Let $(1, i) \in \mathbb{C}^2$ then 
# 
# \begin{align*}
#     T \left( 2 \begin{pmatrix} 1 \\ i \end{pmatrix} \right) &= T \begin{pmatrix} 2 \\ 2 i \end{pmatrix} = 4 i, \\
#     2 T\begin{pmatrix} 1 \\ i \end{pmatrix} = 2 i,
# \end{align*}
# 
# therefore $B$ is not a linear transformation.
# :::
# 
# (j) &emsp; $T: \mathbb{C}^2 \to \mathbb{C}$ where $T: (x, y) \mapsto \bar{y}$.
# 
# $\bar{x}$ is the complex conjugate of $x = a + bi$ defined by $\bar{x} = a - bi$.
# 
# :::{dropdown} Solution
# Let $(x_1 + iy_1, x_2 + iy_2), (x_3 + iy_3, x_4 + iy_4) \in \mathbb{C}$ and $\alpha \in \mathbb{R}$
# 
# \begin{align*}
#     T \left( \begin{pmatrix} x_1 + i y_1 \\ x_2 + i y_2 \end{pmatrix} + 
#     \alpha \begin{pmatrix} x_3 + i y_3 \\ x_4 + i y_4 \end{pmatrix} \right)
#     &= T \begin{pmatrix} x_1 + i y_1 + \alpha(x_3 + i y_3) \\ x_2 + i y_2 + \alpha(x_4 + i y_4) \end{pmatrix} \\
#     &= x_2 - i y_2 + \alpha(x_4 - i y_4) \\
#     &= T \begin{pmatrix} x_1 + i y_1 \\ x_2 + i y_2 \end{pmatrix} + \alpha T \begin{pmatrix} x_3 + i y_3 \\ x_4 + i y_4 \end{pmatrix},
# \end{align*}
# 
# therefore $C$ is a linear transformation.
# :::
# 
# :::::
# 
# :::::{admonition} Exercise 6.2
# :class: note
# :name: ex6.2
# 
# A linear transformation $T: \mathbb{R}^2 \to \mathbb{R}^2$ is defined by $T: (x, y) \mapsto (-x + 3y, x - 4y)$. Determine the transformation matrix for $T$ and hence calculate $T \begin{pmatrix} 2 \\ 5 \end{pmatrix}$.
# 
# ::::{dropdown} Solution
# 
# \begin{align*}
#     A = \begin{pmatrix} -1 & 3 \\ 1 & -4 \end{pmatrix}
# \end{align*}
# 
# Calculating $T \begin{pmatrix} 2 \\ 5 \end{pmatrix}$
# 
# \begin{align*}
#     T\begin{pmatrix} 2 \\ 5 \end{pmatrix} = \begin{pmatrix} -1 & 3 \\ 1 & -4 \end{pmatrix} 
#     \begin{pmatrix} 2 \\ 5 \end{pmatrix}
#     = \begin{pmatrix} 13 \\ -18 \end{pmatrix},
# \end{align*}
# 
# therefore $T\begin{pmatrix} 2 \\ 5 \end{pmatrix} = (13, -18)$.
# ::::
# 
# :::::
# 
# :::::{admonition} Exercise 6.3
# :class: note
# :name: ex6.3
# 
# A linear transformation $T: \mathbb{R}^2 \to \mathbb{R}^2$ is defined by $T: (x, y) \mapsto (x - 2y, 2x + 3y)$. Given $T(\mathbf{u}) = \begin{pmatrix} -1 \\ 5 \end{pmatrix}$ determine $\mathbf{u}$.
# 
# ::::{dropdown} Solution
# 
# The transformation matrix is 
# 
# \begin{align*}
#     A &= \begin{pmatrix} 1 & -2 \\ 2 & 3 \end{pmatrix},
# \end{align*}
# 
# so the inverse is
# 
# \begin{align*}
#     A^{-1} &= \begin{pmatrix} \frac{3}{7} & \frac{2}{7} \\ -\frac{2}{7} & \frac{1}{7} \end{pmatrix}.
# \end{align*}
# 
# Therefore
# 
# \begin{align*}
#     \mathbf{u} &= A^{-1} \begin{pmatrix} -1 \\ 5 \end{pmatrix} 
#     = \begin{pmatrix} \frac{3}{7} & \frac{2}{7} \\ -\frac{2}{7} & \frac{1}{7} \end{pmatrix}
#     \begin{pmatrix} -1 \\ 5 \end{pmatrix}
#     = \begin{pmatrix} 1 \\ 1 \end{pmatrix}.
# \end{align*}
# ::::
# :::::
# 
# :::::{admonition} Exercise 6.4
# :class: note
# :name: ex6.4
# 
# $T: \mathbb{R}^3 \to \mathbb{R}^3$ is a linear transformation such that
# 
# \begin{align*}
#     T\begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} &= \begin{pmatrix} 4 \\ 3 \\ 11 \end{pmatrix}, &
#     T\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} &= \begin{pmatrix} 1 \\ 0 \\ 4 \end{pmatrix}, &
#     T\begin{pmatrix} -2 \\ -1 \\ 1 \end{pmatrix} &= \begin{pmatrix} 1 \\ 3 \\-1 \end{pmatrix}.
# \end{align*}
# 
# Find the transformation matrix for $T$.
# 
# ::::{dropdown} Solution
# 
# The transformation matrix is determined using equation {eq}`determining-the-transformation-matrix` which is
# 
# $$A = (T(\mathbf{u}_1), T(\mathbf{u}_2), \ldots, T(\mathbf{u}_n)) \cdot (\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_n)^{-1}.$$
# 
# Using Gauss-Jordan elimination to calculate the inverse of $(\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3)^{-1}$ 
# 
# \begin{align*}
#     & \left( \begin{array}{rrr|rrr}
#         1 & 0 & 3 & 1 & 0 & 0 \\
#         -1 & 1 & 2 & 0 & 1 & 0 \\
#         0 & 4 & 3 & 0 & 0 & 1 
#     \end{array} \right)
#     \begin{array}{l} \\ R_2 + R_1 \\ \phantom{x} \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{rrr|rrr}
#         1 & 0 & 3 & 1 & 0 & 0 \\
#         0 & 1 & 5 & 1 & 1 & 0 \\
#         0 & 4 & 3 & 0 & 0 & 1 
#     \end{array} \right)
#     \begin{array}{l} \\ \\ R_3 - 4R_2 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{rrr|rrr}
#         1 & 0 & 3 & 1 & 0 & 0 \\
#         0 & 1 & 5 & 1 & 1 & 0 \\
#         0 & 0 & -17 & -4 & -4 & 1 
#     \end{array} \right)
#     \begin{array}{l} \\ \\ -\frac{1}{17}R_3 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{rrr|rrr}
#         1 & 0 & 3 & 1 & 0 & 0 \\
#         0 & 1 & 5 & 1 & 1 & 0 \\
#         0 & 0 & 1 & \frac{4}{17} & \frac{4}{17} & -\frac{1}{17} 
#     \end{array} \right)
#     \begin{array}{l} R_1 - 3 R_3 \\ R_2 - 5 R_3 \\ \phantom{x} \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{rrr|rrr}
#         1 & 0 & 0 & \frac{5}{17} & -\frac{12}{17} & \frac{3}{17} \\
#         0 & 1 & 0 & -\frac{3}{17} & -\frac{3}{17} & \frac{5}{17} \\
#         0 & 0 & 1 & \frac{4}{17} & \frac{4}{17} & -\frac{1}{17} 
#     \end{array} \right)
# \end{align*}
# 
# So $(\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3)^{-1} = \begin{pmatrix} \frac{5}{17} & -\frac{12}{17} & \frac{3}{17} \\ -\frac{3}{17} & -\frac{3}{17} & \frac{5}{17} \\ \frac{4}{17} & \frac{4}{17} & -\frac{1}{17} \end{pmatrix}$ and
# 
# \begin{align*}
#     A &= \begin{pmatrix} 4 & 1 & 1 \\ 3 & 0 & 3 \\ 11 & 4 & -1 \end{pmatrix}
#     \begin{pmatrix} 
#         \frac{5}{17} & -\frac{12}{17} & \frac{3}{17} \\
#         -\frac{3}{17} & -\frac{3}{17} & \frac{5}{17} \\
#         \frac{4}{17} & \frac{4}{17} & -\frac{1}{17} 
#     \end{pmatrix}
#     = \begin{pmatrix} 1 & 0 & 3 \\ -1 & 1 & 2 \\ 0 & 4 & 3 \end{pmatrix}.
# \end{align*}
# 
# Checking $A$
# 
# \begin{align*}
#     T\begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} &=
#     \begin{pmatrix} 1 & 0 & 3 \\ -1 & 1 & 2 \\ 0 & 4 & 3 \end{pmatrix}
#     \begin{pmatrix}1 \\ 2 \\ 1 \end{pmatrix} 
#     = \begin{pmatrix} 4 \\ 3 \\ 11 \end{pmatrix} \quad \checkmark
# \end{align*}
# 
# ::::
# 
# :::::
# 
# :::::{admonition} Exercise 6.5
# :class: note
# :name: ex6.5
# 
# A rotate the point with co-ordinates $(2, 1)$ by $\frac{\pi}{6}$ anti-clockwise about the origin. 
# 
# 
# ::::{dropdown} Solution
# 
# The transformation matrix is
# 
# \begin{align*}
#     Rot\left(\frac{\pi}{6}\right) &= \begin{pmatrix} 
#         \cos(\frac{\pi}{6}) & -\sin(\frac{\pi}{6}) \\
#         \sin(\frac{\pi}{6}) & \cos(\frac{\pi}{6})
#     \end{pmatrix}  \\
#     &= \begin{pmatrix}
#         \frac{\sqrt{3}}{2} & -\frac{1}{2} \\
#         \frac{1}{2} & \frac{\sqrt{3}}{2}
#     \end{pmatrix}
# \end{align*}
# 
# therefore
# 
# \begin{align*}
#     R(\left(\frac{\pi}{6}\right) \begin{pmatrix} 2 \\ 1 \end{pmatrix}
#     &= \begin{pmatrix}
#         \frac{\sqrt{3}}{2} & -\frac{1}{2} \\
#         \frac{1}{2} & \frac{\sqrt{3}}{2}
#     \end{pmatrix}
#     \begin{pmatrix} 2 \\ 1 \end{pmatrix} \\
#     &= \begin{pmatrix} \sqrt{3} - \frac{1}{2} \\ 1 + \frac{\sqrt{3}}{2} \end{pmatrix}
#     \approx \begin{pmatrix} 1.2321 \\ 1.8660 \end{pmatrix}
# \end{align*}
# ::::
# 
# :::::

# In[1]:


from sympy import *

P = Matrix([2, 1])
R = Matrix([[cos(pi / 6), -sin(pi / 6)], [sin(pi / 6), cos(pi / 6)]])

pprint((R * P).evalf(6))


# :::::{admonition} Exercise 6.6
# :class: note
# :name: ex6.6
# 
# Reflect the point $(5, 3)$ about the line that passes through $(0, 0)$ and makes an angle $\frac{\pi}{3}$ with the $x$-axis.
# 
# ::::{dropdown} Solution
# 
# The transformation matrix is
# 
# \begin{align*}
#     Ref\left(\frac{\pi}{3}\right) &=
#     \begin{pmatrix} 
#         \cos(\frac{2\pi}{3}) & \sin(\frac{2\pi}{3}) \\
#         \sin(\frac{2\pi}{3}) & -\cos(\frac{2\pi}{3})
#     \end{pmatrix}
# \end{align*}
# 
# therefore
# 
# \begin{align*}
#     Ref\left(\frac{\pi}{3}\right)\begin{pmatrix} 5 \\ 3 \end{pmatrix} 
#     &= \begin{pmatrix} 
#         \cos(\frac{2\pi}{3}) & \sin(\frac{2\pi}{3}) \\
#         \sin(\frac{2\pi}{3}) & -\cos(\frac{2\pi}{3})
#     \end{pmatrix}
#     \begin{pmatrix} 5 \\ 3 \end{pmatrix} \\
#     &= \begin{pmatrix} \frac{3\sqrt{3}}{2} - \frac{5}{2} \\ \frac{3}{2} + \frac{5\sqrt{3}}{2} \end{pmatrix} 
#     \approx \begin{pmatrix} 0.0981 \\ 5.8301 \end{pmatrix}.
# \end{align*}
# ::::
# 
# :::::

# In[2]:


P = Matrix([5, 3])
theta = pi / 3
R = Matrix([[cos(2 * theta), sin(2 * theta)], [sin(2 * theta), -cos(2 * theta)]])

pprint(R)

pprint(R * P)

pprint((R * P).evalf(6))


# :::::{admonition} Exercise 6.7
# :class: note
# :name: ex6.7
# 
# A square with side lengths 2 is centred at the co-ordinates $(3, 2)$. It is to be translated so the centre is at the origin, rotated by an angle $\frac{\pi}{3}$ clockwise about the origin and then translated back to its initial position. 
# 
# (a) &emsp; Write down matrix containing the homoegeneous co-ordinates for the vertices of the square.
# 
# ::::{dropdown} Solution
# \begin{align*}
#     P = \begin{pmatrix} 
#         2 & 4 & 4 & 2 \\
#         1 & 1 & 3 & 3 \\
#         1 & 1 & 1 & 1 
# \end{pmatrix}
# \end{align*}
# ::::
# 
# (b) &emsp; Determine the transformation matrices that perform the three transformations.
# 
# ::::{dropdown} Solution
# Translate to the origin:
# 
# \begin{align*} 
#     T \begin{pmatrix} -3 \\ -2 \end{pmatrix} = \begin{pmatrix}
#         1 & 0 & -3 \\
#         0 & 1 & -2 \\
#         0 & 0 & 1 
#     \end{pmatrix}
# \end{align*}
# 
# Rotate by $\frac{\pi}{3}$ clockwise about the origin:
# 
# \begin{align*}
#     Rot\left(-\frac{\pi}{3}\right) &=
#     \begin{pmatrix}
#         \cos(\frac{\pi}{3}) & \sin(\frac{\pi}{3}) \\
#         -\sin(\frac{\pi}{3}) & \cos(\frac{\pi}{3})
#     \end{pmatrix} \\
#     &= \begin{pmatrix}
#         \frac{1}{2} & \frac{\sqrt{3}}{2} \\
#         -\frac{\sqrt{3}}{2} & \frac{1}{2}
#     \end{pmatrix} \\
#     &\approx \begin{pmatrix}
#         0.5 & 0.8660 \\
#         -0.8660 & 0.5
#     \end{pmatrix}
# \end{align*}
# 
# Translate back to the original centre:
# 
# \begin{align*}
#     T \begin{pmatrix} 3 \\ 2 \end{pmatrix} &= \begin{pmatrix}
#         1 & 0 & 3 \\
#         0 & 1 & 2 \\
#         0 & 0 & 1
#     \end{pmatrix}
# \end{align*}
# ::::
# 
# (c) &emsp; Calculate the composite transformation matrix and apply with to the co-ordinate matrix from part (a).
# 
# ::::{dropdown} Solution
# 
# Calculate composite alignment matrix
# 
# \begin{align*}
#     A &= T \begin{pmatrix} 3 \\ 2 \end{pmatrix} Rot\left(-\frac{\pi}{3}\right) T \begin{pmatrix} -3 \\ -2 \end{pmatrix} \\
#     &= \begin{pmatrix}
#         1 & 0 & 3 \\
#         0 & 1 & 2 \\
#         0 & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix}
#         \frac{1}{2} & \frac{\sqrt{3}}{2} \\
#         -\frac{\sqrt{3}}{2} & \frac{1}{2}
#     \end{pmatrix}
#     \begin{pmatrix}
#         1 & 0 & -3 \\
#         0 & 1 & -2 \\
#         0 & 0 & 1 
#     \end{pmatrix} \\
#     &= \begin{pmatrix}
#         \frac{1}{2} & \frac{\sqrt{3}}{2} & \frac{3}{2} - \sqrt{3} \\
#         -\frac{\sqrt{3}}{2} & \frac{1}{2} & 1 + \frac{3\sqrt{3}}{2} \\
#         0 & 0 & 1 
#     \end{pmatrix} \\
#     &\approx
#     \begin{pmatrix}
#         0.5 & 0.8660 & -0.2321 \\
#         -0.8660 & 0.5 & 3.5981 \\
#         0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# Apply composite transformation matrix
# 
# \begin{align*}
#     AP &= \begin{pmatrix}
#         \frac{1}{2} & \frac{\sqrt{3}}{2} & \frac{3}{2} - \sqrt{3} \\
#         -\frac{\sqrt{3}}{2} & \frac{1}{2} & 1 + \frac{3\sqrt{3}}{2} \\
#         0 & 0 & 1 
#     \end{pmatrix}
#     \begin{pmatrix} 
#         2 & 4 & 4 & 2 \\
#         1 & 1 & 3 & 3 \\
#         1 & 1 & 1 & 1 
#     \end{pmatrix} \\
#     &= \begin{pmatrix}
#         \frac{5}{2} - \frac{\sqrt{3}}{2} & \frac{7}{2} - \frac{\sqrt{3}}{2} & \frac{\sqrt{3}}{2} + \frac{7}{2} & \frac{\sqrt{3}}{2} + \frac{5}{2} \\
#         \frac{\sqrt{3}}{2} + \frac{3}{2} & \frac{3}{2} - \frac{\sqrt{3}}{2} & \frac{5}{2} - \frac{\sqrt{3}}{2} & \frac{\sqrt{3}}{2} + \frac{5}{2} \\
#         1 & 1 & 1 & 1
#     \end{pmatrix} \\
#     &\approx \begin{pmatrix}
#         1.634 & 2.634 & 4.366 & 3.366 \\
#         2.366 & 0.634 & 1.634 & 3.366 \\
#         1 & 1 & 1 & 1 
#     \end{pmatrix}
# \end{align*}
# 
# :::{glue:} ex6.7_plot 
# :::
# 
# ::::
# 
# :::::

# In[3]:


from sympy import *


c = Matrix([3, 2])
P = Matrix([[c[0]-1, c[0]+1, c[0]+1, c[0]-1], [c[1]-1, c[1]-1, c[1]+1, c[1]+1], [1, 1, 1, 1]])
T1 = Matrix([[1, 0, -c[0]], [0, 1, -c[1]], [0, 0, 1]])
theta = pi / 3
R = Matrix([[cos(theta), sin(theta), 0], [-sin(theta), cos(theta), 0], [0, 0, 1]])
T2 = Matrix([[1, 0, c[0]], [0, 1, c[1]], [0, 0, 1]])

A = T2 * R * T1
P1 = A * P
pprint(P1.evalf(5))


# In[4]:


import numpy as np
import matplotlib.pyplot as plt

c = np.array([3, 2])
P = np.array([[c[0]-1, c[0]+1, c[0]+1, c[0]-1], [c[1]-1, c[1]-1, c[1]+1, c[1]+1], [1, 1, 1, 1]])
T1 = np.array([[1, 0, -c[0]], [0, 1, -c[1]], [0, 0, 1]])
theta = np.pi / 3
R = np.array([[np.cos(theta), np.sin(theta), 0], [-np.sin(theta), np.cos(theta), 0], [0, 0, 1]])
T2 = np.array([[1, 0, c[0]], [0, 1, c[1]], [0, 0, 1]])

A = np.dot(T2, np.dot(R, T1))
P1 = np.dot(A, P)

fig, ax = plt.subplots(figsize=(8, 6))
plt.fill(P[0,:], P[1,:], fill=false, ec='b', alpha=0.5, linewidth=2, label="Original square")
plt.fill(P1[0,:], P1[1,:], fill=false, ec='r', alpha=0.5, linewidth=2, label="Transformed square")
plt.axis([0, 6, 0, 4])
plt.xlabel('$x$', fontsize=14)
plt.ylabel('$y$', fontsize=14)
plt.legend(fontsize=12)
plt.show()

from myst_nb import glue
glue("ex6.7_plot", fig, display=False)

