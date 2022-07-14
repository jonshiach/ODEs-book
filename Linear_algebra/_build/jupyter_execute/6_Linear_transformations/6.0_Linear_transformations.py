#!/usr/bin/env python
# coding: utf-8

# (linear-transformations-chapter)=
# # Linear Transformations
# 
# **Learning outcomes**
# 
# On successful completion of this chapters students will be able to:
# 
# - identify when a transformation is a [linear transformation](linear-transformation-definition);
# - determine the [transformation matrix](transformation-matrix-definition) that represents a linear transformation;
# - perform [composite linear transformation](composite-transformation-definition);
# - apply [rotation](rotation-in-R2-theorem), [reflection](reflection-theorem), [scaling](scaling-theorem) and [translation](translation-definition) transformations in $\mathbb{R}^2$ as well as their inverses;
# - use [homogeneous co-ordinates](homogeneous-coordinates-definition) to describe points in $\mathbb{R}^n$.
# 
# ---
# 
# ## Definition
# 
# :::{admonition} Definition: Linear transformation
# :class: note
# :name: linear-transformation-definition
# 
# If $V$ and $W$ are two vector spaces over the same field $F$ then by a **linear transformation** (or **linear mapping**) is a mapping $T: V \to W,$ such that the following conditions hold
# 
# - addition operation: for all $x,y \in V$, $T(x + y) = T(x) + T(y)$;
# - scalar multiplication: for all $x \in V$ and $\alpha \in F$, $T(\alpha x) = \alpha T(x)$.
# 
# The result of applying a linear transformation to an object is known as the **image**.
# :::
# 
# For example, let $V = \mathbb{R}^2$ and $W = \mathbb{R}^3$ then $T : V \to W$ defined by $T : (x, y) \mapsto (x, y, 0)$ is a linear transformation. Let $(x_1, y_1), (x_2, y_2) \in \mathbb{R}^2$ and $\alpha \in F$ then
# 
# \begin{align*}
#     T \left( \begin{pmatrix} x_1 \\ y_1 \end{pmatrix} + \begin{pmatrix} x_2 \\ y_2 \end{pmatrix} \right)
#     &= T\begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}
#     = \begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \\ 0 \end{pmatrix} \\
#     &= \begin{pmatrix} x_1 \\ y_1 \\ 0 \end{pmatrix} + \begin{pmatrix} x_2 \\ y_2 \\ 0 \end{pmatrix}
#     = T\begin{pmatrix} x_1 \\ y_1 \end{pmatrix} + T\begin{pmatrix} x_2 \\ y_2 \end{pmatrix}.
# \end{align*}
# 
# Similarly
# 
# \begin{align*}
#     T\left( \alpha \begin{pmatrix} x_1 \\ y_1 \end{pmatrix} \right)
#     &= T \begin{pmatrix} \alpha x_1 \\ \alpha y_1 \end{pmatrix} 
#     = \begin{pmatrix} \alpha x_1 \\ \alpha y_1 \\ 0 \end{pmatrix}
#     = \alpha \begin{pmatrix} x_1 \\ y_1 \\ 0 \end{pmatrix}
#     = \alpha T\begin{pmatrix} x_1 \\ y_1 \end{pmatrix}.
# \end{align*}
# 
# To show whether a transformation is a linear transformation can combine both conditions from the [definition of a linear transformation](linear-transformation-definition) to show that
# 
# :::{math}
# :label: linear-transformation-condition-equation
# T(x + \alpha y) = T(x) + \alpha T(y).
# :::
# 
# ::::{admonition} Example 6.1
# :class: seealso
# :name: linear-transformation-example
# 
# Determine which of the following transformations are linear transformations
# 
# (a) &emsp; $T: \mathbb{R}^3 \to \mathbb{R}^2$ defined by $T: (x, y, z) \mapsto (x, y)$
# 
# :::{dropdown} Solution
# Let $(x_1, y_1, z_1), (x_2, y_2, z_2) \in \mathbb{R}^3$ and $\alpha \in F$ then
# 
# \begin{align*}
#     &T \left( \begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} + \alpha \begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix}
#     \right) \\
#     &= T \begin{pmatrix} x_1 + \alpha x_2 \\ y_1 + \alpha y_2 \\ z_1 + \alpha z_2 \end{pmatrix} \\
#     &= \begin{pmatrix} x_1 + \alpha x_2 \\  y_1 + \alpha y_2 \end{pmatrix} \\
#     &= \begin{pmatrix} x_1 \\ y_1 \end{pmatrix} + \alpha \begin{pmatrix}  x_2 \\ y_2 \end{pmatrix} \\
#     &= T\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} + \alpha T\begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix}.
# \end{align*}
# 
# So $T: (x, y, z) \mapsto (x, y)$ is a linear transformation.
# :::
# 
# (b) &emsp; $T: \mathbb{R}^3 \to \mathbb{R}^2$ defined by $T: (x, y, z) \mapsto (x + 3, y)$
# 
# :::{dropdown} Solution
# Let $(x_1, y_1, z_1)$, $(x_2, y_2, z_2) \in \mathbb{R}^3$ and $\alpha \in F$ then
# 
# \begin{align*}
#     T \left( \begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} + \alpha \begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix} \right)
#     &= T \begin{pmatrix} x_1 + \alpha x_2 \\ y_1 + \alpha y_2 \\ z_1 + \alpha z_2 \end{pmatrix} \\
#     &= \begin{pmatrix} x_1 + \alpha x_2 + 3 \\ y_1 + \alpha y_2 \end{pmatrix} \\
#     &= \begin{pmatrix} x_1 + 3 \\ y_1 \end{pmatrix} + \begin{pmatrix} \alpha x_2 \\ \alpha y_2 \end{pmatrix} \\
#     &\neq T\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} + \alpha T \begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix}.
# \end{align*}
# 
# So $T: (x, y, z) \mapsto (x + 3, y)$ is not a linear transformation. Note that we could have shown this by a counterexample, e.g., let $(1, 0, 0), (2, 0, 0) \in \mathbb{R}^3$ then by the first condition the [definition of a linear transformation](linear-transformation-definition)
# 
# \begin{align*}
#     T\left( \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 2 \\ 0 \\ 0 \end{pmatrix} \right)
#     &= T\begin{pmatrix} 3 \\ 0 \\ 0 \end{pmatrix} 
#     = \begin{pmatrix} 6 \\ 0 \end{pmatrix}, \\
#     T \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + T \begin{pmatrix} 2 \\ 0 \\ 0 \end{pmatrix}
#     &= \begin{pmatrix} 4 \\ 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 5 \\ 0 \\ 0 \end{pmatrix}
#     = \begin{pmatrix} 9 \\ 0 \end{pmatrix}.
# \end{align*}
# :::
# 
# (c) &emsp; $T: P(\mathbb{R}) \to P(\mathbb{R})$ defined by $T: f(x) \mapsto f(x) \dfrac{\mathrm{d}}{\mathrm{d}x} f(x)$
# 
# :::{dropdown} Solution
# 
# Let $x^2 \in P(\mathbb{R})$ and $2 \in F$ then 
# 
# \begin{align*}
#     T(2x^2) = 2x^2(4x) = 8x^3 \neq 2T(x^2) = 2(x^2)(2x) = 4x^3,
# \end{align*}
# 
# so $T: f(x) \mapsto f(x) \dfrac{\mathrm{d}}{\mathrm{d}x} f(x)$ is not a linear transformation.
# :::
# ::::
# 
# 
# (transformation-matrix-section)=
# ## Transformation matrices
# 
# For convenience we tend to use matrices to represent linear transformations. Let $T: V \to W$ be a linear transformation from the vector spaces $V$ to $W$. If $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$ is a basis for $V$ then for a vector $\mathbf{u} \in V$
# 
# \begin{align*}
#     \mathbf{u} = u_1 \mathbf{v}_1 + u_2 \mathbf{v}_2 + \cdots + u_n \mathbf{v}_n,
# \end{align*}
# 
# and by the [definition of a linear transformation](linear-transformation-definition)
# 
# \begin{align*}
#     T(\mathbf{u}) = u_1 T(\mathbf{v}_1) + u_2 T(\mathbf{v}_2) + \cdots + u_n T(\mathbf{v}_n),
# \end{align*}
# 
# so $T(\mathbf{u})$ depends on the vectors $T(\mathbf{v}_1)$ and $T(\mathbf{v}_2)$. We can write this as the matrix equation
# 
# \begin{align*}
#     T(\mathbf{u}) &= \begin{pmatrix} 
#         \uparrow & \uparrow & & \uparrow \\
#         T(\mathbf{v}_1) & T(\mathbf{v}_2) & \cdots & T(\mathbf{v}_n) \\
#         \downarrow & \downarrow & & \downarrow
#     \end{pmatrix}
#     \begin{pmatrix} u_1 \\ u_2 \\ \vdots \\ u_n \end{pmatrix} \\
#     &= A \mathbf{u}.
# \end{align*}
# 
# i.e., we can apply a linear transformation in $\mathbb{R}^n$ by multiplying a vector $\mathbf{u}$ by a matrix $A$.
# 
# 
# :::{admonition} Definition: Transformation matrix
# :class: note
# :name: transformation-matrix-definition
# 
# Let $T : V \to W$ be a linear transformation and $A$ be a matrix such that
# 
# \begin{align*}
#     A = \begin{pmatrix} 
#         \uparrow & \uparrow & & \uparrow \\
#         T(\mathbf{v}_1) & T(\mathbf{v}_2) & \cdots & T(\mathbf{v}_n) \\
#         \downarrow & \downarrow & & \downarrow
#     \end{pmatrix}
# \end{align*}
# 
# then 
# 
# \begin{align*}
#     T(\mathbf{u}) = A\mathbf{u}.
# \end{align*}
# 
# $A$ is said to be the **matrix representation of the linear transformation** $T$ (also known as the **transformation matrix**).
# :::
# 
# ::::{admonition} Example 6.2
# :class: seealso
# :name: transformation-matrix-example
# 
# A linear transformation $T:\mathbb{R}^2 \to \mathbb{R}^2$ is defined by $T: (x, y) \mapsto (3x + y, x + 2y)$. Calculate the transformation matrix and use it to calculate $T(1, 1)$.
# 
# :::{dropdown} Solution
# 
# Since we are mapping from $\mathbb{R}^2$ the transformation matrix is
# 
# \begin{align*}
#     A &= \begin{pmatrix} T(\mathbf{e}_1) & T(\mathbf{e}_2) \end{pmatrix}
# \end{align*}
# 
# Applying the transformation to the standard basis vectors
# 
# \begin{align*}
#     T(\mathbf{e}_1) = T\begin{pmatrix} 1 \\ 0 \end{pmatrix} 
#     = \begin{pmatrix} 3(1) + 0 \\ 1 + 2(0) \end{pmatrix} 
#     =  \begin{pmatrix} 3 \\ 1 \end{pmatrix}, \\
#     T(\mathbf{e}_2) = T\begin{pmatrix} 0 \\ 1 \end{pmatrix} 
#     = \begin{pmatrix} 3(0) + 1 \\ 0 + 2(1) \end{pmatrix} 
#     = \begin{pmatrix} 1 \\ 2 \end{pmatrix},
# \end{align*}
# 
# so the transformation matrix is
# \begin{align*}
#     A &= \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}.
# \end{align*}
# 
# Applying the transformation matrix to $(1, 1)$
# \begin{align*}
#     T\begin{pmatrix} 1 \\ 1 \end{pmatrix} = A \cdot \begin{pmatrix} 1 \\ 1 \end{pmatrix} =  
#     \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix} 
#     \begin{pmatrix} 1 \\ 1 \end{pmatrix} = 
#     \begin{pmatrix} 4 \\ 3 \end{pmatrix}.
# \end{align*}
# 
# :::
# ::::
# 
# The affects of the linear transformation from [example 6.2](linear-transformation-example) is illustrated in {numref}`linear-transformation-figure`. Note that the transformation $T$ can be thought of as changing the basis of the vector space. The unit square with respect to the basis $\{\mathbf{e}_1, \mathbf{e}_1\}$ has been transformed into a unit parallelogram with respect to the basis $\{ T(\mathbf{e}_1), T(\mathbf{e}_2)\}$.
# 
# :::{figure} ../Images/linear_transformation.png
# :name: linear-transformation-figure
# 
# The affect of applying a linear transformation $T: (x,y) \mapsto (3x + y, x + 2y)$ to the vector $(1,1)$.
# :::
# 
# ## Finding the transformation matrix from a set of images
# 
# The calculation of the transformation matrix in [example 6.2](transformation-matrix-example) was straightforward as we knew what the transformation was. This will not always be a the case and we may know what the output (known as the image) of the transformation is but not the transformation itself. Consider a linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$ applied to vectors $u_1, u_2, \ldots, u_n$. If $A$ is the transformation matrix for $T$ then
# 
# \begin{align*}
#     A
#     \begin{pmatrix}
#         \uparrow & \uparrow & & \uparrow \\
#         \mathbf{u}_1 & \mathbf{u}_2 & \cdots & \mathbf{u}_n \\
#         \downarrow & \downarrow & & \downarrow
#     \end{pmatrix} = 
#     \begin{pmatrix}
#         \uparrow & \uparrow & & \uparrow \\
#         T(\mathbf{u}_1) & T(\mathbf{u}_2) & \cdots & T(\mathbf{u}_n) \\
#         \downarrow & \downarrow & & \downarrow
#     \end{pmatrix}
# \end{align*}
# 
# therefore
# 
# \begin{align*}
#     A &=  
#     \begin{pmatrix}
#         \uparrow & \uparrow & & \uparrow \\
#         T(\mathbf{u}_1) & T(\mathbf{u}_2) & \cdots & T(\mathbf{u}_n) \\
#         \downarrow & \downarrow & & \downarrow
#     \end{pmatrix}
#     \begin{pmatrix}
#         \uparrow & \uparrow & & \uparrow \\
#         \mathbf{u}_1 & \mathbf{u}_2 & \cdots & \mathbf{u}_n \\
#         \downarrow & \downarrow & & \downarrow
#     \end{pmatrix}^{-1}
# \end{align*}
# 
# ::::{admonition} Theorem: Determining the linear transformation given the inputs and image vectors
# :class: important
# :name: finding-transformation-matrix-theorem
# 
# Given a linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$ applied to a set of $n$ vectors $\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_n$ with known image vectors $T(\mathbf{u}_1), T(\mathbf{u}_2), \ldots, T(\mathbf{u}_n)$ then the transformation matrix $A$ for $T$ is 
# 
# :::{math}
# :label: determining-the-transformation-matrix
# 
# A = (T(\mathbf{u}_1), T(\mathbf{u}_2), \ldots, T(\mathbf{u}_n)) \cdot (\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_n)^{-1}.
# :::
# ::::
# 
# ::::{admonition} Example 6.3
# :class: seealso
# :name: transformation-matrix-example-2
# 
# Determine the transformation matrix $A$ for the linear transformation $T$ such that
# 
# \begin{align*}
#     T\begin{pmatrix} 1 \\ 1 \end{pmatrix} &= \begin{pmatrix} 4 \\ 3 \end{pmatrix}, &
#     T\begin{pmatrix} 1 \\ 2 \end{pmatrix} &= \begin{pmatrix} 5 \\ 5 \end{pmatrix}.
# \end{align*}
# 
# :::{dropdown} Solution
# 
# Using Gauss-Jordan elimination to determine the inverse of $(\mathbf{u}_1, \mathbf{u}_2)$
# 
# \begin{align*}
#     & \left( \begin{array}{rr|rr} 
#         1 & 1 & 1 & 0 \\
#         1 & 2 & 0 & 1
#     \end{array} \right)
#     \begin{array}{l} \\ R_2 - R_1 \end{array}  \\ \\ 
#     \longrightarrow \quad &
#     \left( \begin{array}{rr|rr} 
#         1 & 1 & 1 & 0 \\
#         0 & 1 & -1 & 1
#     \end{array} \right)
#     \begin{array}{l} R_1 - R_2 \\ \phantom{x} \end{array}  \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{rr|rr} 
#         1 & 0 & 2 & -1 \\
#         0 & 1 & -1 & 1
#     \end{array} \right)
# \end{align*}
# 
# so $(\mathbf{u}_1, \mathbf{u}_2)^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}$. Right multiplying the image matrix
# 
# \begin{align*}
#     A &= \begin{pmatrix} 4 & 5 \\ 3 & 5 \end{pmatrix} \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}
#     = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}.
# \end{align*}
# 
# This is the transformation matrix from [example 6.2](transformation-matrix-example).
# 
# ::::
# 
# ## Inverse linear transformation
# 
# ::::{admonition} Definition: Inverse linear transformation
# :class: note
# :name: inverse-transformation-definition
# 
# Let $T: V \to W$ be a linear transformation with the transformation matrix $A$ then $T$ has an inverse transformation denoted by $T^{-1}: W \to V$ which reverses the affects of $T$. If $\mathbf{u} \in V$ and $\mathbf{v} \in W$ then 
# 
# \begin{align*}
#     \mathbf{v} &= A \mathbf{u} \\
#     \therefore \mathbf{u} & = A^{-1}\mathbf{v},
# \end{align*}
# 
# where $A^{-1}$ is the transformation matrix for $T^{-1}$.
# ::::
# 
# ::::{admonition} Example 6.4
# :class: seealso
# :name: inverse-transformation-example
#     
# Determine the inverse of the transformation $T: \mathbb{R}^2 \to \mathbb{R}^2$ defined by $T(x, y) \mapsto (3 x + y, x + 2 y)$ and calculate $T^{-1}(4, 3)$.
# 
# :::{dropdown} Solution
# We saw in [example 6.2](transformation-matrix-example) that the transformation matrix for $T$ is
# 
# \begin{align*}
#     A = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix},
# \end{align*}
# 
# which has the inverse
# 
# \begin{align*}
#     A^{-1} = \begin{pmatrix} \frac{2}{5} & -\frac{1}{5} \\ -\frac{1}{5} & \frac{3}{5} \end{pmatrix}.
# \end{align*}
# 
# Determining the inverse transformation
# 
# \begin{align*}
#     T^{-1}\begin{pmatrix} x \\ y \end{pmatrix} &= A^{-1} \cdot \begin{pmatrix} x \\ y \end{pmatrix} =
#     \begin{pmatrix} \frac{2}{5} & -\frac{1}{5} \\ -\frac{1}{5} & \frac{3}{5} \end{pmatrix}
#     \begin{pmatrix} x \\ y \end{pmatrix} \\
#     &= \begin{pmatrix} \frac{2}{5}x - \frac{1}{5}y \\ -\frac{1}{5}x + \frac{3}{5}y \end{pmatrix}.
# \end{align*}
# 
# Calculating $T^{-1}(4, 3)$
# 
# \begin{align*}
#     A^{-1} \begin{pmatrix} 4 \\ 3 \end{pmatrix} &=
#     \begin{pmatrix} \frac{2}{5} & -\frac{1}{5} \\ -\frac{1}{5} & \frac{3}{5} \end{pmatrix}
#     \begin{pmatrix} 4 \\ 3 \end{pmatrix} 
#     = \begin{pmatrix} 1 \\ 1 \end{pmatrix}.
# \end{align*}
# :::
# ::::
