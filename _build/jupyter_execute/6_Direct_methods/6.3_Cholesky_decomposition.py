#!/usr/bin/env python
# coding: utf-8

# (cholesky-section)=
# # Cholesky decomposition
# 
# **Cholesky decomposition** is an efficient matrix decomposition method that can be used when a square matrix is **positive definite**.
# 
# ````{admonition} Definition: Positive definite matrix
# :class: note
# :name: positive-definite-definition
# 
# A square matrix $A$ is said to be positive definite if
# \begin{align*}
#     \mathbf{x}^T A \mathbf{x} > 0 \text{ for all } \mathbf{x} \in \mathbb{R}^n \backslash \{\mathbf{0}\}.
# \end{align*}
# ````
# 
# ````{admonition} Theorem: Determinant test for a positive definite matrix
# :class: important
# :name: determinant-test-for-positive-definte-matrix-theorem
# 
# A square matrix $A$ is positive definite if it is symmetric and the determinants of all $k \times k$ upper-left sub-matrices are all positive.
# ````
# 
# ````{admonition} Example 6.5
# :class: seealso
# :name: positive-definite-example
# 
# Use the determinant test to show that the following matrix is positive definite
# 
# \begin{align*}
#     A = \begin{pmatrix}
#         2 & -1 & 0 \\
#         -1 & 2 & -1 \\
#         0 & -1 & 2
#     \end{pmatrix}.
# \end{align*}
# 
# ```{dropdown} Solution
# 
# Matrix $A$ is symmetric since $A=A^T$. Checking the determinants of the upper-left sub-matrices
# 
# \begin{align*}
#     \det(2) &= 2 > 0, \\
#     \det\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} &= 4 - 1 = 3 > 0, \\
#     \det\begin{pmatrix}
#         2 & -1 & 0 \\
#         -1 & 2 & -1 \\
#         0 & -1 & 2
#     \end{pmatrix}
#     &= 6 - 2 + 0 = 4 > 0 .
# \end{align*}
# 
# Since $A$ is a symmetric matrix and all the determinants of the upper-left sub-matrices are positive then $A$ is a positive definite matrix.
# 
# ```
# ````
# 
# Given a positive definite matrix $A$ then Cholesky decomposition factorises $A$ into the product of a lower triangular matrix $L$ and its transpose, i.e.,
# 
# \begin{align*}
#     A = LL^T.
# \end{align*}
# 
# Consider the Cholesky decomposition of a $3\times 3$ matrix
# 
# \begin{align*}
#     \begin{pmatrix}
#         a_{11}  & a_{12}  & a_{13} \\
#         a_{21}  & a_{22}  & a_{23} \\
#         a_{31}  & a_{32}  & a_{33} 
#     \end{pmatrix} &= 
#     \begin{pmatrix}
#         \ell_{11}  & 0 & 0 \\
#         \ell_{21}  & \ell_{22}  & 0 \\
#         \ell_{31}  & \ell_{32}  & \ell_{33} 
#     \end{pmatrix}
#     \begin{pmatrix}
#         \ell_{11}  & \ell_{21}  & \ell_{31} \\
#         0 & \ell_{22}  & \ell_{32} \\
#         0 & 0 & \ell_{33} 
#     \end{pmatrix}\\
#     &= 
#     \begin{pmatrix}
#         \ell_{11}^2  & \ell_{11} \ell_{21}  & \ell_{11} \ell_{31} \\
#         \ell_{11} \ell_{21}  & \ell_{21}^2 +\ell_{22}^2  & \ell_{21} \ell_{31} +\ell_{22} \ell_{33} \\
#         \ell_{11} \ell_{31}  & \ell_{21} \ell_{31} +\ell_{22} \ell_{33}  & \ell_{31}^2 +\ell_{32}^2 +\ell_{33}^2 
#     \end{pmatrix}.
# \end{align*}
# 
# The elements on the main diagonal are
# 
# \begin{align*}
#     a_{jj} =\ell_{jj}^2 +\sum_{k=1}^{j-1} \ell_{jk}^2 ,
# \end{align*}
# 
# and the other elements are
# 
# \begin{align*}
#     a_{ij} =\sum_{k=1}^j \ell_{ik} \ell_{jk} = \ell_{jj} \ell_{ij} +\sum_{k=1}^{j-1} \ell_{ik} \ell_{jk}.
# \end{align*}
# 
# Rearranging these expressions gives the following definition
# 
# ````{admonition} Definition: Cholesky decomposition
# :class: note
# :name: cholesky-definition
# 
# The Cholesky decomposition of an $n \times n$ positive-definite matrix $A$ results in an $n \times n$ matrix $L$ such that $A = LL^T$. The elements of $L$ are calculated using
# 
# ```{math}
# :label: cholesky-equation
# 
# \begin{align}
#     \ell_{jj} &= \sqrt{a_{jj} - \sum_{k=1}^{j-1} \ell_{jk}^2 }, & j &= 1, \ldots, n,\\
#     \ell_{ij} &= \dfrac{1}{\ell_{jj} }\left(a_{ij} -\displaystyle \sum_{k=1}^{i-1} \ell_{ik} \ell_{jk} \right), & i &= j + 1,\ldots ,n.
# \end{align}
# ```
# ````
# 
# ````{admonition} Example 6.6
# :class: seealso
# :name: cholesky-example
# 
# Calculate the Cholesky decomposition of the following matrix
# 
# \begin{align*}
#     A = \begin{pmatrix}
#         4 & -2 & -4\\
#         -2 & 10 & 5\\
#         -4 & 5 & 14
#     \end{pmatrix}.
# \end{align*}
# 
# ```{dropdown} Solution
# 
# Stepping through the columns of $A$ and using equation {eq}`cholesky-equation`
# 
# \begin{align*}
#     j &= 1: & \ell_{11} &= \sqrt{a_{11}} = \sqrt{4} = 2,\\
#     && \ell_{21} &= \frac{1}{\ell_{11}}(a_{21}) = \frac{1}{2}(-2) = -1,\\
#     && \ell_{31} &= \frac{1}{\ell_{11}}(a_{31}) = \frac{1}{2}(-4) = -2,\\
#     \\
#     j &= 2: & \ell_{22} &= \sqrt{a_{22} - \ell_{21}^2} = \sqrt{10 - (-1)^2} = \sqrt{9} = 3,\\
#     && \ell_{32} &= \frac{1}{\ell_{22}}(a_{32} - \ell_{31} \ell_{21}) = \frac{1}{3}(5 - (-2)(-1)) = 1,\\
#     \\
#     j &= 3: & \ell_{33} &= \sqrt{a_{33} - \ell_{31}^2 - \ell_{32}^2} = \sqrt{14 - (-2)^2 - 1^2} = \sqrt{9} = 3,
# \end{align*}
# 
# therefore
# 
# $L=\begin{pmatrix} 2 & 0 & 0 \\ -1 & 3 & 0 \\ -2 & 1 & 3 \end{pmatrix}$. Checking that $A = LL^T$
# 
# \begin{align*}
#     \begin{pmatrix}
#         2 & 0 & 0\\
#         -1 & 3 & 0\\
#         -2 & 1 & 3
#     \end{pmatrix}
#     \begin{pmatrix}
#         2 & -1 & -2\\
#         0 & 3 & 1\\
#         0 & 0 & 3
#     \end{pmatrix} =
#     \begin{pmatrix}
#         4 & -2 & -4\\
#         -2 & 10 & 5\\
#         -4 & 5 & 14
#     \end{pmatrix}.
# \end{align*}
# 
# ```
# ````
# 
# ## Python code
# 
# The code below defines the function called `cholesky()` which calculates the Cholesky decomposition of a square matrix `A`. If `A` is not positive-definite then it returns and error message.

# In[1]:


import numpy as np


# In[5]:


def cholesky(A):
    n = A.shape[0]
    for i in range(n):
        if np.linalg.det(A[:n,:n]) < 0:
            print("Error! A is not a positive definite matrix")
            return
        
    L = np.zeros((n, n))   
    for j in range(n):
        for i in range(j, n):
            for k in range(j):
                L[i,j] += L[i,k] * L[j,k]
                
            if i == j:
                L[i,j] = np.sqrt(A[i,j] - L[i,j])
            else:
                L[i,j] = 1 / L[j,j] * (A[i,j] - L[i,j])   
    
    return L


# The code below calculates the Cholesky decomposition of the matrix from [example 6.6](cholesky-example).

# In[6]:


# Define matrix
A = np.array([[4, -2, -4], [-2, 10, 5], [-4, 5, 14]])

# Calculate Cholesky decomposition
L = cholesky(A)

print(f"L = \n{L}\n")


# (cholesky-crout-method-section)=
# ## The Cholesky-Crout method
# 
# The **Cholesky-Crout method** is used to solve a system of linear equations of the form $A\mathbf{x}=\mathbf{b}$ where $A$ is a positive definite matrix. Let $\mathbf{y} = L^T \mathbf{x}$ then since $A=LL^T$
# 
# \begin{align*}
#     L \mathbf{y} &= \mathbf{b}, \\
#     L^T \mathbf{x} &= \mathbf{y}.
# \end{align*}
# 
# ````{admonition} Example 6.7
# :class: seealso
# :name: cholesky-crout-example
# 
# Solve the following system of linear equations using the Cholesky-Crout method.
# 
# \begin{align*}
#     \begin{pmatrix}
#         4 & -2 & -4\\
#         -2 & 10 & 5\\
#         -4 & 5 & 14
#     \end{pmatrix}
#     \begin{pmatrix}
#         x_1 \\ x_2 \\ x_3 \end{pmatrix} =
#     \begin{pmatrix} -2 \\ 49 \\ 27 \end{pmatrix}.
# \end{align*}
# 
# ```{dropdown} Solution
# 
# We saw in [example 6.6](cholesky-example) that the Cholesky decomposition of the matrix $A$ is
# 
# $L=\begin{pmatrix} 2 & 0 & 0 \\ -1 & 3 & 0 \\ -2 & 1 & 3 \end{pmatrix}$. Solving $L\mathbf{y}=\mathbf{b}$ using forward substitution
# 
# \begin{align*}
#     \begin{pmatrix}
#         2 & 0 & 0\\
#         -1 & 3 & 0\\
#         -2 & 1 & 3
#     \end{pmatrix}
#     \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix} =
#     \begin{pmatrix} -2 \\ 49 \\ 27 \end{pmatrix},
# \end{align*}
# 
# gives
# 
# \begin{align*}
#     y_1 &=\frac{-2}{2}=-1,\\
#     y_2 &=\frac{1}{3}(49+y_1 )=\frac{1}{3}(49-1)=16,\\
#     y_3 &=\frac{1}{3}(27+2y_1 -y_2 )=\frac{1}{3}(27+2(-1)-16)=3.
# \end{align*}
# 
# Solving $L^T \mathbf{x}=\mathbf{y}$ using back substitution
# 
# \begin{align*}
#     \begin{pmatrix}
#         2 & -1 & -2\\
#         0 & 3 & 1\\
#         0 & 0 & 3
#     \end{pmatrix}
#     \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} =
#     \begin{pmatrix} -1 \\ 16 \\ 3 \end{pmatrix},
# \end{align*}
# 
# gives
# 
# \begin{align*}
#     x_3 &=\frac{3}{3}=1,\\
#     x_2 &=\frac{1}{3}(16-x_3 )=\frac{1}{3}(16-1)=5,\\
#     x_1 &=\frac{1}{2}(-1+x_2 +2x_3 )=\frac{1}{2}(-1+5+2(1))=3.
# \end{align*}
# 
# So the solution is $\mathbf{x}=(3,5,1)$.
# 
# ```
# ````
# 
# ## Python code
# 
# The code below solves the system of linear equations from [example 6.7](cholesky-crout-example) using the Cholesky-Crout method.

# In[ ]:


def forward_substitution(L, b):
    n = L.shape[0]
    x = np.zeros(n)
    for i in range(n):
        for j in range(i):
            x[i] += L[i,j] * x[j]
            
        x[i] = 1 / L[i,i] * (b[i] - x[i])
    
    return x


def back_substitution(U, b):
    n = U.shape[0]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            x[i] += U[i,j] * x[j]
            
        x[i] = 1 / U[i,i] * (b[i] - x[i])
        
    return x


# In[2]:


# Define linear system
A = np.array([[4, -2, -4], [-2, 10, 5], [-4, 5, 14]])
b = np.array([-2, 49, 27])

# Calculate Cholesky decomposition
L = cholesky(A)

print(f"L = \n{L}\n")

# Solve linear system
y = forward_substitution(L, b)
x = back_substitution(L.T, y)

print(f"y = {y}\nx = {x}")

