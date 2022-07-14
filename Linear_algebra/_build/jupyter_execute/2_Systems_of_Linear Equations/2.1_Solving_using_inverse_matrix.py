#!/usr/bin/env python
# coding: utf-8

# # Solving systems of linear equations using the inverse matrix
#     
# If we have a system of linear equations of the form $A\mathbf{x}=\mathbf{b}$ where $A$ is a non-singular (invertible) square matrix then use of matrix algebra shows that
# 
# \begin{align*}
#     A\mathbf{x} &= \mathbf{b}\\
#     A^{-1}A \mathbf{x} &= A^{-1}\mathbf{b}\\
#     \mathbf{x} &= A^{-1}\mathbf{b} \qquad \text{(since $I = A^{-1}A$)}.
# \end{align*}
# 
# ::::{admonition} Theorem: Solution of a linear system of equations using the inverse matrix
# :class: important
# :name: solution-using-inverse-matrix-theorem
# 
# The solution to a system of linear equations $A\mathbf{x} = \mathbf{b}$ can be calculated using $\mathbf{x} = A^{-1}\mathbf{b}$. 
# ::::
# 
# Consider the system of linear equations from [example 2.1](system-of-linear-equations-matrix-form-example). 
# 
# \begin{align*}
#     \begin{pmatrix} 
#         2 & 1 \\ 
#         4 & 3 
#     \end{pmatrix}
#     \begin{pmatrix}
#         x_1 \\ x_2 
#     \end{pmatrix} = 
#     \begin{pmatrix} 
#         4 \\ 10 
#     \end{pmatrix}.
# \end{align*}
# 
# The inverse of the coefficient matrix can be easily calculated using the [adjoint-determinant formula](adjoint-determinant-formula-definition) to give
# 
# \begin{align*}
#     A^{-1} = \begin{pmatrix} \frac{3}{2} & -\frac{1}{2} \\ -2 & 1 \end{pmatrix}.
# \end{align*}
# 
# Using $\mathbf{x} = A^{-1}\mathbf{b}$ the solution is
# 
# \begin{align*}
#     \mathbf{x} = 
#     \begin{pmatrix} \frac{3}{2} & -\frac{1}{2} \\ -2 & 1 \end{pmatrix}
#     \begin{pmatrix} 4 \\ 10 \end{pmatrix} =
#     \begin{pmatrix} 1 \\ 2 \end{pmatrix},
# \end{align*}
# 
# so $x_1 = 1$ and $x_2 = 2$ (which we saw when we used [algebra to solve this system](solving-linear-systems-using-algebra-section)). We can check whether this is the correct solution by substituting $\mathbf{x}$ into $A\mathbf{x}= \mathbf{b}$
# 
# \begin{align*}
#     A \mathbf{x} = \begin{pmatrix} 2 & 1 \\ 4 & 3 \end{pmatrix}
#     \begin{pmatrix} 1 \\ 2 \end{pmatrix} =
#     \begin{pmatrix} 4 \\ 10 \end{pmatrix} = \mathbf{b}.
# \end{align*}
# 
# :::::{admonition} Example 2.2
# :class: seealso
# :name: solution-by-inverse-example
# 
# Solve the following systems of linear equations using the inverse of the coefficient matrix:
# 
# ::::{grid}
# 
# :::{grid-item}
# (i) &emsp; $\begin{array}{rl}
#         x_1 - 2x_2 &= 11, \\
#         2x_1 + 4x_2 &= -18.
#     \end{array}$
# :::
# 
# :::{grid-item}
# (ii) &emsp; $\begin{array}{rl}
#         x_1 - 2x_2 + 3x_3 &= -7, \\
#         2x_2 - 4x_3 &= 8, \\
#         3x_1 + x_2 - 4x_3 &= 7.
#     \end{array}$
# :::
# 
# ::::
# 
# ::::{dropdown} Solution
# 
# (i) $A = \begin{pmatrix} 1 & -2 \\ 2 & 4 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} 11 \\ -18 \end{pmatrix}$
# \begin{align*}
#     \det\begin{pmatrix} 1 & -2 \\ 2 & 4 \end{pmatrix} &= 8, \\
#     \operatorname{adj}\begin{pmatrix} 1 & -2 \\ 2 & 4 \end{pmatrix} &= 
#     \begin{pmatrix} 4 & -2 \\ 2 & 1 \end{pmatrix}^T = 
#     \begin{pmatrix} 4 & 2 \\ -2 & 1 \end{pmatrix},\\
#     \therefore A^{-1} &= \frac{1}{8}\begin{pmatrix} 4 & 2 \\ -2 & 1 \end{pmatrix}
#     = \begin{pmatrix} \frac{1}{2} & \frac{1}{4} \\ -\frac{1}{4} & \frac{1}{8} \end{pmatrix}, \\
#     \therefore \mathbf{x} &= \begin{pmatrix} \frac{1}{2} & \frac{1}{4} \\ -\frac{1}{4} & \frac{1}{8} \end{pmatrix}     
#     \begin{pmatrix} 11 \\ -18 \end{pmatrix} = 
#     \frac{1}{8}\begin{pmatrix} 8 \\ -40 \end{pmatrix} = 
#     \begin{pmatrix} 1 \\ -5 \end{pmatrix}.
# \end{align*}
# 
# Check solution:
# 
# $$A\mathbf{x} = \begin{pmatrix} 1 & -2 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} 1 \\ -5 \end{pmatrix} = \begin{pmatrix}  11 \\  -18    \end{pmatrix}  = \mathbf{b}.$$
# 
# (ii) $A = \begin{pmatrix} 1 & -2 & 3 \\ 0 & 2 & -4 \\ 3 & 1 & -4 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix}-7 \\ 8 \\ 7 \end{pmatrix}$
# \begin{align*}
#     \det \begin{pmatrix} 1 & -2 & 3 \\ 0 & 2 & -4 \\ 3 & 1 & -4 \end{pmatrix} &= 
#     \begin{vmatrix} 2 & -4 \\ 1 & -4 \end{vmatrix} + 
#     3 \begin{vmatrix} -2 & 3 \\ 2 & -4 \end{vmatrix} = -4 + 3(2) = 2, \\
#     \operatorname{adj} \begin{pmatrix} 1 & -2 & 3 \\ 0 & 2 & -4 \\ 3 & 1 & -4 \end{pmatrix}
#     &= \begin{pmatrix} -4 & -12 & -6 \\ -5 & -13 & -7 \\ 2 & 4 & 2 \end{pmatrix}^T 
#     = \begin{pmatrix} -4 & -5 & 2 \\ -12 & -13 & 4 \\ -6 & -7 & 2 \end{pmatrix}, \\
#     \therefore A^{-1} &= \frac{1}{2}\begin{pmatrix} -4 & -5 & 2 \\ -12 & -13 & 4 \\ -6 & -7 & 2 \end{pmatrix} 
#     = \begin{pmatrix} -2 & -\frac{5}{2} & 1 \\ -6 & -\frac{13}{2} & 2 \\ -3 & -\frac{7}{2} & 1 \end{pmatrix}, \\
#     \therefore \mathbf{x} &= \begin{pmatrix} -2 & -\frac{5}{2} & 1 \\ -6 & -\frac{13}{2} & 2 \\ -3 & -\frac{7}{2} & 1 \end{pmatrix} 
#     \begin{pmatrix}-7 \\ 8 \\ 7 \end{pmatrix}
#     = \begin{pmatrix} 1 \\4 \\ 0 \end{pmatrix}.
# \end{align*}
# 
# Check solution:
# 
# $$A \mathbf{x} = \begin{pmatrix} 1 & -2 &  3 \\ 0 & 2 & -4 \\ 3 & 1 & -4 \end{pmatrix} \begin{pmatrix} 1 \\ 4 \\ 0 \end{pmatrix} = \begin{pmatrix} -7 \\ 8 \\ 7 \end{pmatrix} = \mathbf{b}.$$
# ::::
# :::::
# 
# ## Python code
# 
# The Python code below calculates the solution to the systems of linear equations from [example 2.2](solution-by-inverse-example).

# In[1]:


from sympy import *
from IPython.display import Math

# (i)
A = Matrix([[1, -2], [2, 4]])
b = Matrix([[11], [-18]])
x = A.inv() * b

print("(i) x =")
display(x)

# (ii)
A = Matrix([[1, -2, 3], [0, 2, -4], [3, 1, -4]])
b = Matrix([[-7], [8], [7]])
x = A.inv() * b

print("(ii) x =")
display(x)

