#!/usr/bin/env python
# coding: utf-8

# (lu-section)=
# # LU decomposition
# 
# **LU decomposition** (also known as **LU factorisation**) is a procedure for decomposing a square matrix $A$ into the product of a lower triangular matrix $L$ and an upper triangular matrix $U$ such that
# 
# \begin{align*}
#     A = LU.
# \end{align*}
# 
# The advantage of writing a matrix as a product of $L$ and $U$ is that the solution to a triangular set of equations is easy to calculate using forward or back substitution. Consider the LU decomposition of a $3\times 3$ matrix
# 
# \begin{align*}
#     \begin{pmatrix}
#         a_{11}  & a_{12}  & a_{13} \\
#         a_{21}  & a_{22}  & a_{32} \\
#         a_{31}  & a_{32}  & a_{33} 
#     \end{pmatrix}=
#     \begin{pmatrix}
#         \ell_{11}  & 0 & 0\\
#         \ell_{21}  & \ell_{22}  & 0\\
#         \ell_{31}  & \ell_{32}  & \ell_{33} 
#     \end{pmatrix}\begin{pmatrix}
#         u_{11}  & u_{12}  & u_{13} \\
#         0 & u_{22}  & u_{23} \\
#         0 & 0 & u_{33} 
#     \end{pmatrix},
# \end{align*}
# 
# which gives a system of 9 equations (one for each element in $A$) in 12 unknowns which has an infinite number of solutions. If we use the condition $\ell_{ii} = 1$ then[^1]
# 
# [^1]: Here we use $\ell$ instead of the lowercase character $l$ to avoid confusion with the uppercase character $I$ or the number 1.
# 
# \begin{align*}
#     \begin{pmatrix}
#         a_{11}  & a_{12}  & a_{13} \\
#         a_{21}  & a_{22}  & a_{23} \\
#         a_{31}  & a_{32}  & a_{33} 
#     \end{pmatrix}=
#     \begin{pmatrix}
#         u_{11}  & u_{12}  & u_{13} \\
#         \ell_{21} u_{11}  & \ell_{21} u_{12} + \ell_{22} u_{22}  & \ell_{21} u_{13} + \ell_{22} u_{23} \\
#         \ell_{31} u_{11}  & \ell_{31} u_{12} + \ell_{32} u_{22}  & \ell_{31} u_{13} +\ell_{32} u_{23} +\ell_{33} u_{33} 
#     \end{pmatrix}.
# \end{align*}
# 
# The elements in the lower triangular region, where $i>j$, are
# \begin{align*}
#     \ell_{ij} =\sum_{k=1}^j \ell_{ik} u_{kj} =\ell_{ij} u_{jj} +\sum_{k=1}^{j-1} \ell_{ik} u_{kj}, 
# \end{align*}
# 
# which is rearranged to
# 
# \begin{align*}
#     \ell_{ij} =\frac{1}{u_{jj} }\left(a_{ij} -\sum_{k=1}^{j-1} \ell_{ik} u_{kj} \right).
# \end{align*}
# 
# For the elements in the upper triangular region where $i\le j$ we have
# 
# \begin{align*}
#     u_{ij} =u_{ij} +\sum_{k=1}^{i-1} \ell_{ik} u_{kj},
# \end{align*}
# 
# which is rearranged to 
# 
# \begin{align*}
#     u_{ij} = a_{ij} -\sum_{k=1}^{i-1} \ell_{ik} u_{kj}.
# \end{align*}
# 
# So to calculate an LU decomposition we loop through each column of $A$ and calculate the elements of $\ell_{ij}$ and $u_{ij}$ for that column.
# 
# ````{admonition} Definition: LU decomposition
# :class: note
# :name: lu-definition
# 
# The LU decomposition of an $n \times n$ square matrix $A$ results in two $n \times n$ matrices $L$ and $U$ such that $A = LU$. The elements of $L$ and $U$ are calculated using
# 
# ```{math}
# :label: lu-equation
# \begin{align}
# u_{ij} &= a_{ij} - \sum_{k=1}^{i-1} \ell_{ik}u_{kj}, & i &= 1, \ldots, j, \\
# \ell_{ij} &= \dfrac{1}{u_{jj}} \left(a_{ij} - \displaystyle \sum_{k=1}^{j-1} \ell_{ik}u_{kj}\right), & i &= j+1, \ldots, n.
# \end{align}
# ```
# ````
# 
# ````{admonition} Example 6.1
# :class: seealso
# :name: lu-example
# 
# Determine the LU decomposition of the following matrix
# \begin{align*}
#     A=\begin{pmatrix}
#         1 & 3 & 0\\
#         2 & -4 & -1\\
#         -3 & 1 & 2
#     \end{pmatrix}.
# \end{align*}
# 
# ```{dropdown} Solution
# 
# Stepping through the columns of $A$
# 
# \begin{align*}
#     j&=1: & u_{11} &=a_{11} =1,\\
#     && \ell_{21} &=\frac{1}{u_{11} }(a_{21} )=\frac{1}{1}(2)=2,\\
#     && \ell_{31} &=\frac{1}{u_{11} }(a_{31} )=\frac{1}{1}(-3)=-3,\\
#     \\
#     j&=2: & u_{12} &=a_{12} =3,\\
#     && u_{22} &=a_{22} -\ell_{21} u_{12} =-4-2(3)=-10,\\
#     && \ell_{32} &=\frac{1}{u_{22} }(a_{32} -\ell_{31} u_{12} ) = \frac{1}{-10}(1+3(3))=1,\\
#     \\
#     j&=3: & u_{13} &=a_{13} =0,\\
#     && u_{23} &=a_{23} -\ell_{21} u_{13} =-1-2(0)=-1,\\
#     && u_{33} &=a_{33} -\ell_{31} u_{13} -\ell_{32} u_{23} =2+-3(0)-1(-1)=3.
# \end{align*}
# 
# Therefore
# 
# \begin{align*}
#     L &= \begin{pmatrix}
#         1 & 0 & 0\\
#         2 & 1 & 0\\
#         -3 & -1 & 1
#     \end{pmatrix},&
#     U &= \begin{pmatrix}
#         1 & 3 & 0 \\
#         0 & -10 & -1 \\
#         0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# Checking that $LU=A$
# 
# \begin{align*}
#     \begin{pmatrix}
#         1 & 0 & 0\\
#         2 & 1 & 0\\
#         -3 & -1 & 1
#     \end{pmatrix}
#     \begin{pmatrix}
#         1 & 3 & 0\\
#         0 & -10 & -1\\
#         0 & 0 & 1
#     \end{pmatrix}=
#     \begin{pmatrix}
#         1 & 3 & 0\\
#         2 & -4 & -1\\
#         -3 & 1 & 2
#     \end{pmatrix}.
# \end{align*}
# 
# ```
# ````
# 
# ## Python Code
# 
# The code below defines a function called `lu()` which calculates the LU decomposition of a square matrix `A`. 

# In[1]:


import numpy as np


# In[35]:


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


# The code below applies the function `lu()` to calculate the LU decomposition of the matrix from [example 6.1](lu-example).

# In[25]:


# Define matrix
A = np.array([[1, 3, 0], [2, -4, -1], [-3, 1, 2]])

# Calculate LU decomposition
L, U = lu(A)

print(f"L = \n{L}\n")
print(f"U = \n{U}\n")


# (crouts-method-section)=
# ## Crout's method
# 
# Given a system of linear equations of the form $A \mathbf{x} = \mathbf{b}$ then the solution can be calculated using the LU decomposition of $A$ using **Crout's method**. Since $A = LU$ then
# 
# \begin{align*}
#     U\mathbf{x} = \mathbf{b},
# \end{align*}
# 
# let $\mathbf{y} = U \mathbf{x}$ then
# 
# \begin{align*}
#     \mathbf{y} = \mathbf{b}.
# \end{align*}
# 
# $L$ is a lower triangular matrix so the solution of $L \mathbf{y} = \mathbf{b}$ is easily calculated using forward substitution. Once $\mathbf{y}$ has been calculated the solution to $U\mathbf{x} = \mathbf{y}$ is calculated using back substitution.
# 
# The advantage of using Crout's method is that once the LU decomposition of the coefficient matrix has been calculated the can be used for any values of the constant vector $\mathbf{b}$. This is unlike Gaussian elimination where row reduction will need to be repeated for difference values of $\mathbf{b}$.
# 
# ````{admonition} Example 6.2
# :class: seealso
# :name: crout-example
#     
# Use Crout's method to solve the following system of linear equations
# 
# \begin{align*}
#     \begin{pmatrix}
#         1 & 3 & 0 \\
#         2 & -4 & -1 \\
#         -3 & 1 & 2
#     \end{pmatrix}
#     \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix}=
#     \begin{pmatrix} -7 \\ 11 \\ 1 \end{pmatrix}.
# \end{align*}
# 
# ```{dropdown} Solution
# 
# We saw in the [example 6.1](lu-example) above that the LU decomposition of the coefficient matrix is
# 
# \begin{align*}
#     L & =\begin{pmatrix}
#         1 & 0 & 0 \\
#         2 & 1 & 0 \\
#         -3 & -1 & 1
#     \end{pmatrix}, &
#     U &= \begin{pmatrix}
#         1 & 3 & 0 \\
#         0 & -10 & -1 \\
#         0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# Solving $L \mathbf{y} = \mathbf{b}$ using forward substitution
# 
# \begin{align*}
#     \begin{pmatrix}
#         1 & 0 & 0 \\
#         2 & 1 & 0 \\
#         -3 & -1 & 1
#     \end{pmatrix}
#     \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix} =
#     \begin{pmatrix} -7\\ 11\\ 1
#     \end{pmatrix},
# \end{align*}
# 
# gives
# 
# \begin{align*}
#     y_1 &=-7,\\
#     y_2 &=11-2y_1 =-2(-7)=25,\\
#     y_3 &=-1+3y_1 +y_2 =-1+3(-7)+1(25)=5.
# \end{align*}
# 
# Solving $U \mathbf{x} = \mathbf{y}$ using back substitution 
# 
# \begin{align*}
#     \begin{pmatrix}
#         1 & 3 & 0\\
#         0 & -10 & -1\\
#         0 & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} =
#     \begin{pmatrix} -7 \\ 25 \\ 5 \end{pmatrix},
# \end{align*}
# 
# gives
# 
# \begin{align*}
#     x_3 &= 5,\\
#     x_2 &= \frac{1}{-10}(25 + x_3) = -\frac{1}{10}(25 + 5) = -3,\\
#     x_1 &= -7 - 0x_3 - 3x_2 = -7 + 9 = 2.
# \end{align*}
# 
# So the solution is $\mathbf{x}=(2,-3,5)$.
# 
# ```
# ````
# 
# ## Python code
# 
# The Python code below defines two functions called `forward_substitution()` and `back_substitution()` that perform forward and back substitution.

# In[36]:


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


# The code below uses the function `forward_substitution()` and `back_substitution()` to calculate the solution to the linear system from [example 6.2](crout-example) using Crout's method with LU decomposition.

# In[34]:


# Define linear system
A = np.array([[1, 3, 0], [2, -4, -1], [-3, 1, 2]])
b = np.array([-7, 11, 1])

# Calculate LU decomposition
L, U = lu(A)

print(f"L = \n{L}\n\nU = \n{U}\n")

# Solve linear system
y = forward_substitution(L, b)
x = back_substitution(U, y)

for i in range(len(x)):
    print(f"x{i+1} = {x[i]}")

