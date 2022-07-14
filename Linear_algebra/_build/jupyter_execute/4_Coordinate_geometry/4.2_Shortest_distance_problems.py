#!/usr/bin/env python
# coding: utf-8

# (shortest-distance-problems)=
# # Shortest distance problems
# 
# We can take advantage of vector geometry to calculate the solutions to shortest distance problems. 
# 
# (shortest-distance-between-two-points)=
# ## Shortest distance between two points
# 
# In $\mathbb{R}^n$ the shortest distance, $d$, between two points $P$ and $Q$ is the length of a straight line segment connecting them. If we think about this segment as of a vector, then
# 
# \begin{align*}
#     d = |\overrightarrow{PQ}| = \sqrt{\displaystyle\sum_{i=1}^n (p_i-q_i)^2},
# \end{align*}
# 
# where $P=(p_1,p_2,\dots,p_n)$ and $Q=(q_1,q_2,\dots,q_n)$.
# 
# ## Shortest distance between a line and a point
# 
# To find the shortest distance, $d$, between a line $\ell: P + \mathbf{d}t$ and a point $Q$ in $\mathbb{R}^n$ we look at a plane they both lie in. Let $R$ be a point on the line such that the vector $\overrightarrow{RQ}$ is perpendicular to $\mathbf{d}$ ({numref}`line-point-distance-figure`) then
# 
# \begin{align*}
#     d = | \overrightarrow{RQ} |.
# \end{align*}
# 
# :::{figure} ../Images/line_point_distance.png
# :name: line-point-distance-figure
# 
# The shortest distance of a point $Q$ from the line $\ell$ is the length of the chord $R \to Q$ which is perpendicular to $\ell$.
# :::
# 
# Since $\overrightarrow{RQ}$ is perpendicular to $d$ then $\overrightarrow{RQ} \cdot \mathbf{d} = 0$ so we calculate the position of $R$ that satisfies
# 
# :::{math}
# :label: point-line-distance-equation
# 
# (Q - R) \cdot \mathbf{d} = 0.
# :::
# 
# Substituting $R = P + t\mathbf{d}$ into equation {eq}`point-line-distance-equation` and rearranging to make $t$ the subject gives
# 
# \begin{align*}
#     (Q - P - t \mathbf{d}) \cdot \mathbf{d} &= 0 \\
#     (Q - P) \cdot \mathbf{d} - t \mathbf{d} \cdot \mathbf{d} &= 0 \\
#     \therefore t &= \frac{(Q - P) \cdot \mathbf{d}}{ \mathbf{d} \cdot \mathbf{d}}.
# \end{align*}
# 
# This gives the value of the parameter $t$ that can be used to calculate the co-ordinates of the point $R$ and therefore the shortest distance between the point $Q$ and the line $\ell$ is $|Q - R|$.
# 
# ::::{admonition} Theorem: The shortest distance between a point and a line
# :class: important
# :name: point-line-distance-theorem
# 
# The shortest distance between the point $Q$ and a line that passes through the point $P$ in the direction $\mathbf{d}$ is $|Q - R|$ where $R = P + t\mathbf{d}$ and 
# 
# :::{math}
# :label: point-line-t-equation
# 
# t = \frac{(Q - P) \cdot \mathbf{d}}{ \mathbf{d} \cdot \mathbf{d}}.
# :::
# ::::
# 
# ::::{admonition} Example 4.8
# :class: seealso
# :name: point-line-distance-example
# 
# Find the shortest distance between the point $Q = (2,2,2)$ and the line $\ell : (t,t-2, t+1)$.
# 
# :::{dropdown} Solution
# 
# Writing $\ell$ as a vector equation 
# 
# \begin{align*}
#     \begin{pmatrix} 0 \\ -2 \\ 1 \end{pmatrix} + t
#     \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix},
# \end{align*}
# 
# so the direction vector is $\mathbf{d} = (1, 1, 1)$. Using {eq}`point-line-distance-equation`
# 
# \begin{align*}
#     t &= \frac{ \left( \begin{pmatrix} 2 \\ 2 \\ 2 \end{pmatrix} - 
#     \begin{pmatrix} 0 \\ -2 \\ 1 \end{pmatrix}\right) \cdot 
#     \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}}{
#     \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \cdot 
#     \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}
#     }
#     = \frac{\begin{pmatrix} 2 \\ 4 \\ 1 \end{pmatrix} \cdot 
#     \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}
#     }{1 + 1 + 1} 
#     = \frac{2 + 4 + 1}{3} = \frac{7}{3}.
# \end{align*}
# 
# So the point on $\ell$ which is closest to $Q$ is
# 
# \begin{align*}
#     R = \begin{pmatrix} t \\ t - 2 \\ t + 1 \end{pmatrix} 
#     = \begin{pmatrix} \frac{7}{3} \\ \frac{7}{3} - 2 \\ \frac{7}{3} + 1 \end{pmatrix}
#     = \begin{pmatrix} \frac{7}{3} \\ \frac{1}{3} \\ \frac{10}{3} \end{pmatrix},
# \end{align*}
# 
# and the shortest distance is $|Q - R|$ so
# 
# \begin{align*}
#     Q - R = \begin{pmatrix} 2 \\ 2 \\ 2 \end{pmatrix} - 
#     \begin{pmatrix} \frac{7}{3} \\ \frac{1}{3} \\ \frac{10}{3} \end{pmatrix} =
#     \begin{pmatrix} -\frac{1}{3} \\ \frac{5}{3} \\ -4/ 3 \end{pmatrix}, \\
#     \therefore |\overrightarrow{QR}| &= \sqrt{\left(-\frac{1}{3}\right)^2 + \left(\frac{5}{3}\right)^2 + \left( -\frac{4}{3}\right)^2} = \sqrt{\frac{14}{3}} \approx 2.16.
# \end{align*}
# :::
# ::::
# 
# ## Shortest distance between two lines
# 
# Given two lines described by $\ell_1: P_1 + t\mathbf{d}_1$ and $\ell_2: P_2 + t\mathbf{d}_2$ in $\mathbb{R}^n$ we have three situations to consider
# 
# - If the two lines intersect then obviously the shortest distance is obviously 0.   
# - If the two lines are parallel then any point on $\ell_1$ can gives the shortest distance between $\ell_1$ and $\ell_2$. Hence we simply choose a point $R$ on $\ell_2$ and apply method for [finding the distance between a point and a line](point-line-distance-definition).
# - If the two lines are skew then the shortest distance is the distance of the chord that is perpendicular to both $\ell_1$ and $\ell_2$ ({numref}`line-line-distance-figure`). 
# 
# :::{figure} ../Images/line_line_distance.png
# :name: line-line-distance-figure
# 
# The shortest distance between skew lines is the distance of the chord which is perpendicular to both lines.
# :::
# 
# If $Q_1$ and $Q_2$ are points on the lines $\ell_1$ and $\ell_2$ respectively then the chord $Q_2 - Q_1$ which is perpendicular to both lines has the direction vector $\mathbf{n} = \mathbf{d}_1 \times \mathbf{d}_2$. If $d$ is the distance between $Q_1$ and $Q_2$ then
# 
# :::{math}
# :label: line-line-distance-equation-1
# 
# Q_2 - Q_1 = d (\mathbf{d}_1 \times \mathbf{d}_2),
# :::
# 
# Let $\hat{\mathbf{n}} = \dfrac{\mathbf{d}_1 \times \mathbf{d}_2}{|\mathbf{d}_1 \times \mathbf{d}_2|}$ and substituting the equations of $Q_1$ and $Q_2$ equation {eq}`line-line-distance-equation-1` gives
# 
# \begin{align*}
#     Q_2 - Q_1 &= d \hat{\mathbf{n}}\\
#     (P_2 + t_2 \mathbf{d}_2) - (P_1 + t_1 \mathbf{d}_1) 
#     &= d \hat{\mathbf{n}}\\
#     (P_2 + t_2 \mathbf{d}_2) \cdot \hat{\mathbf{n}} - (P_1 + t_1 \mathbf{d}_1) \cdot \hat{\mathbf{n}} 
#     &= d \hat{\mathbf{n}} \cdot \hat{\mathbf{n}} \\
#     P_2 \cdot \hat{\mathbf{n}} + t_2 \mathbf{d}_2 \cdot \hat{\mathbf{n}} - P_1 \cdot \hat{\mathbf{n}} - t_1 \mathbf{d}_1 \cdot \hat{\mathbf{n}} 
#     &= d \hat{\mathbf{n}} \cdot \hat{\mathbf{n}}.
# \end{align*}
# 
# Since $\mathbf{n}$ is perpendicular to both $\ell_1$ and $\ell_2$ then $\mathbf{d}_1 \cdot \mathbf{n} = \mathbf{d}_2 \cdot \mathbf{n} = 0$ and $\hat{\mathbf{n}} \cdot \hat{\mathbf{n}} = 1$ then
# 
# \begin{align*}
#     P_2 \cdot \hat{\mathbf{n}} - P_1 \cdot \hat{\mathbf{n}} &= d,
# \end{align*}
# 
# which simplifies to
# 
# \begin{align*}
#     d &= (P_2 - P_1) \cdot \hat{\mathbf{n}}.
# \end{align*}
# 
# ::::{admonition} Theorem: The shortest distance between two skew lines
# :class: important
# :name: line-line-distance-theorem
# 
# The shortest distance between two skew lines $Q_1 = P_1 + t \mathbf{d}_1$ and $Q_2 = P_2 + t \mathbf{d}_2$ is
# 
# :::{math}
# :label: line-line-distance-equation
# 
# d = (P_2 - P_1) \cdot \hat{\mathbf{n}}.
# :::
# 
# where $\mathbf{n} = \dfrac{\mathbf{d}_1 \times \mathbf{d}_2}{|\mathbf{d}_1 \times \mathbf{d}_2|}$.
# ::::
# 
# ::::{admonition} Example 4.9
# :class: seealso
# :name: line-line-distance-example
# 
# Find the shortest distance between the two lines $\ell_1 = \{(t,1+4t,3 + 2t):t\in\mathbb{R}\}$ and $\ell_2 = \{(1,1+2t,3 + 4t):t\in\mathbb{R}\}$.
# 
# :::{dropdown} Solution
# 
# First, we need to identify the direction vectors $\mathbf{d}_1$ and $\mathbf{d}_2$. Writing $\ell_1$ and $\ell_2$ as vector equations gives
# 
# \begin{align*}
#     Q_1 &= P_1 + t\mathbf{d}_1 = \begin{pmatrix} 0 \\ 1 \\ 3 \end{pmatrix} + t
#     \begin{pmatrix} 1 \\ 4 \\ 2 \end{pmatrix} , \\
#     Q_2 &= P_2 + t\mathbf{d}_2 = \begin{pmatrix} 1 \\ 1 \\ 3 \end{pmatrix} + t
#     \begin{pmatrix} 0 \\ 2 \\ 4 \end{pmatrix},
# \end{align*} 
# 
# therefore $\mathbf{d}_1 = (1, 4, 2)$ and $\mathbf{d}_2 = (0, 2, 4)$. Now we can calculate $\hat{\mathbf{n}}$
# 
# \begin{align*}
#     \mathbf{n} &= \mathbf{d}_1 \times \mathbf{d}_2
#     = \begin{vmatrix} 
#         \mathbf{i} & \mathbf{j} & \mathbf{k} \\
#         1 & 4 & 2 \\
#         0 & 2 & 4
#     \end{vmatrix} = 
#     \begin{pmatrix} 12 \\ -4 \\ 2 \end{pmatrix}, \\
#     |\mathbf{n}| &= \sqrt{12^2 + (-4)^2 + 2^2} = \sqrt{164} = 2\sqrt{41}, \\
#     \therefore \hat{\mathbf{n}} &= \frac{\mathbf{n}}{|\mathbf{n}|} = 
#     \begin{pmatrix} \frac{6}{\sqrt{41}} \\ -\frac{2}{\sqrt{41}} \\ \frac{1}{\sqrt{41}} \end{pmatrix} 
#     = \begin{pmatrix} \frac{6\sqrt{41}}{41} \\ -\frac{2\sqrt{41}}{41} \\ \frac{\sqrt{41}}{41} \end{pmatrix}.
# \end{align*}
# 
# Note that since $\mathbf{n}$ is non-zero, $\ell_1$ and $\ell_2$ are skew lines. Using equation {eq}`line-line-distance-equation`
# 
# \begin{align*}
#     d &= (P_2 - P_1) \cdot \hat{\mathbf{n}} \\
#     &= \left( \begin{pmatrix} 1 \\ 1 \\ 3 \end{pmatrix} -
#     \begin{pmatrix} 0 \\ 1 \\ 3 \end{pmatrix} \right) \cdot 
#     \begin{pmatrix} \frac{6\sqrt{41}}{41} \\ -\frac{2\sqrt{41}}{41} \\ \frac{\sqrt{41}}{41} \end{pmatrix} \\
#     &= \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \cdot 
#     \begin{pmatrix} \frac{6\sqrt{41}}{41} \\ -\frac{2\sqrt{41}}{41} \\ \frac{\sqrt{41}}{41} \end{pmatrix} \\
#     &= \frac{6 \sqrt{41}}{41}.
# \end{align*}
# :::
# ::::
