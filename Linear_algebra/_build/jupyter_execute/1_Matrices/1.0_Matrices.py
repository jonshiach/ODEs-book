#!/usr/bin/env python
# coding: utf-8

# (matrices-chapter)=
# # Matrices
# 
# 
# **Learning outcomes**
# 
# On successful completion of this chapter students will be able to:
# 
# -  define and [index](indexing-a-matrix-section) matrices;
# -  perform the arithmetic operations of [addition](matrix-addition-section), [multiplication by a scalar](scalar-multiplication-of-matrices), [matrix multiplication](matrix-multiplication-definition), [matrix exponents](matrix-exponents-definition) and [matrix transpose](matrix-transpose-definition);  
# -  recognise and define special matrices such as [diagonal matrices](diagonal-matrix-definition), the [zero matrix](zero-matrix-definition), the [identity matrix](identity-matrix-definition) and [symmetric matrices](symmetric-matrix-definition);
# -  calculate the determinant of a [$2\times 2$](2x2-determinant-definition) and [$n\times n$](nxn-determinant-definition) matrix, the [adjoint](adjoint-definition) and [inverse](inverse-matrix-definition) of a non-singular square matrix using the [adjoint-determinant formula](adjoint-determinant-formula-definition);
# - perform [algebraic manipulation](matrix-algebra-section) of equations involving matrices. 
# 
# ---
# 
# (definition-of-a-matrix-section)=
# ## Definition of a matrix
# 
# A **matrix** (plural **matrices**) is a rectangular array of elements which can be numbers, mathematical expressions, symbols, or even other matrices. Matrices are arranged in rows and columns and enclosed by parentheses (or sometimes square brackets), for example
# 
# \begin{align*}
#     \begin{pmatrix}
#         1 & 2 & 3 \\
#         4 & 5 & 6
#     \end{pmatrix}.
# \end{align*}
#     
# This matrix contains 6 elements arranged in 2 (horizontal) rows and 3 (vertical) columns.
# 
# ::::{admonition} Definition: Dimension of a matrix
# :class: note
# :name: dimension-of-a-matrix-definition
# 
# The dimension or size of a matrix is defined to be **rows** $\times$ **columns**, where 'rows' is the number of horizontal rows and 'columns' the number of vertical columns of said matrix. If rows $=$ columns we say that the matrix is a square matrix.
# ::::
# 
# :::::{admonition} Example 1.1
# :class: seealso
# :name: matrix-dimension-example
# 
# Determine the dimensions of the following matrices:
# 
# ::::{grid}
# :gutter: 2
# 
# :::{grid-item}
# :columns: 6
# (i) &emsp; $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 6
# (ii) &emsp; $B = \begin{pmatrix} a & b \\ c & d \\ e & f \end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 6
# (iii) &emsp; $C = \begin{pmatrix} \sin(x) & \ln(x) & \cos(x+1) \end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 6
# (iv) &emsp; $D = \begin{pmatrix} 0 \end{pmatrix}$
# :::
# 
# ::::
# 
# ::::{dropdown} Solution
# 
# (i) &emsp; $2\times 2 $
# 
# (ii) &emsp; $3\times 2$
# 
# (iii) &emsp; $1 \times 3$
# 
# (iv) &emsp; $1 \times 1$
# ::::
# :::::
# 
# ### Python code
# 
# To define and perform operations on matrices in Python we can use the **SymPy** library (short for *symbolic Python*) library. A matrix can then be defined using the `Matrix` command, for example

# In[1]:


from sympy import *

A = Matrix([[1, 2], [3, 4]])
display(A)


# Note that the matrix is defined using square brackets and each row is contained within another pair of square brackets. Commas separate elements in the same row and the different rows of a matrix. 
# 
# The command for determining the number of rows and columns of a matrix `A` is `A.shape` which returns a 2-tuple containing. The following code defines the matrix $A$ from [example 1.1](matrix-dimension-example) and outputs its dimensions

# In[2]:


nrows, ncols = A.shape
print(f"The matrix A is an {nrows} x {ncols} matrix")


# (indexing-a-matrix-section)=
# ## Indexing a matrix
# 
# Matrices are typically labeled using uppercase characters (e.g. $A$) and the elements of a matrix are labeled with the corresponding lowercase character (e.g. $a$). Individual entries of a matrix are **indexed** using two subscript indices: $a_{ij}$ where $i$ corresponds to the row number reading from top to bottom and $j$ is the column number reading from left to right. 
# 
# For example, let $A$ be an $m\times n$ matrix then
# 
# $$A = \begin{pmatrix}
#   a_{11} & a_{12} & \cdots & a_{1n} \\
#   a_{21} & a_{22} & \cdots & a_{2n} \\
#   \vdots & \vdots & \ddots & \vdots \\
#   a_{m1} & a_{m2} & \cdots & a_{mn} 
# \end{pmatrix}.$$
# 
# Some alternate notation includes
# 
# $$a_{ij} = [A]_{ij} = A[i,j].$$
# 
# :::::{admonition} Example 1.2
# :class: seealso
# :name: matrix-indexing-example
# 
# Given the matrix 
# $A = \begin{pmatrix}
#     2 & 0 & -3 \\
#     1 & 7 & 4 
# \end{pmatrix},$ 
# 
# write down the following elements:
# 
# 
# ::::{grid}
# :::{grid-item}
# (i) &emsp; $a_{11}$
# :::
# 
# :::{grid-item}
# (ii) &emsp; $a_{13}$
# :::
# 
# :::{grid-item}
# (iii) &emsp; $[A]_{21}$
# :::
# 
# :::{grid-item}
# (iv) &emsp; $A[2,2]$
# :::
# ::::
# 
# ::::{dropdown} Solution
# 
# (i)  $a_{11} = 2$
# 
# (ii) $a_{13} = -3$
# 
# (iii) $[A]_{21} = 1$
# 
# (iv) $A[2,2] = 7$
#     
# ::::
# :::::
# 
# ### Python code
# 
# Matrices and arrays in Python are indexed using the syntax `A[i,j]` which returns the value of the element in row `i` and column `j`. 
# 
# :::{important}
# Python is a **zero indexing** language which means indexing starts at zero. So to index the element $a_{23}$ we would use `a[1,2]` i.e., remember to subtract 1 from the indices.
# :::
# 
# The following code defines the matrix $A$ from [example 1.2](matrix-indexing-example) and outputs the values of the indexed elements. 

# In[3]:


A = Matrix([[2, 0, -3], [1, 7, 4]])

print(f"(i)   a_11 = {A[0,0]}")
print(f"(ii)  a_13 = {A[0,2]}")
print(f"(iii) [A]_21 = {A[1,0]}")
print(f"(iv)  A[2,2] = {A[1,1]}")


# (basic-arithmetic-operations-section)=
# ## Basic arithmetic operations
# 
# So far, we have given a fancy name to a rectangular array of objects and showed how we can index its elements. Now we are going to fully develop an algebra for matrices. A system, where there are operations of addition and multiplication and necessarily rules that accompany them. This system resembles that of real numbers but we will see some differences and new concepts. For simplicity, we are going to assume that the entries of our matrices are numbers, however the developed theory applies to a broader range of objects.
# 
# ### Matrix equality
# 
# ::::{admonition} Definition: Matrix equality 
# :class: note
# :name: matrix-equality-definition
# 
# We say that an $m \times n$ matrix $A$ and an $p \times q$ matrix $B$ are **equal** and write $A = B$ if and only if **both** of the following conditions are satisfied:
# 
# - they have the same dimensions, in other words $m = p$ and $n = q$;
# - for all $1 \leq i \leq m$ and $1 \leq j \leq n$, $a_{ij} = b_{ij}$.
# ::::
# 
# For example, consider the following matrices
# 
# \begin{align*}
#     A &= \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, &
#     B &= \begin{pmatrix} 1 & 2 & 5 \\ 3 & 4 & 6 \end{pmatrix}, &
#     C &= \begin{pmatrix} 3^0 & \sqrt{4} \\ 1 + 2 & 2^2 \end{pmatrix}.
# \end{align*}
# 
# Here $A \neq B$ since $A$ has 2 columns and $B$ has 3 columns. However, $A=C$ because both $A$ and $C$ have the same number of rows and columns and all of the corresponding elements are equal.
# 
# (matrix-addition-section)=
# ### Matrix addition
# 
# ::::{admonition} Definition: Matrix addition and subtraction 
# :class: note
# :name: matrix-addition-definition
# 
# Let $A$ and $B$ be two $m \times n$ matrices. The addition or subtraction of two $m \times n$ matrices $A$ and $B$ is an $m \times n$ matrix $A \pm B$ defined by:
# 
# $$[A \pm B]_{ij} = a_{ij} \pm a_{ij},$$
#     
# where $1 \leq i \leq m$ and $1 \leq j \leq n$.
# \begin{align*}
#     \begin{pmatrix}
#         a_{11} & a_{12} & \cdots & a_{1n} \\
#         a_{21} & a_{22} & \cdots & a_{2n} \\
#         \vdots & \vdots & \ddots & \vdots \\
#         a_{m1} & a_{m2} & \cdots & a_{mn}
#     \end{pmatrix} \pm 
#     \begin{pmatrix}
#         b_{11} & b_{12} & \cdots & b_{1n} \\
#         b_{21} & b_{22} & \cdots & b_{2n} \\
#         \vdots & \vdots & \ddots & \vdots \\
#         b_{m1} & b_{m2} & \cdots & b_{mn}
#     \end{pmatrix} \\
#     =
#     \begin{pmatrix}
#         a_{11} \pm b_{11} & a_{12} \pm b_{12} & \cdots & a_{1n} \pm b_{1n} \\
#         a_{21} \pm b_{21} & a_{22} \pm b_{22} & \cdots & a_{2n} \pm a_{2n} \\
#         \vdots & \vdots & \ddots & \vdots \\
#         a_{m1} \pm b_{m1} & a_{m2} \pm b_{m2} & \cdots & a_{mn} \pm b_{mn}
#     \end{pmatrix}.
# \end{align*}
# ::::
# 
# The addition and subtraction of two matrices of different sizes is **not defined**.
# 
# ::::{admonition} Theorem: Properties of matrix addition
# :class: important
# :name: properties-of-matrix-addition-theorem
# 
# For all $m \times n$ matrices $A,B$ and $C$, the following conditions are satisfied:
# 
# - matrix addition is commutative, i.e., $A + B = B + A$;
# - matrix addition is associative, i.e., $A + (B + C) = (A + B) + C$.
# ::::
# 
# :::::{admonition} Example 1.3
# :class: seealso
# :name: matrix-addition-example
# 
# Evaluate the following:
# 
# ::::{grid}
# :gutter: 2
# 
# :::{grid-item}
# (i) $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$
# :::
# 
# :::{grid-item}
# (ii) $\begin{pmatrix} 2 \\ 3 \\ 5 \end{pmatrix} - \begin{pmatrix} 7 \\ -11 \\ -13 \end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 12
# 
# (iii) $\begin{pmatrix} 1 & 3 & 5 \\ 7 & 9 & 11 \end{pmatrix} + \begin{pmatrix}2 & 3 \\ 5 & 7 \end{pmatrix}$
# :::
# ::::
# 
# ::::{dropdown} Solution
# 
# (i) $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} 1 + 5 & 2 + 6 \\ 3 + 7 & 4 + 8 \end{pmatrix}= \begin{pmatrix}6 & 8 \\ 10 & 12 \end{pmatrix}$
# 
# (ii) $\begin{pmatrix} 2 \\ 3 \\ 5 \end{pmatrix} - \begin{pmatrix} 7 \\ -11 \\ -13 \end{pmatrix} = \begin{pmatrix}2 - 7 \\ 3 + 11 \\ 5 + 13 \end{pmatrix} = \begin{pmatrix} -5 \\ 14 \\ 18\end{pmatrix}$
# 
# (iii) undefined since the left matrix is $2\times 3$ and the right matrix is $2\times 2$
# ::::
# :::::
# 
# #### Python code
# 
# The Python command for calculating the sum of two matrices `A` and `B` is simply `A + B`. The Python code below calculates the solution to question (i) from [example 1.3](matrix-addition-example).

# In[4]:


A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

AplusB = A + B
display(AplusB)


# (scalar-multiplication-of-matrices)=
# ### Scalar multiplication of matrices
# 
# ::::{admonition} Definition: Scalar multiplication 
# :class: note
# :name: scalar-multiplication-of-a-matrix-definition
# 
# The scalar multiplication of an $m \times n$ matrix by a scalar is calculated by multiplying each element in the matrix by the scalar
# 
# \begin{align*}
#     k[A]_{ij} = ka_{ij}, \qquad i = 1, \ldots, m, \quad j = 1, \ldots, n.
# \end{align*}
# 
# \begin{align*}
#     k \begin{pmatrix}
#         a_{11} & a_{12} & \cdots & a_{1n} \\
#         a_{21} & a_{22} & \cdots & a_{2n} \\
#         \vdots & \vdots & \ddots & \vdots \\
#         a_{m1} & a_{m2} & \cdots & a_{mn}
#     \end{pmatrix} = 
#     \begin{pmatrix}
#         ka_{11} & ka_{12} & \cdots & ka_{1n} \\
#         ka_{21} & ka_{22} & \cdots & ka_{2n} \\
#         \vdots & \vdots & \ddots & \vdots \\
#         ka_{m1} & ka_{m2} & \cdots & ka_{mn}
#     \end{pmatrix}
# \end{align*}
# ::::
# 
# ::::{admonition} Theorem: Properties of scalar multiplication of matrices
# :class: important
# :name: properties-of-scalar-multiplication-of-matrices-theorem
# 
# Let $A$ and $B$ be two $m \times n$ matrices and $k$ and $\ell$ are scalars, then
# 
# - scalar multiplication is commutative: $kA=Ak$;
# - scalar multiplication is distributive over matrix addition: $k(A + B) = kA + kB$;
# - scalar multiplication is distributive over scalar addition: $(k+\ell)A = kA + \ell A$;
# - scalar multiplication is associative: $k(\ell A) = (k \ell)A$;
# - multiplication by $-1$ gives the additive inverse: $(-1)A = -A$.
# 
# ::::
# 
# :::::{admonition} Example 1.4
# :class: seealso
# :name: scalar-multiplication-of-matrices-example
# 
# Evaluate the following:
# 
# ::::{grid}
# :gutter: 2
# 
# :::{grid-item}
# :columns: 6
# (i) $2 \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 6
# (ii) $\dfrac{1}{2} \begin{pmatrix} 0 & -1 \\ 3 & 2 \\ 4 & -2 \end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 6
# (iii) $\dfrac{1}{3} \begin{pmatrix}1 & 6 & 4 \\ 0 & 3 & -1 \end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 6
# (iv) $101 \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} - 99 \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$
# :::
# 
# ::::
# 
# ::::{dropdown} Solution
# 
# (i) $2 \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix}2 & 4 \\ 6 & 8 \end{pmatrix}$
# 
# (ii) $\dfrac{1}{2} \begin{pmatrix} 0 & -1 \\ 3 & 2 \\ 4 & -2 \end{pmatrix} =  \begin{pmatrix} 0 & -\frac{1}{2} \\ \frac{3}{2} & 1 \\ 2 & -1 \end{pmatrix}$
# 
# (iii) $\dfrac{1}{3} \begin{pmatrix}1 & 6 & 4 \\ 0 & 3 & -1 \end{pmatrix} = \begin{pmatrix} \frac{1}{3} & 2 & \frac{4}{3} \\ 0 & 1 & -\frac{1}{3} \end{pmatrix}$
# 
# (iv) $101\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} - 99 \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = 2 \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} =  \begin{pmatrix} 2 & 4 \\ 0 & 2 \end{pmatrix}$
# 
# ::::
# :::::
# 
# ### Python code
# 
# The command for multiplying a SymPy matrix `A` by a scalar `k` is simply `k * A`. The following code calculates the solutions [example 1.4](scalar-multiplication-of-matrices-example).

# In[5]:


# (i)
A = Matrix([[1, 2], [3, 4]])

print("(i)")
display(2 * A)

# (ii)
B = Matrix([[0, -1], [3, 2], [4, -2]])
print("(ii)")
display(B / 2)

# (iii)
C = Matrix([[1, 6, 4], [0, 3, -1]])
print("(iii)")
display(C / 3)

# (iv)
D = Matrix([[1, 2], [0, 1]])
print("(iv)")
display(101 * D - 99 * D)

