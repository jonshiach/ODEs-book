#!/usr/bin/env python
# coding: utf-8

# (linear-combination-of-vectors-section)=
# # Linear combination of vectors
# 
# ::::{admonition} Definition: Linear combination of vectors
# :class: note
# :name: linear-combination-of-vectors-definition
# 
# Let $\mathbf{u},\mathbf{u}_1,\dots,\mathbf{u}_m\in\mathbb{R}^n$ such that
# 
# \begin{align*}
#     \mathbf{u}=\alpha_1\mathbf{u}_1+\alpha_2\mathbf{u}_2+\dots+\alpha_m\mathbf{u}_m,
# \end{align*}
# 
# for some $\alpha_1,\alpha_2,\dots,\alpha_m\in \mathbb{R}$ [^1]. Such a sum is called a **linear combination of vectors**. 
# ::::
# 
# [^1]: $\alpha$ is the lowercase Greek character 'alpha' and is equivalent to 'a' in the Latin alphabet.
# 
# In other words $\mathbf{u}$ can be expressed as a linear combination of the vectors $\mathbf{u}_1, \mathbf{u}_2, \ldots$. For example 
# 
# \begin{align*}
#     \begin{pmatrix} 2 \\ 0 \\ 7 \end{pmatrix} = 
#     2\begin{pmatrix} 1 \\ 5 \\ -1 \end{pmatrix} +
#     \begin{pmatrix} 0 \\ -10 \\ 9 \end{pmatrix},
# \end{align*}
# 
# and so we have expressed $(2,0,7)$ as a linear combination of the vectors $(1,5,-1)$ and $(0,-10,9)$.
# 
# ::::{admonition} Example 3.6
# :class: seealso
# :name: linear-combination-of-vectors-example
# 
# Express the vector $\mathbf{x} = (7, -2, -11)$ as a linear combination of the vectors 
# 
# \begin{align*}
#     \mathbf{u} &= \begin{pmatrix} 1 \\ 0 \\ 7 \end{pmatrix}, &
#     \mathbf{v} &= \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}, &
#     \mathbf{w} &= \begin{pmatrix} 5 \\ -2 \\ -6 \end{pmatrix}.
# \end{align*}
# 
# :::{dropdown} Solution
#    
# We need to find the values of $\alpha_1$, $\alpha_2$ and $\alpha_3$ in the following linear combination
# 
# \begin{align*}
#     \alpha_1 \mathbf{u} + \alpha_2 \mathbf{v} + \alpha_3 \mathbf{w} &= \mathbf{x} \\
#     \alpha_1 \begin{pmatrix} 1 \\ 0 \\ 7 \end{pmatrix} 
#     + \alpha_2 \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} 
#     + \alpha_3 \begin{pmatrix} 5 \\ -2 \\ -6 \end{pmatrix}
#     &= \begin{pmatrix} 7 \\ -2 \\ -11 \end{pmatrix},
# \end{align*}
# 
# so we need the solution to the linear system
# 
# \begin{align*}
#     \alpha_1 + 2\alpha_2 + 5\alpha_3 &= 7, \\
#     -\alpha_2 - 2\alpha_3 &= -2, \\
#     7\alpha_1 + 3\alpha_2 - 6\alpha_3 &= -11.
# \end{align*}
# 
# Using Gaussian elimination
# 
# \begin{align*}
#     &\left( \begin{array}{ccc|c} 
#         1 & 2 & 5 & 7 \\
#         0 & -1 & -2 & -2 \\
#         7 & 3 & -6 & -11
#     \end{array} \right)
#     \begin{array}{l} \phantom{x} \\ \phantom{x} \\ R_3 - 7R_1 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c} 
#         1 & 2 & 5 & 7 \\
#         0 & -1 & -2 & -2 \\
#         0 & -11 & -41 & -60
#     \end{array} \right)
#     \begin{array}{l} \\ \\ R_3 - 11 R_2 \end{array} \\ \\ 
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c} 
#         1 & 2 & 5 & 7 \\
#         0 & -1 & -2 & -2 \\
#         0 & 0 & -19 & -38
#     \end{array} \right)
# \end{align*}
# 
# Solving by back substitution gives $\alpha_1 = 1$, $\alpha_2 = -2$ and $\alpha_3 = 2$ so
# 
# \begin{align*}
#     \mathbf{x} = \mathbf{u} - 2\mathbf{v} + 2\mathbf{w}
#     =  \begin{pmatrix} 1 \\ 0 \\ 7 \end{pmatrix} 
#     - 2 \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} 
#     + 2 \begin{pmatrix} 5 \\ -2 \\ -6 \end{pmatrix}
#     &= \begin{pmatrix} 7 \\ -2 \\ -11 \end{pmatrix}
# \end{align*}
# :::
# ::::
# 
# ::::{admonition} Proposition: Representing a vector as a linear combination of vectors
# :class: important
# :name: linear-combination-of-vectors-proposition
# 
# If the vector $\mathbf{v} = (v_1, v_2, \ldots, v_n)$ can be represented as the linear combination of vectors $\mathbf{v} = \alpha_1 \mathbf{u}_1 + \alpha_2 \mathbf{u}_2 + \cdots + \alpha_n \mathbf{u}_n$ then the values of $\alpha_i$ are the solutions to the system of linear equations
# 
# \begin{align*}
#     \begin{pmatrix} \mathbf{u}_1 & \mathbf{u}_2 & \cdots & \mathbf{u}_n \end{pmatrix}
#     \begin{pmatrix} \alpha_1 \\ \alpha_2 \\ \vdots \\ \alpha_n \end{pmatrix} = 
#     \begin{pmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{pmatrix}.
# \end{align*}
# 
# ::::
# 
# (basis-vectors-section)=
# ## Basis vectors
# 
# A special type of vector is a **basis vector** which all other vectors in the space can be represented as a linear combination of the basis vectors (we cover basis in more detail in \cref{sec:basis}). In a Cartesian space the simplest basis vectors are unit vectors that point in the co-ordinate directions. In $\mathbb{R}^3$ we use the basis vectors $\mathbf{i} = (1, 0, 0)$, $\mathbf{j} = (0, 1, 0)$ and $\mathbf{k} = (0, 0, 1)$ ({numref}`basis-vectors-figure`).
# 
# :::{figure} ../Images/basis_vectors.png
# :name: basis-vectors-figure
# 
# The three basis vectors in $\mathbb{R}^3$.
# :::
# 
# Using basis vectors we can represent any vector, $\mathbf{a} = (a_1, a_2, a_3)$ say, as a linear combination of $\mathbf{i}$, $\mathbf{j}$ and $\mathbf{k}$, i.e.,
# \begin{align*}a_1 \mathbf{i} + a_2 \mathbf{j} + a_3 \mathbf{k}
#     = a_1 \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + a_2 \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} + a_3
#     \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
#     = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix} = \mathbf{a}.
# \end{align*}
# 
# Given the vectors $\mathbf{a} = (a_1, a_2, a_3)$, $\mathbf{b} = (b_1, b_2, b_3)$ and the scalar $k$
# 
# - vector addition: $\mathbf{a} + \mathbf{b} = (a_1 + b_1)\mathbf{i} + (a_2 + b_2) \mathbf{j} + (a_3 + b_3) \mathbf{k}$;
# - multiplication by a scalar: $k\mathbf{a} = k a_1 \mathbf{i} + k a_2 \mathbf{k} + k a_3 \mathbf{k}$.
# 
# ::::{admonition} Example 3.7
# :class: seealso
# :name: basis-vectors-example
# 
# Represent the following vectors as linear combination of the basis vectors $\mathbf{i}$, $\mathbf{j}$ and $\mathbf{k}$
# 
# (i) &emsp; $\begin{pmatrix} 2 \\ 5 \\ 3 \end{pmatrix}$ &emsp; &emsp;
# (ii) &emsp; $3\begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix}$
# 
# :::{dropdown} Solution
# (i) &emsp; $\begin{pmatrix} 2 \\ 5 \\ 3 \end{pmatrix} = 2 \mathbf{i} + 5 \mathbf{j} + 3 \mathbf{k}$
# 
# (ii) &emsp; $3\begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} = 3(\mathbf{i} + 0 \mathbf{j} + 2 \mathbf{k}) = 3 \mathbf{i} + 6 \mathbf{k}$
# :::
# 
# ::::
