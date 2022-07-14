#!/usr/bin/env python
# coding: utf-8

# (translation-section)=
# # Translation
# 
# In the [previous section](rotation-reflection-and-scaling-section) we looked at how to rotate, reflect and scale a vector. To complete the movement of vectors in $\mathbb{R}^2$ we need to be able to **translate** vectors. 
# 
# ::::{admonition} Definition: Translation
# :class: note
# :name: translation-definition
# 
# The translation of a position vector $\mathbf{u} \in \mathbb{R}^n$ by a translation vector $\mathbf{t} \in \mathbb{R}^n$ is the linear transformation $T(\mathbf{t}): \mathbf{u} \mapsto \mathbf{u} + \mathbf{t}$.
# 
# :::{figure} ../Images/translation.png
# :name: translation-figure
# 
# The translation of the vector $\mathbf{u}$ by the vector $\mathbf{t}$ in $\mathbb{R}^2$.
# :::
# 
# ::::
# 
# The problem we have here is what is the matrix representation of translation, i.e., in $\mathbb{R}^2$ what is the matrix $T$ that satisfies
# 
# \begin{align*}
#     T(\mathbf{t}) \cdot \begin{pmatrix} u_1 \\ u_2 \end{pmatrix}  = \begin{pmatrix} u_1 + t_1 \\ u_2 + t_2 \end{pmatrix}.
# \end{align*}
# 
# A matrix $T(\mathbf{t})$ does not exist which is independent of $u_1$ and $u_2$ so we can use a trick which makes use of **homogeneous co-ordinates**.
# 
# :::{admonition} Definition: Homogeneous co-ordinates
# :class: note
# :name: homogeneous-coordinates-definition
# 
# The homogeneous co-ordinates of a point $\mathbf{u}$ in $\mathbb{R}^n$ expressed using the Cartesian co-ordinates is the $(n+1)$-tuple $(\lambda u_1, \lambda u_2, \ldots, \lambda u_n, \lambda)$ where $\lambda \in \mathbb{R}\backslash \{0\}$. 
# 
# Note that a point with homogeneous co-ordinates $(u_1, u_2, \ldots, u_n, \lambda)$ has the Cartesian co-ordinates $\left(\dfrac{u_1}{\lambda}, \dfrac{u_2}{\lambda}, \ldots, \dfrac{u_n}{\lambda}\right)$.
# :::
# 
# If we express a point in $\mathbb{R}^n$ with Cartesian co-ordinates $(u_1, u_2, \ldots, u_n)$ using the homogeneous co-ordinates $(u_1, u_2, \ldots, u_n, 1)$ then we can find a $(n+1) \times (n+1)$ translation matrix $T(\mathbf{t})$ that satisfies
# 
# \begin{align*}
#     T(t_1, t_2, \ldots, t_n) \cdot \begin{pmatrix} u_1 \\ u_2 \\ \vdots \\ u_n \\ 1 \end{pmatrix} = 
#     \begin{pmatrix} u_1 + t_1 \\ u_1 + t_2 \\ \vdots \\ u_n + t_n \\ 1 \end{pmatrix}.
# \end{align*}
# 
# The transformation matrix for translating by the vector $\mathbf{t}$ is
# \begin{align*}
#     T(t_1, t_2, \ldots, t_n) = \begin{pmatrix} 
#         & & & t_1 \\
#         & I_n & & \vdots \\
#         & & & t_n \\
#         0 & \cdots & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# The inverse translation is to translate by $-\mathbf{t}$, therefore
# \begin{align*}
#     T^{-1}(t_1, t_2, \ldots, t_n) = \begin{pmatrix} 
#         & & & -t_1 \\
#         & I_n & & \vdots \\
#         & & & -t_n \\
#         0 & \cdots & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# :::::{admonition} Example 6.10
# :class: seealso
# :name: translation-example
# 
# Translate the point with position vector $\mathbf{u} = (1, 2)$ by the vector $\mathbf{t} = (3, 1)$.
# 
# ::::{dropdown} Solution
# 
# Expressing $\mathbf{u} = (1, 2)$ using homogeneous co-ordinates we have $\mathbf{u} = (1, 2, 1)$. The translation matrix is
# 
# \begin{align*}
#     T(3, 1) = 
#     \begin{pmatrix}
#         1 & 0 & 3 \\
#         0 & 1 & 1 \\
#         0 & 0 & 1 
#     \end{pmatrix}.
# \end{align*}
# 
# Applying the transformation to $\mathbf{u}$
# \begin{align*}
#     T(3, 1)\begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} = 
#     \begin{pmatrix}
#         1 & 0 & 3 \\
#         0 & 1 & 1 \\
#         0 & 0 & 1 
#     \end{pmatrix}
#     \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} =
#     \begin{pmatrix} 4 \\ 3 \\ 1 \end{pmatrix},
# \end{align*}
# 
# so expressed in Cartesian co-ordinates we have $T(3, 1)(\mathbf{u}) = (4, 3)$.
# 
# :::{figure} ../Images/translation_example.png
# :::
# 
# ::::
# :::::
# 
# ## Combining rotation, reflection, scaling and translation
# 
# If we want to combine translation with rotation, reflection and scaling transformations in $\mathbb{R}^2$ then we need all of the transformation matrices to be the same size. This is easily done by adding the third row and column of the identity matrix to $Rot(\theta)$, $Ref(\theta)$ and $S(\mathbf{s})$ , i.e.,
# 
# \begin{align*}
#     Rot(\theta) &= \begin{pmatrix}
#         \cos(\theta) & \sin(\theta) & 0 \\
#         -\sin(\theta) & \cos(\theta) & 0 \\
#         0 & 0 & 1
#     \end{pmatrix}, \\
#     Ref(\theta) &= \begin{pmatrix}
#         \cos(2\theta) & \sin(2\theta) & 0 \\
#         \sin(2\theta) & -cos(2\theta) & 0 \\
#         0 & 0 & 1
#     \end{pmatrix}, \\
#     S(\mathbf{s}) &= \begin{pmatrix}
#         s_1 & 0 & 0 \\
#         0 & s_2 & 0 \\
#         0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# :::::{admonition} Example 6.11
# :class: seealso
# :name: rotation-scaling-and-translating-example
# 
# An isosceles triangle has the vertices with co-ordinates $(-1, -1)$, $(1, -1)$ and $(0, 2)$. The triangle is transformed using the following transformations:
# 
# - Scaled by a factor of 2 in both directions
# - Rotated by $\frac{\pi}{4}$ anti-clockwise about the origin
# - Translated by the vector $\mathbf{t} = (6, 4)$
# 
# Calculate the co-ordinates of the triangle after each of these transformations has been applied and determine a transformation matrix that performs all three transformations at the same time.
# 
# ::::{dropdown} Solution
# The homogeneous vertex co-ordinates are $(-1, -1, 1)$, $(1, -1, 1)$ and $(0, 2, 1)$ and can be written as the following matrix
# 
# \begin{align*}
#     P = \begin{pmatrix} x_1 & x_2 & x_3 \\ y_1 & y_2 & y_3 \\ 1 & 1 & 1 \end{pmatrix} = 
#     \begin{pmatrix} -1 & 1 & 0 \\ -1 & -1 & 2 \\ 1 & 1 & 1 \end{pmatrix}.
# \end{align*}
# 
# Since we are scaling by a factor of 2 in both directions then the scaling vector is $\mathbf{s} = (2, 2)$ so the scaling matrix is
# 
# \begin{align*}
#     S(2, 2) = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix}.
# \end{align*}
# 
# Applying the scaling matrix to the homogeneous co-ordinates 
# 
# \begin{align*}
#     P_1 &= S(2,2) \cdot P \\
#     &= \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix} 
#     \begin{pmatrix} -1 & 1 & 0 \\ -1 & -1 & 2 \\ 1 & 1 & 1 \end{pmatrix}\\
#     &= \begin{pmatrix} -2 & 2 & 0 \\ -2 & -2 & 4 \\ 1 & 1 & 1 \end{pmatrix}.
# \end{align*}
# 
# :::{figure} ../Images/homogeneous_coordinates_example_1.png
# :width: 300
# :::
# 
# We want to rotate by an angle of $\frac{\pi}{4}$ so the rotation matrix is
# 
# \begin{align*}
#     Rot\left( \frac{\pi}{4} \right) &= 
#     \begin{pmatrix} 
#         \cos(\frac{\pi}{4}) & -\sin(\frac{\pi}{4}) & 0 \\
#         \sin(\frac{\pi}{4}) & \cos(\frac{\pi}{4}) & 0 \\
#         0 & 0 & 1
#     \end{pmatrix}
#     = \begin{pmatrix} 
#         \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} & 0 \\
#         \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} & 0 \\
#         0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# Applying the rotating matrix to $P_1$ 
# 
# \begin{align*}
#     P_2 &= Rot(\tfrac{\pi}{4}) \cdot P_1  \\
#     &= \begin{pmatrix} 
#         \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} & 0 \\
#         \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} & 0 \\
#         0 & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix} -2 & 2 & 0 \\ -2 & -2 & 4 \\ 1 & 1 & 1 \end{pmatrix} \\
#     &= \begin{pmatrix}
#         0 & 2 \sqrt{2} & -2\sqrt{2} \\
#         -2\sqrt{2} & 0 & 2\sqrt{2} \\
#         1 & 1 & 1
#     \end{pmatrix} \\
#     &\approx \begin{pmatrix} 
#         0 & 2.8482 & -2.8482 \\
#         -2.8482 & 0 & 2.8482 \\
#         1 & 1 & 1 
#     \end{pmatrix}.
# \end{align*}
# 
# :::{figure} ../Images/homogeneous_coordinates_example_2.png
# :width: 300
# :::
# 
# Finally we need to translate by the translation vector $\mathbf{t} = (6, 4)$ so the translation matrix is
# 
# \begin{align*}
#     T(6, 4) &= \begin{pmatrix} 1 & 0 & 6 \\ 0 & 1 & 4 \\ 0 & 0 & 1 \end{pmatrix}.
# \end{align*}
# 
# Applying the translation matrix to $P_2$
# 
# \begin{align*}
#     P_3 &= T(6, 4) \cdot P_2 \\
#     &= \begin{pmatrix} 1 & 0 & 6 \\ 0 & 1 & 4 \\ 0 & 0 & 1 \end{pmatrix}
#     \begin{pmatrix}
#         0 & 2 \sqrt{2} & -2\sqrt{2} \\
#         -2\sqrt{2} & 0 & 2\sqrt{2} \\
#         1 & 1 & 1
#     \end{pmatrix} \\
#     &= \begin{pmatrix}
#         6 & 6 + 2\sqrt{2} & 6 - 2\sqrt{2} \\
#         4 - 2\sqrt{2} & 4 & 4 + 2\sqrt{2} \\
#         1 & 1 & 1
#     \end{pmatrix} \\
#     &\approx \begin{pmatrix}
#         6 & 8.8284 & 3.1716 \\
#         1.1716 & 4 & 6.8284 \\
#         1 & 1 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# :::{figure} ../Images/homogeneous_coordinates_example_3.png
# :width: 500
# :::
# 
# The single transformation matrix that performs the three transformations at the same time is
# 
# \begin{align*}
#     A &= T(6, 4) \cdot Rot(\tfrac{\pi}{4}) \cdot S(2,2) \\
#     &= \begin{pmatrix}
#         0 & 2 \sqrt{2} & -2\sqrt{2} \\
#         -2\sqrt{2} & 0 & 2\sqrt{2} \\
#         1 & 1 & 1
#     \end{pmatrix}
#     \begin{pmatrix} 
#         \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} & 0 \\
#         \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} & 0 \\
#         0 & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix} \\
#     &= \begin{pmatrix} 
#         \sqrt{2} & -\sqrt{2} & 6 \\
#         \sqrt{2} & \sqrt{2} & 4 \\
#         0 & 0 & 1 
#     \end{pmatrix} \\
#     &\approx
#     \begin{pmatrix}
#         1.4142 & -1.4142 & 6 \\
#         1.4142 & 1.4142 & 4 \\
#         0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# Checking $A$:
# 
# \begin{align*}
#     A P &= \begin{pmatrix} 
#         \sqrt{2} & -\sqrt{2} & 6 \\
#         \sqrt{2} & \sqrt{2} & 4 \\
#         0 & 0 & 1 
#     \end{pmatrix}
#     \begin{pmatrix} 
#         -1 & 1 & 0 \\ 
#         -1 & -1 & 2 \\ 
#         1 & 1 & 1 
#     \end{pmatrix} \\
#     &= \begin{pmatrix}
#         6 & 6 + 2\sqrt{2} & 6 - 2\sqrt{2} \\
#         4 - 2\sqrt{2} & 4 & 4 + 2\sqrt{2} \\
#         1 & 1 & 1 
#     \end{pmatrix} \quad \checkmark
# \end{align*}
# 
# ::::
# 
# :::::
