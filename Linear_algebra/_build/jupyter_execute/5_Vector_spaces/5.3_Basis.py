#!/usr/bin/env python
# coding: utf-8

# (basis-section)=
# # Basis
# 
# ## Spanning sets
# 
# ::::{admonition} Definition: Spanning set
# :class: note
# :name: spanning-set-definition
# 
# Let $V$ be a vector space over the field $F$ and $S$ is a subset of $V$. Let $W$ be a subset of $V$ that are expressible as a linear combination of vectors in $S$, i.e., for $\mathbf{u} \in W$, $\mathbf{v}_1, \ldots, \mathbf{v}_n \in S$ and $\alpha_1, \ldots, \alpha_n \in F$
# 
# \begin{align*}
#     \mathbf{u} = \alpha_1 \mathbf{v}_1 + \alpha_2 \mathbf{v}_2 + \cdots + \alpha_n \mathbf{v}_n.
# \end{align*}
# then $W$ is a subspace of $V$ and $S$ is a **spanning set** for $W$. We write this as $\operatorname{span}(S)$.
# ::::
# 
# For example, $\mathbb{C} = \operatorname{span}(\{1, i\})$ over $\mathbb{R}$ since every element of $\mathbb{C}$ can be expressed as a linear combination of 1 and $i$.
# 
# ::::{admonition} Example 5.6
# :class: seealso
# :name: spanning-set-example
# 
# (i) &emsp; Show that  $\{ \mathbf{v}_1, \mathbf{v}_2 \}$ where $\mathbf{v}_1 = (2, 1)$ and $\mathbf{v}_2 = (4, 3)$ is a spanning set for $\mathbb{R}^2$.
# 
# 
# :::{dropdown} Solution
# 
# We need to show that $\alpha_1 \mathbf{v}_1 + \alpha_2 \mathbf{v}_2 = (a, b)$ for any $a, b \in \mathbb{R}$, i.e., so that the following system has a non-trivial solution.
# 
# \begin{align*}
#     2 \alpha_1 + 4 \alpha_2 &= a, \\
#     \alpha_1 + 3 \alpha_2 &= b. 
# \end{align*}
# 
# A system of linear equations has a solution if it is [non-singular](inverse-matrix-definition) (the determinant of the coefficient matrix is non-zero), therefore
# 
# \begin{align*}
#     \det \begin{pmatrix} 2 & 4 \\ 1 & 3 \end{pmatrix} = 2 \neq 0, 
# \end{align*}
# 
# so $\{\mathbf{v}_1, \mathbf{v}_2\}$ is a spanning set for $\mathbb{R}^2$.
# :::
# 
# (ii) &emsp; Determine a spanning set for $\mathbb{R}^3$.
# 
# :::{dropdown} Solution
# 
# Lets suggest $\{ (1, 0, 0), (0, 1, 0), (0, 0, 1) \}$ as a spanning set for $\mathbb{R}^3$
# \begin{align*}
#     (x, y, z) &= \{ \alpha_1 (1, 0, 0) + \alpha_2 (0, 1, 0) + \alpha_3(0, 0, 1) : \alpha_1, \alpha_2, \alpha_3 \in \mathbb{R}\} \\
#     &= \{ \alpha_1 \mathbf{i} + \alpha_2 \mathbf{j} + \alpha_3 \mathbf{k} : \alpha_1, \alpha_2, \alpha_3 \in \mathbb{R} \},
# \end{align*}
# 
# therefore $\{ \mathbf{i}, \mathbf{j}, \mathbf{k} \}$ is a spanning set for $\mathbb{R}^3$. Note that this is just one of many examples of spanning sets for $\mathbb{R}^3$.
# :::
# 
# ::::
# 
# The vectors $\mathbf{i}$, $\mathbf{j}$ and $\mathbf{j}$ were introduced in [basis vectors](basis-vectors-section). This leads to the definition of a basis of a vector space.
# 
# ## Basis of a vector space
# 
# ::::{admonition} Definition: Basis of a vector space
# :class: note
# :name: basis-definition
#     
# A **basis** of a vector space $V$ of a field $F$ is a linearly independent subset of $V$ that spans $V$. A subset $W$ is a basis if it satisfies the following
# 
# - [linear independence property](linear-dependence-definition): for every subset $\{\mathbf{v}_1, \ldots , \mathbf{v}_n\}$ of $W$ the following equation only has the trivial soluion $\alpha_i = 0$.
# 
# \begin{align*}
#     \alpha_1 \mathbf{v}_1 + \alpha_2 \mathbf{v}_2 + \cdots + \alpha_n \mathbf{v}_n &= \mathbf{0};
# \end{align*}
# 
# - [spanning property](spanning-set-definition): for all $\mathbf{u} \in V$ we can write $\mathbf{u}$ as a linear combination of $\mathbf{v} \in W$, i.e.,
# 
# \begin{align*}
#     \mathbf{u} = \alpha_1 \mathbf{v}_1 + \alpha_2 \mathbf{v}_2 + \cdots + \alpha_n \mathbf{v}_n.
# \end{align*}
# ::::
# 
# :::{admonition} Definition: Orthogonal basis
# :class: note
# :name: orthogonal-basis-definition
# 
# An **orthogonal basis** of a vector space is one in which each of the vectors are orthogonal (perpendicular) to one another.
# :::
# 
# :::{admonition} Definition: Orthonormal basis
# :class: note
# :name: orthonormal-basis-definition
# 
# An **orthonormal basis** of a vector space is one in which each of the vectors are orthogonal to one another and each vector is a unit vector.
# :::
# 
# :::{admonition} Definition: Dimension of a vector space
# :class: note
# :name: vector-space-dimension-definition
# 
# The **dimension** of a vector space $V$ is denoted by $\dim(V)$ and is the number of elements in the basis for the vector space. 
# :::
# 
# ::::{admonition} Example 5.7
# :class: seealso
# :name: basis-example
# 
# Show that the vectors $\mathbf{v}_1 = (1, 1, 0)$, $\mathbf{v}_2 = (1, -1, 1)$ and $\mathbf{v}_3 = (1, -1, -2)$ is a basis for $\mathbb{R}^3$.
# 
# :::{dropdown} Solution
# 
# We need to show that the three vectors are linearly independent, i.e., show that the only solution to the following system is $\alpha_1 = \alpha_2 = \alpha_3 = 0$
# 
# \begin{align*}
#     \alpha_1 \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} +
#     \alpha_2 \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} +
#     \alpha_3 \begin{pmatrix} 1 \\ -1 \\ -2 \end{pmatrix}  = 
#     \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}.
# \end{align*}
# 
# Using Gauss-Jordan elimination
# 
# \begin{align*}
#     & \left( \begin{array}{ccc|c}
#         1 & 1 & 1 & 0 \\
#         1 & -1 & 1 & 0\\
#         1 & -1 & -2 & 0
#     \end{array} \right)
#     \begin{matrix} \\ R_2 - R_1 \\ R_3 - R_1 \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 1 & 1 & 0 \\
#         0 & -2 & 0 & 0\\
#         0 & -2 & -3 & 0
#     \end{array} \right)
#     \begin{matrix} \\ -\frac{1}{2}R_2 \\ \phantom{x} \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 1 & 1 & 0 \\
#         0 & 1 & 0 & 0\\
#         0 & -2 & -3 & 0
#     \end{array} \right)
#     \begin{matrix} R_1 - R_2 \\ \\ R_3 + 2R_2 \end{matrix}  \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & 1 & 0 \\
#         0 & 1 & 0 & 0\\
#         0 & 0 & -3 & 0
#     \end{array} \right)
#     \begin{matrix} \\ \phantom{x} \\ -\frac{1}{3}R_3 \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & 1 & 0 \\
#         0 & 1 & 0 & 0\\
#         0 & 0 & 1 & 0
#     \end{array} \right)
#     \begin{matrix} R_1 - R_3 \\ \phantom{x} \\ \phantom{x} \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & 0 & 0 \\
#         0 & 1 & 0 & 0\\
#         0 & 0 & 1 & 0
#     \end{array} \right)
# \end{align*}
# So $\mathbf{v}_1$, $\mathbf{v}_2$ and $\mathbf{v}_3$ are linearly independent. We also need to show that $\{ \mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3 \}$ spans $\mathbb{R}^3$. 
# \begin{align*}
#     \det \begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & -1 \\ 0 & 1 & -2 \end{pmatrix} = 3 + 3 = 6 \neq 0,
# \end{align*}
# so $\{ \mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3 \}$ is a spanning set for $\mathbb{R}^3$. Note that in showing that $\mathbf{v}_1$, $\mathbf{v}_2$ and $\mathbf{v}_3$ are linearly independent we have also shown that $\alpha_1 \mathbf{v}_1 + \alpha_2 \mathbf{v}_2 + \alpha_3 \mathbf{v}_3 = (a, b, c)$ has a solution and $\{ \mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3 \}$ is a spanning set. Futhermore 
# \begin{align*}
#     \mathbf{v}_1 \cdot \mathbf{v}_2 &= \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} \cdot
#     \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} = 0, \\
#     \mathbf{v}_1 \cdot \mathbf{v}_3 &= \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} \cdot
#     \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix} = 0, \\
#     \mathbf{v}_2 \cdot \mathbf{v}_3 &= \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} \cdot
#     \begin{pmatrix} 1 \\ -1 \\ -2 \end{pmatrix} = 0,
# \end{align*}
# so $\{ \mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3 \}$ is an orthogonal basis. It is not an orthonormal basis since $|\mathbf{v}_1| = \sqrt{2} \neq 1$.
# :::
# ::::
# 
# (change-of-basis-section)=
# ## Change of basis
# 
# $\mathbb{R}^n$ has a particularly nice basis that is easy to write down
# 
# \begin{align*}
#     E = \left\{ 
#         \mathbf{e}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix}, 
#         \mathbf{e}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}, \ldots,
#         \mathbf{e}_n = \begin{pmatrix} 0 \\ 0 \\ 0 \\ \vdots \\ 1 \end{pmatrix} 
#         \right\},
# \end{align*}
# 
# which is called the **standard basis**. Note that for $\mathbb{R}^3$ we have $\mathbf{i} = \mathbf{e}_1$, $\mathbf{j} = \mathbf{e}_2$ and $\mathbf{k} = \mathbf{e}_3$ and $\mathbf{e}_i$ is column $i$ of the identity matrix.
# 
# We can represent a vector $\mathbf{u} = (u_1, u_2, \ldots, u_n) \in \mathbb{R}^n$ in the standard basis as a vector with respect to another basis $W = \{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$ which is denoted using $[\mathbf{u}]_W$. Using the standard basis we have
# 
# \begin{align*}
#     \mathbf{u} &= u_1 \mathbf{e}_1 + u_2 \mathbf{e}_2 + \cdots + u_n \mathbf{e}_n = (u_1, u_2, \ldots, u_n),
# \end{align*}
# 
# and to express $\mathbf{u}$ with respect to the basis $W$ we need to solve 
# 
# \begin{align*}
#     [\mathbf{u}]_W &= w_1 \mathbf{v}_1 + w_2 \mathbf{v}_2 + \cdots + w_n \mathbf{v}_n = (w_1, w_2, \ldots, w_n),
# \end{align*}
# 
# for $w_1, w_2, \ldots, w_n$. This concept is illustrated for $\mathbb{R}^2$ in {numref}`change-of-basis-figure`.
# 
# :::{figure} ../Images/change_of_basis.png
# :name: change-of-basis-figure
# 
# The vector $(u_1, u_2)$ in $\mathbb{R}^2$ expressed with respect to the basis $E = \{\mathbf{e}_1, \mathbf{e}_2 \}$ and $W = \{\mathbf{v}_1, \mathbf{v}_2\}$.
# :::
# 
# ::::{admonition} Example 5.8
# :class: seealso
# :name: change-of-basis-example
# 
# Represent the vector $\mathbf{u} = (4, 0, 5)$ with respect to the basis $W = \{(1, 1, 0), (1, -1, 1), (1, -1, -2)\}$.
# 
# :::{dropdown} Solution
# 
# We need to solve the system
# 
# \begin{align*}
#     w_1 \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + 
#     w_2 \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} +
#     w_3 \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix} =
#     \begin{pmatrix} 4 \\ 0 \\ 5 \end{pmatrix},
# \end{align*}
# 
# which can be written as the matrix equation
# 
# \begin{align*}
#     \begin{pmatrix}
#         1 & 1 & 1 \\
#         1 & -1 & -1 \\
#         0 & 1 & 2 
#     \end{pmatrix}
#     \begin{pmatrix} w_1 \\ w_2 \\ w_3 \end{pmatrix} =
#     \begin{pmatrix} 4 \\ 0 \\ 5 \end{pmatrix},
# \end{align*}
# 
# where $[\mathbf{u}]_w = (w_1, w_2, w_3)$. Calculating the inverse of the coefficient matrix
# 
# \begin{align*}
#     \begin{pmatrix} 
#         1 & 1 & 1 \\
#         1 & -1 & -1 \\
#         0 & 1 & -2 
#     \end{pmatrix}^{-1} &=
#     \frac{1}{6}
#     \begin{pmatrix}
#         3 & 2 & 1 \\
#         3 & -2 & -1 \\
#         0 & 2 & -2
#     \end{pmatrix}^\mathrm{T} \\
#     &= \frac{1}{6} 
#     \begin{pmatrix}
#         3 & 3 & 0 \\
#         2 & -2 & 2 \\
#         1 & -1 & -2
#     \end{pmatrix} \\
#     &=
#     \begin{pmatrix} 
#         \frac{1}{2} & \frac{1}{2} & 0 \\
#         \frac{1}{3} & -\frac{1}{3} & \frac{1}{3} \\
#         \frac{1}{6} & -\frac{1}{6} & -\frac{1}{3}
#     \end{pmatrix},
# \end{align*}
# 
# so
# 
# \begin{align*}
#     [\mathbf{u}]_W = 
#     \begin{pmatrix} 
#         \frac{1}{2} & \frac{1}{2} & 0 \\
#         \frac{1}{3} & -\frac{1}{3} & \frac{1}{3} \\
#         \frac{1}{6} & -\frac{1}{6} & -\frac{1}{3}
#     \end{pmatrix}
#     \begin{pmatrix} 4 \\ 0 \\ 5 \end{pmatrix} =
#     \begin{pmatrix} 2 \\ 3 \\ -1 \end{pmatrix}.
# \end{align*}
# 
# ::::
# 
# Note that in [example 5.8](change-of-basis-example) we can represent any vector $\mathbf{u}$ with respect to the basis $W$ by multiplying by the square matrix in the final equation. This matrix is known as the [**change of basis matrix**](https://en.wikipedia.org/wiki/Change_of_basis).
# 
# ::::{admonition} Definition: Change of basis matrix
# :class: note
# :name: change-of-basis-matrix-definition
# 
# Let $V$ be a vector space over the field $F$ and $\mathbf{u} \in V$. If $E$ and $W$ are two basis for $V$ then the change of basis matrix is the matrix $A_{E \to W}$ such that $[u]_{W} = A_{E \to W} [u]_E$.
# ::::
# 
# So to express the vector $\mathbf{u}$ to the basis $W$ we simply multiply $\mathbf{u}$ by the change of basis matrix. Changing from a non-standard basis is a slightly more complicated procedure and will be covered in the more advanced materials on linear algebra.
