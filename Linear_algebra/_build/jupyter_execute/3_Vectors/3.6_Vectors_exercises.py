#!/usr/bin/env python
# coding: utf-8

# (vectors-exercises-section)=
# # Vectors exercises
# 
# :::::{admonition} Exercise 3.1
# :class: note
# :name: ex3.1
# 
# The points $U$, $V$ and $W$ have the following position vectors:
# \begin{align*}
#     \mathbf{u} &= \begin{pmatrix} 2 \\ 3 \end{pmatrix}, &
#     \mathbf{v} &= \begin{pmatrix} 3 \\ -2 \end{pmatrix}, &
#     \mathbf{w} &= \begin{pmatrix} 1 \\ 6 \end{pmatrix}.
# \end{align*}
# 
# Find:
# 
# ::::{grid}
# :gutter: 2
# 
# :::{grid-item} 
# :columns: 4
# (a) &emsp; $2 \mathbf{u} + \mathbf{w}$
# :::
# :::{grid-item} 
# :columns: 4
# (b) &emsp; $\mathbf{w} - \mathbf{u}$
# :::
# :::{grid-item}  
# :columns: 12
# (c) &emsp; a unit vector pointing in the same direction of $\mathbf{u}$
# :::
# :::{grid-item}  
# :columns: 12
# (d) &emsp; a unit vector pointing in the opposite direction of $\mathbf{v}$ 
# :::
# :::{grid-item}  
# :columns: 12
# (e) &emsp; a vector pointing in the same direction as $\mathbf{v}$ with half its magnitude
# :::
# :::{grid-item}  
# :columns: 4
# (f) &emsp; $\overrightarrow{UV}$
# :::
# :::{grid-item}  
# :columns: 4
# (g) &emsp; $\overrightarrow{UW}$
# :::
# :::{grid-item}  
# :columns: 4
# (h) &emsp; $\mathbf{u} \cdot \mathbf{w}$
# :::
# :::{grid-item}  
# :columns: 4
# (i) &emsp; the angle $\angle VUW$
# :::
# :::{grid-item}  
# :columns: 8
# (j) &emsp; show that $\mathbf{u}$ is at right angles to $\mathbf{v}$
# :::
# :::{grid-item}  
# :columns: 4
# (k) &emsp; $\mathbf{v} \times \mathbf{w}$
# :::
# 
# ::::
# 
# 
# ::::{dropdown} Solutions
# 
# (a) &emsp; $2\mathbf{u} + \mathbf{w} = 2\begin{pmatrix} 2 \\ 3 \end{pmatrix} + \begin{pmatrix} 1 \\ 6 \end{pmatrix} 
# = \begin{pmatrix} 4 \\ 6 \end{pmatrix} + \begin{pmatrix} 1 \\ 6 \end{pmatrix} 
# = \begin{pmatrix} 5 \\ 12 \end{pmatrix}$;
# 
# (b) &emsp; $\mathbf{w} - \mathbf{u} = \begin{pmatrix} 1 \\ 6 \end{pmatrix} - \begin{pmatrix} 2 \\ 3 \end{pmatrix} 
# = \begin{pmatrix} 1 - 2 \\ 6 - 3 \end{pmatrix} = \begin{pmatrix} -1 \\ 3 \end{pmatrix}$;
# 
# (c) &emsp; $\hat{\mathbf{u}} = \dfrac{\mathbf{u}}{|\mathbf{u}|} = \dfrac{1}{\sqrt{13}} \begin{pmatrix} 2 \\ 3 \end{pmatrix} 
# = \begin{pmatrix} \frac{2}{\sqrt{13}} \\ \frac{3}{\sqrt{13}} \end{pmatrix}$;
# 
# (d) &emsp; $-\hat{\mathbf{v}} = -\dfrac{\mathbf{v}}{|\mathbf{v}|} = -\dfrac{1}{\sqrt{13}} \begin{pmatrix} 3 \\ -2 \end{pmatrix} = \begin{pmatrix} -\frac{3}{\sqrt{13}} \\ \frac{2}{\sqrt{13}} \end{pmatrix}$;
# 
# (e) &emsp; $\dfrac{1}{2}\mathbf{v} = \dfrac{1}{2} \begin{pmatrix} 3 \\ -2 \end{pmatrix} 
# = \begin{pmatrix} 3 / 2 \\ -2 / 2 \end{pmatrix}$;
# 
# (f) &emsp; $\overrightarrow{UV} = \mathbf{v} - \mathbf{u} = \begin{pmatrix} 3 \\ -2 \end{pmatrix} - \begin{pmatrix} 2 \\ 3 \end{pmatrix}= \begin{pmatrix} 1 \\ -5 \end{pmatrix}$;
# 
# (g) &emsp; $\overrightarrow{UW} = \mathbf{w} - \mathbf{u} = \begin{pmatrix} 1 \\ 6 \end{pmatrix} - \begin{pmatrix} 2 \\ 3 \end{pmatrix} = \begin{pmatrix} -1 \\ 3 \end{pmatrix}$;
# 
# (h) &emsp; $\mathbf{u} \cdot \mathbf{w} = \begin{pmatrix} 2 \\ 3 \end{pmatrix} \cdot \begin{pmatrix} 1 \\ 6 \end{pmatrix} = 2 \times 1 + 3 \times 6 = 20$;
# 
# (i) &emsp; Using equation {eq}`geometric-dot-product-equation`
# 
# \begin{align*}
#     \overrightarrow{UV} \cdot \overrightarrow{UW} &= |\overrightarrow{UV}||\overrightarrow{UW}| \cos(\theta) \\
#     \begin{pmatrix} 1 \\ -5 \end{pmatrix} \cdot \begin{pmatrix} -1 \\ 3 \end{pmatrix} &=
#     \left| \begin{pmatrix} 1 \\ -5 \end{pmatrix} \right|
#     \left| \begin{pmatrix} -1 \\ 3 \end{pmatrix} \right| \cos(\theta) \\
#     -16 &= \sqrt{26} \sqrt{10} \cos(\theta) \\
#     \theta &= \cos^{-1} \left( \frac{-16}{\sqrt{260}} \right) = 3.0172
# \end{align*}
# 
# (j) &emsp; $\mathbf{u} \cdot \mathbf{v} = \begin{pmatrix} 2 \\ 3 \end{pmatrix} \cdot \begin{pmatrix} 3 \\ -2 \end{pmatrix} = 2 \times 3 + 3 \times (-2) = 0$;
# 
# (k) &emsp; $\begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 3 & -2 & 0 \\ 1 & 6 & 0 \end{vmatrix} = 0\mathbf{i} - 0 \mathbf{j} + 20 \mathbf{k} = \begin{pmatrix} 0 \\ 0 \\ 20 \end{pmatrix}$.
# ::::
# :::::

# :::::{admonition} Exercise 3.2
# :class: note
# :name: ex3.2
# 
# Write $\mathbf{u} = (2,7,1)$ as:
# 
# (a) &emsp; a linear combination of $\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$, $\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$ and $\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$.
# 
# (b) &emsp; a linear combination of vectors $\mathbf{f}_1 = \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}, \mathbf{f}_2 = \begin{pmatrix} 0 \\ 2 \\ 0 \end{pmatrix}$ and $\mathbf{f}_3 = \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}$.
# 
# ::::{dropdown} Solutions
# 
# (a) &emsp; $\mathbf{u} = 2 \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + 7 \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} + \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = 2 \mathbf{i} + 7 \mathbf{j} + \mathbf{k}$;
# 
# (b)
# \begin{align*}
#     & \left( \begin{array}{ccc|c}
#     1 & 0 & 1 & 2 \\
#     -1 & 2 & 0 & 7 \\
#     0 & 0 & -1 & 1
#     \end{array} \right)
#     \begin{array}{l} \\ R_2 + R_1 \\ \phantom{x} \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & 1 & 2 \\
#         0 & 2 & 1 & 9 \\
#         0 & 0 & -1 & 1
#     \end{array} \right)
#     \begin{array}{l} \\ \\ R_3 + R_1 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & 1 & 2 \\
#         0 & 1 & 1/2 & 9/2 \\
#         0 & 0 & 1 & -1
#     \end{array} \right) \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & 0 & 3 \\
#         0 & 1 & 0 & 5 \\
#         0 & 0 & 1 & -1
#     \end{array} \right)
# \end{align*}
# 
#  Therefore $\mathbf{u} = 3 \mathbf{f}_1 + 5 \mathbf{f}_2 - \mathbf{f}_3$.
# ::::
# 
# :::::

# :::::{admonition} Exercise 3.3
# :class: note
# :name: ex3.3
#         
# Let $\mathbf{u} \in \mathbb{R}^3$ be given as $\mathbf{u} = (x, x + y, z - x) = (1, 3, 5)$.
# 
# (a) &emsp; Find $x$, $y$ and $z$.
# 
# (b) &emsp; What property of vectors are you using to determine $x,y$ and $z$?
# 
# ::::{dropdown} Solutions
# (a) &emsp; Equating the first element gives $x = 1$, equating the second element gives $x + y = 1 + y = 3$ so $y = 2$, equating the third element gives $z - x = z - 1 = 5$ so $z = 6$.
# 
# (b) &emsp; [Vector equality](vector-equality-definition).
# 
# ::::
# :::::

# :::::{admonition} Exercise 3.4
# :class: note
# :name: ex3.4
# 
# Find $k$ such that the vectors $\mathbf{u}$ and $\mathbf{v}$ are perpendicular:
# 
# (a) &emsp; $\mathbf{u} = (1, k, -2)$ and $\mathbf{v} = (2, -5, 4)$ in $\mathbb{R}^3$.
# 
# (b) &emsp; $\mathbf{u} =(1, 0, k+2, -1, 2)$ and $\mathbf{v} = (1, k, -2, 1, 2)$ in $\mathbb{R}^5$.
# 
# ::::{dropdown} Solutions
# 
# (a) &emsp; If $\mathbf{u}$ and $\mathbf{v}$ are perpendicular then $\mathbf{u} \cdot \mathbf{v} = 0$.
# 
# \begin{align*}
#     \mathbf{u} \cdot \mathbf{v} &= 0 \\
#     (1, k, -2) \cdot (2, -5, 4) &= 0 \\
#     2 - 5 k - 8 &= 0 \\
#     -5k &= 6 \\
#     k &= -\frac{6}{5}.
# \end{align*}
#         
# (b) &emsp; 
# \begin{align*}
#     \mathbf{u} \cdot \mathbf{v} &= 0 \\
#     (1, 0, k+2, -1, 2) \cdot (1, k, -2, 1, 2) &= 0 \\
#     1 - 2k - 2 - 1 + 2 &= 0 \\
#     -2k &= 0 \\
#     k &= 0.
# \end{align*}
# ::::
# :::::
# 

# :::::{admonition} Exercise 3.5
# Which pair of the following vectors is perpendicular? For the remaining pairs, what is the angle between them?
# 
# \begin{align*}
#     \mathbf{u} &= \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}, &
#     \mathbf{v} &= \begin{pmatrix} -1 \\ 2 \\ -1 \end{pmatrix}, &
#     \mathbf{w} &= \begin{pmatrix} 2 \\ -3 \\ 1 \end{pmatrix}.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
#     \mathbf{u} \cdot \mathbf{v} &= \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \cdot
#     \begin{pmatrix} -1 \\ 2 \\ -1 \end{pmatrix} = -1 + 4 - 3 = 0, \\
#     \mathbf{u} \cdot \mathbf{w} &= \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \cdot
#     \begin{pmatrix} 2 \\ -3 \\ 1 \end{pmatrix} = 2 - 6 + 3 = -1, \\
#     \mathbf{v} \cdot \mathbf{w} &= \begin{pmatrix} -1 \\ 2 \\ -1 \end{pmatrix} \cdot
#     \begin{pmatrix} 2 \\ -3 \\ 1 \end{pmatrix} = -2 -6 -1 =  -9.
# \end{align*}
# 
# Therefore $\mathbf{u} \perp \mathbf{v}$. The angle between $\mathbf{u}$ and $\mathbf{w}$ is
# 
# \begin{align*}
#     \theta &= \cos^{-1} \left( \frac{\mathbf{u} \cdot \mathbf{w}}{|\mathbf{u} ||\mathbf{w}|} \right) \\
#     &= \cos^{-1} \left( \frac{-1}{\sqrt{14}\sqrt{14}}\right) \\
#     &= \cos^{-1}\left(\frac{-1}{14}\right) = 1.6423,
# \end{align*}
# 
# and the angle between $\mathbf{v}$ and $\mathbf{w}$ is
# 
# \begin{align*}
#     \theta &= \cos^{-1} \left( \frac{\mathbf{v} \cdot \mathbf{w}}{|\mathbf{v} ||\mathbf{w}|} \right) \\
#     &= \cos^{-1} \left( \frac{-9}{\sqrt{6}\sqrt{14}} \right) = 2.9515.
# \end{align*}
# ::::
# 
# :::::
