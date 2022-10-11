#!/usr/bin/env python
# coding: utf-8

# (lup-section)=
# # LUP decomposition
# 
# (partial-pivoting-section)=
# ## Partial pivoting
# 
# A problem that can be encountered with [LU decomposition](lu-definition) is that if the value of $u_{jj}$ in the expression for [$\ell_{ij}$](lu-definition) is zero or some small number it will mean that it is undefined or prone to computational rounding errors due to the value of $\ell_{ij}$ being very large, this is known as an [**ill-conditioned system**](https://en.wikipedia.org/wiki/Condition_number).
# 
# This problem can be overcome by using **partial pivoting** where rows of the coefficient matrix are permuted (swapped) so that the pivot element $a_{jj}$ has a larger absolute value than the elements in the column beneath it. Note that swapping two rows of the coefficient matrix does not change the solution to the system as long as the same swap is applied to the constant vector. The permutations applied to the coefficient matrix are recorded in a matrix $P$ which is determined by applying the same permutations to the identity matrix.
# 
# ````{admonition} Example 6.3
# :class: seealso
# :name: pivoting-example
# 
# Apply partial pivoting the following matrix and determine the permutation matrix $P$
# 
# \begin{align*}
#     A =\begin{pmatrix}
#         0 & 1 & -2\\
#         1 & 0 & 2\\
#         3 & -2 & 2
#     \end{pmatrix}.
# \end{align*}
# 
# ```{dropdown} Solution
# 
# Using elementary row operations
# 
# \begin{align*}
#     &\begin{pmatrix}
#         0 & 1 & -2\\
#         1 & 0 & 2\\
#         3 & -2 & 2
#     \end{pmatrix}
#     \begin{array}{l} R_1 \leftrightarrow R_3 \\ \phantom{x} \\ \phantom{x} \end{array}
#     \longrightarrow 
#     \begin{pmatrix}
#         3 & -2 & 2\\
#         1 & 0 & 2\\
#         0 & 1 & -2
#     \end{pmatrix}
#     \begin{array}{l} \phantom{x} \\ R_2 \leftrightarrow R_3 \\ \phantom{x} \end{array} \\ \\
#     \longrightarrow
#     &\begin{pmatrix}
#         3 & -2 & 2\\
#         0 & 1 & -2\\
#         1 & 0 & 2
#     \end{pmatrix}.
# \end{align*}
# 
# Apply the same row operations to the identity matrix
# 
# \begin{align*}
#     &\begin{pmatrix}
#         1 & 0 & 0 \\
#         0 & 1 & 0 \\
#         0 & 0 & 1
#     \end{pmatrix}
#     \begin{array}{l} R_1 \leftrightarrow R_3 \\ \phantom{x} \\ \phantom{x} \end{array}
#     \longrightarrow 
#     \begin{pmatrix}
#         0 & 0 & 1 \\
#         0 & 1 & 0 \\
#         1 & 0 & 0
#     \end{pmatrix}
#     \begin{array}{l} \phantom{x} \\ R_2 \leftrightarrow R_3 \\ \phantom{x} \end{array} \\ \\
#     \longrightarrow
#     &\begin{pmatrix}
#         0 & 0 & 1 \\
#         1 & 0 & 0 \\
#         0 & 1 & 0
#     \end{pmatrix}.
# \end{align*}
# 
# So 
# $P=\begin{pmatrix}
#     0 & 0 & 1\\
#     1 & 0 & 0\\
#     0 & 1 & 0
# \end{pmatrix}$. Note that pre-multiplying $A$ by $P$ gives the matrix $A$ after partial pivoting has been applied 
# \begin{align*}
#     \begin{pmatrix}
#         0 & 0 & 1\\
#         1 & 0 & 0\\
#         0 & 1 & 0
#     \end{pmatrix}
#     \begin{pmatrix}
#         0 & 1 & -2\\
#         1 & 0 & 2\\
#         3 & -2 & 2
#     \end{pmatrix} =
#     \begin{pmatrix}
#         3 & -2 & 2\\
#         0 & 1 & -2\\
#         1 & 0 & 2
#     \end{pmatrix}.
# \end{align*}
# 
# ```
# ````
# 
# ## Python code
# 
# The code below defines a function called `partial_pivot()` which performs partial pivoting on the matrix `A` and returns the pivoted matrix `A` and the permutation matrix `P`. 

# In[1]:


import numpy as np


# In[2]:


def partial_pivot(A):
    n = A.shape[0]
    P = np.eye(n)
    for j in range(n):
        maxpivot, k = A[j,j], j
        for i in range(j + 1, n):
            if A[i,j] > maxpivot:
                maxpivot, k = A[i,j], i
                
        A[[j, k]] = A[[k, j]]
        P[[j, k]] = P[[k, j]]
        
    return A, P


# The code below applies the function `partial_pivot()` to calculate the permutation matrix for the matrix from [example 6.3](pivoting-example).

# In[3]:


# Define linear system
A = np.array([[0, 1, -2], [1, 0, 2], [3, -2, 2]])
b = np.array([10, -4, -8])

# Apply partial pivoting to the coefficent matrix
A, P = partial_pivot(A)

print(f"A = \n{A}\n\nP = \n{P}")


# (lup-decomposition-section)=
# ## LU decomposition with partial pivoting
# 
# To calculate **LU decomposition with partial pivoting** (also known as **LUP decomposition**) we use the same process as in [LU decomposition](LU-definition) with the exception that the coefficient matrix has partial pivoting applied prior to the calculation of $L$ and $U$, i.e., 
# 
# \begin{align*}
#     LU = PA.
# \end{align*}
# 
# So to solve the system $A \mathbf{x} = \mathbf{b}$ using LUP decomposition we have
# 
# \begin{align*}
#     PA \mathbf{x} &= P \mathbf{b} \\ 
#     \therefore LU \mathbf{x} &= P \mathbf{b}.
# \end{align*}
# 
# So applying Crout's method to solve $A \mathbf{x} = \mathbf{b}$ we solve the following for $\mathbf{y}$ and $\mathbf{x}$
# 
# \begin{align*}
#     L \mathbf{y} &= P \mathbf{b}, \\
#     U \mathbf{x} &= \mathbf{y}.
# \end{align*}
# 
# ````{admonition} Example 6.4
# :class: seealso
# :name: lup-example
# 
# Solve the following system of linear equations using Crout's method with LUP decomposition
# 
# \begin{align*}
#     \begin{pmatrix}
#         0 & 1 & -2\\
#         1 & 0 & 2\\
#         3 & -2 & 2
#     \end{pmatrix}
#     \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} =
#     \begin{pmatrix} 10 \\ -4 \\ -8 \end{pmatrix}.
# \end{align*}
# 
# ```{dropdown} Solution
# 
# We have seen from the [example 6.3](pivoting-example) above that applying partial pivoting to the coefficient matrix results in
# 
# \begin{align*}
#     PA &= \begin{pmatrix}
#         3 & -2 & 2\\
#         0 & 1 & -2\\
#         1 & 0 & 2
#     \end{pmatrix}, &
#     P &= \begin{pmatrix}
#         0 & 0 & 1\\
#         1 & 0 & 0\\
#         0 & 1 & 0
#     \end{pmatrix}.
# \end{align*}
# 
# Calculating the LU decomposition of $PA$ using {eq}`lu-equation`
# 
# \begin{align*}
#     j &= 1: & u_{11} &=a_{11} =3, \\
#     & & \ell_{21} &= \frac{1}{u_{11} }a_{21} = \frac{1}{3}(0)=0, \\
#     & & \ell_{31} &= \frac{1}{u_{11} }a_{31} = \frac{1}{3}(1)=\frac{1}{3}, \\
#     \\
#     j &= 2: & u_{12} &= a_{12} =-2, \\
#     & & u_{22} &= a_{22} - \ell_{21} u_{12} = 1 - 0(-2) = 1, \\
#     & & \ell_{32} &= \frac{1}{u_{22}}(a_{32} -\ell_{31} u_{12}) = \frac{1}{1} \left( 0 - \frac{1}{3}(-2) \right) = \frac{2}{3}, \\
#     \\
#     j &= 3: & u_{13} &= a_{13} = 2, \\
#     & & u_{23} &= a_{23} -\ell_{21} u_{13} = -2 - 0(-2) = -2, \\
#     & & u_{33} &= a_{33} -\ell_{31} u_{13} -\ell_{32} u_{23} = 2 - \frac{1}{3}(2)- \frac{2}{3}(-2) = \frac{8}{3}.
# \end{align*}
# 
# Therefore
# 
# \begin{align*}
#     L &= \begin{pmatrix}
#         1 & 0 & 0\\
#         0 & 1 & 0\\
#         \frac{1}{3} & \frac{2}{3} & 1
#     \end{pmatrix}, &
#     U &= \begin{pmatrix}
#         3 & -2 & 2\\
#         0 & 1 & -2\\
#         0 & 0 & \frac{8}{3}
#     \end{pmatrix}.
# \end{align*}
# 
# Solving $L \mathbf{y} = P \mathbf{b}$ using forward substitution 
# 
# \begin{align*}
#     \begin{pmatrix}
#         1 & 0 & 0\\
#         0 & 1 & 0\\
#         \frac{1}{3} & \frac{2}{3} & 1
#     \end{pmatrix}
#     \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix} =
#     \begin{pmatrix}
#         0 & 0 & 1\\
#         1 & 0 & 0\\
#         0 & 1 & 0
#     \end{pmatrix}
#     \begin{pmatrix} 10 \\ -4 \\ -8 \end{pmatrix} =
#     \begin{pmatrix} -8 \\ 10 \\ -4 \end{pmatrix},
# \end{align*}
# 
# gives
# 
# \begin{align*}
#     y_1 &= -8, \\
#     y_2 &= 10 - 0(8)=10, \\
#     y_3 &= -4 - \frac{1}{3}(8) + \frac{2}{3}(10) = -8.
# \end{align*}
# 
# Solving $U \mathbf{x} = \mathbf{y}$ using back substitution
# 
# \begin{align*}
#     \begin{pmatrix}
#         3 & -2 & 2\\
#         0 & 1 & -2\\
#         0 & 0 & \frac{8}{3}
#     \end{pmatrix}
#     \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = 
#     \begin{pmatrix} -8 \\ 10 \\ -8 \end{pmatrix},
# \end{align*}
# 
# gives
# 
# \begin{align*}
#     x_3 &= \frac{3}{8}(-8) = -3, \\
#     x_2 &= \frac{1}{1}(10+2(-3)) = 4, \\
#     x_1 &= \frac{1}{3}(-8+2(4)-2(-3)) = 2.
# \end{align*}
# 
# So the solution is $\mathbf{x}=(2,4,-3)$.
# 
# ```
# ````
# 
# ## Python code 
# 
# The code below calculates the solution to the system of linear equations from [example 6.4](lup-example) using Crout's method with LUP decomposition. The `np.dot(A, B)` command calculates the matrix multiplication $AB$

# In[4]:


import numpy as np

def lu(A):
    n = A.shape[0]
    L, U = np.eye(n), np.zeros((n, n))
    for j in range(n):
        for i in range(j + 1):
            for k in range(i):
                U[i,j] += L[i,k] * U[k,j]
                
            U[i,j] = A[i,j] - U[i,j]   
            
        for i in range(j + 1, n):
            for k in range(j):
                L[i,j] += L[i,k] * U[k,j]
                
            L[i,j] = 1 / U[j,j] * (A[i,j] - L[i,j])
    
    return L, U

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


def partial_pivot(A):
    n = A.shape[0]
    P = np.eye(n)
    for j in range(n):
        maxpivot, k = A[j,j], j
        for i in range(j + 1, n):
            if A[i,j] > maxpivot:
                maxpivot, k = A[i,j], i 
                
        A[[j, k]] = A[[k, j]]
        P[[j, k]] = P[[k, j]]
        
    return A, P


# In[5]:


# Define linear system
A = np.array([[0, 1, -2], [1, 0, 2], [3, -2, 2]])
b = np.array([10, -4, -8])

# Apply partial pivoting to the coefficent matrix
A, P = partial_pivot(A)

print(f"P = \n{P}\n")

# Calculate LU decomposition
L, U = lu(A)

print(f"L = \n{L}\n\nU = \n{U}\n")

# Solve linear system
y = forward_substitution(L, np.dot(P, b))
x = back_substitution(U, y)

for i in range(len(x)):
    print(f"x{i+1} = {x[i]}")

