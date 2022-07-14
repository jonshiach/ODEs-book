#!/usr/bin/env python
# coding: utf-8

# (co-ordinate-geometry-exercises-section)=
# # Co-ordinate geometry exercises
# 
# ::::{admonition} Exercise 4.1
# The points $A, B, C, D$ in $\mathbb{R}^3$ have the following position vectors
# 
# \begin{align*}
#     \mathbf{a} &= \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix}, &
#     \mathbf{b} &= \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, &
#     \mathbf{c} &= \begin{pmatrix} 3 \\ -1 \\ 4 \end{pmatrix}, &
#     \mathbf{d} &= \begin{pmatrix} 5 \\ 2 \\ 6 \end{pmatrix}.
# \end{align*}
# 
# Find:
# 
# (a) &emsp; the equation of the line that passes through $A$ and $B$;
# 
# :::{dropdown} Solution
# 
# Using the [vector equation of a line](vector-equation-of-a-line-definition) then $Q = \mathbf{a} + t\mathbf{d}_1$
# 
# \begin{align*}
#     \mathbf{d}_1 &= \mathbf{b} - \mathbf{a} =
#     \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} -
#     \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} = 
#     \begin{pmatrix} -1 \\ 0 \\ 0 \end{pmatrix}, \\
#     \therefore Q &= \mathbf{a} + t\mathbf{d}_1 =
#     \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} + t 
#     \begin{pmatrix} -1 \\ 0 \\ 0 \end{pmatrix} = 
#     \begin{pmatrix} 2 - t \\ 1 \\ 1 \end{pmatrix}
# \end{align*}
# :::
# 
# (b) &emsp; the equation of the line that passes through $C$ and $D$;
# 
# :::{dropdown} Solution
# 
# Using the [vector equation of a line](vector-equation-of-a-line-definition) then $Q = \mathbf{c} + t\mathbf{d}_2$
# 
# \begin{align*}
#     \mathbf{d}_2 &= \mathbf{d} - \mathbf{c} =
#     \begin{pmatrix} 5 \\ 2 \\ 6 \end{pmatrix} -
#     \begin{pmatrix} 3 \\ -1 \\ 4 \end{pmatrix} = 
#     \begin{pmatrix} 2 \\ 3 \\ 2 \end{pmatrix}, \\
#     \therefore Q &= \mathbf{c} + t\mathbf{d}_2 =
#     \begin{pmatrix} 3 \\ -1 \\ 4 \end{pmatrix} + t 
#     \begin{pmatrix} 2 \\ 3 \\ 2 \end{pmatrix} = 
#     \begin{pmatrix} 3 + 2 t \\ -1 + 3 t \\ 4 + 2 t \end{pmatrix}
# \end{align*}
# :::
# 
# (c) &emsp; the equation of the plane which $A$, $B$ and $C$ lie on;
# 
# :::{dropdown} Solution
# \begin{align*}
#     \overrightarrow{AB} &= \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} - 
#     \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} = 
#     \begin{pmatrix} -1 \\ 0 \\ 0 \end{pmatrix}, \\
#     \overrightarrow{AC} &= \begin{pmatrix} 3 \\ -1 \\ 4 \end{pmatrix} -
#     \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} =
#     \begin{pmatrix} 1 \\ -2 \\ 4 \end{pmatrix}, \\
#     \therefore \mathbf{n} &= \overrightarrow{AB} \times \overrightarrow{AC} = 
#     \begin{vmatrix} 
#         \mathbf{i} & \mathbf{j} & \mathbf{k} \\
#         -1 & 0 & 0 \\
#         1 & -2 & 4 
#     \end{vmatrix} =
#     \begin{pmatrix} 0 \\ 4 \\ 2 \end{pmatrix},
# \end{align*}
# 
# Using the [point normal definition of a plane](point-normal-definition)
# \begin{align*}
#     \mathbf{n} \cdot \begin{pmatrix} x - x_0 \\ y - y_0 \\ z - z_0 \end{pmatrix} &= 0 \\
#     \begin{pmatrix} 0 \\ 4 \\ 2 \end{pmatrix} \cdot \begin{pmatrix} x - 1 \\ y - 1 \\ z - 0 \end{pmatrix} &= 0 \\
#     4 y + 2 z - 4 &= 0.
# \end{align*}
# :::
# 
# 
# (d) &emsp; the equation of the plane which $B$, $C$ and $D$ lie on.
# 
# :::{dropdown} Solution
# \begin{align*}
#     \overrightarrow{BC} &= \begin{pmatrix} 3 \\ -1 \\ 4 \end{pmatrix} - 
#     \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} =
#     \begin{pmatrix} 2 \\ -2 \\ 4 \end{pmatrix}, \\
#     \overrightarrow{BD} &= \begin{pmatrix} 5 \\ 2 \\ 6 \end{pmatrix} -
#     \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} =
#     \begin{pmatrix} 4 \\ 1 \\ 6 \end{pmatrix}, \\
#     \mathbf{n} &= \overrightarrow{BC} \times \overrightarrow{BD} = 
#     \begin{vmatrix}
#         \mathbf{i} & \mathbf{j} & \mathbf{k} \\
#         2 & -2 & 4 \\
#         4 & 1 & 6
#     \end{vmatrix} =
#     \begin{pmatrix} -16 \\ 4 \\ 10 \end{pmatrix},
# \end{align*}
# 
# Using the [point normal definition of a plane](point-normal-definition)
# 
# \begin{align*}
#     \mathbf{n} \cdot \begin{pmatrix} x - x_0 \\ y - y_0 \\ z - z_0 \end{pmatrix} &= 0 \\
#     \begin{pmatrix} -16 \\ 4 \\ 10 \end{pmatrix} \cdot 
#     \begin{pmatrix} x - 1 \\ y - 1 \\ z - 0 \end{pmatrix} &= 0 \\
#     -16 x + 4 y + 10 z + 12 &= 0.
# \end{align*}
# :::
# 
# ::::
# 
# ::::{admonition} Exercise 4.2
# Find the equation of the line that passes through the point $(3, 2, 1)$ which is parallel to $2 \mathbf{i} + \mathbf{j} + 3 \mathbf{k}$.
# 
# :::{dropdown} Solution
# $$ Q = \begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix} + t \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix}  = \begin{pmatrix} 3 + 2 t \\ 2 + 3 t \\ 1 + 3 t \end{pmatrix} $$
# :::
# 
# ::::
# 
# ::::{admonition} Exercise 4.3
# Find the equation of the plane that passes through the point $(3, 2, 5)$ which has a normal vector $\mathbf{n} = (2, 1, 3)$.
# 
# :::{dropdown} Solution
# Using the [point normal definition of a plane](point-normal-definition)
# \begin{align*}
#     \mathbf{n} \cdot \begin{pmatrix} x - x_0 \\ y - y_0 \\ z - z_0 \end{pmatrix} &= 0 \\
#     \begin{pmatrix} 2 \\ 1 \\ 3 \end{pmatrix} \cdot
#     \begin{pmatrix} x - 3 \\ y - 2 \\ z - 5 \end{pmatrix} \\
#     2(x - 3) + (y - 2) + 3(z - 5) &= 0 \\
#     2 x + y + 3 z - 23 &= 0
# \end{align*}
# :::
# ::::
# 
# ::::{admonition} Exercise 4.4
# Two lines in $\mathbb{R}^3$ are defined by $\ell_1: (1 + 2t, -t, 1 + 3t)$ and $\ell_2: (1 + 2t, 4, 7 - t)$ respectively.
# 
# (a) &emsp; find the intersection of the lines or show they are skew;
# 
# :::{dropdown} Solution
# Equating $\ell_1$ and $\ell_2$ and attempting to solve for $t$
# \begin{align*}
#     1 + 2t &= 1 + 2t \\
#     -t &= 4 \\
#     1 + 3t &= 7 - t
# \end{align*}
# 
# From the second equation $t = -4$ which when substituted into the third equation gives $-11 = 11$ which is a contradiction, therefore $\ell_1$ and $\ell_2$ do not intersect. 
# 
# We also need to show that they are not parallel, i.e., there is no value $k$ such that $\mathbf{d}_1 = k \mathbf{d}_2$. The direction vectors for $\ell_1$ and $\ell_2$ are $\mathbf{d}_1 = (2, -1, 3)$ and $\mathbf{d}_2 = (2, 0, -1)$ so
# 
# \begin{align*}
#     \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} &= k \begin{pmatrix} 2 \\ 0 \\ -1 \end{pmatrix},
# \end{align*}
# 
# which gives the system
# 
# \begin{align*}
#     2 &= 2k ,\\
#     -1 &= 0, \\
#     3 &= -k.
# \end{align*}
# 
# The second equation is a contradiction so $\ell_1$ and $\ell_2$ are not parallel, and since they do not intersect then they must be skew.
# :::
# 
# (b) &emsp; find the shortest distance between the lines;
# 
# :::{dropdown} Solution
# Here $\ell_1$ is $P_1 + t\mathbf{d}_1 = (1, 0, 1) + t(2, -1, 3)$ and $\ell_2$ is $P_2 + \mathbf{d}_2 = (1, 4, 7) + t(2, 0, -1)$, so calculating a vector perpendicular to both $\ell_1$ and $\ell_2$ gives
# 
# \begin{align*}
#     \mathbf{n} &= \mathbf{d}_1 \times \mathbf{d_1} = \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} \times
#     \begin{pmatrix} 2 \\ 0 \\ -1 \end{pmatrix} =
#     \begin{vmatrix}
#         \mathbf{i} & \mathbf{j} & \mathbf{k} \\
#         2 & -1 & 3 \\
#         2 & 0 & -1 
#     \end{vmatrix} = 
#     \begin{pmatrix} 1 \\ 8 \\ 2 \end{pmatrix}, \\
# \end{align*}
# 
# and normalising gives
# 
# \begin{align*}
#     \hat{\mathbf{n}} = \frac{\mathbf{n}}{|\mathbf{n}|} = \frac{1}{\sqrt{69}} 
#     \begin{pmatrix} 1 \\ 8 \\ 2 \end{pmatrix} =
#     \begin{pmatrix} \frac{\sqrt{69}}{69} \\ \frac{8\sqrt{69}}{69} \\ \frac{2\sqrt{69}}{69} \end{pmatrix}.
# \end{align*}
# 
# Using [the distance between two lines](line-line-distance-definition)
# 
# \begin{align*}
#     d &= (\mathbf{p}_2 - \mathbf{p}_1) \cdot \hat{\mathbf{n}} \\
#     &= \left( \begin{pmatrix} 1 \\ 4 \\ 7 \end{pmatrix} -
#     \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} \right) \cdot
#     \begin{pmatrix} \frac{\sqrt{69}}{69} \\ \frac{8\sqrt{69}}{69} \\ \frac{2\sqrt{69}}{69} \end{pmatrix} \\
#     &= \begin{pmatrix} 0 \\ 4 \\ 6 \end{pmatrix} \cdot
#     \begin{pmatrix} \frac{\sqrt{69}}{69} \\ \frac{8\sqrt{69}}{69} \\ \frac{2\sqrt{69}}{69} \end{pmatrix} \\
#     &= \frac{44\sqrt{69}}{69}.
# \end{align*}
# :::
# 
# (c) &emsp; find the distance between the point $P = (0, -1, 3)$ and $\ell_1$.
# 
# :::{dropdown} Solution
# Using the [shortest distance between a point and a line](point-line-distance-definition)
# 
# \begin{align*}
#     t &= \frac{(P - P_1)\cdot \mathbf{d}_1}{\mathbf{d}_1 \cdot \mathbf{d}_1} = \frac{ 
#     \left( \begin{pmatrix} 0 \\ -1 \\ 3 \end{pmatrix} -
#     \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} \right) \cdot
#     \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}}{
#         \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} \cdot
#         \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}
#     } 
#     = \frac{5}{14}, \\
#     \therefore Q &= P_1 + t\mathbf{d}_1 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} + \frac{5}{14} 
#     \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} = 
#     \begin{pmatrix} \frac{12}{7} \\ - \frac{5}{14} \\ \frac{29}{14} \end{pmatrix}, \\
#     \overrightarrow{QP} &= \begin{pmatrix} 0 \\ -1 \\ 3 \end{pmatrix} - 
#     \begin{pmatrix} \frac{12}{7} \\ -\frac{5}{14} \\ \frac{29}{14} \end{pmatrix} =
#     \begin{pmatrix} -\frac{12}{7} \\ -\frac{9}{14} \\ \frac{13}{14} \end{pmatrix}, \\
#     \therefore |\overrightarrow{QP}| &= 
#     \sqrt{\left(-\frac{12}{7}\right)^2 + \left(-\frac{9}{14}\right)^2 + \left(\frac{13}{14}\right)^2} 
#     = \frac{\sqrt{826}}{14}.
# \end{align*}
# :::
# ::::
# 
# ::::{admonition} Exercise 4.5
# A plane has the equation $3x - 2y + z = 10$. Identify the normal to the plane and find the co-ordinates of 2 points on the plane having $z = 2$.
# 
# :::{dropdown} Solution
# $\mathbf{n} = (3, -2, 1)$. 
# 
# Let $x=0$ then $3(0) - 2 y + 2 = 10$ so $y = -4$ and a point on the plane has co-ordinates $(0, -4, 2)$.
# 
# Let $x = 2$ then $3(2) - 2 y + 2 = 10$ so $y = -1$ and a point on the plane has co-ordinates $(2, -4, -1)$.
# :::
# ::::
# 
# ::::{admonition} Exercise 4.6
# Find the point where the line $Q = (1 + 2t, 2 + t, -1 + 4t)$ meets the plane $6x - y - 4z = 3$. 
# 
# :::{dropdown} Solution
# 
# First we need to find the co-ordinates of a point, $R$ say, that lies on the plane. Let $x=0$ and $y=1$ then $z=-1$ so we know that $R = (0, 1, -1)$ lies on the plane. Using the [point normal definition of a plane](point-normal-definition)
# 
# \begin{align*}
#     \mathbf{n} \cdot \begin{pmatrix} x - x_0 \\ y - y_0 \\ z - z_0 \end{pmatrix} &= 0 \\
#     \begin{pmatrix} 6 \\ -1 \\ -4 \end{pmatrix} \cdot
#     \begin{pmatrix} 0 - (1 + 2 t) \\ 1 - (2 + t) \\ -1 - (-1 + 4 t) \end{pmatrix} &= 0 \\
#     \begin{pmatrix} 6 \\ -1 \\ -4 \end{pmatrix} \cdot
#     \begin{pmatrix} - 1 - 2 t \\ -1 - t \\  -4 t \end{pmatrix} &= 0 \\
#     -6 - 12 t + 1 + t + 16 t &= 0 \\
#     5 t - 5 &= 0 \\
#     \therefore t = 1.
# \end{align*}
# 
# So the line intersects with the plane at
# 
# \begin{align*}
#     P + t \mathbf{d} = 
#     \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix} + 
#     \begin{pmatrix} 2 \\ 1 \\ 4 \end{pmatrix} =
#     \begin{pmatrix} 3 \\ 3 \\ 3 \end{pmatrix}.
# \end{align*}
# :::
# ::::
# 
# ::::{admonition} Exercise 4.7
# :class: note
# :name: ex4.7
# Consider the diagram below that shows a plane that passes through the point $\mathbf{p}$ and has normal vector $\mathbf{n}$ and the point with position $\mathbf{q}$ not on the plane. 
# 
# :::{figure} ../Images/point_plane_distance.png
# :::
# 
# Using the [geometric definition of a dot product](dot-product-definition) derive an expression for calculating the shortest distance between a point and a plane. Use your expression to find the shortest distance from the point $(2, 4, -3)$ to the plane $6x - y - 4z = 3$.
# 
# :::{dropdown} Solution
# Using the [geometric definition of a dot product](dot-product-definition)
# 
# \begin{align*}
#     (Q - P)\cdot \mathbf{n} &= |\mathbf{n}||Q - P| \cos(\theta).
# \end{align*}
# 
# Since $d$ is the length of the adjacent side of the right-angled triangle then
# 
# \begin{align*}
#     \cos(\theta) &= \frac{d}{|Q - P|},
# \end{align*}
# 
# So
# 
# \begin{align*}
#     (Q - P) \cdot \mathbf{n} &= |\mathbf{n}| |Q - P| \frac{d}{|Q - P|} \\
#     \therefore d &= (Q - P)\cdot \frac{\mathbf{n}}{|\mathbf{n}|}.
# \end{align*}
# 
# The equation of the plane is $6 x-y-4 z=3$ so letting $x=0$ and $y=1$ then $z = 1$ so we know that $P = (0, 1, -1)$ lies on the plane. Since $Q = (2, 4, -3)$ and $\mathbf{n} = (6, -1, -4)$ then applying the above formula gives
# 
# \begin{align*}
#     d &= \left( \begin{pmatrix} 2 \\ 4 \\ -3 \end{pmatrix} -
#     \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix} \right) \cdot 
#     \begin{pmatrix} 6 \\ -1 \\ -4 \end{pmatrix} / \left|
#     \begin{pmatrix} 6 \\ -1 \\ -4 \end{pmatrix} \right| \\
#     &= \begin{pmatrix} 2 \\ 3 \\ -2 \end{pmatrix} \cdot \frac{1}{\sqrt{53}} 
#     \begin{pmatrix} 6 \\ -1 \\ -4 \end{pmatrix} \\
#     &= \frac{12 - 3 + 8}{\sqrt{53}} = \frac{17}{\sqrt{53}}
# \end{align*}
# :::
# ::::
