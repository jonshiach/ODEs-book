#!/usr/bin/env python
# coding: utf-8

# (gauss-seidel-method-section)=
# # Gauss-Seidel method
# 
# In the previous section on the [Jacobi method](jacobi-method-section) we saw that the solution to the linear system of equations $A \mathbf{x} = \mathbf{x}$ can be calculated by estimating the solution $\mathbf{x}$ and calculate an improved estimation $\mathbf{x}^{(k+1)}$ using values from the current estimation $\mathbf{x}^{(k)}$. We continue to calculate the improved estimates until the largest absolute value in the [residual](residual-definition) is less than some convergence tolerance. When calculating the values in $\mathbf{x}^{(k+1)}$ we only use values from the previous estimate $\mathbf{x}^{k}$
# 
# \begin{align*}
#     x_i^{(k+1)} &= \frac{1}{a_{ii}} \left( b_i - \sum_{j=1}^n a_{ij} x_j^{(k)} \right), \\
#     &= \frac{1}{a_{ii}} \left( b_i - \underbrace{a_{i1} x_1^{(k)} - \cdots - a_{i,j-1} x_{j-1}^{(k)}}_{\mathsf{already\,calculated}} - \underbrace{a_{i,j+1} x_{j+1}^{(k)} - \cdots - a_{in} x_n^{(k)}}_{\mathsf{yet\, to\, be\, calculated}} \right)
# \end{align*}
# 
# so when calculating $x_i$, we have already calculated the next values of $x_1, x_2, \ldots, x_{i-1}$. We can improve the speed of which the Jacobi method converges by using these new values to calculate $x_i^{(k+1)}$. This gives us the **Gauss-Seidel method**
# 
# ````{admonition} Definition: The Gauss-Seidel method
# :class: note
# :name: gauss-seidel-method-definition
#     
# The Gauss-Seidel method for solving a system of linear equations of the form $A \mathbf{x} = \mathbf{b}$ is
# 
# ```{math}
# :label: gauss-seidel-method-equation
# x_i^{(k+1)} = \frac{1}{a_{ii} }\left(b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{(k+1)} -\sum_{j=i+1}^n a_{ij} x_j^{(k)} \right), \qquad i=1, \ldots , n
# ```
# ````
# 
# The iteration matrix for the Gauss-Seidel method can be found by rearranging $(L+D+U)\mathbf{x}=\mathbf{b}$
# 
# \begin{align*}
#     (L+D+U)\mathbf{x}&=\mathbf{b}\\
#     (L+D)\mathbf{x}&=\mathbf{b}-U\mathbf{x}\\
#     \mathbf{x}&=-(L+D)^{-1} U\mathbf{x}+(L+D)^{-1} \mathbf{x}.
# \end{align*}
# 
# So the matrix equation for the Gauss-Seidel method is
# 
# \begin{align*}
#     \mathbf{x}^{(k+1)} =-(L+D)^{-1} U\mathbf{x}^{(k)} +(L+D)^{-1} \mathbf{x}^{(k+1)},
# \end{align*}
# 
# and the iteration matrix is
# ````{admonition} Definition: Iteration matrix for the Gauss-Seidel method
# :class: note
# :name: gauss-seidel-method-iteration-matrix-definition
# 
# ```{math}
# :label: gauss-seidel-method-iteration-matrix-equation
# T_{GS} =-(L+D)^{-1} U,
# ```
# where $A = L + D + U$ such that $L$, $D$ and $U$ are lower triangular, diagonal and upper triangular matrices respectively.
# ````
# 
# ````{admonition} Example 7.2
# :class: seealso
# :name: gauss-seidel-method-example
# 
# Use the Gauss-Seidel method to solve the system of linear equations from [example 7.1](jacobi-method-example)
# 
# \begin{align*}
#     4x_1 +3x_2 &=-2,\\
#     3x_1 +4x_2 -x_3 &=-8,\\
#     -x_2 +4x_3 &=14.
# \end{align*}
# 
# ```{dropdown} Solution
# 
# The Gauss-Seidel method for this system is
# 
# \begin{align*}
#     x_{1}^{(k+1)} &= \frac{1}{4} \left( -2 - 3 x_{2}^{(k)} \right), \\
#     x_{2}^{(k+1)} &= \frac{1}{4} \left( -8 - 3 x_{1}^{(k+1)} + x_{3}^{(k)} \right), \\
#     x_{3}^{(k+1)} &= \frac{1}{4} \left( 14 + x_{2}^{(k+1)} \right).
# \end{align*}
# 
# Using starting values of $\mathbf{x} = \mathbf{0}$. Calculating the first iteration
# 
# \begin{align*}
#     x_{1}^{(1)} &= \frac{1}{4} \left( -2 - 3 (-1.625) \right) = -0.5, \\
#     x_{2}^{(1)} &= \frac{1}{4} \left( -8 - 3 (-0.5) + -3.09375 \right) = -1.625, \\
#     x_{3}^{(1)} &= \frac{1}{4} \left( 14 + 1.625 \right) = 3.09375.
# \end{align*}
# 
# Calculate the residual
# 
# \begin{align*}
#     \mathbf{r}^{(1)} = \mathbf{b} - A \mathbf{x}^{(1)} = 
#     \begin{pmatrix} -2 \\ -8 \\ 14 \end{pmatrix} -
#     \begin{pmatrix} 4 & 3 & 0 \\ 3 & 4 & -1 \\ 0 & -1 & 4 \end{pmatrix}
#     \begin{pmatrix} -0.5 \\ -1.625 \\ 3.09375 \end{pmatrix} =
#     \begin{pmatrix} 4.875 \\ 3.09375 \\ 0.0 \end{pmatrix}.
# \end{align*}
# 
# Since $\max(| \mathbf{r}^{(1)} |) = 4.875 > 10^{-4}$ we continue iterating. Calculating the second iteration
# 
# \begin{align*}
#     x_{1}^{(2)} &= \frac{1}{4} \left( -2 - 3 (-1.765625) \right) = 0.71875, \\
#     x_{2}^{(2)} &= \frac{1}{4} \left( -8 - 3 (0.71875) + -3.058594 \right) = -1.765625, \\
#     x_{3}^{(2)} &= \frac{1}{4} \left( 14 + 1.765625 \right) = 3.058594.
# \end{align*}
# 
# Calculate the residual
# 
# \begin{align*}
#     \mathbf{r}^{(2)} = \mathbf{b} - A \mathbf{x}^{(1)} = 
#     \begin{pmatrix} -2 \\ -8 \\ 14 \end{pmatrix} -
#     \begin{pmatrix} 4 & 3 & 0 \\ 3 & 4 & -1 \\ 0 & -1 & 4 \end{pmatrix}
#     \begin{pmatrix} 0.71875 \\ -1.765625 \\ 3.058594 \end{pmatrix} =
#     \begin{pmatrix} 0.421875 \\ -0.035156 \\ 0 \end{pmatrix}.
# \end{align*}
# 
# Since $\max(| \mathbf{r}^{(2)} |) = 0.421875 > 10^{-4}$ we continue iterating. The Gauss-Seidel method was iterated until $|\mathbf{r}| < 10^{-4}$ and a selection of the iteration values are given in the table below. Note that the Gauss-Seidel method took 19 iterations to achieve convergence to $tol=10^{-4}$ whereas the [Jacobi method](jacobi-method-example) took 48 iterations to achieve the same accuracy. 
# 
# | $k$ |  $x_{0}$  |  $x_{1}$  |  $x_{2}$  | $\max(\mathbf{r})$ |
# |:---:|:---------:|:---------:|:---------:|:---------:|
# |   0 |  0.000000 |  0.000000 |  0.000000 | 14.000000 |
# |   1 | -0.500000 | -1.625000 |  3.093750 |  4.875000 |
# |   2 |  0.718750 | -1.765625 |  3.058594 |  0.421875 |
# |   3 |  0.824219 | -1.853516 |  3.036621 |  0.263672 |
# |   4 |  0.890137 | -1.908447 |  3.022888 |  0.164795 |
# |   5 |  0.931335 | -1.942780 |  3.014305 |  0.102997 |
# | $\vdots$ |  $\vdots$ | $\vdots$ | $\vdots$ |
# |  19 |  0.999905 | -1.999921 |  3.000020 |  0.000143 |
# |  20 |  0.999940 | -1.999950 |  3.000012 |  0.000089 |
# 
# ```
# ````

# In[1]:


import numpy as np

def gauss_seidel_latex(A, b, tol=1e-6):
    n = len(b)
    x = np.zeros(n)
    maxiter = 100
    ordinal = ["first", "second", "third"]
    print("The Gauss-Seidel method for this system is")
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
            if j < i and A[i,j] != 0:
                string += rf"^{{(k+1)}}"
            elif j > i and A[i,j] != 0:
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
        for i in range(n):
            s = b[i]
            for j in range(n):
                if i != j:
                    s -= A[i,j] * x[j]

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
gauss_seidel_latex(A, b)


# In[2]:


import numpy as np

def gauss_seidel_with_table(A, b, tol=1e-6):
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
        for i in range(n):
            s = b[i]
            for j in range(n):
                if i != j:
                    s -= A[i,j] * x[j]
        
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
x = gauss_seidel_with_table(A, b, tol=1e-4)


# ## Python code
# 
# The code below defines the function `gauss_seidel()` which solves a linear system of equations of the for $A \mathbf{x} = \mathbf{b}$ using the Gauss-Seidel method.

# In[3]:


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
    
    return x

