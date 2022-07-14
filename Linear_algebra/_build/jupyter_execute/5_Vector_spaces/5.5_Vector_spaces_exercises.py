#!/usr/bin/env python
# coding: utf-8

# (vector-spaces-exercises-section)=
# # Vector spaces exercises
# 
# ::::{admonition} Exercise 5.1
# :class: note
# :name: ex5.1
# 
# Prove that the [axioms](vector-space-axioms-theorem) of the vector space $\mathbb{R}^3$ hold.
# 
# :::{dropdown} Solution
# Let $\mathbf{u}, \mathbf{v}, \mathbf{w} \in \mathbb{R}^3$ and $\alpha, \beta \in \mathbb{R}$ then 
# 
# - A1: $\mathbf{u} + (\mathbf{v} + \mathbf{w}) = (\mathbf{u} + \mathbf{v}) + \mathbf{w} \quad \checkmark$
# - A2: $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u} \quad \checkmark$
# - A3: $\mathbf{u} + \mathbf{0} = \mathbf{u} \quad \checkmark$
# - A4: $\mathbf{u} + (-\mathbf{u}) = \mathbf{0} \quad \checkmark$
# - M1: $\alpha(\beta \mathbf{u}) = (\alpha \beta) \mathbf{u} \quad \checkmark$
# - M2: $1 \mathbf{u} = \mathbf{u} \quad \checkmark$
# - M3: $\alpha(\mathbf{u} + \mathbf{v}) = \alpha\mathbf{u} + \alpha \mathbf{v} \quad \checkmark$
# - M4: $(\alpha + \beta) \mathbf{u} = \alpha \mathbf{u} + \beta \mathbf{u} \quad \checkmark$
# 
# All of the axioms of vector spaces hold for $\mathbb{R}^3$.
# :::
# ::::
# 
# ::::{admonition} Exercise 5.2
# :class: note
# :name: ex5.2
# 
# Using [the subspace condition](subspace-condition-theorem), determine whether the following subsets of $\mathbb{R}^3$ are subspaces:
# 
# 
# (a) &emsp; $U = \{ (x, y, 0) : x, y \in \mathbb{R} \}$
# 
# :::{dropdown} Solution
# $U$ is non-empty since $(0,0,0) \in U$. Let $\mathbf{u} = (x_1, y_1, 0), \mathbf{v} = (x_2, y_2, 0) \in U$ and $\alpha \in \mathbb{R}$ then
# 
# \begin{align*}
#     \mathbf{u} + \alpha \mathbf{v} = 
#     \begin{pmatrix} x_1 \\ y_1 \\ 0 \end{pmatrix} + \alpha 
#     \begin{pmatrix} x_2 \\ y_2 \\ 0 \end{pmatrix} = 
#     \begin{pmatrix} 
#         x_1 + \alpha x_2 \\ 
#         y_1 + \alpha y_2 \\ 
#         0 
#     \end{pmatrix} \in U,
# \end{align*}
# therefore $U$ is a subspace.
# :::
# 
# (b) &emsp; $V = \{ (1, 2, 0) \}$
# 
# :::{dropdown} Solution
# $V$ is non-empty since $(1,2,0) \in V$. However $\alpha (1, 2, 0) = (\alpha , 2\alpha , 0) \notin V$ for $\alpha \in \mathbb{R}$ so $V$ is not a subspace.
# :::
# 
# (c) &emsp; $W = \{ (0, y, 0) : y \in \mathbb{R} \}$
# 
# :::{dropdown} Solution
# $W$ is non-empty since $(0, 0, 0) \in W$. Let $\mathbf{u} = (0, y_1, 0), \mathbf{v} = (0, y_2, 0) \in U$ and $\alpha \in \mathbb{R}$ then
# 
# \begin{align*}
#     \mathbf{u} + \alpha \mathbf{v} = 
#     \begin{pmatrix} 0 \\ y_1 \\ 0 \end{pmatrix} + \alpha 
#     \begin{pmatrix} 0 \\ y_2 \\ 0 \end{pmatrix} = 
#     \begin{pmatrix} 0 \\ y_1 + \alpha y_2 \\ 0 \end{pmatrix} \in W,
# \end{align*}
# 
# therefore $W$ is a subspace. Note that $W \subseteq U$ so since we showed $U$ is a subspace then $W$ must also be a subspace.
# :::
# 
# (d) &emsp; $X = \{ (x, y, z) : y = |x|, x, y, z \in \mathbb{R}\}$
# 
# :::{dropdown} Solution
# $X$ is non a subspace since if $\mathbf{u} = (1, 1, 0), \mathbf{v} = (-1, 1, 0) \in X$ then $\mathbf{u} + \mathbf{v} = (0, 2, 0) \notin X$.
# :::
# 
# 
# ::::
# 
# ::::{admonition} Exercise 5.3
# :class: note
# :name: ex5.3
# 
# Which of the following sets are subspaces of $M_{2\times 2}$?
# 
# (a) &emsp; $A = \left\{ \begin{pmatrix} a & b \\ c & d \end{pmatrix} : a, b, c, d \in \mathbb{R}, a + b = 1,  \right\}$
# 
# :::{dropdown} Solution
# $A$ is non-empty since $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \in A$. Let $U = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \in A$ then 
# 
# \begin{align*}
#     2U = \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix} \notin A
# \end{align*}
# 
# so $A$ is not a subspace.
# :::
# 
# (b) &emsp; $B = \left\{ \begin{pmatrix} a & b \\ c & d \end{pmatrix}: a, b, c, d \in \mathbb{R}, a = c = d \right\}$
# 
# :::{dropdown} Solution
# $B$ is non-empty since $0_{2\times 2} \in B$. Let $U = \begin{pmatrix} x_1 & 0 \\ x_1 & x_1 \end{pmatrix}, V = \begin{pmatrix} x_2 & 0 \\ x_2 & x_2 \end{pmatrix} \in B$ and $\alpha \in \mathbb{R}$ then
# 
# \begin{align*}
#     U + \alpha V = 
#     \begin{pmatrix} x_1 & 0 \\ x_1 & x_1 \end{pmatrix} + \alpha
#     \begin{pmatrix} x_2 & 0 \\ x_2 & x_2 \end{pmatrix}
#     = \begin{pmatrix} x_1 + \alpha x_2 & 0 \\ x_1 + \alpha x_2 & x_1 + \alpha x_2 \end{pmatrix} \in B,
# \end{align*}
# 
# so $B$ is a subspace.
# :::
# 
# (c) &emsp; $C = \{ A \in M_{2\times 2} : A^2 = A \}$
# 
# :::{dropdown} Solution
# $C$ is not a subspace since $U = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \in C$ but $2U = \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix} \notin C$.
# :::
# ::::
# 
# ::::{admonition} Exercise 5.4
# :class: note
# :name: ex5.4
# 
# Prove that $\{ (1, 2, 0), (0, 5, 7), (-1, 1, 3) \}$ is a basis for $\mathbb{R}^3$ and find the co-ordinates of $(0, 13, 17)$ and $(2, 3, 1)$ relative to this basis.
# 
# :::{dropdown} Solution
# 
# We need to show that the vectors in the set are [linearly independent](linear-dependence-definition).
# 
# \begin{align*}
#     & \left( \begin{array}{ccc|c}
#         1 & 0 & -1 & 0 \\
#         2 & 5 & 1 & 0 \\
#         0 & 7 & 3 & 0
#     \end{array} \right)
#     \begin{matrix} \\ R_2 - \frac{1}{2}R_1 \\ \phantom{x} \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & -1 & 0 \\
#         0 & 5 & 3/2 & 0 \\
#         0 & 7 & 3 & 0
#     \end{array} \right)
#     \begin{matrix} \\ \frac{1}{5}R_2 \\ \phantom{x} \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & -1 & 0 \\
#         0 & 1 & 3/10 & 0 \\
#         0 & 7 & 3 & 0
#     \end{array} \right)
#     \begin{matrix} \\ \\ R_3 - 7R_2 \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & -1 & 0 \\
#         0 & 1 & 3/10 & 0 \\
#         0 & 0 & 9/10 & 0
#     \end{array} \right)
#     \begin{matrix} \\ \\ \frac{10}{9}R_3 \end{matrix}  \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & -1 & 0 \\
#         0 & 1 & 3/10 & 0 \\
#         0 & 0 & 1 & 0
#     \end{array} \right)
#     \begin{matrix} R_1 + R_3 \\ R_2 - \frac{3}{10}R_3 \\ \phantom{x} \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & 0 & 0 \\
#         0 & 1 & 0 & 0 \\
#         0 & 0 & 1 & 0
#     \end{array} \right) 
# \end{align*}
# So this set of vectors is a basis for $\mathbb{R}^3$, calculating the inverse of the coefficient matrix
# \begin{align*}
#     \operatorname{adj} 
#     \begin{pmatrix}
#         1 & 0 & -1 \\
#         2 & 5 & 1 \\
#         0 & 7 & 3
#     \end{pmatrix} &= 
#     \begin{pmatrix}
#         8 & -6 & 14 \\
#         -7 & 3 & -7 \\
#         5 & -3 & 5
#     \end{pmatrix}^T =
#     \begin{pmatrix}
#         8 & -7 & 5 \\
#         -6 & 3 & -3 \\
#         14 & -7 & 5
#     \end{pmatrix}, \\
#     \det \begin{pmatrix}
#         1 & 0 & -1 \\
#         2 & 5 & 1 \\
#         0 & 7 & 3
#     \end{pmatrix} &= 8 - 14 = -6, \\
#     \therefore \begin{pmatrix}
#         8 & -7 & 5 \\
#         -6 & 3 & -3 \\
#         14 & -7 & 5
#     \end{pmatrix}^{-1} &= -\frac{1}{6} 
#     \begin{pmatrix}
#         8 & -7 & 5 \\
#         -6 & 3 & -3 \\
#         14 & -7 & 5
#     \end{pmatrix} \\
#     &=
#     \begin{pmatrix}
#         -\frac{4}{3} & \frac{7}{6} & \frac{5}{6} \\
#         1 & -\frac{1}{2} & \frac{1}{2} \\
#         -\frac{7}{3} & -\frac{7}{6} & -\frac{5}{6}
#     \end{pmatrix}
# \end{align*}
# Let $U = \{(1, 2, 0), (0, 5, 7), (-1, 1, 3)\}$ then
# \begin{align*}
#     \left[ \begin{pmatrix} 0 \\ 13 \\ 17 \end{pmatrix} \right]_U &= 
#     \begin{pmatrix}
#         -\frac{4}{3} & \frac{7}{6} & \frac{5}{6} \\
#         1 & -\frac{1}{2} & \frac{1}{2} \\
#         -\frac{7}{3} & -\frac{7}{6} & -\frac{5}{6}
#     \end{pmatrix}
#     \begin{pmatrix} 0 \\ 13 \\ 17 \end{pmatrix} =
#     \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}, \\
#     \left[ \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix} \right]_U &= 
#     \begin{pmatrix}
#         -\frac{4}{3} & \frac{7}{6} & \frac{5}{6} \\
#         1 & -\frac{1}{2} & \frac{1}{2} \\
#         -\frac{7}{3} & -\frac{7}{6} & -\frac{5}{6}
#     \end{pmatrix}
#     \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix} =
#     \begin{pmatrix} 0 \\ 1 \\ -2  \end{pmatrix}.
# \end{align*}
# 
# :::
# ::::
# 
# ::::{admonition} Exercise 5.5
# :class: note
# :name: ex5.5
# 
# Extend $\{(1, 1, 2, 4), (2, -1, -5, 2)\}$ to a basis of $\mathbb{R}^4$.
# 
# :::{dropdown} Solution
# 
# We need to find two vectors in $\mathbb{R}^4$ that are linearly independent to $(1,1, 2, 4)$ and $(2, -1, -5, 2)$ and one another. Let's choose $(1, 0, 0, 0)$ and $(0, 1, 0, 0)$  and check for linear dependence
# 
# \begin{align*}
#     & \left( \begin{array}{cccc|c}
#         1 & 0 & 1 & 2 & 0 \\
#         0 & 1 & 1 & -1 & 0 \\
#         0 & 0 & 2 & -5 & 0 \\
#         0 & 0 & 4 & 2 & 0
#     \end{array} \right)
#     \begin{matrix} \\ \\ \frac{1}{2}R_3 \\ \phantom{x} \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|c}
#         1 & 0 & 1 & 2 & 0 \\
#         0 & 1 & 1 & -1 & 0 \\
#         0 & 0 & 1 & -5/2 & 0 \\
#         0 & 0 & 4 & 2 & 0
#     \end{array} \right)
#     \begin{matrix} R_1 - R_3 \\ R_2 - R_3 \\ \\ R_4 - 4R_1 \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|c}
#         1 & 0 & 0 & 9/2 & 0 \\
#         0 & 1 & 0 & 3/2 & 0 \\
#         0 & 0 & 1 & -5/2 & 0 \\
#         0 & 0 & 0 & 12 & 0
#     \end{array} \right)
#     \begin{matrix} \\ \\ \\ \frac{1}{12}R_4 \end{matrix}  \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|c}
#         1 & 0 & 0 & 9/2 & 0 \\
#         0 & 1 & 0 & 3/2 & 0 \\
#         0 & 0 & 1 & -5/2 & 0 \\
#         0 & 0 & 0 & 1 & 0
#     \end{array} \right)
#     \begin{matrix} R_1 - \frac{9}{2}R_4 \\ R_2 - \frac{3}{2}R_4 \\ R_3 + \frac{5}{2}R_4 \\ \phantom{x} \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|c}
#         1 & 0 & 0 & 0 & 0 \\
#         0 & 1 & 0 & 0 & 0 \\
#         0 & 0 & 1 & 0 & 0 \\
#         0 & 0 & 0 & 1 & 0
#     \end{array} \right)
# \end{align*}
# Therefore $\{ (1, 1, 2, 5), (2, -1, -5, 2), (1, 0, 0, 0), (0, 1, 0, 0) \}$ is a basis for $\mathbb{R}^4$.
# :::
# 
# ::::
# 
# ::::{admonition} Exercise 5.6
# :class: note
# :name: ex5.6
# 
# Suppose that $W$ is a subspace of $\mathbb{R}^4$ generated by the vectors
# 
# \begin{align*}
#     \left\{ \mathbf{u} = \begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix}, 
#     \mathbf{v} = \begin{pmatrix} 1 \\ -1 \\ 2 \\ 0 \end{pmatrix}, 
#     \mathbf{w} = \begin{pmatrix} 2 \\ 1 \\ 5 \\ 3 \end{pmatrix}, 
#     \mathbf{x} = \begin{pmatrix} 1 \\ -1 \\ 0 \\ 3 \end{pmatrix}, 
#     \mathbf{y} = \begin{pmatrix} 1 \\ -1 \\ 0 \\ 4 \end{pmatrix} \right\}.
# \end{align*}
# 
# Find a basis for $W$ and determine $\dim(W)$.
# 
# :::{dropdown} Solution
# We need to find which of the vectors $\mathbf{u}$, $\mathbf{v}$, $\mathbf{w}$, $\mathbf{x}$ and $\mathbf{y}$ are linearly dependent (and therefore remove them to form the basis).
# 
# \begin{align*}
#     & \left( \begin{array}{ccccc|c}
#         1 & 1 & 2 & 1 & 1 & 0 \\
#         2 & -1 & 1 & -1 & -1 & 0 \\
#         3 & 2 & 5 & 0 & 0 & 0 \\
#         4 & 0 & 3 & 3 & 4 & 0
#     \end{array} \right)
#     \begin{matrix} \\ R_2 - 2R_1 \\ R_3 - 3R_1 \\ R_4 - 4R_1 \end{matrix} \\ \\ 
#     \longrightarrow \quad &
#     \left( \begin{array}{ccccc|c}
#         1 & 1 & 2 & 1 & 1 & 0 \\
#         0 & -3 & -3 & -3 & -3 & 0 \\
#         0 & -1 & -1 & -3 & -3 & 0 \\
#         0 & -4 & -5 & -1 & 0 & 0
#     \end{array} \right)
#     \begin{matrix} \\ -\frac{1}{3}R_2 \\ \phantom{x} \\ \phantom{x} \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccccc|c}
#         1 & 1 & 2 & 1 & 1 & 0 \\
#         0 & 1 & 1 & 1 & 1 & 0 \\
#         0 & -1 & -1 & -3 & -3 & 0 \\
#         0 & -4 & -5 & -1 & 0 & 0
#     \end{array} \right)
#     \begin{matrix} R_1 - R_2 \\ \\ R_3 + R_2 \\ R_4 + 4R_2 \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccccc|c}
#         1 & 0 & 1 & 0 & 0 & 0 \\
#         0 & 1 & 1 & 1 & 1 & 0 \\
#         0 & 0 & 0 & -2 & -2 & 0 \\
#         0 & 0 & -1 & 3 & 4 & 0
#     \end{array} \right)
#     \begin{matrix} \\ \\ R_3 \leftrightarrow R_4 \\ \phantom{x} \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccccc|c}
#         1 & 0 & 1 & 0 & 0 & 0 \\
#         0 & 1 & 1 & 1 & 1 & 0 \\
#         0 & 0 & -1 & 3 & 4 & 0 \\
#         0 & 0 & 0 & -2 & -2 & 0 
#     \end{array} \right)
#     \begin{matrix} \\ \\ -R_3 \\ \phantom{x} \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccccc|c}
#         1 & 0 & 1 & 0 & 0 & 0 \\
#         0 & 1 & 1 & 1 & 1 & 0 \\
#         0 & 0 & 1 & -3 & -4 & 0 \\
#         0 & 0 & 0 & -2 & -2 & 0 
#     \end{array} \right)
#     \begin{matrix} R_1 - R_3 \\ R_2 - R_3 \\ \phantom{x} \\ \phantom{x} \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccccc|c}
#         1 & 0 & 0 & 0 & 0 & 0 \\
#         0 & 1 & 0 & 4 & 5 & 0 \\
#         0 & 0 & 1 & -3 & -4 & 0 \\
#         0 & 0 & 0 & -2 & -2 & 0 
#     \end{array} \right) 
#     \begin{matrix} \\  \\  \\ -\frac{1}{2}R_4 \end{matrix}  \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccccc|c}
#         1 & 0 & 0 & 0 & 0 & 0 \\
#         0 & 1 & 0 & 4 & 5 & 0 \\
#         0 & 0 & 1 & -3 & -4 & 0 \\
#         0 & 0 & 0 & 1 & 1 & 0 
#     \end{array} \right)
#     \begin{matrix} \\ R_2 - 4R_4 \\ R_3 + 3R_4 \\ \phantom{x} \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccccc|c}
#         1 & 0 & 0 & 0 & 0 & 0 \\
#         0 & 1 & 0 & 4 & 5 & 0 \\
#         0 & 0 & 1 & -3 & -4 & 0 \\
#         0 & 0 & 0 & 1 & 1 & 0 
#     \end{array} \right)
#     \begin{matrix} \\ R_2 - 4R_4 \\ R_3 + 3R_4 \\ \phantom{x} \end{matrix}  \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccccc|c}
#         1 & 0 & 0 & 0 & 0 & 0 \\
#         0 & 1 & 0 & 0 & 1 & 0 \\
#         0 & 0 & 1 & 0 & -1 & 0 \\
#         0 & 0 & 0 & 1 & 1 & 0 
# \end{array} \right)
# \end{align*}
# 
# The fifth column does not have a pivot element so $\mathbf{y}$ is linearly dependent on the other vectors, therefore a basis for $W$ is $\{ \mathbf{u}, \mathbf{v}, \mathbf{w}, \mathbf{x}\}$ and $\dim(W) = 4$.
# :::
# ::::
