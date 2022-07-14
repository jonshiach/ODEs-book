#!/usr/bin/env python
# coding: utf-8

# (planes-section)=
# # Planes
# 
# A **plane** is a flat two-dimensional surface. The vector equation for a plane in $\mathbb{R}^n$ is very similar to that of a line. We just need two direction vectors instead of just the one we needed for a line.
# 
# ::::{admonition} Definition: Vector equation of a plane
# :class: note
# :name: plane-vector-equation
# 
# Let $P = (p_1, \ldots ,p_n)$ be a point in $\mathbb{R}^n$ and $\mathbf{d}_1,\mathbf{d}_2$ are two non-zero vectors in $\mathbb{R}^n$ which are not parallel. The plane $p$, which passes through $P$ in the directions of $\mathbf{d}_1$ and $\mathbf{d}_2$ has the equation
# 
# $$ Q = P + t_1 \mathbf{d}_1 + t_2 \mathbf{d}_2, $$
# 
# where $Q$ is a general point on $p$ and $t_1,t_2 \in \mathbb{R}$ are parameter ({numref}`plane-1-figure`). 
# ::::
# 
# :::{figure} ../Images/plane_1.png
# :name: plane-1-figure
# 
# The position of a point $Q$ on the plane $p$ can be obtained by adding scalar multiples of the direction vectors $\mathbf{d}_1$ and $\mathbf{d}_2$ to $P$.
# :::
# 
# In other words, every point on $p$ is obtained by adding some scalar multiples of $\mathbf{d}_1$ and $\mathbf{d}_2$ to $P$. So $p$ is indeed the plane which passes through $P$ in the directions of $\mathbf{d}_1$ and $\mathbf{d}_2$. We call the vectors $\mathbf{d}_1,\mathbf{d}_2$ **direction vectors** of the plane. Note we needed $\mathbf{d}_1$ and $\mathbf{d}_2$ not to be parallel else we would have only described a line again.
# 
# ::::{admonition} Definition: The normal vector
# :class: note
# :name: normal-vector-definition
# 
# The **normal vector** to a plane is a vector that is perpendicular to that plane. If $\mathbf{a}$ and $\mathbf{b}$ are two vectors that lie on a plane then the normal vector is calculated using $\mathbf{n} = \mathbf{a} \times \mathbf{b}$. 
# 
# :::{figure} ../Images/plane_2.png
# :name: plane-2-figure
# 
# The normal vector $\mathbf{n}$ is perpendicular to the plane $p$.
# :::
# 
# ::::
# 
# Recall that [the dot product](dot-product-definition) between two perpendicular vectors is zero. So if a plane is defined by the normal vector $\mathbf{n}$ and a point $P=(x_0, y_0, z_0)$ which lies on the plane and if $Q=(x,y,z)$ is another point the plane then
# 
# \begin{align*}
#     \mathbf{n} \cdot \overrightarrow{PQ} &= 0 \\
#     \mathbf{n} \cdot (Q - P) &= 0 \\
#     \mathbf{n} \cdot \left( 
#     \begin{pmatrix} x \\ y \\ z \end{pmatrix} -
#     \begin{pmatrix} x_0 \\ y_0 \\ z_0 \end{pmatrix} \right) &= 0 \\
#     \mathbf{n} \cdot \begin{pmatrix} x - x_0 \\ y - y_0 \\ z - z_0 \end{pmatrix} &= 0.
# \end{align*}
# 
# This is known as the point normal definition for a plane.
# 
# :::{figure} ../Images/plane_3.png
# :name: point-normal-figure
# 
# The point normal definition of a plane.
# :::
# 
# ::::{admonition} Definition: Point normal equation of a plane
# :class: note
# :name: point-normal-definition
# 
# The plane in $\mathbb{R}^3$ which passes through the point with co-ordinates $(x_0, y_0, z_0)$ with normal vector $\mathbf{n}$ can be defined by
# 
# :::{math}
# :label: point-normal-equation
# 
# \mathbf{n} \cdot \begin{pmatrix} x - x_0 \\ y - y_0 \\ z - z_0 \end{pmatrix} &= 0,
# :::
# 
# which is known as the **point normal** definition of a plane.
# ::::
# 
# :::::{admonition} Example 4.6
# :class: seealso
# 
# A plane $p$ in $\mathbb{R}^3$ passes the three points $P_1 = (1, 0, 0)$, $P_2 = (1, 0, -1)$ and $P_3 = (2, 1, 3)$
# 
# (i) &emsp; Find the point normal definition of the plane;
# 
# (ii) &emsp; Do the points $P_4 = (2, 3, 1)$ and $P_5 = (3, 2, 4)$ lie on $p$?
# 
# ::::{dropdown} Solution
# 
# (i) &emsp; First we need to calculate the normal vector to the plane. We can do this by calculating the cross product of any two vectors that line on the plane, since we know $P_1$, $P_2$ and $P_3$ lie on the plane then so must the vectors $\overrightarrow{P_1P_2}$ and $\overrightarrow{P_2P_3}$ (or any other combination of these points)
# 
# \begin{align*}
#     \overrightarrow{P_1P_2} &= P_2 - P_1 = 
#     \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} - 
#     \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} =
#     \begin{pmatrix} 0 \\ 0 \\ -1 \end{pmatrix}, \\
#     \overrightarrow{P_2P_3} &= P_3 - P_2 =
#     \begin{pmatrix} 2 \\ 1 \\ 3 \end{pmatrix} -
#     \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} =
#     \begin{pmatrix} 1 \\ 1 \\ 4 \end{pmatrix}, \\
#     \therefore \mathbf{n} &= \overrightarrow{P_1P_2} \times \overrightarrow{P_2P_3} =
#     \begin{pmatrix} 0 \\ 0 \\ -1 \end{pmatrix} \times
#     \begin{pmatrix} 1 \\ 1 \\ 4 \end{pmatrix} =
#     \begin{vmatrix} 
#         \mathbf{i} & \mathbf{j} & \mathbf{k} \\
#         0 & 0 & -1 \\
#         1 & 1 & 4
#     \end{vmatrix} = 
#     \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}.
# \end{align*}
# 
# Using equation {eq}`point-normal-equation` with $P = P_1$ (note we could have used any of $P_1$, $P_2$ or $P_3$ but I chose $P_1$ since it has the simplest co-ordinates)
# 
# \begin{align*}
#     \mathbf{n} \cdot \begin{pmatrix} x - x_0 \\ y - y_0 \\ z - z_0 \end{pmatrix} &= 0 \\
#     \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} \cdot
#     \begin{pmatrix} x - 1 \\ y - 0 \\ z - 0 \end{pmatrix} &= 0 \\
#     \therefore x - y - 1 &= 0.
# \end{align*}
# 
# If we had chosen $P = P_2$ instead
# 
# \begin{align*}
#     \mathbf{n} \cdot \begin{pmatrix} x - x_0 \\ y - y_0 \\ z - z_0 \end{pmatrix} &= 0 \\
#     \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} \cdot
#     \begin{pmatrix} x - 1 \\ y - 0 \\ z - (-1) \end{pmatrix} &= 0 \\
#     \therefore x - y - 1 &= 0,
# \end{align*}
# 
# which was the same answer as before.
# 
# (ii) &emsp; Checking $P_4$
# \begin{align*}
#     x - y - 1 = 2 - 3 - 1 = -2 \neq 0,
# \end{align*}
# so $P_4$ does not lie on $p$.
# 
# Checking $P_5$
# \begin{align*}
#     x - y - 1 = 3 - 2 - 1 = 0,
# \end{align*}
# so $P_5$ does lie on $p$.
# 
# ::::
# :::::
# 
# (intersection-of-planes-section)=
# ## Intersection of planes in $\mathbb{R}^3$
# 
# We distinguish between various arrangements of planes, which are defined in terms of their normal vectors. We saw that a plane $p$ is perpendicular to a normal vector $\mathbf{n}$. Now, any plane that can be described using $\mathbf{n}$ as a direction vector will be described as a **plane perpendicular to $p$**. This is equivalent to the two normal vectors being perpendicular. In a similar way if two distinct planes $p$ and $r$ have the same normal vector then they are **parallel**.
# 
# Often we would like to know when (and how) two or more objects in $\mathbb{R}^n$ meet. Similar to the lines in $\mathbb{R}^2$ we present a finite list of arrangements for three planes meeting in $\mathbb{R}^3$.
# 
# :::::{grid}
# :gutter: 2
# 
# ::::{grid-item-card} 
# :columns: 4
# 
# :::{figure} ../Images/intersecting_planes_1.png
# :::
# 3 planes intersect at a single point: a unique solution
# ::::
# 
# ::::{grid-item-card} 
# :columns: 4
# 
# :::{figure} ../Images/intersecting_planes_2.png
# :::
# 3 planes intersect on a single line: infinite solutions
# ::::
# 
# ::::{grid-item-card} 
# :columns: 4
# 
# :::{figure} ../Images/intersecting_planes_3.png
# :::
# 2 planes coincide and intersect a third: infinite solutions
# ::::
# 
# ::::{grid-item-card} 
# :columns: 4
# 
# :::{figure} ../Images/intersecting_planes_4.png
# :::
# 2 parallel planes intersect another: no solutions
# ::::
# 
# ::::{grid-item-card} 
# :columns: 4
# 
# :::{figure} ../Images/intersecting_planes_5.png
# :::
# each plane intersects with 2 others: no solutions
# ::::
# 
# ::::{grid-item-card} 
# :columns: 4
# 
# :::{figure} ../Images/intersecting_planes_6.png
# :::
# 3 parallel planes: no solutions
# ::::
# 
# ::::{grid-item-card} 
# :columns: 4
# 
# :::{figure} ../Images/intersecting_planes_7.png
# :::
# 2 coincident planes parallel to another: no solutions
# ::::
# 
# ::::{grid-item-card} 
# :columns: 4
# 
# <br>
# 
# :::{figure} ../Images/intersecting_planes_8.png
# :::
# <br>
# all 3 planes coincide: infinite solutions
# ::::
# 
# :::::
# 
# 
# It is possible to classify such arrangements for higher dimensions - but it makes more sense to do it purely algebraically. That is precisely what linear algebra is useful for.
# 
# ::::{admonition} Example 4.7
# :class: seealso
# :name: intersecting-planes-example
# 
# Two non-parallel planes in $\mathbb{R}^3$ are given by $p:3x-4y+z-5 = 0$ and $r:x+ y - z -2 = 0$ respectively. Find the intersection of these two planes
# 
# :::{dropdown} Solution
# 
# The normal vectors for these planes is given by the coefficients of $x$, $y$ and $z$, therefore $\mathbf{n}_p = (3, -4, 1)$ and $\mathbf{n}_r = (1, 1, -1)$ for planes $p$ and $r$ respectively. The direction vector of the line of intersection must be parallel to both $\mathbf{n}_p$ and $\mathbf{n}_r$ (the line must lie in both planes), therefore we need to construct a vector perpendicular to both of these. A vector perpendicular to $\mathbf{n}_p$ and $\mathbf{n}_r$ can be found using $\mathbf{n}_p \times \mathbf{n}_r$
# 
# \begin{align*}
#     \mathbf{d} = \mathbf{n}_p \times \mathbf{n}_r =
#     \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 3 & -4 & 1 \\ 1 & 1 & -1 \end{vmatrix} =
#     \begin{pmatrix} 3 \\ 4 \\ 7 \end{pmatrix}.
# \end{align*}
# 
# In addition to the direction vector we need a point on $\ell$ which must lie on both planes so we need to find a solution that satisfies
# 
# \begin{align*}
#     3x - 4y + z &= 5, \\
#     x + y - z &= 2
# \end{align*}
# 
# Adding these two equations gives
# 
# \begin{align*}
#     3x - 4y + z + x + y -z &= 7 \\
#     4x - 3y &= 7\\ 
#     \therefore y &= \frac{4x - 7}{3}.
# \end{align*}
# 
# Let $x = 1$ then $y = -1$ and $z = -2$ so the line of intersection between the two planes is
# 
# \begin{align*}
#     Q = \begin{pmatrix} 1 \\ -1 \\ -2 \end{pmatrix} + t
#     \begin{pmatrix} 3 \\ 4 \\ 7 \end{pmatrix} = 
#     \begin{pmatrix} 1 + 3t \\ -1 + 4t \\ -2 + 7t \end{pmatrix}.
# \end{align*}
# 
# ::::
