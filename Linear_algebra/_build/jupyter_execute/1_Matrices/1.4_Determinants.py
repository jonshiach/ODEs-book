#!/usr/bin/env python
# coding: utf-8

# (determinant-section)=
# # Determinants
# 
# Determinants of square matrices play a very important role in linear algebra. One of their uses is they enable us to determine if a system of equations has a unique solution. Consider the system of two linear equations
# 
# \begin{align*}
#     a x + b y &= e, \\
#     c x + d y &= f.
# \end{align*}
# 
# To solve for $x$ we could multiply the second equation by $\dfrac{b}{d}$ and subtract from first equation and rearrange to make $x$ the subject
# 
# \begin{align*}
#     a x - \frac{b c}{d} x + b y - \frac{b d}{d} y &= e - \frac{b}{d} f \\
#     (a d - b c) x &= d e - b f \\
#     x &= \frac{d e - b f}{a d - b c}.
# \end{align*}
# 
# We can also solve for $y$ by multiplying the first equation by $\dfrac{c}{a}$ and subtract from the second equation and rearrange to make $y$ the subject
# 
# \begin{align*}
#     c x - \frac{c a}{a} x + d y - \frac{b c}{a} y &= f - \frac{c}{a} e \\
#     (a d - b c) y &= a f - c e \\
#     y &= \frac{a f - c e}{a d - b c}.
# \end{align*}
# 
# Note that the denominators in the solutions to $x$ and $y$ are both $a d - b c$. If this value is zero then the system of equations does not have a solution. The expression $a d - b c$ is the **determinant** of the $2 \times 2$ matrix containing the coefficients of $x$ and $y$
# 
# \begin{align*}
#     \begin{pmatrix} a & b \\ c & d \end{pmatrix}.
# \end{align*}
# 
# The determinant of a square matrix $A$ is denoted by $\det(A)$ or $|A|$ and is a scalar value that can be computed from the values of its elements.
# 
# 
# ## Calculating the determinant of a $2\times 2$ matrix
# 
# ::::{admonition} Definition: Determinant of a $2\times 2$ matrix
# :class: note
# :name: 2x2-determinant-definition
# 
# The determinant of the $2\times 2$ matrix $\begin{pmatrix}a & b \\ c & d \end{pmatrix}$ is
# 
# :::{math}
# :label: 2x2-determinant-equation
# \begin{align*}
#     \det \begin{pmatrix} a & b \\ c & d \end{pmatrix} =
#     \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc,
# \end{align*}
# :::
# i.e., the product of the elements on the main diagonal minus the product of the other two elements. Note that the vertical bars denoting a determinant is different from brackets that denote a matrix.
# ::::
# 
# :::::{admonition} Example 1.10
# :class: seealso
# :name: 2x2-determinant-example
# 
# Calculate the following determinants
# 
# ::::{grid}
# :gutter: 2
# 
# :::{grid-item}
# :columns: 6
# (i) &emsp; $\begin{vmatrix} 5 & 2 \\ 3 & 4 \end{vmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 6
# (ii) &emsp; $\det \begin{pmatrix} a & b \\ ka & kb \end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 6
# (iii) &emsp; $\begin{vmatrix} 5 & 0 \\ 0 & 2 \end{vmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 6
# (iv) &emsp; $\begin{vmatrix} 2-\alpha & 3 \\ 5 & 6 - \alpha \end{vmatrix}$
# :::
# 
# ::::
# 
# ::::{dropdown} Solution
# 
# (i) &emsp; $\begin{vmatrix} 5 & 2 \\ 3 & 4 \end{vmatrix} = 5 \times 4 - 2 \times 3 = 20 - 6 = 14$
# 
# (ii) &emsp; $\det \begin{pmatrix} a & b \\ ka & kb \end{pmatrix} = akb - akb = 0$
# 
# (iii) &emsp; $\begin{vmatrix} 5 & 0 \\ 0 & 2 \end{vmatrix} = 5 \times 2 - 0 \times 0 = 10 - 0 = 10$
# 
# (iv) &emsp; $\begin{vmatrix} 2-\alpha & 3 \\ 5 & 6 - \alpha \end{vmatrix} = (2-\alpha)(6-\alpha) - 3 \times 5 = \alpha^2 - 8\alpha - 3$
# ::::
# :::::
# 
# ## Calculating the determinant of an $n \times n$ matrix
# 
# To compute the determinant of a matrix larger than $2\times 2$ we need to split the matrix up into multiple $2\times 2$ matrices so we can use equation {eq}`2x2-determinant-equation`. This is done in a specific way explained below which using things called **minors** and **cofactors**.
# 
# 
# ::::{admonition} Definition: Minor
# :class: note
# :name: minor-definition
# 
# The **minor** of an element of an $n\times n$ square matrix is denoted by $M_{ij}$ and is the determinant of the $(n-1)\times (n-1)$ square matrix that is formed by removing row $i$ and column $j$ from $A$. 
# ::::
# 
# For example, if 
# $A = \begin{pmatrix}
#     a_{11} & a_{12} & a_{13} \\
#     a_{21} & a_{22} & a_{23} \\
#     a_{31} & a_{32} & a_{33}
# \end{pmatrix}$ 
# then
# \begin{align*}
#     M_{21} &= \begin{vmatrix}
#         \square & a_{12} & a_{13} \\
#         \square & \square & \square \\
#         \square & a_{32} & a_{33}
#     \end{vmatrix}
#     = \begin{vmatrix}
#         a_{12} & a_{13} \\
#         a_{32} & a_{33}
#     \end{vmatrix}
#     = a_{12}a_{33} - a_{13}a_{32}.
# \end{align*}
# 
# :::::{admonition} Example 1.11
# :class: seealso
# :name: minor-example
# 
# Given the matrix $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix},$ calculate:
# 
# 
# ::::{grid}
# 
# :::{grid-item}
# :columns: 2
# (i) &emsp; $M_{11}$
# :::
# 
# :::{grid-item}
# :columns: 2
# (ii) &emsp; $M_{12}$
# :::
# 
# :::{grid-item}
# :columns: 2
# (iii) &emsp; $M_{13}$
# :::
# 
# ::::
# 
# ::::{dropdown} Solution
# (i) &emsp; $M_{11} = \begin{vmatrix} 5 & 6 \\ 8 & 9 \end{vmatrix} = 5(9) - 6(8) = 45 - 48 = -3$
# 
# (ii) &emsp; $M_{12} = \begin{vmatrix} 4 & 6 \\ 7 & 9 \end{vmatrix} = 4(9) - 6(7) = 36 - 42 = -6$
# 
# (iii) &emsp; $M_{13} = \begin{vmatrix} 4 & 5 \\ 7 & 8 \end{vmatrix} = 4(8) - 5(7) = 32 - 35 = -3$
# ::::
# :::::
# 
# ::::{admonition} Definition: Cofactor
# :class: note
# :name: cofactor-definition
# 
# The **cofactor** of an element of a square matrix is denoted by $C_{ij}$ and is defined by
# 
# :::{math}
# :label: cofactor-equation
# 
# \begin{align*}
#     C_{ij} = (-1)^{i+j}M_{ij}.
# \end{align*}
# :::
# ::::
# 
# Note that the $(-1)^{i+j}$ in equation {eq}`cofactor-equation` is positive when $i + j$ is even and negative when $i+j$ is odd which results in the following pattern of signs
# 
# \begin{align*}
#     \begin{matrix} 
#         + & - & + & \cdots \\
#         - & + & - & \cdots \\
#         + & - & + & \cdots \\
#         \vdots & \vdots & \vdots & \ddots
#       \end{matrix}
# \end{align*}
# 
# 
# ::::{admonition} Definition: Determinant of an $n\times n$ matrix
# :class: note
# :name: nxn-determinant-definition
# 
# The determinant of an $n\times n$ matrix $A$ is defined by
# 
# :::{math}
# :label: nxn-determinant-equation
# 
# \begin{align*}
#     \det(A) = \sum_{i=1}^n a_{ik} C_{ik} = \sum_{j=1}^n a_{kj} C_{kj},
# \end{align*}
# :::
# for some fixed value $1 \leq k \leq n$ which represents a single row or column of $A$.
# ::::
# 
# Equation {eq}`nxn-determinant-equation` allows us to express the determinant of an $n\times n$ matrix in terms of determinants of $(n-1)\times(n-1)$ matrices. We can then if needed, apply the formula again to the sub-matrices. Continuing in this fashion we will eventually just be calculating $2\times 2$ matrices, which we know how to do from equation {eq}`2x2-determinant-equation`.
# 
# To calculate the determinant of the matrix 
# 
# \begin{align*}
#     A = \begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix},
# \end{align*}
# 
# we can expand across row 1 using $k = 1$ in the first summation in equation {eq}`nxn-determinant-equation`
# 
# \begin{align*}
#     \det(A) &= a C_{11} + b C_{12} + c C_{13} \\
#     &= a (-1)^{(1+1)} \begin{vmatrix} e & f \\ h & i \end{vmatrix}
#     + b (-1)^{(1+2)} \begin{vmatrix}d & f \\ g & i \end{vmatrix} 
#     + c (-1)^{(2+2)} \begin{vmatrix}d & e \\ g & h \end{vmatrix} \\
#     &= a(ei - fh) - b(di - fg) + c(dh - eg) \\
#     &= aei - afh - bdi + bfg + cdh - ceg.
# \end{align*}
# 
# We could also had chosen to expand along column 2 using $k = 2$ and the second summation in equation {eq}`nxn-determinant-equation`.
# 
# \begin{align*}
#   \det(A) &= b C_{12} + e C_{22} + h C_{32} \\
#   &= (-1)^{(1+2)} b\begin{vmatrix} d & f \\ g & i \end{vmatrix} 
#   + (-1)^{(2+2)}e \begin{vmatrix} a & c \\ g & i \end{vmatrix} 
#   + (-1)^{(3+2)}h \begin{vmatrix} a & c \\ d & f \end{vmatrix} \\
#   &= -b(di-fg) + e(ai-cg) - h(af-cd) \\
#   &= -bdi + bfg + aei - ceg - afh + cdh.
# \end{align*}
# 
# Which is the same as the result when expanded along row 1. So it does not matter which row or column we expand along to compute the determinant, we will always get the same answer. It is usually preferable to expand along the row or columns with the most zero elements or smallest integer values to simplify the calculations.
# 
# :::::{admonition} Example 1.12
# :class: seealso
# :name: nxn-determinant-example
# 
# Calculate the determinant of the matrix 
# 
# \begin{align*}
#     \begin{pmatrix} 1 & 0 & 4 \\ 2 & 5 & 6 \\ 4 & 5 & 2 \end{pmatrix},
# \end{align*}
# 
# by expanding along:
# 
# ::::{grid}
# 
# :::{grid-item}
# :columns: 3
# (i) &emsp; row 1
# :::
# 
# :::{grid-item}
# :columns: 3
# (ii) &emsp; column 3
# :::
# 
# ::::
# 
# ::::{dropdown} Solution
# 
# (i) 
# \begin{align*}
#     \begin{vmatrix}1 & 0 & 4 \\ 2 & 5 & 6 \\ 4 & 5 & 2 \end{vmatrix} 
#     &= 1\begin{vmatrix}5 & 6 \\ 5 & 2 \end{vmatrix} - 0 \begin{vmatrix} 2 & 6 \\ 4 & 2 \end{vmatrix} + 4 \begin{vmatrix}2 & 5 \\ 4 & 5 \end{vmatrix} \\
#     &= (10-30) + 4(10-20) \\
#     &= -60
# \end{align*}
# 
# (ii) 
# \begin{align*} 
#     \begin{vmatrix}1 & 0 & 4 \\ 2 & 5 & 6 \\ 4 & 5 & 2 \end{vmatrix} 
#     &= 4 \begin{vmatrix} 2 & 5 \\ 4 & 5 \end{vmatrix} - 6\begin{vmatrix}1 & 0 \\ 4 & 5 \end{vmatrix} + 2\begin{vmatrix}1 & 0 \\ 2 & 5 \end{vmatrix} \\
#     &= 4(10-20) - 6(5 - 0) + 2(5 - 0) \\
#     &= -60
# \end{align*}
# ::::
# :::::
# 
# For larger matrices we have to apply equation {eq}`nxn-determinant-equation` recursively until we get to $2 \times 2$ determinants where we can use {eq}`2x2-determinant-equation`.
# 
# :::::{admonition} Example 1.13
# :class: seealso
# :name: 4x4-determinant-example
# 
# Calculate the determinant of the $4\times 4$ matrix 
#    
# $$\begin{pmatrix} 1 & -1 & 4 & 3 \\ 2 & 0 & 5 & -3 \\ 1 & 2 & 4 & 5 \\ 2 & 0 & -2 & 4 \end{pmatrix}.$$
# 
# ::::{dropdown} Solution
# 
# Here column 2 has two zero elements so it would be simpler to expand along this column
# \begin{align*}
#     \begin{vmatrix} 1 & -1 & 4 & 3 \\ 2 & 0 & 5 & -3 \\ 1 & 2 & 4 & 5 \\ 2 & 0 & -2 & 4 \end{vmatrix} &=
#     - (-1) \begin{vmatrix}2 & 5 & -3 \\ 1 & 4 & 5 \\ 2 & -2 & 4 \end{vmatrix} 
#     - 2 \begin{vmatrix} 1 & 4 & 3 \\ 2 & 5 & -3 \\ 2 & -2 & 4 \end{vmatrix} \\
#     &= 2 \begin{vmatrix} 4 & 5 \\ -2 & 4 \end{vmatrix} 
#     - 5\begin{vmatrix}1 & 5 \\ 2 & 4 \end{vmatrix}
#     - 3 \begin{vmatrix} 1 & 4 \\ 2 & -2 \end{vmatrix} \\
#     & \qquad - 2 \left( \begin{vmatrix} 5 & -3 \\ -2 & 4 \end{vmatrix}
#     - 4 \begin{vmatrix} 2 & -3 \\ 2 & 4 \end{vmatrix}
#     + 3 \begin{vmatrix} 2 & 5 \\ 2 & -2 \end{vmatrix} \right) \\
#     &= 2(16 + 10) - 5(4 - 10) - 3(-2-8) \\
#     & \qquad - 2(20-6) + 8(8+6) - 6(-4-10) \\
#     &= 280.
# \end{align*}
# ::::
# :::::
# 
# ::::{admonition} Theorem: Properties of determinants
# :class: important
# :name: properties-of-determinants-theorem
# 
# Determinants have the following properties:
# 
# - $\det(AB) = \det(A)\det(B)$.
# - $\det(A) = \det(A^\mathrm{T})$.
# - If a matrix has a row or column with all zero elements then its determinant is zero.
# - Interchanging any two rows of a matrix changes the sign of the determinant.
# - If all elements in a row are multiplied by a scalar $k$ then the determinant is also multiplied by $k$.
# - If one row of a matrix is a multiple of another row then the matrix has a determinant of zero.
# - The value of a determinant is unchanged by adding a multiple of one row to another row.
# ::::
# 
# ### Python
# 
# The Sympy code for calculating the determinant of a square matrix `A` is `A.det()`. The code below calculates the determinant of the matrix from [example 1.13](4x4-determinant-example).

# In[1]:


from sympy import *

A = Matrix([[1, -1, 4, 3], [2, 0, 5, -3], [1, 2, 4, 5], [2, 0, -2, 4]])
detA = A.det()
print(f"det(A) = {detA}")

