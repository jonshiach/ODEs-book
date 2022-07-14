#!/usr/bin/env python
# coding: utf-8

# # Matrix multiplication
# 
# We can multiply any two real numbers together but multiplication of two or more matrices is a much more complicated idea. Similarly to addition, which is only defined for matrices of the same size, matrix multiplication has constrains on the sizes of the multipliers:
# 
# ::::{admonition} Definition: Matrix multiplication
# :class: note
# :name: matrix-multiplication-definition
# 
# Let $A$ be an $m \times n$ matrix and $B$ a $p \times q$ matrix. The product $AB$ is only defined if $n = p$ and the resulting matrix has dimension $m \times q$ (i.e., the number of columns in $A$ has to equal the number of rows in $B$). The product of an $m\times p$ matrix $A$ and a $p\times n$ matrix $B$ is defined as
# \begin{align*}
#     [AB]_{ij} = \sum_{k=1}^p a_{ik}b_{kj}.
# \end{align*}
# 
# I.e., if $A$ and $B$ are two $2\times 2$ matrices
# \begin{align*}
#     \begin{pmatrix} 
#         a_{11} & a_{12} \\
#         a_{21} & a_{22} 
#     \end{pmatrix}
#     \begin{pmatrix} 
#         b_{11} & b_{12} \\
#         b_{21} & b_{22}
#     \end{pmatrix} =
#     \begin{pmatrix}
#         a_{11} b_{11} + a_{12}b_{21} & a_{11}b_{12} + a_{12} b_{22} \\
#         a_{21} b_{11} + a_{22}b_{21} & a_{21}b_{12} + a_{22} b_{22}
#     \end{pmatrix}.
# \end{align*}
# ::::
# 
# The technique used to multiply two matrices together requires us to move across the horizontal rows of the first matrix (the $i$ index) and down the vertical columns of the second matrix (the $j$ index). We multiply corresponding elements together and sum the result. For example, consider the multiplication of the two $2\times 2$ matrices below
# 
# \begin{align*}
#     \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}.
# \end{align*}
# 
# The first thing we need to do is check whether matrix multiplication is defined for these matrices. An easy way to do this is to write the dimensions of the matrix underneath, e.g.,
# 
# \begin{align*}
#     \underbrace{\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}}_{2\times \mathbf{\textcolor{red}{2}}}
#     \underbrace{\begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}}_{\mathbf{\textcolor{red}{2}}\times 2}.
# \end{align*}
# 
# Here the two inside numbers are the same so this matrix multiplication is defined. Also, the dimensions of the product of these two matrices is given by the two outside numbers. To calculate the value of the element in row 1 and column 1 of the product of $[AB]_{11}$, we move across row 1 of the first matrix and down column 1 of the second matrix
# 
# \begin{align*}
#     \begin{pmatrix} \textcolor{blue}{1} & \textcolor{blue}{2} \\ 3 & 4 \end{pmatrix}
#     \begin{pmatrix} \textcolor{red}{5} & 6 \\ \textcolor{red}{7} & 8 \end{pmatrix} = 
#     \begin{pmatrix} 
#         \textcolor{blue}{1} \times \textcolor{red}{5} + \textcolor{blue}{2} \times \textcolor{red}{7} & \square \\
#         \square & \square
#     \end{pmatrix} 
#     = \begin{pmatrix} 5 + 14 & \square \\ \square & \square \end{pmatrix}
#     = \begin{pmatrix} 19 & \square \\ \square & \square \end{pmatrix}.
# \end{align*}
# 
# For the element in the first row and second column, $[AB]_{12}$, we move across row 1 of the first matrix and down column 2 of the second matrix
# 
# \begin{align*}
#     \begin{pmatrix} \textcolor{blue}{1} & \textcolor{blue}{2} \\ 3 & 4 \end{pmatrix}
#     \begin{pmatrix} 5 & \textcolor{red}{6} \\ 7 & \textcolor{red}{8} \end{pmatrix} = 
#     \begin{pmatrix} 
#         19 & \textcolor{blue}{1} \times \textcolor{red}{6} + \textcolor{blue}{2} \times \textcolor{red}{8} \\
#         \square & \square
#     \end{pmatrix}
#     = \begin{pmatrix} 19 & 6 + 16 \\ \square & \square \end{pmatrix}
#     = \begin{pmatrix} 19 & 22 \\ \square & \square \end{pmatrix}.
# \end{align*}
# 
# Now that we have finished the top row, to calculate the element in row 2 column 1, $[AB]_{21}$, we move across row 2 of the first matrix and down column 1 of the second matrix
# 
# \begin{align*}
#     \begin{pmatrix} 1 & 2 \\ \textcolor{blue}{3} & \textcolor{blue}{4} \end{pmatrix}
#     \begin{pmatrix} \textcolor{red}{5} & 6 \\ \textcolor{red}{7} & 8 \end{pmatrix} = 
#     \begin{pmatrix} 
#         19 & 22 \\
#         \textcolor{blue}{3} \times \textcolor{red}{5} + \textcolor{blue}{4} \times \textcolor{red}{7} & \square
#     \end{pmatrix}
#     = \begin{pmatrix} 19 & 22 \\ 15 + 28 & \square \end{pmatrix}
#     = \begin{pmatrix} 19 & 22 \\ 43 & \square \end{pmatrix}.
# \end{align*}
# 
# Finally to calculate the elements in row 2 column 2, $[AB]_{22}$, we move across row 2 of the first matrix and down column 2 of the second matrix 
# 
# \begin{align*}
#     \begin{pmatrix} 1 & 2 \\ \textcolor{blue}{3} & \textcolor{blue}{4} \end{pmatrix}
#     \begin{pmatrix} 5 & \textcolor{red}{6} \\ 7 & \textcolor{red}{8} \end{pmatrix} = 
#     \begin{pmatrix} 
#         19 & 22 \\
#         43 & \textcolor{blue}{3} \times \textcolor{red}{6} + \textcolor{blue}{4} \times \textcolor{red}{8}
#     \end{pmatrix}
#     = \begin{pmatrix} 19 & 22 \\ 43 & 18 + 32 \end{pmatrix}
#     = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}.
# \end{align*}
# 
# :::::{admonition} Example 1.5
# :class: seealso
# :name: matrix-multiplication-example
# 
# Given the matrices
# \begin{align*}
#     A &= \begin{pmatrix} 1 & 0 \\ -2 & 3 \end{pmatrix}, &
#     B &= \begin{pmatrix} 2 & 3 \\ 1 & 5 \end{pmatrix}, \\
#     C &= \begin{pmatrix} 1 & 1 & 0 \\ 3 & -2 & 1 \end{pmatrix}, &
#     D &= \begin{pmatrix} 1 \\ 3 \end{pmatrix}.
# \end{align*}
# 
# calculate the following (where possible):
# 
# ::::{grid}
# 
# :::{grid-item}
# :columns: 2
# (i) &emsp; $AB$
# :::
# 
# :::{grid-item}
# :columns: 2
# (ii) &emsp; $BC$
# :::
# 
# :::{grid-item}
# :columns: 2
# (iii) &emsp; $CD$
# :::
# 
# ::::
# 
# ::::{dropdown} Solution
# 
# (i) 
# \begin{align*}
#     AB &= \begin{pmatrix} 1 & 0 \\ -2 & 3 \end{pmatrix} \begin{pmatrix} 2 & 3 \\ 1 & 5 \end{pmatrix} \\
#     &= \begin{pmatrix} 2+0 & 3 + 0 \\ -4+3 & -6+15\end{pmatrix} \\
#     &= \begin{pmatrix} 2 & 3 \\ -1 & 9 \end{pmatrix}
# \end{align*}
# 
# (ii) 
# \begin{align*}
#     BC &= \begin{pmatrix} 2 & 3 \\ 1 & 5 \end{pmatrix} \begin{pmatrix} 1 & 1 & 0 \\ 3 & -2 & 1 \end{pmatrix} \\
#     &= \begin{pmatrix} 2+9 & 2-6 & 0+3 \\ 1+15 & 1-10 & 0+5 \end{pmatrix} \\
#     &= \begin{pmatrix}11 & -4 & 3 \\ 16 & -9 & 5 \end{pmatrix}
# \end{align*}
# 
# (iii) &emsp; $CD$ is undefined since $C$ is $2\times 3$ and $D$ is $2\times 1$.
# ::::
#     
# :::::
# 
# ## Python code
# 
# The Sympy command for calculating the product of two matrices `A` and `B` is `A * B`. The Python code below calculates the solution to question (i) from [example 1.5](matrix-multiplication-example). 

# In[1]:


from sympy import *

A = Matrix([[1, 0], [-2, 3]])
B = Matrix([[2, 3], [1, 5]])
AB = A * B
display(AB)


# Note that this will only work when using the Sympy library. If this has not been imported, `A * B` will multiply the corresponding elements together which is known as **element-wise multiplication** and denoted mathematically as $A \odot B$. If you are using Sympy and wish to use element-wise multiplication then the command is `matrices.dense.matrix_multiply_elementwise(A, B)` (so it is probably better to not use Sympy in this case!).

# ## Matrix exponents
# 
# ::::{admonition} Definition: Matrix exponents
# :class: note
# :name: matrix-exponents-definition
# 
# 
# Let $A$ be a square $n \times n$ matrix. Then we write $A^2=AA$ and more generally:
# \begin{align}
#     A^n = \underbrace{A A \cdots A}_{n \text{ times}}.
# \end{align}
# ::::
# 
# :::::{admonition} Example 1.6
# :class: seealso
# :name: matrix-exponents-example
# 
# Given the matrix 
# $
#     A = \begin{pmatrix} 1 & 0 \\ 3 & 2 \end{pmatrix},
# $
# evaluate:
# 
# ::::{grid}
# 
# :::{grid-item}
# :columns: 2
# (i) &emsp; $A^2$
# :::
# 
# :::{grid-item}
# :columns: 2
# (ii) &emsp; $A^3$
# :::
# 
# :::{grid-item}
# :columns: 2
# (iii) &emsp; $A^5$
# :::
# 
# ::::
# 
# ::::{dropdown} Solution
# 
# (i) 
# \begin{align*}
#     A^2 &= AA = \begin{pmatrix} 1 & 0 \\ 3 & 2 \end{pmatrix}
#     \begin{pmatrix} 1 & 0 \\ 3 & 2 \end{pmatrix} \\
#     &= \begin{pmatrix} 1 + 0 & 0 + 0 \\ 3 + 6 & 0 + 4 \end{pmatrix} \\
#     &= \begin{pmatrix} 1 & 0 \\ 9 & 4 \end{pmatrix}
# \end{align*}
# 
# (ii) 
# \begin{align*}
#     A^3 &= A^2A = \begin{pmatrix} 1 & 0 \\ 9 & 4 \end{pmatrix}
#     \begin{pmatrix} 1 & 0 \\ 3 & 2 \end{pmatrix} \\
#     &= \begin{pmatrix} 1 + 0 & 0 + 0 \\ 9 + 12 & 0 + 8 \end{pmatrix} \\
#     &= \begin{pmatrix} 1 & 0 \\ 21 & 8 \end{pmatrix}
# \end{align*}
# 
# (iii)
# \begin{align*}
#     A^5 &= A^3A^2 = \begin{pmatrix} 1 & 0 \\ 21 & 8 \end{pmatrix}
#     \begin{pmatrix} 1 & 0 \\ 9 & 4 \end{pmatrix} \\
#     &= \begin{pmatrix} 1 + 0 & 0 + 0 \\ 21 + 72 & 0 + 32 \end{pmatrix} \\
#     &= \begin{pmatrix} 1 & 0 \\ 93 & 32 \end{pmatrix}
# \end{align*}
# ::::
# :::::
# 
# ### Python code
# 
# The SymPy command for calculating the `k`th exponent of the matrix `A` is `A ** k`. The following code calculates the solution to [example 1.6](matrix-exponents-example).

# In[2]:


A = Matrix([[1, 0], [3, 2]])

# (i)
print("(i) A^2 =")
display(A ** 2)

# (ii)
print("(ii) A^3 =")
display(A ** 3)

# (iii)
print("(iii) A^5 =")
display(A ** 5)

