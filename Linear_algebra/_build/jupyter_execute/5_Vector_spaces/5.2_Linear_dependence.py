#!/usr/bin/env python
# coding: utf-8

# (linear-dependence-section)=
# # Linear dependence
# 
# ::::{admonition} Definition: Linear combination
# :class: note
# :name: linear-combination-definition
# 
# Let $V$ be a vector space over a field $F$ and $W$ a non-empty subset of $V$. We say that $\mathbf{u} \in V$ is a **linear combination of elements in $W$** if there exist $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \in W$ and $\alpha_1, \alpha_2, \ldots, \alpha_n \in F$ such that
# 
# :::{math}
# :label: linear-combination-equation
# 
# \mathbf{u} = \sum_{i = 1}^n \alpha_i \mathbf{v}_i = \alpha_1 \mathbf{v}_1 + \alpha_2 \mathbf{v}_2 + \ldots + \alpha_n \mathbf{v}_n.
# :::
# ::::
# 
# We next introduce the notion of linear independence. 
# 
# ::::{admonition} Definition: Linear dependence
# :class: note
# :name: linear-dependence-definition
# 
# Let $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \in V$ and consider the equation
# 
# :::{math}
# :label: linear-dependence-equation
# 
# \alpha_1 \mathbf{v}_1 + \alpha_2 \mathbf{v}_2 + \cdots + \alpha_n \mathbf{v}_n = \mathbf{0},
# :::
# 
# where $\alpha \in F$. The vectors $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \in V$ are said to be **linearly independent over $F$** if the only solution to the above equation is when all of the $\alpha_i$ values are zero (this solution is called the trivial solution). If the above equation is satisfied where $\alpha_i \neq 0$ for $1 \leq i \leq n$, then the vectors $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \in V$ are said to be **linearly dependent over $F$**.
# ::::
# 
# Another way to think about linear independence is that a set of vectors is linearly independent if none of the vectors in the set can be represented as a linear combination of the other vectors in the same set. For example, are the matrices $A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$, $B = \begin{pmatrix} -1 & -1 \\ 0 & -2 \end{pmatrix}$ and $C = \begin{pmatrix} -4 & 0 \\ 0 & -8 \end{pmatrix}$ linearly independent over $\mathbb{R}$? 
# 
# We can see by inspection that $B = -A$ therefore $A$, $B$ and $C$ are linearly dependent as
# \begin{align*}
#     1 \cdot A + 1 \cdot B + 0 \cdot C = \mathbf{0}_{2\times 2}.
# \end{align*} 
# 
# So if any two members of a set are scalar multiples of each other then they are linearly dependent because we can choose $\alpha_i$ values to satisfy equation {eq}`linear-dependence-equation`.
# 
# ::::{admonition} Example 5.5
# :class: seealso
# :name: linear-dependence-equation
# 
# Determine whether the following are linearly dependent
# 
# (i) &emsp; $(1, 0, 2), (2, 1, 3), (-3, -4, -2) \in \mathbb{R}^3$ over $\mathbb{R}$
# 
# :::{dropdown} Solution
# 
# Let $\alpha_1, \alpha_2, \alpha_3 \in \mathbb{R}$ then equation {eq}`linear-dependence-equation` becomes
# 
# \begin{align*}
#     \alpha_1 \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} + 
#     \alpha_2 \begin{pmatrix} 2 \\ 1 \\ 3 \end{pmatrix} + 
#     \alpha_3 \begin{pmatrix} -3 \\ -4 \\ -2 \end{pmatrix} &= 
#     \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}.
# \end{align*}
# 
# This holds if and only if
# 
# \begin{align*}
#     \alpha_1 + 2\alpha_2 - 3\alpha_3 &= 0, \\
#     \alpha_2 - 4\alpha_3 &= 0, \\
#     2\alpha_3 + 3\alpha_2 - 2\alpha_3 &= 0.
# \end{align*}
# 
# Solving this homogeneous system using Gaussian elimination
# \begin{align*}
#     & \left( \begin{array}{ccc|c}
#         1 & 2 & -3 & 0 \\
#         0 & 1 & -4 & 0 \\
#         2 & 3 & -2 & 0
#     \end{array} \right)
#     \begin{matrix} \\ \\ R_3 - 2R_1 \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 2 & -3 & 0 \\
#         0 & 1 & -4 & 0 \\
#         0 & -1 & 4 & 0
#     \end{array} \right)
#     \begin{matrix} \\ \\ R_3 + R_2 \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 2 & -3 & 0 \\
#         0 & 1 & -4 & 0 \\
#         0 & -1 & 4 & 0
#     \end{array} \right)
#     \begin{matrix} R_1 - 2R_1 \\ \phantom{x} \\ \phantom{x} \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & 5 & 0 \\
#         0 & 1 & -4 & 0 \\
#         0 & 0 & 0 & 0
#     \end{array} \right)
# \end{align*}
# 
# Here $\alpha_3$ is a free variable, so let $\alpha_3 = r$ then $\alpha_1 = -5r$ and $\alpha_2 = 4r$. There vectors are therefore linearly dependent, i.e., if $r = 1$, then $\alpha_1 = -5$ and $\alpha_2 = 4$, i.e.,
# 
# \begin{align*}
#     - 5 \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix}
#     + 4 \begin{pmatrix} 2 \\ 1 \\ 3 \end{pmatrix}
#     + \begin{pmatrix} -3 \\ -4 \\ -2 \end{pmatrix} =
#     \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}.
# \end{align*}
# :::
#  
# (ii) &emsp; $p(x) = x^2 + x + 1$, $r(x) = x - 1$ and $s(x) = x^2 - 1 \in P(\mathbb{R}_2)$ over $\mathbb{R}$
# 
# :::{dropdown} Solution
# 
# Let $\alpha_1, \alpha_2, \alpha_3 \in \mathbb{R}$ then we need to ascertain when
# 
# \begin{align*}
#     \alpha_1 p(x) + \alpha_2 r(x) + \alpha_3 s(x) = 0.
# \end{align*}
# 
# Now
# \begin{align*}
#     \alpha_1 (x^2 + x + 1) + \alpha_2 (x - 1) + \alpha_3 (x^2 - 1) &= 0 \\
#     (\alpha_1 + \alpha_3)x^2 + (\alpha_1 + \alpha_2)x + (\alpha_1 - \alpha_2 - \alpha_3)x^0 &= 0.
# \end{align*}
# 
# For a polynomial to be equal to zero, the coefficients of $x^i$ must all be equal to zero, therefore
# 
# \begin{align*}
#     \alpha_1 + \alpha_3 &= 0, \\
#     \alpha_1 + \alpha_2 &= 0, \\
#     \alpha_1 - \alpha_2 - \alpha_3 &= 0.
# \end{align*}
# 
# Solving using Gauss-Jordan elimination
# 
# \begin{align*}
#     & \left( \begin{array}{ccc|c}
#         1 & 0 & 1 & 0 \\
#         1 & 1 & 0 & 0 \\
#         1 & -1 & -1 & 0
#     \end{array} \right)
#     \begin{matrix} \\ R_2 - R_1 \\ R_3 - R_1 \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & 1 & 0 \\
#         0 & 1 & -1 & 0 \\
#         0 & -1 & -2 & 0
#     \end{array} \right)
#     \begin{matrix} \\  \\ R_3 + R_2 \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & 1 & 0 \\
#         0 & 1 & -1 & 0 \\
#         0 & 0 & -3 & 0
#     \end{array} \right)
#     \begin{matrix} \\  \\ -\frac{1}{3}R_3 \end{matrix} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & 1 & 0 \\
#         0 & 1 & -1 & 0 \\
#         0 & 0 & 1 & 0
#     \end{array} \right)
#     \begin{matrix} R_1 - R_3 \\ R_2 - R_3 \\ \phantom{x} \end{matrix}  \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & 0 & 0 \\
#         0 & 1 & 0 & 0 \\
#         0 & 0 & 1 & 0
#     \end{array} \right)
# \end{align*}
# 
# Therefore the only solution is $\alpha_1 = \alpha_2 = \alpha_3 = 0$ so the polynomials are linearly independent.
# :::
# ::::
# 
