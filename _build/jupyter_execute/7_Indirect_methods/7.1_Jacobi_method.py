#!/usr/bin/env python
# coding: utf-8

# (jacobi-method-section)=
# # Jacobi method
# 
# The Jacobi method is the simplest indirect method. Splitting the coefficient matrix $A$ into the of elements from the lower triangular, diagonal and upper triangular parts of $A$ to form matrices $L$,$D$ and $U$ such that $A = L + D + U$, e.g., 
# 
# \begin{align*}
#     L&=\begin{pmatrix}
#         0 & 0 & \cdots  & 0\\
#         a_{21}  & 0 & \ddots  & \vdots \\
#         \vdots  & \ddots  & \ddots  & 0\\
#         a_{n1}  & \cdots  & a_{n,n-1}  & 0
#     \end{pmatrix},&
#     D&=\begin{pmatrix}
#         a_{11}  & 0 & \cdots  & 0\\
#         0 & a_{22}  & \ddots  & \vdots \\
#         \vdots  & \ddots  & \ddots  & 0\\
#         0 & \cdots  & 0 & a_{nn} 
#     \end{pmatrix}, \\ \\
#     U&=\begin{pmatrix}
#         0 & a_{12}  & \cdots  & a_{1n}  \\
#         0 & 0 & \ddots  & \vdots  \\
#         \vdots  & \ddots  & \ddots  & a_{n-1,n}  \\
#         0 & \cdots  & 0 & 0 
#     \end{pmatrix}.
# \end{align*}
# 
# Rewriting the linear system $A\mathbf{x}=\mathbf{b}$ using $L$, $D$ and $U$ gives
# 
# \begin{align*}
#     (L+D+U)\mathbf{x}&=\mathbf{b}\\
#     (L+U)\mathbf{x}+D\mathbf{x}&=\mathbf{b}\\
#     D\mathbf{x}&=\mathbf{b}-(L+U)\mathbf{x}\\
#     \mathbf{x}&=D^{-1} (\mathbf{b}-(L+U)\mathbf{x}).
# \end{align*}
# 
# Let the $\mathbf{x}$ on the left-hand side be $\mathbf{x}^{(k+1)}$ and the $\mathbf{x}$ on the right-hand side be $\mathbf{x}^{(k)}$ then
# 
# ```{math}
# :label: matrix-form-of-the-jacobi-method-equation
# 
# \mathbf{x}^{(k+1)} = D^{-1} (\mathbf{b} - (L + U)\mathbf{x}^{(k)}),
# ```
# 
# and writing this out for each element gives the Jacobi method gives the following definition of the Jacobi method.
# 
# ````{admonition} Definition: The Jacobi method
# :class: note
# :name: jacobi-method-definition
# 
# The Jacobi method for solving a system of linear equations of the form $A \mathbf{x} = \mathbf{b}$ is
# 
# ```{math}
# :label: jacobi-method-equation
#     x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j = 1}^{i-1} a_{ij} x_j^{(k)} - \sum_{j = i+1}^n a_{ij} x_j^{(k)} \right), \qquad i = 1, \ldots ,n.
# ```
# 
# ````
# 
# The iteration matrix for the Jacobi method can be determined by rearranging equation {eq}`matrix-form-of-the-jacobi-method-equation`
# 
# \begin{align*}
#     \mathbf{x}^{(k+1)} &= D^{-1}(\mathbf{b} - (L + U) \mathbf{x}^{(k)}) \\
#     &= - D^{-1}(L + U) \mathbf{x}^{(k)} + D^{-1}\mathbf{b},
# \end{align*}
# 
# and comparing to equation {eq}`iteration-matrix-equation` we have
# 
# ````{admonition} Definition: Iteration matrix for the Jacobi method
# :class: note
# :name: jacobi-method-iteration-matrix-definition
# 
# The iteration matrix for the Jacobi method is
# ```{math}
# :label: jacobi-method-iteration-matrix-equation
# 
# T_J = - D^{-1}(L + U),
# ```
# 
# where $A = L + D + U$ such that $L$, $D$ and $U$ are lower triangular, diagonal and upper triangular matrices respectively.
# 
# ````
# 
# The iteration matrix is used to analyse the convergence properties of the method.
# 
# The Jacobi method is applied by iterating equation {eq}`jacobi-method-equation` until the estimate $\mathbf{x}^{(k+1)}$ is accurate enough for our needs. Since we do not know what the exact solution is, we need a way to estimate the error in our approximations. Since $\mathbf{x}^{(k)}$ is an approximation of the exact solution $\mathbf{x}$ then if $\mathbf{e}^{(k)}$ is the error of the $k$th iteration we have $\mathbf{x} = \mathbf{x}^{(k)} + \mathbf{e}^{(k)}$. Substituting this into the linear system $A\mathbf{x} = \mathbf{b}$ and rearranging gives
# 
# \begin{align*}
#     A (\mathbf{x}^{(k)} +\mathbf{e}^{(k)}) &= \mathbf{b} \\
#     A\mathbf{e}^{(k)} &= \mathbf{b} - A\mathbf{x}^{(k)}.
# \end{align*}
# 
# Let $\mathbf{r}^{(k)} = A\mathbf{e}^{(k)}$ be an $n \times 1$ column vector known as the **residual**
# 
# ````{admonition} Definition: The residual
# :class: note
# :name: residual-definition
# 
# ```{math}
# :label: residual-equation
# 
# \mathbf{r}  = \mathbf{b} - A \mathbf{x}^{(k)}.
# ```
# ````
# 
# As $\mathbf{x}^{(k)} \to \mathbf{x}$, $\mathbf{r} \to 0$ so we can use the following convergence criteria
# 
# \begin{align*}
#     \max(|\mathbf{r}|) < tol,
# \end{align*}
# 
# where $tol$ is some small number. The smaller the value of $tol$ the closer $\mathbf{x}^{(k)}$ is to the exact solution but of course this will require more iterations. In practice a compromise is made between the accuracy required and the computational resources available. Typical values of $tol$ are around $10^{-4}$ or $10^{-6}$.
# 
# ````{admonition} Example 7.1
# :class: seealso
# :name: jacobi-method-example
# 
# Use the Jacobi method to solve the following system of linear equations
# 
# \begin{align*}
#     4x_1 +3x_2 &=-2, \\
#     3x_1 +4x_2 -x_3 &=-8, \\
#     -x_2 +4x_3 &=14.
# \end{align*}
# 
# ```{dropdown} Solution
# 
# The Jacobi method for this system is
# 
# \begin{align*}
#     x_{1}^{(k+1)} &= \frac{1}{4} \left( -2 - 3 x_{2}^{(k)} \right), \\
#     x_{2}^{(k+1)} &= \frac{1}{4} \left( -8 - 3 x_{1}^{(k)} + x_{3}^{(k)} \right), \\
#     x_{3}^{(k+1)} &= \frac{1}{4} \left( 14 + x_{2}^{(k)} \right).
# \end{align*}
# 
# Using starting values of $\mathbf{x} = \mathbf{0}$. Calculating the first iteration
# 
# \begin{align*}
#     x_{1}^{(1)} &= \frac{1}{4} \left( -2 - 3 (-2.0) \right) = -0.5, \\
#     x_{2}^{(1)} &= \frac{1}{4} \left( -8 - 3 (-0.5) + -3.5 \right) = -2.0, \\
#     x_{3}^{(1)} &= \frac{1}{4} \left( 14 + 2.0 \right) = 3.5.
# \end{align*}
# 
# Calculate the residual
# 
# \begin{align*}
#     \mathbf{r}^{(1)} = \mathbf{b} - A \mathbf{x}^{(1)} = 
#     \begin{pmatrix} -2 \\ -8 \\ 14 \end{pmatrix} -
#     \begin{pmatrix} 4 & 3 & 0 \\ 3 & 4 & -1 \\ 0 & -1 & 4 \end{pmatrix}
#     \begin{pmatrix} -0.5 \\ -2.0 \\ 3.5 \end{pmatrix} =
#     \begin{pmatrix} 6.0 \\ 5.0 \\ -2.0 \end{pmatrix}.
# \end{align*}
# 
# Since $\max(| \mathbf{r}^{(1)} |) = 6.0 > 10^{-4}$ we continue iterating. Calculating the second iteration
# 
# \begin{align*}
#     x_{1}^{(2)} &= \frac{1}{4} \left( -2 - 3 (-0.75) \right) = 1.0, \\
#     x_{2}^{(2)} &= \frac{1}{4} \left( -8 - 3 (1.0) + -3.0 \right) = -0.75, \\
#     x_{3}^{(2)} &= \frac{1}{4} \left( 14 + 0.75 \right) = 3.0.
# \end{align*}
# 
# Calculate the residual
# 
# \begin{align*}
#     \mathbf{r}^{(2)} = \mathbf{b} - A \mathbf{x}^{(1)} = 
#     \begin{pmatrix} -2 \\ -8 \\ 14 \end{pmatrix} -
#     \begin{pmatrix} 4 & 3 & 0 \\ 3 & 4 & -1 \\ 0 & -1 & 4 \end{pmatrix}
#     \begin{pmatrix} 1.0 \\ -0.75 \\ 3.0 \end{pmatrix} =
#     \begin{pmatrix} -3.75 \\ -5.0 \\ 1.25 \end{pmatrix}.
# \end{align*}
# 
# Since $\max(| \mathbf{r}^{(2)} |) = 5.0 > 10^{-4}$ we continue iterating. The Jacobi method was iterated until $\max(|\mathbf{r}|) < 10^{-4}$ and a selection of the iteration values are given in the table below.
# 
# | $k$ |  $x_{0}$  |  $x_{1}$  |  $x_{2}$  | $\max(\mathbf{r})$ |
# |:---:|:---------:|:---------:|:---------:|:---------:|
# |   0 |  0.000000 |  0.000000 |  0.000000 | 14.000000 |
# |   1 | -0.500000 | -2.000000 |  3.500000 |  6.000000 |
# |   2 |  1.000000 | -0.750000 |  3.000000 |  5.000000 |
# |   3 |  0.062500 | -2.000000 |  3.312500 |  3.750000 |
# |   4 |  1.000000 | -1.218750 |  3.000000 |  3.125000 |
# |   5 |  0.414062 | -2.000000 |  3.195312 |  2.343750 |
# | $\vdots$ |  $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |
# |  48 |  1.000000 | -1.999975 |  3.000000 |  0.000101 |
# |  49 |  0.999981 | -2.000000 |  3.000006 |  0.000076 |
# 
# So the Jacobi method took 48 iterations to converge to the solution $x_1 =1$, $x_2 =-2$ and $x_3 = 3$.
# 
# ```
# ````
# 
# ## Python code
# 
# The code below defines the function called `jacobi()` which solves a linear system of equations of the form $A \mathbf{b} = \mathbf{x}$ using the Jacobi method.

# In[1]:


import numpy as np


def jacobi_latex(A, b, tol=1e-4):
    n = len(b)
    x = np.zeros(n)
    maxiter = 100
    ordinal = ["first", "second", "third"]
    print("The Jacobi method for this system is")
    print()
    print(r"\begin{align*}")
    for i in range(n):
        string = rf"    x_{{{i+1}}}^{{(k+1)}} &= \frac{{1}}{{{A[i,i]}}} \left( {b[i]}"
        for j in range(n):
            if i == j:
                continue
            if A[i,j] == 1:
                string += rf" - x_{{{j+1}}}"
            elif A[i,j] == -1:
                string += rf" + x_{{{j+1}}}"
            elif A[i,j] < 0:
                string += rf" + {-A[i,j]} x_{{{j+1}}}"
            elif A[i,j] > 0:
                string += rf" - {A[i,j]} x_{{{j+1}}}"
            if A[i,j] != 0:
                string += rf"^{{(k)}}"
        
        if i == n - 1:
            string += r" \right)."
        else:
            string += r" \right), \\"
            
        print(string)
    print(r"\end{align*}")
    print()
    print("Using starting values of $\mathbf{x} = \mathbf{0}$. ", end="")
        
    for k in range(2):
        xo = np.copy(x)
        for i in range(n):
            s = b[i]
            for j in range(n):
                if i != j:
                    s -= A[i,j] * xo[j]
        
            x[i] = s / A[i,i]
            
        r = b - np.dot(A, x)   
        
        print(rf"Calculating the {ordinal[k]} iteration")
        print()
        print(r"\begin{align*}")
        for i in range(n):
            string = rf"    x_{{{i+1}}}^{{({k+1})}} &= \frac{{1}}{{{A[i,i]}}} \left( {b[i]}"
            for j in range(n):
                if i == j:
                    continue
                if A[i,j] == 1:
                    string += rf" - {x[j]}"
                elif A[i,j] == -1:
                    string += rf" + {-x[j]}"
                elif A[i,j] < 0:
                    string += rf" + {-A[i,j]} ({x[j]})"
                elif A[i,j] > 0:
                    string += rf" - {A[i,j]} ({x[j]})"

            if i == n - 1:
                string += rf" \right) = {x[i]}."
            else:
                string += rf" \right) = {x[i]}, \\"

            print(string)
        
        print(r"\end{align*}")
        print()
        print("Calculate the residual")
        print()
        print(r"\begin{align*}")
        print(rf"    \mathbf{{r}}^{{({k+1})}} = \mathbf{{b}} - A \mathbf{{x}}^{{(1)}} = ")
        string = r"    \begin{pmatrix}"
        for i in range(n):
            string += rf" {b[i]}"
            if i < n - 1:
                string += r" \\"
        string += r" \end{pmatrix} -"
        print(string)

        string = r"    \begin{pmatrix}"
        for i in range(n):
            for j in range(n):
                string += rf" {A[i,j]}"
                if j < n - 1:
                    string += r" &"
            if i < n - 1:
                string += r" \\"
        string += r" \end{pmatrix}"
        print(string)

        string = r"    \begin{pmatrix}"
        for i in range(n):
            string += rf" {x[i]}"
            if i < n - 1:
                string += r" \\"
        string += r" \end{pmatrix} ="
        print(string)

        string = r"    \begin{pmatrix}"
        for i in range(n):
            string += rf" {r[i]}"
            if i < n - 1:
                string += r" \\"
        string += r" \end{pmatrix}."
        print(string)
        print(r"\end{align*}")
        print()
        print(rf"Since $\max(| \mathbf{{r}}^{{({k+1})}} |) = {max(abs(r))} > 10^{{-4}}$ we continue iterating. ", end="")
        
# Define linear system
A = np.array([[4, 3, 0], [3, 4, -1], [0, -1, 4]])
b = np.array([-2, -8, 14])

# Solve linear system
jacobi_latex(A, b)


# In[2]:


import numpy as np

def jacobi_with_table(A, b, tol=1e-6):
    n = len(b)
    x = np.zeros(n)
    maxiter = 100
    r = b - np.dot(A, x)
    headings = f"| $k$ |"
    line = "|:---:|"
    for i in range(n):
        headings += f"  $x_{{{i}}}$  |"
        line += ":---------:|"
    headings += r" $\max(\mathbf{r})$ |"
    line += ":---------:|"
    print(headings)
    print(line)
    string = f"| {0:3d} |"
    for i in range(n):
        string += f" {x[i]:9.6f} |"
    string += f" {max(abs(r)):9.6f} |"
    print(string)
        
    for k in range(maxiter):
        xo = np.copy(x)
        for i in range(n):
            s = b[i]
            for j in range(n):
                if i != j:
                    s -= A[i,j] * xo[j]
        
            x[i] = s / A[i,i]
            
        r = b - np.dot(A, x)
        
        string = f"| {k+1:3d} |"
        for i in range(n):
            string += f" {x[i]:9.6f} |"
        string += f" {max(abs(r)):9.6f} |"
        print(string)
            
        if max(abs(r)) < tol:
            break
    
    return x


 # Define linear system
A = np.array([[4, 3, 0], [3, 4, -1], [0, -1, 4]])
b = np.array([-2, -8, 14])

# Solve linear system
x = jacobi_with_table(A, b, tol=1e-4)


# In[3]:


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
    
    return x


# The inputs are:
#     
# - `A` - the coefficient matrix;
# - `b` - the constant vector;
# - `tol` - the convergence tolerance (optional, default is $10^{-6}$).
# 
# An $n$ element array `x` is initialised to all zeros and will contain the solution vector $\mathbf{x}$ for the system of linear equations. The Jacobi method is calculated until the maximum absolute residual value is less than `tol` or 100 iterations have been calculated, whichever comes first. Since the Jacobi method only uses previous estimates to calculate the next estimates we store the old values in `xo`.

# In[4]:


# Define linear system
A = np.array([[4, 3, 0], [3, 4, -1], [0, -1, 4]])
b = np.array([-2, -8, 14])

# Solve linear system
x = jacobi(A, b, tol=1e-4)

for i in range(len(x)):
    print(f"x{i+1} = {x[i]:1.6f}")

