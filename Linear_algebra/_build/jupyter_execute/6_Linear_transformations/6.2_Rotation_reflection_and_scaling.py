#!/usr/bin/env python
# coding: utf-8

# (rotation-reflection-and-scaling-section)=
# # Rotation, reflection and scaling
# 
# (rotation-section)=
# ## Rotation
# 
# ::::{admonition} Definition: Rotation transformation
# :class: note
# :name: rotation-definition
# 
# The linear transformation $\operatorname{Rot}(\theta): \mathbb{R}^2 \to \mathbb{R}^2$ applied to the vector $\mathbf{u}$ rotates $\mathbf{u}$ by an angle $\theta$ *anti-clockwise* about the origin.
# 
# :::{figure} ../Images/rotation.png
# :name: rotation-figure
# 
# Rotation of the vector $\mathbf{u}$ anti-clockwise about the origin.
# :::
# ::::
# 
# 
# Consider the diagram in {numref}`rotation-figure`. To determine the linear mapping $\operatorname{Rot}(\theta): \mathbf{u} \mapsto \mathbf{v}$ we first consider the values of $\mathbf{u} = (x, y)$ as the vector which points along the $x$-axis with the same magnitude as $\mathbf{u}$ rotated by an angle $\phi$ anti-clockwise about the origin. Forming a right-angled triangle with the angle $\phi$ and hypotenuse of length $|\mathbf{u}|$ then
# 
# :::{math}
# :label: rotation-equation-1
# 
# \begin{align*}
#     \cos(\phi) &= \frac{x}{|\mathbf{u}|} & \therefore x &= |\mathbf{u}| \cos(\phi), \\
#     \sin(\phi) &= \frac{y}{|\mathbf{u}|} & \therefore y &= |\mathbf{u}| \sin(\phi).
# \end{align*}
# :::
# 
# Doing similar for $\mathbf{v} = (v_x, v_y)$ we have
# 
# \begin{align*}
#     v_x &= |\mathbf{u}| \cos(\phi + \theta), \\
#     v_y &= |\mathbf{u}| \sin(\phi + \theta),
# \end{align*}
# 
# using the [angle sum indentities](https://en.wikipedia.org/wiki/List_of_trigonometric_identities#Angle_sum_and_difference_identities)
# 
# \begin{align*}
#     \cos(\phi + \theta) &= \cos(\phi) \cos(\theta) - \sin(\phi) \sin(\theta), \\
#     \sin(\phi + \theta) &= \sin(\phi) \cos(\theta) + \cos(\phi) \sin(\theta),
# \end{align*}
# 
# then we have
# 
# :::{math}
# :label: rotation-equation-2
# 
# \begin{align*}
#     v_x &= |\mathbf{u}| \cos(\phi) \cos(\theta) - |\mathbf{u}|\sin(\phi) \sin(\theta) \\
#     v_y &= |\mathbf{u}| \sin(\phi) \cos(\theta) + |\mathbf{u}|\cos(\phi) \sin(\theta).
# \end{align*}
# :::
# 
# Substituting equation {eq}`rotation-equation-1` into equation {eq}`rotation-equation-2` 
# 
# \begin{align*}
#     v_x &= x \cos(\theta) - y \sin(\theta), \\
#     v_y &= y \cos(\theta) + x \sin(\theta).
# \end{align*}
# 
# Therefore the rotation matrix is
# 
# \begin{align*}
#     \operatorname{Rot}(\theta)\mathbf{u} = \begin{pmatrix} 
#         x \cos(\theta) - y \sin(\theta) \\ 
#         x \sin(\theta) + y \cos(\theta)
#     \end{pmatrix}
# \end{align*}
# 
# ::::{admonition} Theorem: Rotation in $\mathbb{R}^2$
# :class: important
# :name: rotation-in-R2-theorem
# 
# The rotation of a vector $\mathbf{u} \in \mathbb{R}^2$ **anti-clockwise** by an angle $\theta$ is the linear transformation $\operatorname{Rot}(\theta): \mathbb{R}^2 \to \mathbb{R}^2$ defined by
# 
# \begin{align*}
#     \operatorname{Rot}(\theta) \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \mapsto 
#     \begin{pmatrix} u_1 \cos(\theta) - u_2 \sin(\theta) \\ u_1 \sin(\theta) + u_2 \cos(\theta) \end{pmatrix}.
# \end{align*}
# 
# The transformation matrix for rotation in $\mathbb{R}^2$ is
# 
# :::{math}
# :label: rotation-matrix-equation
# 
# \begin{align*}
#     \operatorname{Rot}(\theta) = \begin{pmatrix} 
#         \cos(\theta) & -\sin(\theta) \\
#         \sin(\theta) & \cos(\theta)
#     \end{pmatrix}.
# \end{align*}
# :::
# 
# ::::
# 
# ### Inverse rotation transformation
# 
# The inverse transformation of rotating a vector anti-clockwise by an angle $\theta$ is rotating **clockwise** by the same angle. This can be achieved by negating $\theta$, since $\cos(-\theta) = \cos(\theta)$ and $\sin(-\theta) = -\sin(\theta)$ then
# 
# \begin{align*}
#     \operatorname{Rot}(\theta)^{-1} &= \begin{pmatrix}
#         \cos(-\theta) & -\sin(-\theta) \\
#         \sin(-\theta) & \cos(-\theta)
#    \end{pmatrix} 
#    = \begin{pmatrix}
#        \cos(\theta) & \sin(\theta) \\
#        -\sin(\theta) & \cos(\theta)
#    \end{pmatrix}.
# \end{align*}
# 
# We could have also calculated the inverse of the rotation matrix to give the same result
# 
# \begin{align*}
#     \operatorname{Rot}(\theta)^{-1} &= \frac{\operatorname{adj}(\operatorname{Rot}(\theta))}{\det(\operatorname{Rot}(\theta))} \\
#     &= \frac{1}{\cos^2(\theta) + \sin^2(\theta)}
#     \begin{pmatrix}
#         \cos(\theta) & -\sin(\theta) \\
#         \sin(\theta) & \cos(\theta)
#     \end{pmatrix}^\mathrm{T} \\
#     &= \begin{pmatrix}
#         \cos(\theta) & \sin(\theta) \\
#         -\sin(\theta) & \cos(\theta)
#     \end{pmatrix}.
# \end{align*}
# 
# :::::{admonition} Example 6.7
# :class: seealso
# :name: rotation-example
# 
# Rotate the vector $\mathbf{u} = (2, 1)$ by angle $\theta = \frac{\pi}{2}$ anti-clockwise about the origin.
# 
# ::::{dropdown} Solution
# 
# The transformation matrix for this rotation is
# 
# \begin{align*}
#     \operatorname{Rot} \left( \frac{\pi}{2} \right) &= 
#     \begin{pmatrix}
#         \cos(\frac{\pi}{2}) & -\sin(\frac{\pi}{2}) \\
#         \sin(\frac{\pi}{2}) & \cos(\frac{\pi}{2})
#     \end{pmatrix}
#     = \begin{pmatrix}
#         0 & -1 \\ 
#         1 & 0
#     \end{pmatrix}.
# \end{align*}
# 
# Applying the transformation to $\mathbf{u} = (2, 1)$
# 
# \begin{align*}
#     \operatorname{Rot}\left( \frac{\pi}{2} \right) (\mathbf{u}) &= 
#     \begin{pmatrix}
#         0 & -1 \\ 
#         1 & 0
#     \end{pmatrix}
#     \begin{pmatrix} 2 \\ 1 \end{pmatrix}
#     = \begin{pmatrix} -1 \\ 2 \end{pmatrix}.
# \end{align*}
# 
# This rotation is illustrated in the diagram below
# 
# :::{figure} ../Images/rotation-example.png
# :::
# 
# ::::
# :::::
# 
# (reflection-section)=
# ## Reflection
# 
# ::::{admonition} Definition: Reflection about a line
# :class: note
# :name: reflection-definition
# 
# The linear transformation $\operatorname{Ref}(\theta): \mathbb{R}^2 \to \mathbb{R^2}$ is the reflection of a vector $\mathbf{u} \in \mathbf{R}^2$ about the line which passes through the origin and makes an angle of $\theta$ with the $x$-axis such that the distance of the head of the image vector $\mathbf{v}$ is the same as that of $\mathbf{u}$. 
# 
# :::{figure} ../Images/reflection.png
# :name: reflection-figure
# 
# The reflection of the vector $\mathbf{u}$ about a line.
# :::
# ::::
# 
# The simplest reflection we can perform is to reflect a vector $\mathbf{u} =(x, y)$ about the $x$-axis or $y$-axis. For example, to reflect about the $x$-axis we simply change the sign of the $y$ co-ordinate ({numref}`reflection-about-x-figure`), i.e.,
# 
# $$\operatorname{Ref}(0) \begin{pmatrix} x \\ y \end{pmatrix} &= \begin{pmatrix} x \\ -y \end{pmatrix},$$
# 
# and the transformation matrix is
# 
# :::{math}
# :label: reflection-about-x-equation
# 
# \operatorname{Ref}(0) = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.
# :::
# 
# Note that here the line of reflection makes an angle of $\theta=0$ with the $x$-axis.
# 
# :::{figure} ../Images/reflection_about_x.png
# :scale: 75%
# :name: reflection-about-x-figure
# 
# Reflection of the vector $\mathbf{u}$ about the $x$ axis.
# :::
# 
# The determine the reflection about a line that makes and arbitrary angle $\theta$ with the $x$-axis we first perform a rotation by $-\theta$ so that the line of reflection is on the $x$-axis ({numref}`reflection-about-line-1-figure`). This means we can then use equation {eq}`reflection-about-x-equation` to reflect the rotated $\mathbf{u}$ vector to give the vector $\mathbf{v}$ ({numref}`reflection-about-line-2-figure`) before rotating by $\theta$ so that the line of reflection is back to its original position ({numref}`reflection-about-line-3-figure`).
# 
# :::::{grid}
# 
# ::::{grid-item}
# :::{figure} ../Images/reflection_about_line_1.png
# :name: reflection-about-line-1-figure
# 
# Rotate by $-\theta$.
# :::
# ::::
# 
# ::::{grid-item}
# :::{figure} ../Images/reflection_about_line_2.png
# :name: reflection-about-line-2-figure
# 
# Reflect about the $x$-axis.
# :::
# ::::
# 
# 
# ::::{grid-item}
# :::{figure} ../Images/reflection_about_line_3.png
# :name: reflection-about-line-3-figure
# 
# Rotate by $\theta$.
# :::
# ::::
# 
# :::::
# 
# Using composite transformations we can calculate the transformation matrix for reflection about a line
# 
# \begin{align*}
#     \operatorname{Ref}(\theta) &= \operatorname{Rot}(\theta) \cdot \operatorname{Ref}(0) \cdot \operatorname{Rot}(-\theta),
# \end{align*}
# 
# therefore
# 
# \begin{align*}
#     \operatorname{Ref}(\theta) &= 
#     \begin{pmatrix} \cos(\theta) & -\sin(\theta) \\ \sin(\theta) & \cos(\theta) \end{pmatrix}
#     \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} 
#     \begin{pmatrix} \cos(\theta) & \sin(\theta) \\ -\sin(\theta) & \cos(\theta) \end{pmatrix} \\
#     &= \begin{pmatrix} 
#         \cos^2(\theta) - \sin^2(\theta) & 2\cos(\theta)\sin(\theta) \\
#         2\cos(\theta)\sin(\theta) & \sin^2(\theta) - \cos^2(\theta)
#     \end{pmatrix}.
# \end{align*}
# 
# Using [double angle formulae](https://en.wikipedia.org/wiki/List_of_trigonometric_identities#Double-angle_formulae) 
# 
# \begin{align*}
#     \cos(2\theta) &= \cos^2(\theta) - \sin^2(\theta), \\
#     \sin(2\theta) &= 2\cos(\theta) \sin(\theta), 
# \end{align*}
# 
# then
# 
# \begin{align*}
#     \operatorname{Ref}(\theta) &= 
#     \begin{pmatrix} 
#         \cos(2\theta) & \sin(2\theta) \\
#         \sin(2\theta) & -\cos(2\theta)
#     \end{pmatrix}.
# \end{align*}
# 
# ::::{admonition} Theorem: Reflection in $\mathbb{R}^2$
# :class: important
# :name: reflection-theorem
# 
# The reflection of a vector $\mathbf{u} \in \mathbb{R}^2$ about a line which passes through the origin and makes an angle $\theta$ with the $x$-axis (i.e., $y = \tan(\theta)x$) is the linear transformation $Ref(\theta) : \mathbb{R}^2 \to \mathbb{R}^2$ defined by 
# 
# \begin{align*}
#     Ref(\theta) : \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \mapsto 
#     \begin{pmatrix} u_1 \cos (2\theta) + u_2 \sin(2 \theta) \\ u_1 \sin(2\theta) - u_2 \cos (2\theta) \end{pmatrix}.
# \end{align*}
# 
# The transformation matrix for reflection in $\mathbb{R}^2$ is 
# 
# :::{math}
# :label: reflection-matrix-equation
# \begin{align*}
#     \operatorname{Ref}(\theta) = 
#     \begin{pmatrix} 
#         \cos(2\theta) & \sin(2 \theta) \\ 
#         \sin(2\theta) & -\cos(2\theta) 
#     \end{pmatrix}.
# \end{align*}
# :::
# 
# ::::
# 
# ### Inverse reflection transformation
# 
# The inverse of reflecting about a line is to simply perform the reflection again, i.e.,
# 
# $$\operatorname{Ref}^{-1}(\theta) = \operatorname{Ref}(\theta).$$
# 
# :::::{admonition} Example 6.8
# :class: seealso
# :name: reflection-example
# 
# Reflect the vector $\mathbf{u} = (3, -1)$ about the line that passes through the origin and has gradient of 1. 
# 
# ::::{dropdown} Solution
# 
# Since the line of reflection has gradient 1 then $\theta = \tan^{-1}(1) = \frac{\pi}{4}$ and the reflection matrix is
# \begin{align*}
#     \operatorname{Ref} \left( \frac{\pi}{4} \right) = \begin{pmatrix}
#         \cos(\frac{\pi}{2}) & \sin(\frac{\pi}{2}) \\
#         \sin(\frac{\pi}{2}) & -\cos(\frac{\pi}{2})
#     \end{pmatrix} =
#     \begin{pmatrix}
#         0 & 1 \\
#         1 & 0
#     \end{pmatrix}.
# \end{align*}
# Applying the transformation to $\mathbf{u} = (3, -1)$
# \begin{align*}
#     \operatorname{Ref}\left(\frac{\pi}{4}\right) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
#     \begin{pmatrix} 3 \\ -1 \end{pmatrix} =
#     \begin{pmatrix} -1 \\ 3 \end{pmatrix}.
# \end{align*}
# 
# :::{figure} ../Images/reflection-example.png
# :::
# 
# ::::
# :::::
# 
# (scaling-section)=
# ## Scaling
# 
# 
# ::::{admonition} Definition: Scaling transformation
# :class: note
# :name: scaling-definition
# 
# The linear transformation $\operatorname{S}(\mathbf{s}) : \mathbf{R}^n \to \mathbf{R}^n$ where $\mathbf{s} \in \mathbb{R}^n$ applied to the position vector $\mathbf{u} \in \mathbb{R}^n$ scales $\mathbf{u}$ so that the head is moved closer or further away from the origin.
# 
# :::{figure} ../Images/scaling.png
# :name: scaling-figure
# 
# The scaling of the vector $\mathbf{u}$ by the scaling vector $\mathbf{s}$.
# :::
# ::::
# 
# 
# The scaling of a vector $\mathbf{u} = (u_1, u_2, \ldots, u_n) \in \mathbb{R}^n$ by a scaling vector $\mathbf{s} = (v_1, v_2, \ldots, v_n)$ is achieved simply by multiplying the corresponding elements in $\mathbf{u}$ and $\mathbf{s}$.
# 
# ::::{admonition} Theorem: Scaling transformation
# :class: important
# :name: scaling-theorem
# 
# The scaling of a vector $\mathbf{u} \in \mathbb{R}^n$ by the scaling vector $\mathbf{s}$ is the linear transformation $\operatorname{S}(\mathbf{s}): \mathbf(u) \mapsto \mathbf{v}$ calculated using
# 
# \begin{align*}
#     \operatorname{S}(\mathbf{v}): \begin{pmatrix} u_1 \\ u_2 \\ \vdots \\ u_n \end{pmatrix} \mapsto 
#     \begin{pmatrix} s_1 u_1 \\ s_2 u_2 \\ \vdots \\ s_n u_n \end{pmatrix}.
# \end{align*}
# 
# The transformation matrix for scaling is
# 
# :::{math}
# :label: scaling-matrix-equation
# \begin{align*}
#     \operatorname{S}(\mathbf{s}) = 
#     \begin{pmatrix} 
#         s_1 & 0 & \cdots & 0 \\ 
#         0 & s_2 & \ddots & \vdots \\ 
#         \vdots & \ddots & \ddots & 0 \\
#         0 & \cdots & 0 & s_n
#         \end{pmatrix}.
# \end{align*}
# :::
# 
# ::::
# 
# ### Inverse scaling transformation
# 
# Since the inverse operation of scalar multiplication is scalar division then the inverse scaling matrix is 
# 
# \begin{align*}
#     \operatorname{S}^{-1}(\mathbf{v}) = 
#     \begin{pmatrix} 
#         \frac{1}{s_1} & 0 & \cdots & 0 \\ 
#         0 & \frac{1}{s_2} & \ddots & \vdots \\ 
#         \vdots & \ddots & \ddots & 0 \\
#         0 & \cdots & 0 & \frac{1}{s_n}
#         \end{pmatrix}.
# \end{align*}
# 
# :::::{admonition} Example 6.9
# :class: seealso
# :name: scaling-example
# 
# Scale the point with position vector $\mathbf{u} = (2,1)$ by scaling scaling vector $\mathbf{s} = (2, 3)$.
# 
# ::::{dropdown} Solution
# 
# The transformation matrix is 
# 
# \begin{align*}
#     \operatorname{S}(2, 3) = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}.
# \end{align*}
# 
# Applying the transformation to $\mathbf{u} = (2, 1)$
# 
# \begin{align*}
#     \operatorname{S}(\mathbf{u}) = \begin{pmatrix}
#         2 & 0 \\ 0 & 3
#     \end{pmatrix}
#     \begin{pmatrix} 2 \\ 1 \end{pmatrix}
#     = \begin{pmatrix} 4 \\ 3 \end{pmatrix}.
# \end{align*}
# 
# :::{figure} ../Images/scaling_example.png
# :::
# 
# ::::
# :::::
