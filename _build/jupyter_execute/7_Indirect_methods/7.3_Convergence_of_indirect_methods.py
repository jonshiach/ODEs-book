#!/usr/bin/env python
# coding: utf-8

# (convergence-of-indirect-methods-section)=
# # Convergence of indirect methods
# 
# We have seen that both the [Jacobi](jacobi-method-section) and [Gauss-Seidel](gauss-seidel-method-section) methods are iterated until the estimates of the solution converge to a given tolerance. In [example 7.1](jacobi-method-example) required 49 iterations to converge to the solution of a system of linear equations whereas in [example 7.2](gauss-seidel-method-example) only required 20 iterations to converge to the solution for the same system. 
# 
# Not all indirect methods will converge for a given system of linear equations, we can establish whether a method will be convergent using the theorem below. Let $\mathbf{e}^{(k)} = |\mathbf{x} - \mathbf{x}^{(k)}|$ be the error between the exact solution $\mathbf{x}$ and the estimate $\mathbf{x}^{(k)}$. The error from one estimate to the next is updated using the iteration matrix for the method
# 
# \begin{align*}
#     \mathbf{e}^{(k+1)} = T\mathbf{e}^{(k)}.
# \end{align*}
# 
# We can write the first error, $\mathbf{e}^{(0)}$ as a linear combination of some vectors $\mathbf{v}_i$ 
# 
# \begin{align*}
#     \mathbf{e}^{(0)} =\alpha_1 \mathbf{v}_1 +\alpha_2 \mathbf{v}_2 +\cdots +\alpha_n \mathbf{v}_n =\sum_{i=1}^n \alpha_i \mathbf{v}_i,
# \end{align*}
# 
# where $\alpha_i$ are scalars. If $\mathbf{v}_i$ are the [eigenvectors](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors) of the matrix $T$ with eigenvalues $\lambda_i$ so $T\mathbf{v}_i = \lambda_i \mathbf{v}_i$ then iterating $\mathbf{e}^{(k)}$ gives
# 
# \begin{align*}
#     \mathbf{e}^{(1)} &= T\mathbf{e}^{(0)} =T\left(\sum_{i=1}^n \alpha_i \mathbf{v}_i \right)=\sum_{i=1}^n \alpha_i T\mathbf{v}_i = \sum_{i=1}^n \alpha_i \lambda_i \mathbf{v}_i , \\
#     \mathbf{e}^{(2)} &=T\mathbf{e}^{(1)} =T\left(\sum_{i=1}^n \alpha_i \lambda_i \mathbf{v}_i \right)=\sum_{i=1}^n \alpha_i \lambda_i T\mathbf{v}_i =\sum_{i=1}^n \alpha_i \lambda_i^2 \mathbf{v}_i , \\
#     &\vdots \\
#     \mathbf{e}^{(k+1)} &=\sum_{i=1}^n \alpha_i \lambda_i^{k+1} \mathbf{v}_i .
# \end{align*}
# 
# If $|\lambda_1|>\lambda_2, \lambda_3, \ldots \lambda_n$ then
# 
# \begin{align*}
#     \mathbf{e}^{(k+1)} =\alpha_1 \lambda_1^{k+1} \mathbf{v}_1 +\sum_{i=2}^n \alpha_i \lambda_i^{k+1} \mathbf{v}_i =\lambda_1^{k+1} \left(\alpha_1 \mathbf{v}_1 +\sum_{i=2}^n \alpha_i \mathbf{v}_i {\left(\frac{\lambda_i }{\lambda_1 }\right)}^{k+1} \right)
# \end{align*}
# 
# and since $\lambda_i / \lambda_ 1 < 1$ then
# 
# \begin{align*}
#     \lim_{k\to \infty } \mathbf{e}^{(k+1)} =\alpha_1 \lambda_1^{k+1} \mathbf{v}_1 .
# \end{align*}
# 
# This means that as the number of iterations increases, the error varies by a factor of $\lambda_1^{k+1}$ where $\lambda_1$ is the largest eigenvalue of $T$ which is known as the **spectral radius**.
# 
# ````{admonition} Definition: Spectral radius
# :class: note
# :name: spectral-radius-definition
# 
# Let $\lambda_1, \lambda_2, \ldots, \lambda_n$ be the eigenvalues of a matrix $A$ then the spectral radius of $A$ denoted by $\rho(A)$ is
# 
# ```{math}
# :label: spectral-radius-equation
# 
# \begin{align*}
#     \rho(A) = \max_i(|\lambda_i|).
# \end{align*}
# ```
# ````
# 
# ```{admonition} Theorem: Convergence criteria for an indirect method
# :class: important
# :name: indirect-methods-convergence-criteria-theorem
# 
# The spectral radius of $T$ gives us the following information about an indirect method
# 
# - If $\rho (T) > 1$ then the errors will increase over each iteration, therefore for an indirect method to converge to the solution we require $\rho (T)< 1$.
# - The smaller the value of $\rho (T)$ the faster the errors will tend to zero.
# \end{itemize}
# ```
# 
# ````{admonition} Example 7.3
# :class: seealso
# :name: convergence-example
# 
# Show that the Jacobi and Gauss-Seidel methods are convergent of the system of linear equations from [example 7.1](jacobi-method-example).
# 
# ```{dropdown} Solution
# 
# The coefficient matrix for this linear system is
# 
# \begin{align*}
#     A = \begin{pmatrix} 4 & 3 & 0 \\ 3 & 4 & -1 \\ 0 & -1 & 4 \end{pmatrix}.
# \end{align*}
# 
# so
# 
# \begin{align*}
#     L &= \begin{pmatrix} 0 & 0 & 0 \\ 3 & 0 & 0 \\ 0 & -1 & 0 \end{pmatrix}, &
#     D &= \begin{pmatrix} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 4 \end{pmatrix}, \\
#     U &= \begin{pmatrix} 0 & 3 & 0 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{pmatrix}.
# \end{align*}
# 
# The iteration matrices for the Jacobi and Gauss-Seidel methods are given in equations {eq}`jacobi-method-iteration-matrix-equation` and {eq}`gauss-seidel-method-iteration-matrix-equation` which for this system are
# 
# \begin{align*}
#     T_J &= -D ( L + U) 
#     = -\begin{pmatrix} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 4 \end{pmatrix} \left(
#     \begin{pmatrix} 0 & 0 & 0 \\ 3 & 0 & 0 \\ 0 & -1 & 0 \end{pmatrix} +
#     \begin{pmatrix} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 4 \end{pmatrix} \right) \\
#     &= - \begin{pmatrix} \frac{1}{4} & 0 & 0 \\ 0 & \frac{1}{4} & 0 \\ 0 & 0 & \frac{1}{4} \end{pmatrix}
#     \begin{pmatrix} 0 & 3 & 0 \\ 3 & 0 & -1 \\ 0 & -1 & 0 \end{pmatrix} 
#     = \begin{pmatrix} 0 & -\frac{3}{4} & 0 \\ -\frac{3}{4} & 0 & \frac{1}{4} \\ 0 & \frac{1}{4} & 0 \end{pmatrix}, \\
#     T_{GS} &= - (L + D)^{-1} U 
#     = - \begin{pmatrix} 3 & 0 & 0 \\ 3 & 4 & 0 \\ 0 & -1 & 4 \end{pmatrix}^{-1}
#     \begin{pmatrix} 0 & 3 & 0 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{pmatrix} \\ 
#     &= \begin{pmatrix} -\frac{1}{4} & 0 & 0 \\ \frac{3}{16} & \frac{1}{4} & 0 \\ \frac{3}{64} & -\frac{1}{16} & \frac{1}{4} \end{pmatrix}
#     \begin{pmatrix} 0 & 3 & 0 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{pmatrix} =
#     \begin{pmatrix} 0 & -\frac{3}{4} & 0 \\ 0 & \frac{9}{16} & \frac{1}{4} \\ 0 & \frac{9}{64} & \frac{1}{16} \end{pmatrix}
# \end{align*}
# 
# Calculating the spectral radius for these iteration matrices gives $\rho(T_J )=0.7906$ and $\rho (T_{GS})=0.625$ which are both less than 1 so both of these methods are convergent for this system. Furthermore, the Gauss-Seidel method will converge faster than the Jacobi method since it has a smaller spectral radius.
# 
# ```
# ````

# In[1]:


import numpy as np

def jacobi_iteration_matrix(A):
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    D = A - L - U
    return - np.dot(np.linalg.inv(D), L + U)


def gauss_seidel_iteration_matrix(A):
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    D = A - L - U
    return - np.dot(np.linalg.inv(L + D), U)

A = np.array([[4, 3, 0], [3, 4, -1], [0, -1, 4]])

T_J = jacobi_iteration_matrix(A)
T_GS = gauss_seidel_iteration_matrix(A)
print(T_J)
print(T_GS)
print(np.linalg.eigvals(T_J))
print(np.linalg.eigvals(T_GS))


# In[2]:


from sympy import *

def jacobi_iteration_matrix(L, D, U):
    return - D.inv() * (L + U)


def gauss_seidel_iteration_matrix(L, D, U):
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    D = A - L - U
    return - (L + D).inv() * U

A = Matrix([[4, 3, 0], [3, 4, -1], [0, -1, 4]])
L = Matrix([[0, 0, 0], [3, 0, 0], [0, -1, 0]])
D = Matrix([[4, 0, 0], [0, 4, 0], [0, 0, 4]])
U = Matrix([[0, 4, -1], [0, 0, 4], [0, 0, 0]])

T_J = jacobi_iteration_matrix(L, D, U)
T_GS = gauss_seidel_iteration_matrix(L, D, U)
pprint(T_J)
pprint(T_GS)

pprint(T_J.eigenvals())

