#!/usr/bin/env python
# coding: utf-8

# # Inverse matrix
# 
# The multiplicative inverse of a number $x$ is a number denoted by $x^{-1}$ that when multiplied by $x$ results in the multiplicative identity 1, so the multiplicative inverse of $x$ is $\dfrac{1}{x}$. For matrices, the multiplicate identity is the identity matrix so we can define a multiplicative inverse with respect to matrix multiplication.
# 
# ::::{admonition} Definition: Inverse matrix
# :class: note
# :name: inverse-matrix-definition
# 
# Let $A$ be a non-zero $m \times n$ matrix. Then, if there exist an $n \times m$ matrix $A^{-1}$, such that $A^{-1}A = I_n,$ we say that $A^{-1}$ is the **inverse** of the matrix $A$.
# ::::
# 
# Note:
# 
# - not all square matrices have an inverse;
# - if a matrix does not have an inverse it is said to be **singular**;
# - if a matrix has an inverse it is said to be **non-singular** or **invertible**;
# - an inverse of a square matrix is unique.
# 
# :::::{admonition} Example 1.14
# :class: seealso
# :name: inverse-matrix-example-1
# 
# Given the two matrices
# $A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$ and
# $B = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix},$ 
# show that $B$ is the inverse of $A$. 
# 
# ::::{dropdown} Solution
# \begin{align*}
#     BA = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I.
# \end{align*}
# ::::
# :::::
# 
# ## The adjoint of a matrix
# 
# :::::{admonition} Definition: Adjoint of a matrix
# :class: note
# :name: adjoint-definition
# 
# The **adjoint** (also known as the **adjugate**) of a square matrix $A$ is denoted by $\operatorname{adj}(A)$ and is the transpose of the matrix of cofactors of $A$
# 
# \begin{align*}
#     \operatorname{adj}(A) &= C^\mathrm{T}, \\
#     \therefore [\operatorname{adj}(A)]_{ij}&=(-1)^{i+j}M_{ij}.
# \end{align*}
# :::::
# 
# :::::{admonition} Example 1.15
# :class: seealso
# :name: adjoint-example
# 
# Calculate the adjoint of the following matrices:
# 
# ::::{grid}
# 
# :::{grid-item}
# :columns: 4
# (i) &emsp; $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (ii) &emsp; $\begin{pmatrix} 5 & 2 \\ 3 & 4 \end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (iii) &emsp; $\begin{pmatrix} 1 & 0 & 3 \\ 4 & -2 & 1 \\ 2 & 1 & 3 \end{pmatrix}$
# :::
# 
# ::::
# 
# ::::{dropdown} Solution
# 
# (i)
# \begin{align*}
#     \operatorname{adj}\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} d & -c \\ -b & a \end{pmatrix}^\mathrm{T}
# = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
# \end{align*}
# 
# (ii) 
# \begin{align*}
#     \operatorname{adj}\begin{pmatrix} 5 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 4 & -3 \\ -2 & 5 \end{pmatrix}^\mathrm{T}
# = \begin{pmatrix} 4 & -2 \\ -3 & 5 \end{pmatrix}
# \end{align*}
# 
# (iii)
# \begin{align*}
#     \operatorname{adj}\begin{pmatrix} 1 & 0 & 3 \\ 4 & -2 & 1 \\ 2 & 1 & 3 \end{pmatrix} 
#     &= \begin{pmatrix}
#         \begin{vmatrix} -2 & 1 \\ 1 & 3 \end{vmatrix} &
#         -\begin{vmatrix} 4 & 1 \\ 2 & 3 \end{vmatrix} &
#         \begin{vmatrix} 4 & -2 \\ 2 & 1 \end{vmatrix} \\
#         -\begin{vmatrix} 0 & 3 \\ 1 & 3 \end{vmatrix} &
#         \begin{vmatrix} 1 & 3 \\ 2 & 3 \end{vmatrix} &
#         -\begin{vmatrix} 1 & 0 \\ 2 & 1 \end{vmatrix} \\
#         \begin{vmatrix} 0 & 3 \\ -2 & 1 \end{vmatrix} &
#         -\begin{vmatrix} 1 & 3 \\ 4 & 1 \end{vmatrix} &
#         \begin{vmatrix} 1 & 0 \\ 4 & -2 \end{vmatrix}
#     \end{pmatrix}^\mathrm{T} \\
#     &= \begin{pmatrix} -7 & -10 & 8 \\ 3 & -3 & -1 \\ 6 & 11 & -2 \end{pmatrix}^\mathrm{T} \\
#     &= \begin{pmatrix} -7 & 3 & 6 \\ -10 & -3 & 11 \\ 8 & -1 & -2 \end{pmatrix}.
# \end{align*}
#   
# ::::
# :::::
# 
# ### Python code
# 
# The Sympy code for calculating the adjoint of a square matrix `A` is `A.adjugate()`. The code below calculates the adjoint of the matrices from [example 1.14](adjoint-example).

# In[1]:


from sympy import *

# (i)
a, b, c, d = symbols("a, b, c, d")
A = Matrix([[a, b], [c, d]])
adjA = A.adjugate()

print("(i)")
display(adjA)

# (ii)
A = Matrix([[5, 2], [3, 4]])
adjA = A.adjugate()

print("(ii)")
display(adjA)

# (iii)
A = Matrix([[1, 0, 3], [4, -2, 1], [2, 1, 3]])
adjA = A.adjugate()

print("(iii)")
display(adjA)


# ## Calculating a matrix inverse using the adjoint-determinant formula
# 
# There are several methods used to calculate the inverse of a matrix. For smaller matrices we can use the adjoint-determinant formula.
# 
# ::::{admonition} Theorem: Adjoint-determinant formula
# :class: important
# :name: adjoint-determinant-formula-definition
# 
# The inverse of a non-singular square matrix $A$ can be calculated using
# 
# :::{math}
# :label: adjoint-determinant-formula-equation
# \begin{align*}
#     A^{-1} = \frac{\operatorname{adj}(A)}{\det(A)}.
# \end{align*}
# :::
# 
# In particular, $A$ is invertible if and only if $\det(A)\neq 0$.
# 
# ::::
# 
# It is useful to calculate the determinant first to check that it is non-zero before calculating the adjoint.
# 
# :::::{admonition} Example 1.16
# :class: seealso
# :name: matrix-inverse-example-2
# 
# Calculate the inverses of the following matrices if they exist:
# 
# ::::{grid}
# 
# :::{grid-item}
# :columns: 4
# (i) &emsp; $A = \begin{pmatrix}1 & 0 \\ 3 & 2\end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (ii) &emsp; $B = \begin{pmatrix} 1 & 2 & 0 \\ -2 & 1 & 1 \\ 1 & 0 & 3 \end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (iii) &emsp; $C = \begin{pmatrix}1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$
# :::
# 
# ::::
# 
# ::::{dropdown} Solution
# 
# (i)
# \begin{align*}
#     \det(A) &= 2, \\
#     \operatorname{adj}(A) &= \begin{pmatrix} 2 & -3 \\ 0 & 1 \end{pmatrix}^\mathrm{T}  = \begin{pmatrix} 2 & 0 \\ -3 & 1\end{pmatrix} \\
#     \therefore A^{-1} &= \frac{1}{2}\begin{pmatrix} 2 & 0 \\ -3 & 1\end{pmatrix}.
# \end{align*}
# Check answer:
# \begin{align*}
#     A^{-1}A = \frac{1}{2}\begin{pmatrix} 2 & 0 \\ -3 & 1\end{pmatrix}\begin{pmatrix}1 & 0 \\ 3 & 2\end{pmatrix} = \frac{1}{2} \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I. 
# \end{align*}
# 
# (ii)
# \begin{align*}
#     \det\begin{pmatrix} 1 & 2 & 0 \\ -2 & 1 & 1 \\ 1 & 0 & 3 \end{pmatrix} &= 
#     \begin{vmatrix} 1 & 1 \\ 0 & 3 \end{vmatrix}  - 2 \begin{vmatrix}-2 & 1 \\ 1 & 3 \end{vmatrix} =
#     3 - 2(-7) = 17, \\
#     \operatorname{adj}\begin{pmatrix} 1 & 2 & 0 \\ -2 & 1 & 1 \\ 1 & 0 & 3 \end{pmatrix} &= 
#     \begin{pmatrix} 3 & 7 & -1 \\ -6 & 3 & 2 \\ 2 & -1 & 5 \end{pmatrix}^\mathrm{T} =
#     \begin{pmatrix} 3 & -6 & 2 \\ 7 & 3 & -1 \\ -1 & 2 & 5 \end{pmatrix}, \\
#     \therefore B^{-1} &= \frac{1}{17}\begin{pmatrix} 3 & -6 & 2 \\ 7 & 3 & -1 \\ -1 & 2 & 5 \end{pmatrix}
# \end{align*}
# Check answer:
# \begin{align*}
#     B^{-1}B &= \frac{1}{17}\begin{pmatrix} 3 & -6 & 2 \\ 7 & 3 & -1 \\ -1 & 2 & 5 \end{pmatrix}
#     \begin{pmatrix} 1 & 2 & 0 \\ -2 & 1 & 1 \\ 1 & 0 & 3 \end{pmatrix} \\
#     &= \frac{1}{17}\begin{pmatrix} 17 & 0 & 0 \\ 0 & 17 & 0 \\ 0 & 0 & 17 \end{pmatrix} =
#     \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = I.
# \end{align*}
# 
# (iii)
# \begin{align*}
#     \det\begin{pmatrix}1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} &= 
#     \begin{vmatrix} 5 & 6 \\ 8 & 9 \end{vmatrix} - 2
#     \begin{vmatrix} 4 & 6 \\ 7 & 9 \end{vmatrix} + 3
#     \begin{vmatrix} 4 & 5 \\ 7 & 8 \end{vmatrix} \\
#     &= -3 - 2(-6) + 3(-3) = 0.
# \end{align*}
# Since $\det(C)=0$ then $C$ is singular and does not have an inverse.
# 
# :::::
# 
# ::::{admonition} Theorem: Properties of inverse matrices
# :class: important
# :name: inverse-matrix-properties-theorem
# 
# Let $A$ and $B$ be two invertible $n \times n$ matrices, then the following hold:
# 
# - $AB$ is also invertible and
#     
#   $$(AB)^{-1} = B^{-1}A^{-1}.$$
#     
#   It follows that $(A^m)^{-1} = (A^{-1})^m$ for all positive integers $m$.
#   
# - $A^\mathrm{T}$ is also invertible and
#    
#   $$(A^\mathrm{T})^{-1} = (A^{-1})^\mathrm{T}.$$
# 
# ::::
# 
# ### Python code
# 
# The Sympy code for calculating the inverse of a square matrix `A` is `A.inv()`. The code below calculates the adjoint of the matrices $A$ and $B$ from [example 1.16](matrix-inverse-example-2).

# In[2]:


from sympy import *
from IPython.display import Math

# (i)
A = Matrix([[1, 0], [3, 2]])
invA = A.inv()

print("(i) A^{-1} =")
display(invA)

# (ii)
B = Matrix([[1, 2, 0], [-2, 1, 1], [1, 0, 3]])
invB = B.inv()

print("(ii) B^{-1} =")
display(invB)

