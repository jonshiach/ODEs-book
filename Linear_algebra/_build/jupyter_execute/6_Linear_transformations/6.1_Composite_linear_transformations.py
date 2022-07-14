#!/usr/bin/env python
# coding: utf-8

# (composite-linear-transformations-section)=
# # Composite linear transformations
# 
# ::::{admonition} Definition: Composite transformations
# :class: note
# :name: composite-transformation-definition
# 
# Let $S : V \to W$ and $T: W \to X$ be two linear transformations over the vector spaces $V, W$ and $X$. The **composition** of $S$ and $T$ is the transformation $S \circ T: V \to X$ defined by
# 
# \begin{align*}
#     (S \circ T)(\mathbf{u}) = S(T(\mathbf{u})),
# \end{align*}
# 
# for all vectors $\mathbf{u} \in V$.
# ::::
# 
# ::::{admonition} Example 6.5
# :class: seealso
# :name: composite-transformation-example
# 
# Two linear transformations is defined as $T:(x, y, z) \mapsto (2x + y - z, 3x + z, y - 2z)$ and $S:(x, y) \mapsto (2 x + 4 y, -x + 3 y, x + 2 y)$, determine the composite linear transformation matrix $S \circ T(\mathbf{u})$ for $\mathbf{u} = (x, y, z)$.
# 
# :::{dropdown} Solution
# 
# \begin{align*}
#     S \circ T\begin{pmatrix} x \\ y \\ z \end{pmatrix} &= 
#     S \left( T\begin{pmatrix} x \\ y \\ z \end{pmatrix} \right)
#     = S \begin{pmatrix} 2 x + 4 \\ - x + 3y \\ x + 2 y \end{pmatrix} \\
#     &= \begin{pmatrix} 
#         2(2 x + 4 y) + (-x + 3 y) - (x + 2 y) \\ 
#         3(2 x + 4 y) + (x + 2 y) \\
#         (-x + 3 y) - 2(x + 2 y)
#     \end{pmatrix} \\
#     &= \begin{pmatrix} 2 x + 9 y \\ 7 x + 14 y \\ -3 x - y \end{pmatrix}.
# \end{align*}
# 
# :::
# 
# ::::
# 
# ## Composite transformation matrices
# 
# We have seen that a linear transformation $T: V \to W$ can be represented by a [transformation matrix](transformation-matrix-definition) so that given a vector $\mathbf{u} \in V$ the image is calculated using 
# 
# :::{math}
# :label: composite-transformation-matrix-equation-1
# 
# T(\mathbf{u}) = A \mathbf{u}.
# :::
# 
# Consider the composition of $T$ with another linear transformation $S: W \to X$ with a transformation matrix $B$
# 
# :::{math}
# :label: composite-transformation-matrix-equation-2
# 
# S \circ T(\mathbf{u}) = B \cdot T(\mathbf{u})
# :::
# 
# Substituting equation {eq}`composite-transformation-matrix-equation-1` into equation {eq}`composite-transformation-matrix-equation-1` gives
# 
# \begin{align*}
#     S \circ T (\mathbf{u}) = B \cdot A \mathbf{u}.
# \end{align*}
# 
# ::::{admonition} Theorem: Composite transformation matrices
# :class: important
# :name: composite-transformation-matrices-theorem
# 
# Given two linear transformations $T:V \to W$ and $S:W \to X$ with transformation matrices $A$ and $B$ respectively then the composition $S \circ T$ of the vector $\mathbf{u} \in V$ is 
# 
# :::{math}
# :label: composite-transformation-matrices-theorem-equation
# 
# S \circ T (\mathbf{u}) = B \cdot A \mathbf{u}.
# :::
# ::::
# 
# ::::{admonition} Example 6.6
# :class: seealso
# :name: composite-transformation-matrix-example
# 
# Calculate the transformation matrices, $A$ and $B$, for the transformations $S$ and $T$ from [example 6.5](composite-transformation-example) and use them to calculate the transformation matrix $C$ for $S\circ T$. 
# 
# :::{dropdown} Solution
# \begin{align*}
#     A &= \begin{pmatrix} 2 & 4 \\ -1 & 3 \\ 1 & 2 \end{pmatrix}, \\
#     B &= \begin{pmatrix} 2 & 1 & - 1 \\ 3 & 0 & 1 \\ 0 & 1 & -2 \end{pmatrix}, \\
#     \therefore C &= BA = \begin{pmatrix} 2 & 1 & - 1 \\ 3 & 0 & 1 \\ 0 & 1 & -2 \end{pmatrix}
#     \begin{pmatrix} 2 & 4 \\ -1 & 3 \\ 1 & 2 \end{pmatrix} \\
#     &= \begin{pmatrix} 2 & 9 \\ 7 & 14 \\ -3 & 1 \end{pmatrix}.
# \end{align*}
# 
# Checking that $C \mathbf{u}$ gives the answer from [example 6.4](composite-transformation-example)
# 
# \begin{align*}
#     C \cdot \begin{pmatrix} x \\ y \\ z \end{pmatrix} = 
#     \begin{pmatrix} 2 & 9 \\ 7 & 14 \\ -3 & 1 \end{pmatrix}
#     \begin{pmatrix} x \\ y \\ z \end{pmatrix} =
#     \begin{pmatrix} 2 x + 9 y \\ 7 x + 14 y \\ -3 x + y \end{pmatrix} \quad \checkmark
# \end{align*}
# :::
# 
# ::::
