#!/usr/bin/env python
# coding: utf-8

# # Matrix transpose
# 
# ````{admonition} Definition: Matrix transpose
# :class: note
# :name: matrix-transpose-definition
# 
#  The **transpose** $A^\mathrm{T}$ of a matrix $A$ is given by
# \begin{align*}
#     [A^\mathrm{T}]_{ij}=a_{ji}.
# \end{align*}
# ````
# 
# Transposing a matrix switches the rows and columns around so that row $i$ becomes column $i$ and column $j$ becomes row $j$, i.e., 
# 
# \begin{align*}
#     \begin{pmatrix}
#         a_{11} & a_{12} & \cdots & a_{1n} \\
#         a_{21} & a_{22} & \cdots & a_{2n} \\
#         \vdots & \vdots & \ddots & \vdots \\
#         a_{m1} & a_{m2} & \cdots & a_{mn} 
#     \end{pmatrix}^\mathrm{T} = 
#     \begin{pmatrix}
#         a_{11} & a_{21} & \cdots & a_{m1} \\
#         a_{12} & a_{22} & \cdots & a_{m2} \\
#         \vdots & \vdots & \ddots & \vdots \\
#         a_{1n} & a_{2n} & \cdots & a_{mn}
#     \end{pmatrix}.
# \end{align*}
# 
# :::::{admonition} Example 1.7
# :class: seealso
# :name: matrix-transpose-example
# 
# Evaluate the following:
# 
# ::::{grid}
# 
# :::{grid-item}
# :columns: 4
# (i) &emsp; $\begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}^\mathrm{T}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (ii) &emsp; $\begin{pmatrix} 1 & 0 & -2 \\ 3 & -4 & 1 \end{pmatrix}^\mathrm{T}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (iii) &emsp; $\begin{pmatrix}2 & 3 & 5 \end{pmatrix}^\mathrm{T}$
# :::
# 
# ::::
# 
# ````{dropdown} Solution
# 
# (i) &emsp; $\begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}^\mathrm{T} = 
#     \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$
# 
# (ii) &emsp; $\begin{pmatrix} 1 & 0 & -2 \\ 3 & -4 & 1 \end{pmatrix}^\mathrm{T} =
#     \begin{pmatrix} 1 & 3 \\ 0 & -4 \\ -2 & 1 \end{pmatrix}$
# 
# (iii) &emsp; $\begin{pmatrix}2 & 3 & 5 \end{pmatrix}^\mathrm{T} = 
#     \begin{pmatrix} 2 \\ 3 \\ 5 \end{pmatrix}$
# ````
# :::::
# 
# ````{admonition} Theorem: Properties of matrix transpose
# :class: important
# :name: properties-of-matrix-transpose-theorem
# 
# Let $A$ and $B$ be two square $n \times n$ matrices and $k$ a scalar, then
# 
# - $(A^\mathrm{T})^\mathrm{T} = A$;
# - $(A + B)^\mathrm{T} = A^\mathrm{T} + B^\mathrm{T}$;
# - $(k A)^\mathrm{T} = k (A^\mathrm{T})$;
# - $(AB)^\mathrm{T} = B^\mathrm{T}A^\mathrm{T}$
# 
# ````
# 
# ## Python code
# 
# The Python command for calculating the transpose of a matrix `A` is `A.T`. The Python code below calculates the solution to question (ii) from [example 1.7](matrix-transpose-example).

# In[1]:


from sympy import *

# (i)
A = Matrix([[1, 2], [3, 4]])
print("(i)")
display(A.T)

# (ii)
B = Matrix([[1, 0, -2], [3, -4, 1]])
print("(ii)")
display(B.T)

# (iii)
C = Matrix([[2, 3, 5]])
print("(iii)")
display(C.T)

