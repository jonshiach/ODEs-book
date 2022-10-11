#!/usr/bin/env python
# coding: utf-8

# # Indirect methods exercises
# 
# `````{admonition} Exercise 7.1
# :class: note
# :name: ex7.1
# 
# Using a pen and calculator, calculate the first 2 iterations of the Jacobi method for solving the system of linear equations below. Use starting values of $x_i^{(0)} = 0 $ and work to 4 decimal places.
# 
# \begin{align*}
#     4x_1 +x_2 -x_3 +x_4 &=14,\\
#     x_1 +4x_2 -x_3 -x_4 &=10,\\
#     -x_1 -x_2 +5x_3 +x_4 &=-15,\\
#     x_1 -x_2 +x_3 +3x_4 &=3.
# \end{align*}
# 
# ````{dropdown} Solution
# The Jacobi method for this system is
# 
# \begin{align*}
#     x_{1}^{(k+1)} &= \frac{1}{5} \left( 14 - x_{2}^{(k)} + x_{3}^{(k)} - x_{4}^{(k)} \right), \\
#     x_{2}^{(k+1)} &= \frac{1}{4} \left( 10 - x_{1}^{(k)} + x_{3}^{(k)} + x_{4}^{(k)} \right), \\
#     x_{3}^{(k+1)} &= \frac{1}{5} \left( -15 + x_{1}^{(k)} + x_{2}^{(k)} - x_{4}^{(k)} \right), \\
#     x_{4}^{(k+1)} &= \frac{1}{3} \left( 3 - x_{1}^{(k)} + x_{2}^{(k)} - x_{3}^{(k)} \right).
# \end{align*}
# 
# Using starting values of $\mathbf{x} = \mathbf{0}$. Calculating the first iteration
# 
# \begin{align*}
#     x_{1}^{(1)} &= \frac{1}{5} \left( 14 - 2.5 + 3.0 - 1.0 \right) = 2.8, \\
#     x_{2}^{(1)} &= \frac{1}{4} \left( 10 - 2.8 + 3.0 + -1.0 \right) = 2.5, \\
#     x_{3}^{(1)} &= \frac{1}{5} \left( -15 + -2.8 + -2.5 - 1.0 \right) = -3.0, \\
#     x_{4}^{(1)} &= \frac{1}{3} \left( 3 - 2.8 + -2.5 - -3.0 \right) = 1.0.
# \end{align*}
# 
# Calculate the residual
# 
# \begin{align*}
#     \mathbf{r}^{(1)} = \mathbf{b} - A \mathbf{x}^{(1)} = 
#     \begin{pmatrix} 14 \\ 10 \\ -15 \\ 3 \end{pmatrix} -
#     \begin{pmatrix} 5 & 1 & -1 & 1 \\ 1 & 4 & -1 & -1 \\ -1 & -1 & 5 & 1 \\ 1 & -1 & 1 & 3 \end{pmatrix}
#     \begin{pmatrix} 2.8 \\ 2.5 \\ -3.0 \\ 1.0 \end{pmatrix} =
#     \begin{pmatrix} -6.5 \\ -4.8 \\ 4.3 \\ 2.7 \end{pmatrix}.
# \end{align*}
# 
# Since $\max(| \mathbf{r}^{(1)} |) = 6.5 > 10^{-4}$ we continue iterating. Calculating the second iteration
# 
# \begin{align*}
#     x_{1}^{(2)} &= \frac{1}{5} \left( 14 - 1.3 + 2.14 - 1.9 \right) = 1.5, \\
#     x_{2}^{(2)} &= \frac{1}{4} \left( 10 - 1.5 + 2.14 + -1.9 \right) = 1.3, \\
#     x_{3}^{(2)} &= \frac{1}{5} \left( -15 + -1.5 + -1.3 - 1.9 \right) = -2.14, \\
#     x_{4}^{(2)} &= \frac{1}{3} \left( 3 - 1.5 + -1.3 - -2.14 \right) = 1.9.
# \end{align*}
# 
# Calculate the residual
# 
# \begin{align*}
#     \mathbf{r}^{(2)} &= \mathbf{b} - A \mathbf{x}^{(1)} = 
#     \begin{pmatrix} 14 \\ 10 \\ -15 \\ 3 \end{pmatrix} -
#     \begin{pmatrix} 5 & 1 & -1 & 1 \\ 1 & 4 & -1 & -1 \\ -1 & -1 & 5 & 1 \\ 1 & -1 & 1 & 3 \end{pmatrix}
#     \begin{pmatrix} 1.5 \\ 1.3 \\ -2.14 \\ 1.9 \end{pmatrix} \\
#     &=
#     \begin{pmatrix} 1.16 \\ 3.06 \\ -3.4 \\ -0.76 \end{pmatrix}.
# \end{align*}
# 
# Since $\max(| \mathbf{r}^{(2)} |) = 3.4 > 10^{-4}$ we continue iterating. 
# ````
# 
# `````

# `````{admonition} Exercise 7.2
# :class: note
# :name: ex7.2
# 
# Repeat question 1 using the Gauss-Seidel method.
# 
# ````{dropdown} Solution
# The Gauss-Seidel method for this system is
# 
# \begin{align*}
#     x_{1}^{(k+1)} &= \frac{1}{5} \left( 14 - x_{2}^{(k)} + x_{3}^{(k)} - x_{4}^{(k)} \right), \\
#     x_{2}^{(k+1)} &= \frac{1}{4} \left( 10 - x_{1}^{(k+1)} + x_{3}^{(k)} + x_{4}^{(k)} \right), \\
#     x_{3}^{(k+1)} &= \frac{1}{5} \left( -15 + x_{1}^{(k+1)} + x_{2}^{(k+1)} - x_{4}^{(k)} \right), \\
#     x_{4}^{(k+1)} &= \frac{1}{3} \left( 3 - x_{1}^{(k+1)} + x_{2}^{(k+1)} - x_{3}^{(k+1)} \right).
# \end{align*}
# 
# Using starting values of $\mathbf{x} = \mathbf{0}$. Calculating the first iteration
# 
# \begin{align*}
#     x_{1}^{(1)} &= \frac{1}{5} \left( 14 - 1.8 + 2.08 - 1.36 \right) = 2.8, \\
#     x_{2}^{(1)} &= \frac{1}{4} \left( 10 - 2.8 + 2.08 + -1.36 \right) = 1.8, \\
#     x_{3}^{(1)} &= \frac{1}{5} \left( -15 + -2.8 + -1.8 - 1.36 \right) = -2.08, \\
#     x_{4}^{(1)} &= \frac{1}{3} \left( 3 - 2.8 + -1.8 - -2.08 \right) = 1.36.
# \end{align*}
# 
# Calculate the residual
# 
# \begin{align*}
#     \mathbf{r}^{(1)} &= \mathbf{b} - A \mathbf{x}^{(1)} = 
#     \begin{pmatrix} 14 \\ 10 \\ -15 \\ 3 \end{pmatrix} -
#     \begin{pmatrix} 5 & 1 & -1 & 1 \\ 1 & 4 & -1 & -1 \\ -1 & -1 & 5 & 1 \\ 1 & -1 & 1 & 3 \end{pmatrix}
#     \begin{pmatrix} 2.8 \\ 1.8 \\ -2.08 \\ 1.36 \end{pmatrix} \\
#     &=
#     \begin{pmatrix} -5.24 \\ -0.72 \\ -1.36 \\ 0.0 \end{pmatrix}.
# \end{align*}
# 
# Since $\max(| \mathbf{r}^{(1)} |) = 5.24 > 10^{-4}$ we continue iterating. Calculating the second iteration
# 
# \begin{align*}
#     x_{1}^{(2)} &= \frac{1}{5} \left( 14 - 1.882 + 2.5452 - 1.89173 \right) = 1.752, \\
#     x_{2}^{(2)} &= \frac{1}{4} \left( 10 - 1.752 + 2.5452 + -1.89173 \right) = 1.882, \\
#     x_{3}^{(2)} &= \frac{1}{5} \left( -15 + -1.752 + -1.882 - 1.89173 \right) = -2.5452, \\
#     x_{4}^{(2)} &= \frac{1}{3} \left( 3 - 1.752 + -1.882 - -2.5452 \right) = 1.89173.
# \end{align*}
# 
# Calculate the residual
# 
# \begin{align*}
#     \mathbf{r}^{(2)} &= \mathbf{b} - A \mathbf{x}^{(1)} = 
#     \begin{pmatrix} 14 \\ 10 \\ -15 \\ 3 \end{pmatrix} -
#     \begin{pmatrix} 5 & 1 & -1 & 1 \\ 1 & 4 & -1 & -1 \\ -1 & -1 & 5 & 1 \\ 1 & -1 & 1 & 3 \end{pmatrix}
#     \begin{pmatrix} 1.752 \\ 1.882 \\ -2.5452 \\ 1.89173 \end{pmatrix} \\
#     &=
#     \begin{pmatrix} -1.07893 \\ 0.06653 \\ -0.53173 \\ 0 \end{pmatrix}.
# \end{align*}
# 
# Since $\max(| \mathbf{r}^{(2)} |) = 1.07893 > 10^{-4}$ we continue iterating. 
# ````
# `````

# `````{admonition} Exercise 7.3
# :class: note
# :name: ex7.3
# 
# Repeat question 1 using the SOR method using the optimum value for the relaxation parameter.
# 
# ````{dropdown} Solution
# 
# The iteration matrix for the Jacobi method for this system of linear equations is
# 
# \begin{align*}
#     T_J &= -D^{-1} (L + U) \\
#     &= 
#     \begin{pmatrix} 5 & 0 & 0 & 0 \\ 0 & 4 & 0 & 0 \\ 0 & 0 & 5 & 0 \\ 0 & 0 & 0 & 3 \end{pmatrix}^1
#     \left(
#     \begin{pmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ -1 & -1 & 0 & 0 \\ 1 & -1 & 1 & 0 \end{pmatrix} +
#     \begin{pmatrix} 0 & 1 & -1 & 1 \\ 0 & 0 & -1 & -1 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}
#     \right) \\
#     &= 
#     \begin{pmatrix} \frac{1}{5} & 0 & 0 & 0 \\ 0 & \frac{1}{4} & 0 & 0 \\ 0 & 0 & \frac{1}{5} & 0 \\ 0 & 0 & 0 & \frac{1}{3} \end{pmatrix}
#     \begin{pmatrix} 0 & 1 & -1 & 1 \\ 1 & 0 & -1 & -1 \\ -1 & -1 & 0 & 1 \\ 1 & -1 & 1 & 0 \end{pmatrix} 
#     = 
#     \begin{pmatrix}
#         0 & - \frac{1}{5} & \frac{1}{5} & - \frac{1}{5} \\
#         - \frac{1}{4} & 0 & \frac{1}{4} & \frac{1}{4} \\
#         \frac{4}{15} & \frac{2}{15} & \frac{1}{15} & - \frac{1}{5} \\
#         - \frac{1}{3} & \frac{1}{3} & - \frac{1}{3} & 0
#     \end{pmatrix}
# \end{align*},
# 
# and the eigenvalues are $\lambda_1 = -0.5347$, $\lambda_2 = -0.249523$, $\lambda_3 = 0.561913$ and $\lambda_4 =  0.222310$ so $\rho(T_J) = 0.561913$. Using equation {eq}`optimum-relaxation-parameter-equation`
# 
# \begin{align*}
#     \omega = 1 + \left( \frac{0.561913}{1 + \sqrt{1 - 0.561913^2}} \right)^2 = 1.0946.
# \end{align*}
# 
# The SOR method for this system is
# 
# \begin{align*}
#     x_{1}^{(k+1)} &= (1 - \omega)x_{1}^{(k)} + \frac{\omega}{5} \left( 14 - x_{2}^{(k)} + x_{3}^{(k)} - x_{4}^{(k)} \right), \\
#     x_{2}^{(k+1)} &= (1 - \omega)x_{2}^{(k)} + \frac{\omega}{4} \left( 10 - x_{1}^{(k+1)} + x_{3}^{(k)} + x_{4}^{(k)} \right), \\
#     x_{3}^{(k+1)} &= (1 - \omega)x_{3}^{(k)} + \frac{\omega}{5} \left( -15 + x_{1}^{(k+1)} + x_{2}^{(k+1)} - x_{4}^{(k)} \right), \\
#     x_{4}^{(k+1)} &= (1 - \omega)x_{4}^{(k)} + \frac{\omega}{3} \left( 3 - x_{1}^{(k+1)} + x_{2}^{(k+1)} - x_{3}^{(k+1)} \right).
# \end{align*}
# 
# Using starting values of $\mathbf{x} = \mathbf{0}$. Calculating the first iteration
# 
# \begin{align*}
#     x_{1}^{(1)} &= (1 - 1.0946)(2.8) - \frac{1.0946}{5} \left( 14 - 1.8 + 2.08 - 1.36 \right) = 2.8, \\
#     x_{2}^{(1)} &= (1 - 1.0946)(1.8) - \frac{1.0946}{4} \left( 10 - 2.8 + 2.08 - 1.36 \right) = 1.8, \\
#     x_{3}^{(1)} &= (1 - 1.0946)(-2.08) - \frac{1.0946}{5} \left( -15 - 2.8 - 1.8 - 1.36 \right) = -2.08, \\
#     x_{4}^{(1)} &= (1 - 1.0946)(1.36) - \frac{1.0946}{3} \left( 3 - 2.8 - 1.8 - -2.08 \right) = 1.36.
# \end{align*}
# 
# Calculate the residual
# 
# \begin{align*}
#     \mathbf{r}^{(1)} &= \mathbf{b} - A \mathbf{x}^{(1)} = 
#     \begin{pmatrix} 14 \\ 10 \\ -15 \\ 3 \end{pmatrix} -
#     \begin{pmatrix} 5 & 1 & -1 & 1 \\ 1 & 4 & -1 & -1 \\ -1 & -1 & 5 & 1 \\ 1 & -1 & 1 & 3 \end{pmatrix}
#     \begin{pmatrix} 2.8 \\ 1.8 \\ -2.08 \\ 1.36 \end{pmatrix} \\
#     &= \begin{pmatrix} -5.24 \\ -0.72 \\ -1.36 \\ 0\end{pmatrix}.
# \end{align*}
# 
# Since $\max(| \mathbf{r}^{(1)} |) = 5.24 > 10^{-4}$ we continue iterating. Calculating the second iteration
# 
# \begin{align*}
#     x_{1}^{(2)} &= (1 - 1.0946)(1.752) - \frac{1.0946}{5} \left( 14 - 1.882 + 2.5452 - 1.891733 \right) \\ 
#     &= 1.752, \\
#     x_{2}^{(2)} &= (1 - 1.0946)(1.882) - \frac{1.0946}{4} \left( 10 - 1.752 + 2.5452 - 1.891733 \right) \\
#     &= 1.882, \\
#     x_{3}^{(2)} &= (1 - 1.0946)(-2.5452) - \frac{1.0946}{5} \left( -15 - 1.752 - 1.882 - 1.891733 \right) \\
#     &= -2.5452, \\
#     x_{4}^{(2)} &= (1 - 1.0946)(1.891733) - \frac{1.0946}{3} \left( 3 - 1.752 - 1.882 - -2.5452 \right) \\
#     &= 1.891733.
# \end{align*}
# 
# Calculate the residual
# 
# \begin{align*}
#     \mathbf{r}^{(2)} &= \mathbf{b} - A \mathbf{x}^{(1)} = 
#     \begin{pmatrix} 14 \\ 10 \\ -15 \\ 3 \end{pmatrix} -
#     \begin{pmatrix} 5 & 1 & -1 & 1 \\ 1 & 4 & -1 & -1 \\ -1 & -1 & 5 & 1 \\ 1 & -1 & 1 & 3 \end{pmatrix}
#     \begin{pmatrix} 1.752 \\ 1.882 \\ -2.5452 \\ 1.891733 \end{pmatrix} \\
#     &= \begin{pmatrix} -1.078933 \\ 0.066533 \\ -0.531733 \\ -0\end{pmatrix}.
# \end{align*}
# 
# Since $\max(| \mathbf{r}^{(2)} |) = 1.078933 > 10^{-4}$ we continue iterating. 
# 
# `````

# `````{admonition} Exercise 7.4
# :class: note
# :name: ex7.4
# 
# Which method would you expect to converge to the solution with the fewest iterations? What quantitative evidence do you have to support your conclusion?
# 
# ````{dropdown} Solution
# The iteration matrices for the Jacobi, Gauss-Seidel and SOR methods (with $\omega = 1.094573$) are
# 
# \begin{align*}
#     T_J &= \begin{pmatrix} 0 & -\frac{1}{5} & \frac{1}{5} & -\frac{1}{5} \\ -\frac{1}{4} & 0 & \frac{1}{4} & \frac{1}{4} \\ \frac{1}{5} & \frac{1}{5} & 0 & -\frac{1}{5} \\ -\frac{1}{3} & \frac{1}{3} & -\frac{1}{3} & 0 \end{pmatrix}, \\
#     T_{GS} &= \begin{pmatrix} 0 & -\frac{1}{5} & \frac{1}{5} & -\frac{1}{5} \\ 0 & \frac{1}{20} & \frac{1}{5} & \frac{3}{10} \\ 0 & -\frac{3}{100} & \frac{8}{100} & -\frac{9}{50} \\ 0 & \frac{7}{75} & -\frac{2}{75} & \frac{17}{75} \end{pmatrix}, \\
#     T_{SOR} &= \begin{pmatrix} -0.094573 & -0.218915 & 0.218915 & -0.218915 \\ 0.025879 & -0.034668 & 0.213739 & 0.333548 \\ -0.015038 & -0.055513 & 0.000141 & -0.193820 \\ 0.049435 & 0.087478 & -0.001940 & 0.177714 \end{pmatrix}.
# \end{align*}
# 
# and the spectral radii for these matrices are
# 
# \begin{align*}
#     \rho(T_J) &= 0.561913, \\
#     \rho(T_{GS}) &= 0.296149, \\
#     \rho(T_{SOR}) &= 0.171610,
# \end{align*}
# 
# so we would expect the SOR method to convergence the fastest. This is supported by the results in [exercise 7.1](ex7.1), [exercise 7.2](ex7.2) and [exercise 7.3](ex7.3).
# 
# ````
# 
# `````

# `````{admonition} Exercise 7.5
# :class: note
# :name: ex7.5
# 
# 
# Write a Python program to calculate the solution to [exercise 7.1](ex7.1), [exercise 7.2](ex7.2) and [exercise 7.3](ex7.2) using a convergence tolerance of $tol=10^{-6}$. How many iterations did each of the three methods take to converge to the solution?
# 
# ````{dropdown} Solution
# 
# Code
# 
# ```python
# import numpy as np
# 
# def jacobi(A, b, tol=1e-6):
#     n = len(b)
#     x = np.zeros(n)
#     maxiter = 100
#     for k in range(maxiter):
#         xo = np.copy(x)
#         for i in range(n):
#             s = b[i]
#             for j in range(n):
#                 if i != j:
#                     s -= A[i,j] * xo[j]
#         
#             x[i] = s / A[i,i]
#             
#         r = b - np.dot(A, x)   
#         if max(abs(r)) < tol:
#             break
#     
#     return x, k
# 
# 
# def gauss_seidel(A, b, tol=1e-6):
#     n = len(b)
#     x = np.zeros(n)
#     maxiter = 100
#     for k in range(maxiter):
#         for i in range(n):
#             s = b[i]
#             for j in range(n):
#                 if i != j:
#                     s -= A[i,j] * x[j]
#         
#             x[i] = s / A[i,i]
#             
#         r = b - np.dot(A, x)   
#         if max(abs(r)) < tol:
#             break
#     
#     return x, k
# 
# 
# def sor(A, b, omega, tol=1e-6):
#     n = len(b)
#     x = np.zeros(n)
#     maxiter = 100
#     for k in range(maxiter):
#         for i in range(n):
#             s = b[i]
#             for j in range(n):
#                 if i != j:
#                     s -= A[i,j] * x[j]
#         
#             x[i] = (1 - omega) * x[i] + omega / A[i,i] * s
#             
#         r = b - np.dot(A, x)   
#         if max(abs(r)) < tol:
#             break
#     
#     return x, k
# 
# 
# # Define linear system
# A = np.array([[5, 1, -1, 1], [1, 4, -1, -1], [-1, -1, 5, 1], [1, -1, 1, 3]])
# b = np.array([14, 10, -15, 3])
# 
# # Solve linear system
# x, iterations = jacobi(A, b)
# print(f"Jacobi method:       {iterations:3d} iterations")
# 
# x, iterations = gauss_seidel(A, b)
# print(f"Gauss-Seidel method: {iterations:3d} iterations")
# 
# x, iterations = sor(A, b, 1.094573)
# print(f"SOR method:          {iterations:3d} iterations")
# 
# print("\nSolution:")
# for i in range(len(x)):
#     print(f"    x{i+1} = {x[i]:9.6f}")
# ```
# 
# Output
# ```
# Jacobi method:        26 iterations
# Gauss-Seidel method:  13 iterations
# SOR method:            9 iterations
# 
# Solution:
#     x1 =  1.438776
#     x2 =  1.979592
#     x3 = -2.734694
#     x4 =  2.091837
# ```
# ````
# 
# `````

# In[1]:


import numpy as np

def jacobi(A, b, tol=1e-6):
    n = len(b)
    x = np.zeros(n)
    maxiter = 100
    for k in range(maxiter):
        xo = np.copy(x)
        for i in range(n):
            s = b[i]
            for j in range(n):
                if i != j:
                    s -= A[i,j] * xo[j]
        
            x[i] = s / A[i,i]
            
        r = b - np.dot(A, x)   
        if max(abs(r)) < tol:
            break
    
    return x, k


def gauss_seidel(A, b, tol=1e-6):
    n = len(b)
    x = np.zeros(n)
    maxiter = 100
    for k in range(maxiter):
        for i in range(n):
            s = b[i]
            for j in range(n):
                if i != j:
                    s -= A[i,j] * x[j]
        
            x[i] = s / A[i,i]
            
        r = b - np.dot(A, x)   
        if max(abs(r)) < tol:
            break
    
    return x, k


def sor(A, b, omega, tol=1e-6):
    n = len(b)
    x = np.zeros(n)
    maxiter = 100
    for k in range(maxiter):
        for i in range(n):
            s = b[i]
            for j in range(n):
                if i != j:
                    s -= A[i,j] * x[j]
        
            x[i] = (1 - omega) * x[i] + omega / A[i,i] * s
            
        r = b - np.dot(A, x)   
        if max(abs(r)) < tol:
            break
    
    return x, k


# Define linear system
A = np.array([[5, 1, -1, 1], [1, 4, -1, -1], [-1, -1, 5, 1], [1, -1, 1, 3]])
b = np.array([14, 10, -15, 3])

# Solve linear system
x, iterations = jacobi(A, b)
print(f"Jacobi method:       {iterations:3d} iterations")

x, iterations = gauss_seidel(A, b)
print(f"Gauss-Seidel method: {iterations:3d} iterations")

x, iterations = sor(A, b, 1.094573)
print(f"SOR method:          {iterations:3d} iterations")

print("\nSolution:")
for i in range(len(x)):
    print(f"    x{i+1} = {x[i]:9.6f}")


# `````{admonition} Exercise 7.6
# :class: note
# :name: ex7.6
# 
# A linear system has the following coefficient matrix. What is the largest value that $\alpha$ can be in order for the Jacobi method to be convergent?
# \begin{align*}
#     A = \begin{pmatrix}
#         2 & 1 \\
#         \alpha  & 2
#     \end{pmatrix}
# \end{align*}
# 
# ````{dropdown} Solution
# 
# The iteration matrix for the Jacobi method use to solve this system of linear equations is
# 
# \begin{align*}
#     T &= -D^{-1}(L + U) 
#     = - \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}^{-1}
#     \begin{pmatrix} 0 & 1 \\ \alpha & 2 \end{pmatrix} \\
#     &= -\begin{pmatrix} \frac{1}{2} & 0 \\ 0 & \frac{1}{2} \end{pmatrix}
#     \begin{pmatrix} 0 & 1 \\ \alpha & 2 \end{pmatrix}
#     = \begin{pmatrix} 0 & -\frac{1}{2} \\ -\frac{1}{2} \alpha & 0 \end{pmatrix}.
# \end{align*}
# 
# Calculate the eigenvalues of $T_J$
# \begin{align*}
#     0 &= \begin{vmatrix} -\lambda & -\frac{1}{2} \\ -\frac{1}{2} \alpha & -\lambda \end{vmatrix}
#     = \lambda^2 - \frac{1}{4} \alpha, \\
#     \therefore \lambda &= \frac{1}{2} \sqrt{\alpha}
# \end{align*}
# 
# For a method to converge $\rho(T) < 1$ so $\frac{1}{2} \sqrt{\alpha} < 1$ therefore $\alpha < 4$.
# ````
# 
# `````
