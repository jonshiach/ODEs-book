#!/usr/bin/env python
# coding: utf-8

# # Direct methods exercises
# 
# `````{admonition} Exercise 6.1
# :class: note
# :name: ex6.1
# 
# Using pen and paper, solve the following systems of linear equations using [LU decomposition](lu-definition).
# 
# (a) 
# \begin{align*}
#     2 x_1 + 3 x_2 -   x_3   &=  4,\\
#     4 x_1 + 9 x_2 -   x_3   &= 18,\\
#             3 x_2 + 2 x_3 &= 11.
# \end{align*}                
# 
# ````{dropdown} Solution
# Calculate LU decomposition of the $A$ matrix
# 
# \begin{align*}
#     u_{11} &= a_{11} = 2 = 2, \\
#     \ell_{21} &= \frac{1}{u_{11}}\left(a_{21}\right) = \frac{1}{2}\left(4\right) = 2, \\
#     \ell_{31} &= \frac{1}{u_{11}}\left(a_{31}\right) = \frac{1}{2}\left(0\right) = 0, \\
#     \\
#     u_{12} &= a_{12} = 3 = 3, \\
#     u_{22} &= a_{22} - \ell_{21} u_{12} = 9 - 2\left(3\right) = 3, \\
#     \ell_{32} &= \frac{1}{u_{22}}\left(a_{32} - \ell_{31} u_{12}\right) = \frac{1}{3}\left(3 - \left(0\right)\left(3\right)\right) = 1, \\
#     \\
#     u_{13} &= a_{13} = -1 = -1, \\
#     u_{23} &= a_{23} - \ell_{21} u_{13} = -1 - 2\left(-1\right) = 1, \\
#     u_{33} &= a_{33} - \ell_{31} u_{13} - \ell_{32} u_{23} = 2 - \left(0\right)\left(-1\right) - 1\left(1\right) = 1, \\
#     \\
#     \therefore L &= \left[\begin{matrix}1 & 0 & 0\\2 & 1 & 0\\0 & 1 & 1\end{matrix}\right], \qquad
#     U = \left[\begin{matrix}2 & 3 & -1\\0 & 3 & 1\\0 & 0 & 1\end{matrix}\right].
# \end{align*}
# 
# Solve $L \mathbf{{y}} = \mathbf{{b}}$
# 
# \begin{align*}
#     y_{1} &= 4, \\
#     y_{2} &= 18 - 2\left(4\right) = 10, \\
#     y_{3} &= 11 - \left(0\right)\left(4\right) - 1\left(10\right) = 1.
# \end{align*}
# 
# Solve $U \mathbf{{x}} = \mathbf{{y}}$
# \begin{align*}
#     x_{3} &= 1, \\
#     x_{2} &= \frac{1}{3}\left(10 - 1\left(1\right)\right) = 3, \\
#     x_{1} &= \frac{1}{2}\left(4 - 3\left(3\right) - \left(-1\right)\left(1\right)\right) = -2.
# \end{align*}
# 
# ````
# 
# (b)
# \begin{align*}
#     3 x_1 + 9 x_2 + 5 x_3 &= 20,\\
#       x_1 + 2 x_2 + 2 x_3 &=  3,\\
#     2 x_1 + 4 x_2 + 5 x_3 &=  4.
# \end{align*}   
# 
# ````{dropdown} Solution
# Calculate LU decomposition of the $A$ matrix
# 
# \begin{align*}
#     u_{11} &= a_{11} = 3 = 3, \\
#     \ell_{21} &= \frac{1}{u_{11}}\left(a_{21}\right) = \frac{1}{3}\left(1\right) = \frac{1}{3}, \\
#     \ell_{31} &= \frac{1}{u_{11}}\left(a_{31}\right) = \frac{1}{3}\left(2\right) = \frac{2}{3}, \\
#     \\
#     u_{12} &= a_{12} = 9 = 9, \\
#     u_{22} &= a_{22} - \ell_{21} u_{12} = 2 - \frac{1}{3}\left(9\right) = -1, \\
#     \ell_{32} &= \frac{1}{u_{22}}\left(a_{32} - \ell_{31} u_{12}\right) = \frac{1}{-1}\left(4 - \frac{2}{3}\left(9\right)\right) = 2, \\
#     \\
#     u_{13} &= a_{13} = 5 = 5, \\
#     u_{23} &= a_{23} - \ell_{21} u_{13} = 2 - \frac{1}{3}\left(5\right) = \frac{1}{3}, \\
#     u_{33} &= a_{33} - \ell_{31} u_{13} - \ell_{32} u_{23} = 5 - \frac{2}{3}\left(5\right) - 2\left(\frac{1}{3}\right) = 1, \\
#     \\
#     \therefore L &= \left[\begin{matrix}1 & 0 & 0\\\frac{1}{3} & 1 & 0\\\frac{2}{3} & 2 & 1\end{matrix}\right], \qquad
#     U = \left[\begin{matrix}3 & 9 & 5\\0 & -1 & \frac{1}{3}\\0 & 0 & 1\end{matrix}\right].
# \end{align*}
# 
# Solve $L \mathbf{{y}} = \mathbf{{b}}$
# 
# \begin{align*}
#     y_{1} &= 20, \\
#     y_{2} &= 3 - \frac{1}{3}\left(20\right) = - \frac{11}{3}, \\
#     y_{3} &= 4 - \frac{2}{3}\left(20\right) - 2\left(- \frac{11}{3}\right) = -2.
# \end{align*}
# 
# Solve $U \mathbf{{x}} = \mathbf{{y}}$
# \begin{align*}
#     x_{3} &= -2 = -2, \\
#     x_{2} &= -\left(- \frac{11}{3} - \frac{1}{3}\left(-2\right)\right) = 3, \\
#     x_{1} &= \frac{1}{3}\left(20 - 9\left(3\right) - 5\left(-2\right)\right) = 1.
# \end{align*}
# 
# ````
# 
# (c) 
# \begin{align*}
#       x_1         + 3 x_3 + 2 x_4 &=  21,\\
#     3 x_1 - 2 x_2 + 5 x_3 +   x_4 &=  28,\\
#     4 x_1 -   x_2 - 2 x_3 - 3 x_4 &= -12,\\
#             2 x_2         + 3 x_4 &=  13.
# \end{align*}   
# 
# ````{dropdown} Solution
# Calculate LU decomposition of the $A$ matrix
# 
# \begin{align*}
#     u_{11} &= a_{11} = 1 = 1, \\
#     \ell_{21} &= \frac{1}{u_{11}}\left(a_{21}\right) = \frac{1}{1}\left(3\right) = 3, \\
#     \ell_{31} &= \frac{1}{u_{11}}\left(a_{31}\right) = \frac{1}{1}\left(4\right) = 4, \\
#     \ell_{41} &= \frac{1}{u_{11}}\left(a_{41}\right) = \frac{1}{1}\left(0\right) = 0, \\
#     \\
#     u_{12} &= a_{12} = 0 = 0, \\
#     u_{22} &= a_{22} - \ell_{21} u_{12} = -2 - 3\left(0\right) = -2, \\
#     \ell_{32} &= \frac{1}{u_{22}}\left(a_{32} - \ell_{31} u_{12}\right) = \frac{1}{-2}\left(-1 - 4\left(0\right)\right) = \frac{1}{2}, \\
#     \ell_{42} &= \frac{1}{u_{22}}\left(a_{42} - \ell_{41} u_{12}\right) = \frac{1}{-2}\left(2 - \left(0\right)\left(0\right)\right) = -1, \\
#     \\
#     u_{13} &= a_{13} = 3 = 3, \\
#     u_{23} &= a_{23} - \ell_{21} u_{13} = 5 - 3\left(3\right) = -4, \\
#     u_{33} &= a_{33} - \ell_{31} u_{13} - \ell_{32} u_{23} = -2 - 4\left(3\right) - \frac{1}{2}\left(-4\right) = -12, \\
#     \ell_{43} &= \frac{1}{u_{33}}\left(a_{43} - \ell_{41} u_{13} - \ell_{42} u_{23}\right) = \frac{1}{-12}\left(0 - \left(0\right)\left(3\right) - \left(-1\right)\left(-4\right)\right) = \frac{1}{3}, \\
#     \\
#     u_{14} &= a_{14} = 2 = 2, \\
#     u_{24} &= a_{24} - \ell_{21} u_{14} = 1 - 3\left(2\right) = -5, \\
#     u_{34} &= a_{34} - \ell_{31} u_{14} - \ell_{32} u_{24} = -3 - 4\left(2\right) - \frac{1}{2}\left(-5\right) = - \frac{17}{2}, \\
#     u_{44} &= a_{44} - \ell_{41} u_{14} - \ell_{42} u_{24} - \ell_{43} u_{34} = 3 - \left(0\right)\left(2\right) - \left(-1\right)\left(-5\right) - \frac{1}{3}\left(- \frac{17}{2}\right) = \frac{5}{6}, \\
#     \\
#     \therefore L &= \left[\begin{matrix}1 & 0 & 0 & 0\\3 & 1 & 0 & 0\\4 & \frac{1}{2} & 1 & 0\\0 & -1 & \frac{1}{3} & 1\end{matrix}\right], \qquad
#     U = \left[\begin{matrix}1 & 0 & 3 & 2\\0 & -2 & -4 & -5\\0 & 0 & -12 & - \frac{17}{2}\\0 & 0 & 0 & \frac{5}{6}\end{matrix}\right].
# \end{align*}
# 
# Solve $L \mathbf{{y}} = \mathbf{{b}}$
# 
# \begin{align*}
#     y_{1} &= 21, \\
#     y_{2} &= 28 - 3\left(21\right) = -35, \\
#     y_{3} &= -12 - 4\left(21\right) - \frac{1}{2}\left(-35\right) = - \frac{157}{2}, \\
#     y_{4} &= 13 - \left(0\right)\left(21\right) - \left(-1\right)\left(-35\right) - \frac{1}{3}\left(- \frac{157}{2}\right) = \frac{25}{6}.
# \end{align*}
# 
# Solve $U \mathbf{{x}} = \mathbf{{y}}$
# \begin{align*}
#     x_{4} &= \frac{1}{\frac{5}{6}}\left(\frac{25}{6}\right) = 5, \\
#     x_{3} &= \frac{1}{-12}\left(- \frac{157}{2} - \left(- \frac{17}{2}\right)\left(5\right)\right) = 3, \\
#     x_{2} &= \frac{1}{-2}\left(-35 - \left(-4\right)\left(3\right) - \left(-5\right)\left(5\right)\right) = -1, \\
#     x_{1} &= 21 - \left(0\right)\left(-1\right) - 3\left(3\right) - 2\left(5\right) = 2.
# \end{align*}
# ````
# 
# (d)
# \begin{align*}
#         x_1 + 5 x_2 + 2 x_3 + 2 x_4 &= -10,\\
#     - 2 x_1 - 4 x_2 + 2 x_3         &=  10,\\
#       3 x_1 +   x_2 - 2 x_3 -   x_4 &= -2,\\
#     - 3 x_1 - 3 x_2 + 4 x_3 -   x_4 &=  4.
# \end{align*}
# 
# ````{dropdown} Solution
# Calculate LU decomposition of the $A$ matrix
# 
# \begin{align*}
#     u_{11} &= a_{11} = 1 = 1, \\
#     \ell_{21} &= \frac{1}{u_{11}}\left(a_{21}\right) = \frac{1}{1}\left(-2\right) = -2, \\
#     \ell_{31} &= \frac{1}{u_{11}}\left(a_{31}\right) = \frac{1}{1}\left(3\right) = 3, \\
#     \ell_{41} &= \frac{1}{u_{11}}\left(a_{41}\right) = \frac{1}{1}\left(-3\right) = -3, \\
#     \\
#     u_{12} &= a_{12} = 5 = 5, \\
#     u_{22} &= a_{22} - \ell_{21} u_{12} = -4 - \left(-2\right)\left(5\right) = 6, \\
#     \ell_{32} &= \frac{1}{u_{22}}\left(a_{32} - \ell_{31} u_{12}\right) = \frac{1}{6}\left(1 - 3\left(5\right)\right) = - \frac{7}{3}, \\
#     \ell_{42} &= \frac{1}{u_{22}}\left(a_{42} - \ell_{41} u_{12}\right) = \frac{1}{6}\left(-3 - \left(-3\right)\left(5\right)\right) = 2, \\
#     \\
#     u_{13} &= a_{13} = 2 = 2, \\
#     u_{23} &= a_{23} - \ell_{21} u_{13} = 2 - \left(-2\right)\left(2\right) = 6, \\
#     u_{33} &= a_{33} - \ell_{31} u_{13} - \ell_{32} u_{23} = -2 - 3\left(2\right) - \left(- \frac{7}{3}\right)\left(6\right) = 6, \\
#     \ell_{43} &= \frac{1}{u_{33}}\left(a_{43} - \ell_{41} u_{13} - \ell_{42} u_{23}\right) = \frac{1}{6}\left(4 - \left(-3\right)\left(2\right) - 2\left(6\right)\right) = - \frac{1}{3}, \\
#     \\
#     u_{14} &= a_{14} = 2 = 2, \\
#     u_{24} &= a_{24} - \ell_{21} u_{14} = 0 - \left(-2\right)\left(2\right) = 4, \\
#     u_{34} &= a_{34} - \ell_{31} u_{14} - \ell_{32} u_{24} = -1 - 3\left(2\right) - \left(- \frac{7}{3}\right)\left(4\right) = \frac{7}{3}, \\
#     u_{44} &= a_{44} - \ell_{41} u_{14} - \ell_{42} u_{24} - \ell_{43} u_{34} = -1 - \left(-3\right)\left(2\right) - 2\left(4\right) - \left(- \frac{1}{3}\right)\left(\frac{7}{3}\right) = - \frac{20}{9}, \\
#     \\
#     \therefore L &= \left[\begin{matrix}1 & 0 & 0 & 0\\-2 & 1 & 0 & 0\\3 & - \frac{7}{3} & 1 & 0\\-3 & 2 & - \frac{1}{3} & 1\end{matrix}\right], \qquad
#     U = \left[\begin{matrix}1 & 5 & 2 & 2\\0 & 6 & 6 & 4\\0 & 0 & 6 & \frac{7}{3}\\0 & 0 & 0 & - \frac{20}{9}\end{matrix}\right].
# \end{align*}
# 
# Solve $L \mathbf{{y}} = \mathbf{{b}}$
# 
# \begin{align*}
#     y_{1} &= -10, \\
#     y_{2} &= 10 - \left(-2\right)\left(-10\right) = -10, \\
#     y_{3} &= -2 - 3\left(-10\right) - \left(- \frac{7}{3}\right)\left(-10\right) = \frac{14}{3}, \\
#     y_{4} &= 4 - \left(-3\right)\left(-10\right) - 2\left(-10\right) - \left(- \frac{1}{3}\right)\left(\frac{14}{3}\right) = - \frac{40}{9}.
# \end{align*}
# 
# Solve $U \mathbf{{x}} = \mathbf{{y}}$
# \begin{align*}
#     x_{4} &= \frac{1}{- \frac{20}{9}}\left(- \frac{40}{9}\right) = 2, \\
#     x_{3} &= \frac{1}{6}\left(\frac{14}{3} - \frac{7}{3}\left(2\right)\right) = 0, \\
#     x_{2} &= \frac{1}{6}\left(-10 - 6\left(0\right) - 4\left(2\right)\right) = -3, \\
#     x_{1} &= -10 - 5\left(-3\right) - 2\left(0\right) - 2\left(2\right) = 1.
# \end{align*}
# 
# ````
# `````

# In[1]:


from sympy import *

def forward_substitution_latex(L, b):
    n = L.shape[0]
    x = zeros(n)
    for i in range(n):
        for j in range(i):
            x[i] += L[i,j] * x[j]
            
        x[i] = 1 / L[i,i] * (b[i] - x[i])
        
    # print output
    print()
    print(r"\begin{align*}")
    
    for i in range(n):
        
        string = ""
        if L[i,i] == 1:
            string += rf"    y_{{{i+1}}} &= {latex(b[i])}"
        elif L[i,i] == -1:
            string += rf"    y_{{{i+1}}} &= - \left({latex(b[i])} = {-latex(b[i])}"
        else:
            string += rf"    y_{{{i+1}}} &= \frac{{1}}{{{latex(L[i,i])}}} \left( {latex(b[i])}"
            
        for j in range(i):
            if L[i,j] > 0:
                string += rf" - {latex(L[i,j])} \left( {latex(x[j])} \right)"
            else:
                string += rf" - \left( {latex(L[i,j])} \right) \left( {latex(x[j])} \right)"

        if L[i,i] == 1:
            string += rf" = {latex(x[i])}"
        else:
            string += rf"\right) = {latex(x[i])}"
            
        if i < n - 1:
            string += r", \\"
        else:
            string += r"."
            
        print(string)
        
    print(r"\end{align*}")
    
    return x


def back_substitution_latex(U, b):
    n = U.shape[0]
    x = zeros(n)
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            x[i] += U[i,j] * x[j]
        x[i] = 1 / U[i,i] * (b[i] - x[i])

    # Print output
    print(r"\begin{align*}") 
    for i in range(n - 1, -1, -1):
        
        string = ""
        if U[i,i] == 1:
            string += rf"    x_{{{i+1}}} &= {latex(b[i])}"
        elif U[i,i] == -1:
            string += rf"    x_{{{i+1}}} &= -\left( {latex(b[i])}"
        else:
            string += rf"    x_{{{i+1}}} &= \frac{{1}}{{{latex(U[i,i])}}} \left({latex(b[i])}"
            
        for j in range(i + 1, n):
            if U[i,j] > 0:
                string += rf" - {latex(U[i,j])} \left( {latex(x[j])} \right)"
            else:
                string += rf" - \left( {latex(U[i,j])} \right) \left( {latex(x[j])} \right)"
        
        if U[i,i] == 1:
            string += rf" = {latex(x[i])}"
        else:
            string += rf" \right) = {latex(x[i])}"
        
        if i > 0:
            string += r", \\"
        else:
            string += "."
            
        print(string)
        
    print(r"\end{align*}")
    
    return x

def lu_latex(A, b):
    
    n = A.shape[0]
    L, U = eye(n), zeros(n, n)
    
    for j in range(n):
        for i in range(j + 1):
            for k in range(i):
                U[i,j] += L[i,k] * U[k,j]
            U[i,j] = A[i,j] - U[i,j]   
            
        for i in range(j + 1, n):
            for k in range(j):
                L[i,j] += L[i,k] * U[k,j]
            L[i,j] = 1 / U[j,j] * (A[i,j] - L[i,j])

    # Print output
    print("\nCalculate LU decomposition of the $A$ matrix\n")
    print(r"\begin{align*}")
    for j in range(n):
        for i in range(j + 1):
            print(rf"    u_{{{i+1}{j+1}}} &= a_{{{i+1}{j+1}}}", end="")  
            for k in range(i):
                print(rf" - \ell_{{{i+1}{k+1}}} u_{{{k+1}{j+1}}}", end="")
            print(rf" = {latex(A[i,j])}", end="")
            for k in range(i):
                if L[i,k] > 0:
                    print(rf" - {latex(L[i,k])}\left({latex(U[k,j])}\right)", end="")
                else:
                    print(rf" - \left({latex(L[i,k])}\right)\left({latex(U[k,j])}\right)", end="")
            print(rf" = {latex(U[i,j])}, \\")
            
        for i in range(j + 1, n):
            print(rf"    \ell_{{{i+1}{j+1}}} &= \frac{{1}}{{u_{{{j+1}{j+1}}}}}\left(a_{{{i+1}{j+1}}}", end="")
            for k in range(j):
                print(rf" - \ell_{{{i+1}{k+1}}} u_{{{k+1}{j+1}}}", end="")
            print(rf"\right) = \frac{{1}}{{{latex(U[j,j])}}}\left({latex(A[i,j])}", end="")
            for k in range(j):
                if L[i,k] > 0:
                    print(rf" - {latex(L[i,k])}\left({latex(U[k,j])}\right)", end="")
                else:
                    print(rf" - \left({latex(L[i,k])}\right)\left({latex(U[k,j])}\right)", end="")
            print(rf"\right) = {latex(L[i,j])}, \\")
        print(r"    \\")
    
    print(rf"    \therefore L &= {latex(L)}, \qquad")
    print(rf"    U = {latex(U)}.")
    print("\end{align*}")
    print()
    print(r"Solve $L \mathbf{{y}} = \mathbf{{b}}$")
    y = forward_substitution_latex(L, b)
    print()
    print(r"Solve $U \mathbf{{x}} = \mathbf{{y}}$")
    x = back_substitution_latex(U, y)

    
# (a) 
A = Matrix([[2, 3, -1], [4, 9, -1], [0, 3, 2]])
b = Matrix([4, 18, 11])

# (b)
# A = Matrix([[3, 9, 5], [1, 2, 2], [2, 4, 5]])
# b = Matrix([20, 3, 4])

# (c)
# A = Matrix([[1, 0, 3, 2], [3, -2, 5, 1], [4, -1, -2, -3], [0, 2, 0, 3]])
# b = Matrix([21, 28, -12, 13])

# (d)
# A = Matrix([[1, 5, 2, 2], [-2, -4, 2, 0], [3, 1, -2, -1], [-3, -3, 4, -1]])
# b = Matrix([-10, 10, -2, 4])

lu_latex(A, b)


# `````{admonition} Exercise 6.2
# :class: note
# :name: ex6.2
# 
# Using pen and paper, solve the systems from [exercise 6.1](ex6.1) using [LUP decomposition](lup-section).
# 
# (a)
# 
# ````{dropdown} Solution
# Perform partial pivoting on the $A$ matrix
# 
# \begin{align*}
#     & \left[\begin{matrix}1 & 5 & 2 & 2\\-2 & -4 & 2 & 0\\3 & 1 & -2 & -1\\-3 & -3 & 4 & -1\end{matrix}\right]
#     \xrightarrow{R_{1} \leftrightarrow R_{3}}
#     \left[\begin{matrix}3 & 1 & -2 & -1\\-2 & -4 & 2 & 0\\1 & 5 & 2 & 2\\-3 & -3 & 4 & -1\end{matrix}\right]
#     \xrightarrow{R_{2} \leftrightarrow R_{3}}\\
#     &
#     \left[\begin{matrix}3 & 1 & -2 & -1\\1 & 5 & 2 & 2\\-2 & -4 & 2 & 0\\-3 & -3 & 4 & -1\end{matrix}\right]
#     \xrightarrow{R_{3} \leftrightarrow R_{4}}
#     \left[\begin{matrix}3 & 1 & -2 & -1\\1 & 5 & 2 & 2\\-3 & -3 & 4 & -1\\-2 & -4 & 2 & 0\end{matrix}\right]
#     , \\
#     & \left[\begin{matrix}1 & 0 & 0 & 0\\0 & 1 & 0 & 0\\0 & 0 & 1 & 0\\0 & 0 & 0 & 1\end{matrix}\right]
#     \xrightarrow{R_{1} \leftrightarrow R_{3}}
#     \left[\begin{matrix}0 & 0 & 1 & 0\\0 & 1 & 0 & 0\\1 & 0 & 0 & 0\\0 & 0 & 0 & 1\end{matrix}\right]\\
#     &
#     \xrightarrow{R_{2} \leftrightarrow R_{3}}
#     \left[\begin{matrix}0 & 0 & 1 & 0\\1 & 0 & 0 & 0\\0 & 1 & 0 & 0\\0 & 0 & 0 & 1\end{matrix}\right]
#     \xrightarrow{R_{3} \leftrightarrow R_{4}}
#     \left[\begin{matrix}0 & 0 & 1 & 0\\1 & 0 & 0 & 0\\0 & 0 & 0 & 1\\0 & 1 & 0 & 0\end{matrix}\right]
# .
# \end{align*}
# 
# Calculate LU decomposition of the $A$ matrix
# 
# \begin{align*}
#     u_{11} &= a_{11} = 4 = 4, \\
#     \ell_{21} &= \frac{1}{u_{11}}\left(a_{21}\right) = \frac{1}{4}\left(2\right) = \frac{1}{2}, \\
#     \ell_{31} &= \frac{1}{u_{11}}\left(a_{31}\right) = \frac{1}{4}\left(0\right) = 0, \\
#     \\
#     u_{12} &= a_{12} = 9 = 9, \\
#     u_{22} &= a_{22} - \ell_{21} u_{12} = 3 - \frac{1}{2}\left(9\right) = - \frac{3}{2}, \\
#     \ell_{32} &= \frac{1}{u_{22}}\left(a_{32} - \ell_{31} u_{12}\right) = \frac{1}{- \frac{3}{2}}\left(3 - \left(0\right)\left(9\right)\right) = -2, \\
#     \\
#     u_{13} &= a_{13} = -1 = -1, \\
#     u_{23} &= a_{23} - \ell_{21} u_{13} = -1 - \frac{1}{2}\left(-1\right) = - \frac{1}{2}, \\
#     u_{33} &= a_{33} - \ell_{31} u_{13} - \ell_{32} u_{23} = 2 - \left(0\right)\left(-1\right) - \left(-2\right)\left(- \frac{1}{2}\right) = 1, \\
#     \\
#     \therefore L &= \left[\begin{matrix}1 & 0 & 0\\\frac{1}{2} & 1 & 0\\0 & -2 & 1\end{matrix}\right], \qquad
#     U = \left[\begin{matrix}4 & 9 & -1\\0 & - \frac{3}{2} & - \frac{1}{2}\\0 & 0 & 1\end{matrix}\right], \qquad
#     P = \left[\begin{matrix}0 & 1 & 0\\1 & 0 & 0\\0 & 0 & 1\end{matrix}\right].
# \end{align*}
# 
# 
# Solve $L \mathbf{y} = P \mathbf{b}$
# 
# \begin{align*} \left[\begin{matrix}1 & 0 & 0\\\frac{1}{2} & 1 & 0\\0 & -2 & 1\end{matrix}\right] \mathbf{y} = \left[\begin{matrix}0 & 1 & 0\\1 & 0 & 0\\0 & 0 & 1\end{matrix}\right] \left[\begin{matrix}4\\18\\11\end{matrix}\right] = \left[\begin{matrix}18\\4\\11\end{matrix}\right]. \end{align*}
# 
# \begin{align*}
#     y_{1} &= 18, \\
#     y_{2} &= 4 - \frac{1}{2}\left(18\right) = -5, \\
#     y_{3} &= 11 - \left(0\right)\left(18\right) - \left(-2\right)\left(-5\right) = 1.
# \end{align*}
# 
# Solve $L \mathbf{x} = \mathbf{y}$
# 
# \begin{align*}
#     x_{3} &= 1 = 1, \\
#     x_{2} &= \frac{1}{- \frac{3}{2}}\left(-5 - \left(- \frac{1}{2}\right)\left(1\right)\right) = 3, \\
#     x_{1} &= \frac{1}{4}\left(18 - 9\left(3\right) - \left(-1\right)\left(1\right)\right) = -2.
# \end{align*}
# ````
# 
# (b)
# 
# ````{dropdown} Solution
# Perform partial pivoting on the $A$ matrix
# 
# \begin{align*}
#     & \left[\begin{matrix}3 & 9 & 5\\1 & 2 & 2\\2 & 4 & 5\end{matrix}\right]
#     \xrightarrow{R_{2} \leftrightarrow R_{3}}
#     \left[\begin{matrix}3 & 9 & 5\\2 & 4 & 5\\1 & 2 & 2\end{matrix}\right]
#     , \\
#     & \left[\begin{matrix}1 & 0 & 0\\0 & 1 & 0\\0 & 0 & 1\end{matrix}\right]
#     \xrightarrow{R_{2} \leftrightarrow R_{3}}
#     \left[\begin{matrix}1 & 0 & 0\\0 & 0 & 1\\0 & 1 & 0\end{matrix}\right]
# .
# \end{align*}
# 
# Calculate LU decomposition of the $A$ matrix
# 
# \begin{align*}
#     u_{11} &= a_{11} = 3 = 3, \\
#     \ell_{21} &= \frac{1}{u_{11}}\left(a_{21}\right) = \frac{1}{3}\left(2\right) = \frac{2}{3}, \\
#     \ell_{31} &= \frac{1}{u_{11}}\left(a_{31}\right) = \frac{1}{3}\left(1\right) = \frac{1}{3}, \\
#     \\
#     u_{12} &= a_{12} = 9 = 9, \\
#     u_{22} &= a_{22} - \ell_{21} u_{12} = 4 - \frac{2}{3}\left(9\right) = -2, \\
#     \ell_{32} &= \frac{1}{u_{22}}\left(a_{32} - \ell_{31} u_{12}\right) = \frac{1}{-2}\left(2 - \frac{1}{3}\left(9\right)\right) = \frac{1}{2}, \\
#     \\
#     u_{13} &= a_{13} = 5 = 5, \\
#     u_{23} &= a_{23} - \ell_{21} u_{13} = 5 - \frac{2}{3}\left(5\right) = \frac{5}{3}, \\
#     u_{33} &= a_{33} - \ell_{31} u_{13} - \ell_{32} u_{23} = 2 - \frac{1}{3}\left(5\right) - \frac{1}{2}\left(\frac{5}{3}\right) = - \frac{1}{2}, \\
#     \\
#     \therefore L &= \left[\begin{matrix}1 & 0 & 0\\\frac{2}{3} & 1 & 0\\\frac{1}{3} & \frac{1}{2} & 1\end{matrix}\right], \qquad
#     U = \left[\begin{matrix}3 & 9 & 5\\0 & -2 & \frac{5}{3}\\0 & 0 & - \frac{1}{2}\end{matrix}\right], \qquad
#     P = \left[\begin{matrix}1 & 0 & 0\\0 & 0 & 1\\0 & 1 & 0\end{matrix}\right].
# \end{align*}
# 
# 
# Solve $L \mathbf{y} = P \mathbf{b}$
# 
# \begin{align*} \left[\begin{matrix}1 & 0 & 0\\\frac{2}{3} & 1 & 0\\\frac{1}{3} & \frac{1}{2} & 1\end{matrix}\right] \mathbf{y} = \left[\begin{matrix}1 & 0 & 0\\0 & 0 & 1\\0 & 1 & 0\end{matrix}\right] \left[\begin{matrix}20\\3\\4\end{matrix}\right] = \left[\begin{matrix}20\\4\\3\end{matrix}\right]. \end{align*}
# 
# \begin{align*}
#     y_{1} &= 20, \\
#     y_{2} &= 4 - \frac{2}{3}\left(20\right) = - \frac{28}{3}, \\
#     y_{3} &= 3 - \frac{1}{3}\left(20\right) - \frac{1}{2}\left(- \frac{28}{3}\right) = 1.
# \end{align*}
# 
# Solve $L \mathbf{x} = \mathbf{y}$
# 
# \begin{align*}
#     x_{3} &= \frac{1}{- \frac{1}{2}}\left(1\right) = -2, \\
#     x_{2} &= \frac{1}{-2}\left(- \frac{28}{3} - \frac{5}{3}\left(-2\right)\right) = 3, \\
#     x_{1} &= \frac{1}{3}\left(20 - 9\left(3\right) - 5\left(-2\right)\right) = 1.
# \end{align*}
# ````
# 
# (c)
# ````{dropdown} Solution
# Perform partial pivoting on the $A$ matrix
# 
# \begin{align*}
#     & \left[\begin{matrix}1 & 0 & 3 & 2\\3 & -2 & 5 & 1\\4 & -1 & -2 & -3\\0 & 2 & 0 & 3\end{matrix}\right]
#     \xrightarrow{R_{1} \leftrightarrow R_{3}}
#     \left[\begin{matrix}4 & -1 & -2 & -3\\3 & -2 & 5 & 1\\1 & 0 & 3 & 2\\0 & 2 & 0 & 3\end{matrix}\right]
#     , \\
#     & \left[\begin{matrix}1 & 0 & 0 & 0\\0 & 1 & 0 & 0\\0 & 0 & 1 & 0\\0 & 0 & 0 & 1\end{matrix}\right]
#     \xrightarrow{R_{1} \leftrightarrow R_{3}}
#     \left[\begin{matrix}0 & 0 & 1 & 0\\0 & 1 & 0 & 0\\1 & 0 & 0 & 0\\0 & 0 & 0 & 1\end{matrix}\right]
# .
# \end{align*}
# 
# Calculate LU decomposition of the $A$ matrix
# 
# \begin{align*}
#     u_{11} &= a_{11} = 4 = 4, \\
#     \ell_{21} &= \frac{1}{u_{11}}\left(a_{21}\right) = \frac{1}{4}\left(3\right) = \frac{3}{4}, \\
#     \ell_{31} &= \frac{1}{u_{11}}\left(a_{31}\right) = \frac{1}{4}\left(1\right) = \frac{1}{4}, \\
#     \ell_{41} &= \frac{1}{u_{11}}\left(a_{41}\right) = \frac{1}{4}\left(0\right) = 0, \\
#     \\
#     u_{12} &= a_{12} = -1 = -1, \\
#     u_{22} &= a_{22} - \ell_{21} u_{12} = -2 - \frac{3}{4}\left(-1\right) = - \frac{5}{4}, \\
#     \ell_{32} &= \frac{1}{u_{22}}\left(a_{32} - \ell_{31} u_{12}\right) = \frac{1}{- \frac{5}{4}}\left(0 - \frac{1}{4}\left(-1\right)\right) = - \frac{1}{5}, \\
#     \ell_{42} &= \frac{1}{u_{22}}\left(a_{42} - \ell_{41} u_{12}\right) = \frac{1}{- \frac{5}{4}}\left(2 - \left(0\right)\left(-1\right)\right) = - \frac{8}{5}, \\
#     \\
#     u_{13} &= a_{13} = -2 = -2, \\
#     u_{23} &= a_{23} - \ell_{21} u_{13} = 5 - \frac{3}{4}\left(-2\right) = \frac{13}{2}, \\
#     u_{33} &= a_{33} - \ell_{31} u_{13} - \ell_{32} u_{23} = 3 - \frac{1}{4}\left(-2\right) - \left(- \frac{1}{5}\right)\left(\frac{13}{2}\right) = \frac{24}{5}, \\
#     \ell_{43} &= \frac{1}{u_{33}}\left(a_{43} - \ell_{41} u_{13} - \ell_{42} u_{23}\right) = \frac{1}{\frac{24}{5}}\left(0 - \left(0\right)\left(-2\right) - \left(- \frac{8}{5}\right)\left(\frac{13}{2}\right)\right) \\
#     &= \frac{13}{6}, \\
#     \\
#     u_{14} &= a_{14} = -3 = -3, \\
#     u_{24} &= a_{24} - \ell_{21} u_{14} = 1 - \frac{3}{4}\left(-3\right) = \frac{13}{4}, \\
#     u_{34} &= a_{34} - \ell_{31} u_{14} - \ell_{32} u_{24} = 2 - \frac{1}{4}\left(-3\right) - \left(- \frac{1}{5}\right)\left(\frac{13}{4}\right) = \frac{17}{5}, \\
#     u_{44} &= a_{44} - \ell_{41} u_{14} - \ell_{42} u_{24} - \ell_{43} u_{34} \\
#     &= 3 - \left(0\right)\left(-3\right) - \left(- \frac{8}{5}\right)\left(\frac{13}{4}\right) - \frac{13}{6}\left(\frac{17}{5}\right) = \frac{5}{6}, \\
#     \\
#     \therefore L &= \left[\begin{matrix}1 & 0 & 0 & 0\\\frac{3}{4} & 1 & 0 & 0\\\frac{1}{4} & - \frac{1}{5} & 1 & 0\\0 & - \frac{8}{5} & \frac{13}{6} & 1\end{matrix}\right], \qquad
#     U = \left[\begin{matrix}4 & -1 & -2 & -3\\0 & - \frac{5}{4} & \frac{13}{2} & \frac{13}{4}\\0 & 0 & \frac{24}{5} & \frac{17}{5}\\0 & 0 & 0 & \frac{5}{6}\end{matrix}\right], \\
#     P &= \left[\begin{matrix}0 & 0 & 1 & 0\\0 & 1 & 0 & 0\\1 & 0 & 0 & 0\\0 & 0 & 0 & 1\end{matrix}\right].
# \end{align*}
# 
# 
# Solve $L \mathbf{y} = P \mathbf{b}$
# 
# \begin{align*} \left[\begin{matrix}1 & 0 & 0 & 0\\\frac{3}{4} & 1 & 0 & 0\\\frac{1}{4} & - \frac{1}{5} & 1 & 0\\0 & - \frac{8}{5} & \frac{13}{6} & 1\end{matrix}\right] \mathbf{y} = \left[\begin{matrix}0 & 0 & 1 & 0\\0 & 1 & 0 & 0\\1 & 0 & 0 & 0\\0 & 0 & 0 & 1\end{matrix}\right] \left[\begin{matrix}21\\28\\-12\\13\end{matrix}\right] = \left[\begin{matrix}-12\\28\\21\\13\end{matrix}\right]. \end{align*}
# 
# \begin{align*}
#     y_{1} &= -12, \\
#     y_{2} &= 28 - \frac{3}{4}\left(-12\right) = 37, \\
#     y_{3} &= 21 - \frac{1}{4}\left(-12\right) - \left(- \frac{1}{5}\right)\left(37\right) = \frac{157}{5}, \\
#     y_{4} &= 13 - \left(0\right)\left(-12\right) - \left(- \frac{8}{5}\right)\left(37\right) - \frac{13}{6}\left(\frac{157}{5}\right) = \frac{25}{6}.
# \end{align*}
# 
# Solve $L \mathbf{x} = \mathbf{y}$
# 
# \begin{align*}
#     x_{4} &= \frac{1}{\frac{5}{6}}\left(\frac{25}{6}\right) = 5, \\
#     x_{3} &= \frac{1}{\frac{24}{5}}\left(\frac{157}{5} - \frac{17}{5}\left(5\right)\right) = 3, \\
#     x_{2} &= \frac{1}{- \frac{5}{4}}\left(37 - \frac{13}{2}\left(3\right) - \frac{13}{4}\left(5\right)\right) = -1, \\
#     x_{1} &= \frac{1}{4}\left(-12 - \left(-1\right)\left(-1\right) - \left(-2\right)\left(3\right) - \left(-3\right)\left(5\right)\right) = 2.
# \end{align*}
# ````
# 
# (d)
# ````{dropdown} Solution
# Perform partial pivoting on the $A$ matrix
# 
# \begin{align*}
#     & \left[\begin{matrix}1 & 5 & 2 & 2\\-2 & -4 & 2 & 0\\3 & 1 & -2 & -1\\-3 & -3 & 4 & -1\end{matrix}\right]
#     \xrightarrow{R_{1} \leftrightarrow R_{3}}
#     \left[\begin{matrix}3 & 1 & -2 & -1\\-2 & -4 & 2 & 0\\1 & 5 & 2 & 2\\-3 & -3 & 4 & -1\end{matrix}\right] 
#     \xrightarrow{R_{2} \leftrightarrow R_{3}}\\
#     &
#     \left[\begin{matrix}3 & 1 & -2 & -1\\1 & 5 & 2 & 2\\-2 & -4 & 2 & 0\\-3 & -3 & 4 & -1\end{matrix}\right]
#     \xrightarrow{R_{3} \leftrightarrow R_{4}}
#     \left[\begin{matrix}3 & 1 & -2 & -1\\1 & 5 & 2 & 2\\-3 & -3 & 4 & -1\\-2 & -4 & 2 & 0\end{matrix}\right]
#     , \\
#     & \left[\begin{matrix}1 & 0 & 0 & 0\\0 & 1 & 0 & 0\\0 & 0 & 1 & 0\\0 & 0 & 0 & 1\end{matrix}\right]
#     \xrightarrow{R_{1} \leftrightarrow R_{3}}
#     \left[\begin{matrix}0 & 0 & 1 & 0\\0 & 1 & 0 & 0\\1 & 0 & 0 & 0\\0 & 0 & 0 & 1\end{matrix}\right]
#     \xrightarrow{R_{2} \leftrightarrow R_{3}}\\
#     &
#     \left[\begin{matrix}0 & 0 & 1 & 0\\1 & 0 & 0 & 0\\0 & 1 & 0 & 0\\0 & 0 & 0 & 1\end{matrix}\right]
#     \xrightarrow{R_{3} \leftrightarrow R_{4}}
#     \left[\begin{matrix}0 & 0 & 1 & 0\\1 & 0 & 0 & 0\\0 & 0 & 0 & 1\\0 & 1 & 0 & 0\end{matrix}\right]
# .
# \end{align*}
# 
# Calculate LU decomposition of the $A$ matrix
# 
# \begin{align*}
#     u_{11} &= a_{11} = 3 = 3, \\
#     \ell_{21} &= \frac{1}{u_{11}}\left(a_{21}\right) = \frac{1}{3}\left(1\right) = \frac{1}{3}, \\
#     \ell_{31} &= \frac{1}{u_{11}}\left(a_{31}\right) = \frac{1}{3}\left(-3\right) = -1, \\
#     \ell_{41} &= \frac{1}{u_{11}}\left(a_{41}\right) = \frac{1}{3}\left(-2\right) = - \frac{2}{3}, \\
#     \\
#     u_{12} &= a_{12} = 1 = 1, \\
#     u_{22} &= a_{22} - \ell_{21} u_{12} = 5 - \frac{1}{3}\left(1\right) = \frac{14}{3}, \\
#     \ell_{32} &= \frac{1}{u_{22}}\left(a_{32} - \ell_{31} u_{12}\right) = \frac{1}{\frac{14}{3}}\left(-3 - \left(-1\right)\left(1\right)\right) = - \frac{3}{7}, \\
#     \ell_{42} &= \frac{1}{u_{22}}\left(a_{42} - \ell_{41} u_{12}\right) = \frac{1}{\frac{14}{3}}\left(-4 - \left(- \frac{2}{3}\right)\left(1\right)\right) = - \frac{5}{7}, \\
#     \\
#     u_{13} &= a_{13} = -2 = -2, \\
#     u_{23} &= a_{23} - \ell_{21} u_{13} = 2 - \frac{1}{3}\left(-2\right) = \frac{8}{3}, \\
#     u_{33} &= a_{33} - \ell_{31} u_{13} - \ell_{32} u_{23} = 4 - \left(-1\right)\left(-2\right) - \left(- \frac{3}{7}\right)\left(\frac{8}{3}\right) = \frac{22}{7}, \\
#     \ell_{43} &= \frac{1}{u_{33}}\left(a_{43} - \ell_{41} u_{13} - \ell_{42} u_{23}\right) \\
#     &= \frac{1}{\frac{22}{7}}\left(2 - \left(- \frac{2}{3}\right)\left(-2\right) - \left(- \frac{5}{7}\right)\left(\frac{8}{3}\right)\right) = \frac{9}{11}, \\
#     \\
#     u_{14} &= a_{14} = -1 = -1, \\
#     u_{24} &= a_{24} - \ell_{21} u_{14} = 2 - \frac{1}{3}\left(-1\right) = \frac{7}{3}, \\
#     u_{34} &= a_{34} - \ell_{31} u_{14} - \ell_{32} u_{24} = -1 - \left(-1\right)\left(-1\right) - \left(- \frac{3}{7}\right)\left(\frac{7}{3}\right) = -1, \\
#     u_{44} &= a_{44} - \ell_{41} u_{14} - \ell_{42} u_{24} - \ell_{43} u_{34} \\
#     &= 0 - \left(- \frac{2}{3}\right)\left(-1\right) - \left(- \frac{5}{7}\right)\left(\frac{7}{3}\right) - \frac{9}{11}\left(-1\right) = \frac{20}{11}, \\
#     \\
#     \therefore L &= \left[\begin{matrix}1 & 0 & 0 & 0\\\frac{1}{3} & 1 & 0 & 0\\-1 & - \frac{3}{7} & 1 & 0\\- \frac{2}{3} & - \frac{5}{7} & \frac{9}{11} & 1\end{matrix}\right], \qquad
#     U = \left[\begin{matrix}3 & 1 & -2 & -1\\0 & \frac{14}{3} & \frac{8}{3} & \frac{7}{3}\\0 & 0 & \frac{22}{7} & -1\\0 & 0 & 0 & \frac{20}{11}\end{matrix}\right], \\
#     & P = \left[\begin{matrix}0 & 0 & 1 & 0\\1 & 0 & 0 & 0\\0 & 0 & 0 & 1\\0 & 1 & 0 & 0\end{matrix}\right].
# \end{align*}
# 
# 
# Solve $L \mathbf{y} = P \mathbf{b}$
# 
# \begin{align*} \left[\begin{matrix}1 & 0 & 0 & 0\\\frac{1}{3} & 1 & 0 & 0\\-1 & - \frac{3}{7} & 1 & 0\\- \frac{2}{3} & - \frac{5}{7} & \frac{9}{11} & 1\end{matrix}\right] \mathbf{y} = \left[\begin{matrix}0 & 0 & 1 & 0\\1 & 0 & 0 & 0\\0 & 0 & 0 & 1\\0 & 1 & 0 & 0\end{matrix}\right] \left[\begin{matrix}-10\\10\\-2\\4\end{matrix}\right] = \left[\begin{matrix}-2\\-10\\4\\10\end{matrix}\right]. \end{align*}
# 
# \begin{align*}
#     y_{1} &= -2, \\
#     y_{2} &= -10 - \frac{1}{3}\left(-2\right) = - \frac{28}{3}, \\
#     y_{3} &= 4 - \left(-1\right)\left(-2\right) - \left(- \frac{3}{7}\right)\left(- \frac{28}{3}\right) = -2, \\
#     y_{4} &= 10 - \left(- \frac{2}{3}\right)\left(-2\right) - \left(- \frac{5}{7}\right)\left(- \frac{28}{3}\right) - \frac{9}{11}\left(-2\right) = \frac{40}{11}.
# \end{align*}
# 
# Solve $L \mathbf{x} = \mathbf{y}$
# 
# \begin{align*}
#     x_{4} &= \frac{1}{\frac{20}{11}}\left(\frac{40}{11}\right) = 2, \\
#     x_{3} &= \frac{1}{\frac{22}{7}}\left(-2 - \left(-1\right)\left(2\right)\right) = 0, \\
#     x_{2} &= \frac{1}{\frac{14}{3}}\left(- \frac{28}{3} - \frac{8}{3}\left(0\right) - \frac{7}{3}\left(2\right)\right) = -3, \\
#     x_{1} &= \frac{1}{3}\left(-2 - 1\left(-3\right) - \left(-2\right)\left(0\right) - \left(-1\right)\left(2\right)\right) = 1.
# \end{align*}
# ````
# 
# `````

# In[2]:


def partial_pivot_latex(A):
    n = A.shape[0]
    P = eye(n)
    A0 = A.copy()
    print(r"\begin{align*}")
    print(rf"    & {latex(A)}")
    for j in range(n):
        maxpivot, k = abs(A[j,j]), j
        for i in range(j + 1, n):
            if abs(A[i,j]) > maxpivot:
                maxpivot, k = abs(A[i,j]), i
    
        if k != j:
            A[j,:], A[k,:] = A[k,:], A[j,:]
            print(rf"    \xrightarrow{{R_{{{j+1}}} \leftrightarrow R_{{{k+1}}}}}")
            print(rf"    {latex(A)}")
    
    print(r"    , \\")
    print(rf"    & {latex(P)}")
    for j in range(n):
        maxpivot, k = abs(A0[j,j]), j
        for i in range(j + 1, n):
            if abs(A0[i,j]) > maxpivot:
                maxpivot, k = abs(A0[i,j]), i
        
        if k != j:
            A0[j,:], A0[k,:] = A0[k,:], A0[j,:]
            P[j,:], P[k,:] = P[k,:], P[j,:]
            print(rf"    \xrightarrow{{R_{{{j+1}}} \leftrightarrow R_{{{k+1}}}}}")
            print(rf"    {latex(P)}")
    
    print(r".")
    print(r"\end{align*}")
        
    return A, P


def lup_latex(A, b):
    
    n = len(b)
    print("Perform partial pivoting on the $A$ matrix\n")
    A, P = partial_pivot_latex(A)
    
    n = A.shape[0]
    L, U = eye(n), zeros(n, n)
    
    for j in range(n):
        for i in range(j + 1):
            for k in range(i):
                U[i,j] += L[i,k] * U[k,j]
            U[i,j] = A[i,j] - U[i,j]   
            
        for i in range(j + 1, n):
            for k in range(j):
                L[i,j] += L[i,k] * U[k,j]
            L[i,j] = 1 / U[j,j] * (A[i,j] - L[i,j])

    # Print output
    print("\nCalculate LU decomposition of the $A$ matrix\n")
    print(r"\begin{align*}")
    for j in range(n):
        for i in range(j + 1):
            print(rf"    u_{{{i+1}{j+1}}} &= a_{{{i+1}{j+1}}}", end="")  
            for k in range(i):
                print(rf" - \ell_{{{i+1}{k+1}}} u_{{{k+1}{j+1}}}", end="")
            print(rf" = {latex(A[i,j])}", end="")
            for k in range(i):
                if L[i,k] > 0:
                    print(rf" - {latex(L[i,k])}\left({latex(U[k,j])}\right)", end="")
                else:
                    print(rf" - \left({latex(L[i,k])}\right)\left({latex(U[k,j])}\right)", end="")
            print(rf" = {latex(U[i,j])}, \\")
            
        for i in range(j + 1, n):
            print(rf"    \ell_{{{i+1}{j+1}}} &= \frac{{1}}{{u_{{{j+1}{j+1}}}}}\left(a_{{{i+1}{j+1}}}", end="")
            for k in range(j):
                print(rf" - \ell_{{{i+1}{k+1}}} u_{{{k+1}{j+1}}}", end="")
            print(rf"\right) = \frac{{1}}{{{latex(U[j,j])}}}\left({latex(A[i,j])}", end="")
            for k in range(j):
                if L[i,k] > 0:
                    print(rf" - {latex(L[i,k])}\left({latex(U[k,j])}\right)", end="")
                else:
                    print(rf" - \left({latex(L[i,k])}\right)\left({latex(U[k,j])}\right)", end="")
            print(rf"\right) = {latex(L[i,j])}, \\")
        print(r"    \\")
    
    print(rf"    \therefore L &= {latex(L)}, \qquad")
    print(rf"    U = {latex(U)}, \qquad")
    print(rf"    P = {latex(P)}.")
    print("\end{align*}")
    print()
    
    print("\nSolve $L \mathbf{y} = P \mathbf{b}$\n")
    print(rf"\begin{{align*}} {latex(L)} \mathbf{{y}} = {latex(P)} {latex(b)} = {latex(P * b)}. \end{{align*}}")
    y = forward_substitution_latex(L, P * b)
    
    print("\nSolve $L \mathbf{x} = \mathbf{y}$\n")
    x = back_substitution_latex(U, y)
    
    
# (a) 
# A = Matrix([[2, 3, -1], [4, 9, -1], [0, 3, 2]])
# b = Matrix([4, 18, 11])

# (b)
# A = Matrix([[3, 9, 5], [1, 2, 2], [2, 4, 5]])
# b = Matrix([20, 3, 4])

# (c)
# A = Matrix([[1, 0, 3, 2], [3, -2, 5, 1], [4, -1, -2, -3], [0, 2, 0, 3]])
# b = Matrix([21, 28, -12, 13])

# (d)
A = Matrix([[1, 5, 2, 2], [-2, -4, 2, 0], [3, 1, -2, -1], [-3, -3, 4, -1]])
b = Matrix([-10, 10, -2, 4])

lup_latex(A, b)


# `````{admonition} Exercise 6.3
# :class: note
# :name: ex6.3
# 
# Using pen and paper, solve the following systems of linear equations using [Cholesky decomposition](cholesky-definition).
# 
# (a)
# \begin{align*}
#     16x_1 +16x_2 +4x_3 &=-8,\\
#     16x_1 +25x_2 +10x_3 &=-47,\\
#     4x_1 +10x_2 +6x_3 &=-30.
# \end{align*}
# 
# ````{dropdown} Solution
# Calculate the Cholesky decomposition of the matrix $A$
# 
# \begin{align*}
#     \ell_{11} &= \sqrt{ a_{11} } = \sqrt{ 16 } = 4, \\
#     \ell_{21} &= \frac{1}{\ell_{11}} \left( a_{12} \right) = \frac{1}{4} \left( 16 \right) = 4, \\
#     \ell_{31} &= \frac{1}{\ell_{11}} \left( a_{13} \right) = \frac{1}{4} \left( 4 \right) = 1, \\
#     \\
#     \ell_{22} &= \sqrt{ a_{22} - \ell_{21}^2 } = \sqrt{ 25 - 4^2 } = \sqrt{ 9 } = 3, \\
#     \ell_{32} &= \frac{1}{\ell_{22}} \left( a_{23} - \ell_{31} \ell_{21} \right) = \frac{1}{3} \left( 10 - 1 \left( 4 \right) \right) = 2, \\
#     \\
#     \ell_{33} &= \sqrt{ a_{33} - \ell_{31}^2 - \ell_{32}^2 } = \sqrt{ 6 - 1^2 - 2^2 } = \sqrt{ 1 } = 1, \\
#     \\
#     \therefore L &= \left[\begin{matrix}4 & 0 & 0\\4 & 3 & 0\\1 & 2 & 1\end{matrix}\right].
# \end{align*}
# 
# Solve $L \mathbf{y} = \mathbf{b}$
# 
# \begin{align*}
#     y_{1} &= \frac{1}{4} \left( -8\right) = -2, \\
#     y_{2} &= \frac{1}{3} \left( -47 - 4 \left( -2 \right)\right) = -13, \\
#     y_{3} &= -30 - 1 \left( -2 \right) - 2 \left( -13 \right) = -2.
# \end{align*}
# 
# Solve $L^T \mathbf{x} = \mathbf{y}$
# \begin{align*}
#     x_{3} &= -2 = -2, \\
#     x_{2} &= \frac{1}{3} \left(-13 - 2 \left( -2 \right) \right) = -3, \\
#     x_{1} &= \frac{1}{4} \left(-2 - 4 \left( -3 \right) - 1 \left( -2 \right) \right) = 3.
# \end{align*}
# ````
# 
# (b)
# \begin{align*}
#     4x_1 +2x_2 +8x_3 &=36,\\
#     2x_1 +17x_2 +20x_3 &=50,\\
#     8x_1 +20x_2 +41x_3 &=122.
# \end{align*}
# 
# ````{dropdown} Solution
# Calculate the Cholesky decomposition of the matrix $A$
# 
# \begin{align*}
#     \ell_{11} &= \sqrt{ a_{11} } = \sqrt{ 4 } = 2, \\
#     \ell_{21} &= \frac{1}{\ell_{11}} \left( a_{12} \right) = \frac{1}{2} \left( 2 \right) = 1, \\
#     \ell_{31} &= \frac{1}{\ell_{11}} \left( a_{13} \right) = \frac{1}{2} \left( 8 \right) = 4, \\
#     \\
#     \ell_{22} &= \sqrt{ a_{22} - \ell_{21}^2 } = \sqrt{ 17 - 1^2 } = \sqrt{ 16 } = 4, \\
#     \ell_{32} &= \frac{1}{\ell_{22}} \left( a_{23} - \ell_{31} \ell_{21} \right) = \frac{1}{4} \left( 20 - 4 \left( 1 \right) \right) = 4, \\
#     \\
#     \ell_{33} &= \sqrt{ a_{33} - \ell_{31}^2 - \ell_{32}^2 } = \sqrt{ 41 - 4^2 - 4^2 } = \sqrt{ 9 } = 3, \\
#     \\
#     \therefore L &= \left[\begin{matrix}2 & 0 & 0\\1 & 4 & 0\\4 & 4 & 3\end{matrix}\right].
# \end{align*}
# 
# Solve $L \mathbf{y} = \mathbf{b}$
# 
# \begin{align*}
#     y_{1} &= \frac{1}{2} \left( 36\right) = 18, \\
#     y_{2} &= \frac{1}{4} \left( 50 - 1 \left( 18 \right)\right) = 8, \\
#     y_{3} &= \frac{1}{3} \left( 122 - 4 \left( 18 \right) - 4 \left( 8 \right)\right) = 6.
# \end{align*}
# 
# Solve $L^T \mathbf{x} = \mathbf{y}$
# \begin{align*}
#     x_{3} &= \frac{1}{3} \left(6 \right) = 2, \\
#     x_{2} &= \frac{1}{4} \left(8 - 4 \left( 2 \right) \right) = 0, \\
#     x_{1} &= \frac{1}{2} \left(18 - 1 \left( 0 \right) - 4 \left( 2 \right) \right) = 5.
# \end{align*}
# ````
# 
# (c)
# \begin{align*}
#     9x_1 -9x_2 -6x_4 &=12,\\
#     -9x_1 +25x_2 +8x_3 -10x_4 &=-116,\\
#     8x_2 +8x_3 -2x_4 &=-58,\\
#     -6x_1 -10x_2 -2x_3 +33x_4 &=91.
# \end{align*}
# 
# ````{dropdown} Solution
# Calculate the Cholesky decomposition of the matrix $A$
# 
# \begin{align*}
#     \ell_{11} &= \sqrt{ a_{11} } = \sqrt{ 9 } = 3, \\
#     \ell_{21} &= \frac{1}{\ell_{11}} \left( a_{12} \right) = \frac{1}{3} \left( -9 \right) = -3, \\
#     \ell_{31} &= \frac{1}{\ell_{11}} \left( a_{13} \right) = \frac{1}{3} \left( 0 \right) = 0, \\
#     \ell_{41} &= \frac{1}{\ell_{11}} \left( a_{14} \right) = \frac{1}{3} \left( -6 \right) = -2, \\
#     \\
#     \ell_{22} &= \sqrt{ a_{22} - \ell_{21}^2 } = \sqrt{ 25 - -3^2 } = \sqrt{ 16 } = 4, \\
#     \ell_{32} &= \frac{1}{\ell_{22}} \left( a_{23} - \ell_{31} \ell_{21} \right) = \frac{1}{4} \left( 8 - \left( 0 \right) \left( -3 \right) \right) = 2, \\
#     \ell_{42} &= \frac{1}{\ell_{22}} \left( a_{24} - \ell_{41} \ell_{21} \right) = \frac{1}{4} \left( -10 - \left( -2 \right) \left( -3 \right) \right) = -4, \\
#     \\
#     \ell_{33} &= \sqrt{ a_{33} - \ell_{31}^2 - \ell_{32}^2 } = \sqrt{ 8 - 0^2 - 2^2 } = \sqrt{ 4 } = 2, \\
#     \ell_{43} &= \frac{1}{\ell_{33}} \left( a_{34} - \ell_{41} \ell_{31} - \ell_{42} \ell_{32} \right) = \frac{1}{2} \left( -2 - \left( -2 \right) \left( 0 \right) - \left( -4 \right) \left( 2 \right) \right) = 3, \\
#     \\
#     \ell_{44} &= \sqrt{ a_{44} - \ell_{41}^2 - \ell_{42}^2 - \ell_{43}^2 } = \sqrt{ 33 - -2^2 - -4^2 - 3^2 } = \sqrt{ 4 } = 2, \\
#     \\
#     \therefore L &= \left[\begin{matrix}3 & 0 & 0 & 0\\-3 & 4 & 0 & 0\\0 & 2 & 2 & 0\\-2 & -4 & 3 & 2\end{matrix}\right].
# \end{align*}
# 
# Solve $L \mathbf{y} = \mathbf{b}$
# 
# \begin{align*}
#     y_{1} &= \frac{1}{3} \left( 12\right) = 4, \\
#     y_{2} &= \frac{1}{4} \left( -116 - \left( -3 \right) \left( 4 \right)\right) = -26, \\
#     y_{3} &= \frac{1}{2} \left( -58 - \left( 0 \right) \left( 4 \right) - 2 \left( -26 \right)\right) = -3, \\
#     y_{4} &= \frac{1}{2} \left( 91 - \left( -2 \right) \left( 4 \right) - \left( -4 \right) \left( -26 \right) - 3 \left( -3 \right)\right) = 2.
# \end{align*}
# 
# Solve $L^T \mathbf{x} = \mathbf{y}$
# \begin{align*}
#     x_{4} &= \frac{1}{2} \left(2 \right) = 1, \\
#     x_{3} &= \frac{1}{2} \left(-3 - 3 \left( 1 \right) \right) = -3, \\
#     x_{2} &= \frac{1}{4} \left(-26 - 2 \left( -3 \right) - \left( -4 \right) \left( 1 \right) \right) = -4, \\
#     x_{1} &= \frac{1}{3} \left(4 - \left( -3 \right) \left( -4 \right) - \left( 0 \right) \left( -3 \right) - \left( -2 \right) \left( 1 \right) \right) = -2.
# \end{align*}
# ````
# 
# (d)
# \begin{align*}
#     x_1 +5x_2 -x_3 +2x_4 &=14,\\
#     5x_1 +29x_2 +3x_3 +12x_4 &=82,\\
#     -x_1 +3x_2 +42x_3 -13x_4 &=40,\\
#     2x_1 +12x_2 -13x_3 +39x_4 &=-34.
# \end{align*}
# 
# ````{dropdown} Solution
# Calculate the Cholesky decomposition of the matrix $A$
# 
# \begin{align*}
#     \ell_{11} &= \sqrt{ a_{11} } = \sqrt{ 1 } = 1, \\
#     \ell_{21} &= \frac{1}{\ell_{11}} \left( a_{12} \right) = \frac{1}{1} \left( 5 \right) = 5, \\
#     \ell_{31} &= \frac{1}{\ell_{11}} \left( a_{13} \right) = \frac{1}{1} \left( -1 \right) = -1, \\
#     \ell_{41} &= \frac{1}{\ell_{11}} \left( a_{14} \right) = \frac{1}{1} \left( 2 \right) = 2, \\
#     \\
#     \ell_{22} &= \sqrt{ a_{22} - \ell_{21}^2 } = \sqrt{ 29 - 5^2 } = \sqrt{ 4 } = 2, \\
#     \ell_{32} &= \frac{1}{\ell_{22}} \left( a_{23} - \ell_{31} \ell_{21} \right) = \frac{1}{2} \left( 3 - \left( -1 \right) \left( 5 \right) \right) = 4, \\
#     \ell_{42} &= \frac{1}{\ell_{22}} \left( a_{24} - \ell_{41} \ell_{21} \right) = \frac{1}{2} \left( 12 - 2 \left( 5 \right) \right) = 1, \\
#     \\
#     \ell_{33} &= \sqrt{ a_{33} - \ell_{31}^2 - \ell_{32}^2 } = \sqrt{ 42 - -1^2 - 4^2 } = \sqrt{ 25 } = 5, \\
#     \ell_{43} &= \frac{1}{\ell_{33}} \left( a_{34} - \ell_{41} \ell_{31} - \ell_{42} \ell_{32} \right) = \frac{1}{5} \left( -13 - 2 \left( -1 \right) - 1 \left( 4 \right) \right) = -3, \\
#     \\
#     \ell_{44} &= \sqrt{ a_{44} - \ell_{41}^2 - \ell_{42}^2 - \ell_{43}^2 } = \sqrt{ 39 - 2^2 - 1^2 - -3^2 } = \sqrt{ 25 } = 5, \\
#     \\
#     \therefore L &= \left[\begin{matrix}1 & 0 & 0 & 0\\5 & 2 & 0 & 0\\-1 & 4 & 5 & 0\\2 & 1 & -3 & 5\end{matrix}\right].
# \end{align*}
# 
# Solve $L \mathbf{y} = \mathbf{b}$
# 
# \begin{align*}
#     y_{1} &= 14 = 14, \\
#     y_{2} &= \frac{1}{2} \left( 82 - 5 \left( 14 \right)\right) = 6, \\
#     y_{3} &= \frac{1}{5} \left( 40 - \left( -1 \right) \left( 14 \right) - 4 \left( 6 \right)\right) = 6, \\
#     y_{4} &= \frac{1}{5} \left( -34 - 2 \left( 14 \right) - 1 \left( 6 \right) - \left( -3 \right) \left( 6 \right)\right) = -10.
# \end{align*}
# 
# Solve $L^T \mathbf{x} = \mathbf{y}$
# \begin{align*}
#     x_{4} &= \frac{1}{5} \left(-10 \right) = -2, \\
#     x_{3} &= \frac{1}{5} \left(6 - \left( -3 \right) \left( -2 \right) \right) = 0, \\
#     x_{2} &= \frac{1}{2} \left(6 - 4 \left( 0 \right) - 1 \left( -2 \right) \right) = 4, \\
#     x_{1} &= 14 - 5 \left( 4 \right) - \left( -1 \right) \left( 0 \right) - 2 \left( -2 \right) = -2.
# \end{align*}
# ````
# `````

# In[3]:


def cholesky(A):
    n = A.shape[0]
    L = zeros(n, n)   
    for j in range(n):
        for i in range(j, n):
            for k in range(j):
                L[i,j] += L[i,k] * L[j,k]
                
            if i == j:
                L[i,j] = sqrt(A[i,j] - L[i,j])
            else:
                L[i,j] = 1 / L[j,j] * (A[i,j] - L[i,j])
     
    
    print("Calculate the Cholesky decomposition of the matrix $A$")
    print()
    print(r"\begin{align*}")
    for j in range(n):
        for i in range(j, n):
        
            string = rf"    \ell_{{{i+1}{j+1}}} &= "
            if i == j:
                string += r"\sqrt{ " + rf"a_{{{j+1}{j+1}}} "
                for k in range(j):
                    string += rf"- \ell_{{{i+1}{k+1}}}^2 " 
                
                if j == 0:
                    string += "}" + rf" = \sqrt{{ {latex(A[i,j])} }} = {latex(L[i,j])}, \\"
                else:
                    string += "}" + r" = \sqrt{ " + rf"{latex(A[i,j])} "
                    for k in range(j):
                        string += rf"- {latex(L[i,k])}^2 "
                    
                    string += "}" + rf" = \sqrt{{ {latex(L[i,j] ** 2)} }} = {latex(L[i,j])}, \\"
            
            else:
                string += rf"\frac{{1}}{{\ell_{{{j+1}{j+1}}}}} \left( a_{{{j+1}{i+1}}} "
                for k in range(j):
                    string += rf"- \ell_{{{i+1}{k+1}}} \ell_{{{j+1}{k+1}}} "
                    
                string += r"\right) = "
#                 if L[j,j] != 1:
                string += rf"\frac{{1}}{{{latex(L[j,j])}}} \left( {latex(A[i,j])} "
                
                for k in range(j):
                    if L[i,k] > 0:
                        string += rf"- {latex(L[i,k])} \left( {latex(L[j,k])} \right) "
                    else:
                        string += rf"- \left( {latex(L[i,k])} \right) \left( {latex(L[j,k])} \right) "
                
                string += rf"\right) = {latex(L[i,j])}, \\"

            print(string)
        print(r"    \\")
    print(rf"    \therefore L &= {latex(L)}.")
    print(r"\end{align*}")

    print()
    print("Solve $L \mathbf{y} = \mathbf{b}$")
    y = forward_substitution_latex(L, b)
    print()
    print("Solve $L^T \mathbf{x} = \mathbf{y}$")
    x = back_substitution_latex(L.T, y)


# (a)
# A = Matrix([[16, 16, 4], [16, 25, 10], [4, 10, 6]])
# b = Matrix([-8, -47, -30])

# (b)
# A = Matrix([[4, 2, 8], [2, 17, 20], [8, 20, 41]])
# b = Matrix([36, 50, 122])

# (c)
# A = Matrix([[9, -9, 0, -6], [-9, 25, 8, -10], [0, 8, 8, -2], [-6, -10, -2, 33]])
# b = Matrix([12, -116, -58, 91])

# (d)
A = Matrix([[1, 5, -1, 2], [5, 29, 3, 12], [-1, 3, 42, -13], [2, 12, -13, 39]])
b = Matrix([14, 82, 40, -34])

cholesky(A)


# `````{admonition} Exercise 6.4
# :class: note
# :name: ex6.4
# 
# Using pen and paper, solve the following system of equations using QR decomposition with the [Gram-Schmidt process](qr-gramschmidt-definition)
# 
# (a)
# \begin{align*}
#     x_1 +x_2 &=9,\\
#     -x_1 &=-5.
# \end{align*}
# 
# ````{dropdown} Solution
# $j = 1$:
# \begin{align*}
#     \mathbf{u}_{1} &= \mathbf{a}_{1} = \left[\begin{matrix}1 & -1\end{matrix}\right]^T, \\
#     r_{11} &= \| \mathbf{u}_{1} \| = \sqrt{2}, \\
#     \mathbf{q}_{1} &= \frac{\mathbf{u}_{1}}{r_{11}} = \frac{\left[\begin{matrix}1 & -1\end{matrix}\right]^T}{\sqrt{2}} = \left[\begin{matrix}\frac{\sqrt{2}}{2} & - \frac{\sqrt{2}}{2}\end{matrix}\right]^T, \\
#      \\
# \end{align*}
# $j = 2$:
# \begin{align*}
#     r_{12} &= \mathbf{q}_{1} \cdot \mathbf{a}_{2} = \frac{\sqrt{2}}{2}, \\
#     \mathbf{u}_{2} &= \mathbf{a}_{2} - r_{12} \mathbf{q}_{1} = \left[\begin{matrix}\frac{1}{2} & \frac{1}{2}\end{matrix}\right]^T, \\
#     r_{22} &= \| \mathbf{u}_{2} \| = \frac{\sqrt{2}}{2}, \\
#     \mathbf{q}_{2} &= \frac{\mathbf{u}_{2}}{r_{22}} = \frac{\left[\begin{matrix}\frac{1}{2} & \frac{1}{2}\end{matrix}\right]^T}{\frac{\sqrt{2}}{2}} = \left[\begin{matrix}\frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2}\end{matrix}\right]^T, \\
#      \\
# \end{align*}
# 
# therefore
# 
# \begin{align*}
#     Q &= \left[\begin{matrix}\frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2}\\- \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2}\end{matrix}\right], \qquad R = \left[\begin{matrix}\sqrt{2} & \frac{\sqrt{2}}{2}\\0 & \frac{\sqrt{2}}{2}\end{matrix}\right].
# \end{align*}
# 
# Solve $R \mathbf{{x}} = Q^T \mathbf{{b}}$
# 
# \begin{align*}
#     \left[\begin{matrix}\sqrt{2} & \frac{\sqrt{2}}{2}\\0 & \frac{\sqrt{2}}{2}\end{matrix}\right] \mathbf{x} = \left[\begin{matrix}\frac{\sqrt{2}}{2} & - \frac{\sqrt{2}}{2}\\\frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2}\end{matrix}\right]\left[\begin{matrix}9\\-5\end{matrix}\right] = \left[\begin{matrix}7 \sqrt{2}\\2 \sqrt{2}\end{matrix}\right],
# \end{align*}
# gives
# \begin{align*}
#     x_{2} &= \frac{1}{\frac{\sqrt{2}}{2}} (2 \sqrt{2}) = 4, \\
#     x_{1} &= \frac{1}{\sqrt{2}} (7 \sqrt{2} - \frac{\sqrt{2}}{2}(4)) = 5.
# \end{align*}
# ````
# 
# (b)
# \begin{align*}
#     6x_1 +6x_2 +x_3 &=3,\\
#     3x_1 +6x_2 +x_3 &=0,\\
#     2x_1 +x_2 +x_3 &=4.
# \end{align*}
# 
# ````{dropdown} Solution
# $j = 1$:
# \begin{align*}
#     \mathbf{u}_{1} &= \mathbf{a}_{1} = \left[\begin{matrix}6 & 3 & 2\end{matrix}\right]^T, \\
#     r_{11} &= \| \mathbf{u}_{1} \| = 7, \\
#     \mathbf{q}_{1} &= \frac{\mathbf{u}_{1}}{r_{11}} = \frac{\left[\begin{matrix}6 & 3 & 2\end{matrix}\right]^T}{7} = \left[\begin{matrix}\frac{6}{7} & \frac{3}{7} & \frac{2}{7}\end{matrix}\right]^T, \\
#      \\
# \end{align*}
# $j = 2$:
# \begin{align*}
#     r_{12} &= \mathbf{q}_{1} \cdot \mathbf{a}_{2} = 8, \\
#     \mathbf{u}_{2} &= \mathbf{a}_{2} - r_{12} \mathbf{q}_{1} = \left[\begin{matrix}- \frac{6}{7} & \frac{18}{7} & - \frac{9}{7}\end{matrix}\right]^T, \\
#     r_{22} &= \| \mathbf{u}_{2} \| = 3, \\
#     \mathbf{q}_{2} &= \frac{\mathbf{u}_{2}}{r_{22}} = \frac{\left[\begin{matrix}- \frac{6}{7} & \frac{18}{7} & - \frac{9}{7}\end{matrix}\right]^T}{3} = \left[\begin{matrix}- \frac{2}{7} & \frac{6}{7} & - \frac{3}{7}\end{matrix}\right]^T, \\
#      \\
# \end{align*}
# $j = 3$:
# \begin{align*}
#     r_{13} &= \mathbf{q}_{1} \cdot \mathbf{a}_{3} = \frac{11}{7}, \\
#     r_{23} &= \mathbf{q}_{2} \cdot \mathbf{a}_{3} = \frac{1}{7}, \\
#     \mathbf{u}_{3} &= \mathbf{a}_{3} - r_{13} \mathbf{q}_{1} - r_{23} \mathbf{q}_{2} = \left[\begin{matrix}- \frac{15}{49} & \frac{10}{49} & \frac{30}{49}\end{matrix}\right]^T, \\
#     r_{33} &= \| \mathbf{u}_{3} \| = \frac{5}{7}, \\
#     \mathbf{q}_{3} &= \frac{\mathbf{u}_{3}}{r_{33}} = \frac{\left[\begin{matrix}- \frac{15}{49} & \frac{10}{49} & \frac{30}{49}\end{matrix}\right]^T}{\frac{5}{7}} = \left[\begin{matrix}- \frac{3}{7} & \frac{2}{7} & \frac{6}{7}\end{matrix}\right]^T, \\
#      \\
# \end{align*}
# 
# therefore
# 
# \begin{align*}
#     Q &= \left[\begin{matrix}\frac{6}{7} & - \frac{2}{7} & - \frac{3}{7}\\\frac{3}{7} & \frac{6}{7} & \frac{2}{7}\\\frac{2}{7} & - \frac{3}{7} & \frac{6}{7}\end{matrix}\right], \qquad R = \left[\begin{matrix}7 & 8 & \frac{11}{7}\\0 & 3 & \frac{1}{7}\\0 & 0 & \frac{5}{7}\end{matrix}\right].
# \end{align*}
# 
# Solve $R \mathbf{{x}} = Q^T \mathbf{{b}}$
# 
# \begin{align*}
#     \left[\begin{matrix}7 & 8 & \frac{11}{7}\\0 & 3 & \frac{1}{7}\\0 & 0 & \frac{5}{7}\end{matrix}\right] \mathbf{x} = \left[\begin{matrix}\frac{6}{7} & \frac{3}{7} & \frac{2}{7}\\- \frac{2}{7} & \frac{6}{7} & - \frac{3}{7}\\- \frac{3}{7} & \frac{2}{7} & \frac{6}{7}\end{matrix}\right]\left[\begin{matrix}3\\0\\4\end{matrix}\right] = \left[\begin{matrix}\frac{26}{7}\\- \frac{18}{7}\\\frac{15}{7}\end{matrix}\right],
# \end{align*}
# gives
# \begin{align*}
#     x_{3} &= \frac{1}{\frac{5}{7}} (\frac{15}{7}) = 3, \\
#     x_{2} &= \frac{1}{3} (- \frac{18}{7} - \frac{1}{7}(3)) = -1, \\
#     x_{1} &= \frac{1}{7} (\frac{26}{7} - 8(-1) - \frac{11}{7}(3)) = 1.
# \end{align*}
# ````
# 
# (c)
# \begin{align*}
#     x_1 + 2 x_2 +   x_3 &= 3,\\
#     x_1 + 4 x_2 + 3 x_3 &= 9,\\
#     x_1 - 4 x_2 + 6 x_3 &= 29,\\
#     x_1 + 2 x_2 +   x_3 &= 3.
# \end{align*}
# 
# ````{dropdown} Solution
# $j = 1$:
# \begin{align*}
#     \mathbf{u}_{1} &= \mathbf{a}_{1} = \left[\begin{matrix}1 & 1 & 1 & 1\end{matrix}\right]^T, \\
#     r_{11} &= \| \mathbf{u}_{1} \| = 2, \\
#     \mathbf{q}_{1} &= \frac{\mathbf{u}_{1}}{r_{11}} = \frac{\left[\begin{matrix}1 & 1 & 1 & 1\end{matrix}\right]^T}{2} = \left[\begin{matrix}\frac{1}{2} & \frac{1}{2} & \frac{1}{2} & \frac{1}{2}\end{matrix}\right]^T, \\
#      \\
# \end{align*}
# $j = 2$:
# \begin{align*}
#     r_{12} &= \mathbf{q}_{1} \cdot \mathbf{a}_{2} = 2, \\
#     \mathbf{u}_{2} &= \mathbf{a}_{2} - r_{12} \mathbf{q}_{1} = \left[\begin{matrix}1 & 3 & -5 & 1\end{matrix}\right]^T, \\
#     r_{22} &= \| \mathbf{u}_{2} \| = 6, \\
#     \mathbf{q}_{2} &= \frac{\mathbf{u}_{2}}{r_{22}} = \frac{\left[\begin{matrix}1 & 3 & -5 & 1\end{matrix}\right]^T}{6} = \left[\begin{matrix}\frac{1}{6} & \frac{1}{2} & - \frac{5}{6} & \frac{1}{6}\end{matrix}\right]^T, \\
#      \\
# \end{align*}
# $j = 3$:
# \begin{align*}
#     r_{13} &= \mathbf{q}_{1} \cdot \mathbf{a}_{3} = \frac{11}{2}, \\
#     r_{23} &= \mathbf{q}_{2} \cdot \mathbf{a}_{3} = - \frac{19}{6}, \\
#     \mathbf{u}_{3} &= \mathbf{a}_{3} - r_{13} \mathbf{q}_{1} - r_{23} \mathbf{q}_{2} = \left[\begin{matrix}- \frac{11}{9} & \frac{11}{6} & \frac{11}{18} & - \frac{11}{9}\end{matrix}\right]^T, \\
#     r_{33} &= \| \mathbf{u}_{3} \| = \frac{11 \sqrt{2}}{6}, \\
#     \mathbf{q}_{3} &= \frac{\mathbf{u}_{3}}{r_{33}} = \frac{\left[\begin{matrix}- \frac{11}{9} & \frac{11}{6} & \frac{11}{18} & - \frac{11}{9}\end{matrix}\right]^T}{\frac{11 \sqrt{2}}{6}} \\
#     &= \left[\begin{matrix}- \frac{\sqrt{2}}{3} & \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{6} & - \frac{\sqrt{2}}{3}\end{matrix}\right]^T, \\
#      \\
# \end{align*}
# 
# therefore
# 
# \begin{align*}
#     Q &= \left[\begin{matrix}\frac{1}{2} & \frac{1}{6} & - \frac{\sqrt{2}}{3}\\\frac{1}{2} & \frac{1}{2} & \frac{\sqrt{2}}{2}\\\frac{1}{2} & - \frac{5}{6} & \frac{\sqrt{2}}{6}\\\frac{1}{2} & \frac{1}{6} & - \frac{\sqrt{2}}{3}\end{matrix}\right], \qquad R = \left[\begin{matrix}2 & 2 & \frac{11}{2}\\0 & 6 & - \frac{19}{6}\\0 & 0 & \frac{11 \sqrt{2}}{6}\end{matrix}\right].
# \end{align*}
# 
# Solve $R \mathbf{{x}} = Q^T \mathbf{{b}}$
# 
# \begin{align*}
#     \left[\begin{matrix}2 & 2 & \frac{11}{2}\\0 & 6 & - \frac{19}{6}\\0 & 0 & \frac{11 \sqrt{2}}{6}\end{matrix}\right] \mathbf{x} = \left[\begin{matrix}\frac{1}{2} & \frac{1}{2} & \frac{1}{2} & \frac{1}{2}\\\frac{1}{6} & \frac{1}{2} & - \frac{5}{6} & \frac{1}{6}\\- \frac{\sqrt{2}}{3} & \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{6} & - \frac{\sqrt{2}}{3}\end{matrix}\right]\left[\begin{matrix}3\\9\\29\\3\end{matrix}\right] = \left[\begin{matrix}22\\- \frac{56}{3}\\\frac{22 \sqrt{2}}{3}\end{matrix}\right],
# \end{align*}
# gives
# \begin{align*}
#     x_{3} &= \frac{1}{\frac{11 \sqrt{2}}{6}} (\frac{22 \sqrt{2}}{3}) = 4, \\
#     x_{2} &= \frac{1}{6} (- \frac{56}{3} - (- \frac{19}{6})(4)) = -1, \\
#     x_{1} &= \frac{1}{2} (22 - 2(-1) - \frac{11}{2}(4)) = 1.
# \end{align*}
# ````
# 
# `````

# In[4]:


def qr_gramschmidt_latex(A):
    m, n = A.shape
    Q, R, U = zeros(m, n), zeros(n, n), zeros(m, n)
    
    for j in range(n):
        for i in range(j):
            R[i,j] = Q[:,i].dot(A[:,j])
            U[:,j] += R[i,j] * Q[:,i]
            
        U[:,j] = A[:,j] - U[:,j]
        R[j,j] = U[:,j].norm()
        Q[:,j] = U[:,j] / R[j,j]
    
    
    for j in range(n):
        
        print(rf"$j = {j+1}$:")
        print(r"\begin{align*}")
        for i in range(j):
            print(rf"    r_{{{i+1}{j+1}}} &= \mathbf{{q}}_{{{i+1}}} \cdot \mathbf{{a}}_{{{j+1}}}")
            print(rf" = {latex(R[i,j])}, \\")
        print(rf"    \mathbf{{u}}_{{{j+1}}} &= \mathbf{{a}}_{{{j+1}}}", end="")
        for i in range(j):
            print(rf" - r_{{{i+1}{j+1}}} \mathbf{{q}}_{{{i+1}}}", end="")
        print(rf" = {latex(U[:,j].T)}^T, \\")
        print(rf"    r_{{{j+1}{j+1}}} &= \| \mathbf{{u}}_{{{j+1}}} \| ")
        print(rf" = {latex(R[j,j])}, \\")
        print(rf"    \mathbf{{q}}_{{{j+1}}} &= \tfrac{{\mathbf{{u}}_{{{j+1}}}}}{{r_{{{j+1}{j+1}}}}} ")
        print(rf" = \tfrac{{{latex(U[:,j].T)}^T}}{{{latex(R[j,j])}}} = {latex(Q[:,j].T)}^T, \\")
        print(r"     \\")
        print(r"\end{align*}")
        
    print("\ntherefore\n")
    print(r"\begin{align*}")
    print(rf"    Q &= {latex(Q)}, \qquad R = {latex(R)}.")
    print(r"\end{align*}")
        
    
    return Q, R

A = Matrix([[1, 1], [-1, 0]])
b = Matrix([9, -5])
Q, R = qr_gramschmidt_latex(A)

print()
print(r"Solve $R \mathbf{{x}} = Q^T \mathbf{{b}}$")
print()
print(r"\begin{align*}")
print(rf"    {latex(R)} \mathbf{{x}} = {latex(Q.T)}{latex(b)} = {latex(Q.T * b)},")
print(r"\end{align*}")
print("gives")

x = back_substitution_latex(R, Q.T * b)


# `````{admonition} Exercise 6.5
# :class: note
# :name: ex6.5
# 
# Using pen and paper, solve the system of equations from part (b) of [exercise 6.4](ex6.4) using QR decomposition with [Householder transformations](qr-householder-definition).
# 
# ````{dropdown} Solution
# Column $j = 1$:
# \begin{align*}
#     \mathbf{u} &= \mathbf{r}_{1} + \operatorname{sign}(r_{11}) \| \mathbf{r}_{1} \| \mathbf{e} = \left[\begin{matrix}6 & 3 & 2\end{matrix}\right]^T + 7 \left[\begin{matrix}1 & 0 & 0\end{matrix}\right]^T \\
#     &= \left[\begin{matrix}13 & 3 & 2\end{matrix}\right]^T, \\
#     \mathbf{v} &= \frac{\mathbf{u}}{\| \mathbf{u} \|} = \frac{\left[\begin{matrix}13 & 3 & 2\end{matrix}\right]^T}{\sqrt{182}}, \\
#     H &= I_3 - 2\mathbf{vv}^T = I_3 - \frac{2}{182}\left[\begin{matrix}\frac{\sqrt{182}}{14}\\\frac{3 \sqrt{182}}{182}\\\frac{\sqrt{182}}{91}\end{matrix}\right]\left[\begin{matrix}\frac{\sqrt{182}}{14} & \frac{3 \sqrt{182}}{182} & \frac{\sqrt{182}}{91}\end{matrix}\right] \\
#       &= I_3 - \frac{1}{91}\left[\begin{matrix}\frac{13}{14} & \frac{3}{14} & \frac{1}{7}\\\frac{3}{14} & \frac{9}{182} & \frac{3}{91}\\\frac{1}{7} & \frac{3}{91} & \frac{2}{91}\end{matrix}\right] = \left[\begin{matrix}- \frac{6}{7} & - \frac{3}{7} & - \frac{2}{7}\\- \frac{3}{7} & \frac{82}{91} & - \frac{6}{91}\\- \frac{2}{7} & - \frac{6}{91} & \frac{87}{91}\end{matrix}\right],
# \end{align*}
# 
# Updating $R$ and $Q$
# \begin{align*}
#     R &= H R = \left[\begin{matrix}- \frac{6}{7} & - \frac{3}{7} & - \frac{2}{7}\\- \frac{3}{7} & \frac{82}{91} & - \frac{6}{91}\\- \frac{2}{7} & - \frac{6}{91} & \frac{87}{91}\end{matrix}\right]\left[\begin{matrix}6 & 6 & 1\\3 & 6 & 1\\2 & 1 & 1\end{matrix}\right] = \left[\begin{matrix}-7 & -8 & - \frac{11}{7}\\0 & \frac{36}{13} & \frac{37}{91}\\0 & - \frac{15}{13} & \frac{55}{91}\end{matrix}\right], \\
#     Q &= Q H = \left[\begin{matrix}1 & 0 & 0\\0 & 1 & 0\\0 & 0 & 1\end{matrix}\right]\left[\begin{matrix}- \frac{6}{7} & - \frac{3}{7} & - \frac{2}{7}\\- \frac{3}{7} & \frac{82}{91} & - \frac{6}{91}\\- \frac{2}{7} & - \frac{6}{91} & \frac{87}{91}\end{matrix}\right] = \left[\begin{matrix}- \frac{6}{7} & - \frac{3}{7} & - \frac{2}{7}\\- \frac{3}{7} & \frac{82}{91} & - \frac{6}{91}\\- \frac{2}{7} & - \frac{6}{91} & \frac{87}{91}\end{matrix}\right].
# \end{align*}
# 
# Column $j = 2$:
# \begin{align*}
#     \mathbf{u} &= \mathbf{r}_{2} + \operatorname{sign}(r_{22}) \| \mathbf{r}_{2} \| \mathbf{e} = \left[\begin{matrix}\frac{36}{13} & - \frac{15}{13}\end{matrix}\right]^T + 3 \left[\begin{matrix}1 & 0\end{matrix}\right]^T = \left[\begin{matrix}\frac{75}{13} & - \frac{15}{13}\end{matrix}\right]^T, \\
#     \mathbf{v} &= \frac{\mathbf{u}}{\| \mathbf{u} \|} = \frac{\left[\begin{matrix}\frac{75}{13} & - \frac{15}{13}\end{matrix}\right]^T}{\frac{15 \sqrt{26}}{13}}, \\
#     H &= I_2 - 2\mathbf{vv}^T = I_2 - \frac{2}{\frac{450}{13}}\left[\begin{matrix}\frac{5 \sqrt{26}}{26}\\- \frac{\sqrt{26}}{26}\end{matrix}\right]\left[\begin{matrix}\frac{5 \sqrt{26}}{26} & - \frac{\sqrt{26}}{26}\end{matrix}\right] \\
#       &= I_2 - \frac{13}{225}\left[\begin{matrix}\frac{25}{26} & - \frac{5}{26}\\- \frac{5}{26} & \frac{1}{26}\end{matrix}\right] = \left[\begin{matrix}- \frac{12}{13} & \frac{5}{13}\\\frac{5}{13} & \frac{12}{13}\end{matrix}\right],
# \end{align*}
# 
# Adding the first 1 rows and columns of the identity matrix to $H$
# 
# \begin{align*}
#     H &= \left[\begin{matrix}1 & 0 & 0\\0 & - \frac{12}{13} & \frac{5}{13}\\0 & \frac{5}{13} & \frac{12}{13}\end{matrix}\right].
# \end{align*}
# 
# Updating $R$ and $Q$
# \begin{align*}
#     R = H R &= \left[\begin{matrix}1 & 0 & 0\\0 & - \frac{12}{13} & \frac{5}{13}\\0 & \frac{5}{13} & \frac{12}{13}\end{matrix}\right]\left[\begin{matrix}-7 & -8 & - \frac{11}{7}\\0 & \frac{36}{13} & \frac{37}{91}\\0 & - \frac{15}{13} & \frac{55}{91}\end{matrix}\right] \\
#     &= \left[\begin{matrix}-7 & -8 & - \frac{11}{7}\\0 & -3 & - \frac{1}{7}\\0 & 0 & \frac{5}{7}\end{matrix}\right], \\
#     Q = Q H &= \left[\begin{matrix}- \frac{6}{7} & - \frac{3}{7} & - \frac{2}{7}\\- \frac{3}{7} & \frac{82}{91} & - \frac{6}{91}\\- \frac{2}{7} & - \frac{6}{91} & \frac{87}{91}\end{matrix}\right]\left[\begin{matrix}1 & 0 & 0\\0 & - \frac{12}{13} & \frac{5}{13}\\0 & \frac{5}{13} & \frac{12}{13}\end{matrix}\right] \\
#     &= \left[\begin{matrix}- \frac{6}{7} & \frac{2}{7} & - \frac{3}{7}\\- \frac{3}{7} & - \frac{6}{7} & \frac{2}{7}\\- \frac{2}{7} & \frac{3}{7} & \frac{6}{7}\end{matrix}\right].
# \end{align*}
# 
# Column $j = 3$:
# \begin{align*}
#     \mathbf{u} &= \mathbf{r}_{3} + \operatorname{sign}(r_{33}) \| \mathbf{r}_{3} \| \mathbf{e} = \left[\begin{matrix}\frac{5}{7}\end{matrix}\right]^T + \frac{5}{7} \left[\begin{matrix}1\end{matrix}\right]^T = \left[\begin{matrix}\frac{10}{7}\end{matrix}\right]^T, \\
#     \mathbf{v} &= \frac{\mathbf{u}}{\| \mathbf{u} \|} = \frac{\left[\begin{matrix}\frac{10}{7}\end{matrix}\right]^T}{\frac{10}{7}}, \\
#     H &= I_1 - 2\mathbf{vv}^T = I_1 - \frac{2}{\frac{100}{49}}\left[\begin{matrix}1\end{matrix}\right]\left[\begin{matrix}1\end{matrix}\right] \\
#       &= I_1 - \frac{49}{50}\left[\begin{matrix}1\end{matrix}\right] = \left[\begin{matrix}-1\end{matrix}\right],
# \end{align*}
# 
# Adding the first 2 rows and columns of the identity matrix to $H$
# 
# \begin{align*}
#     H &= \left[\begin{matrix}1 & 0 & 0\\0 & 1 & 0\\0 & 0 & -1\end{matrix}\right].
# \end{align*}
# 
# Updating $R$ and $Q$
# \begin{align*}
#     R &= H R = \left[\begin{matrix}1 & 0 & 0\\0 & 1 & 0\\0 & 0 & -1\end{matrix}\right]\left[\begin{matrix}-7 & -8 & - \frac{11}{7}\\0 & -3 & - \frac{1}{7}\\0 & 0 & \frac{5}{7}\end{matrix}\right] = \left[\begin{matrix}-7 & -8 & - \frac{11}{7}\\0 & -3 & - \frac{1}{7}\\0 & 0 & - \frac{5}{7}\end{matrix}\right], \\
#     Q &= Q H = \left[\begin{matrix}- \frac{6}{7} & \frac{2}{7} & - \frac{3}{7}\\- \frac{3}{7} & - \frac{6}{7} & \frac{2}{7}\\- \frac{2}{7} & \frac{3}{7} & \frac{6}{7}\end{matrix}\right]\left[\begin{matrix}1 & 0 & 0\\0 & 1 & 0\\0 & 0 & -1\end{matrix}\right] = \left[\begin{matrix}- \frac{6}{7} & \frac{2}{7} & \frac{3}{7}\\- \frac{3}{7} & - \frac{6}{7} & - \frac{2}{7}\\- \frac{2}{7} & \frac{3}{7} & - \frac{6}{7}\end{matrix}\right].
# \end{align*}
# 
# Solve $R \mathbf{{x}} = Q^T \mathbf{{b}}$
# 
# \begin{align*}
#     \left[\begin{matrix}-7 & -8 & - \frac{11}{7}\\0 & -3 & - \frac{1}{7}\\0 & 0 & - \frac{5}{7}\end{matrix}\right] \mathbf{x} = \left[\begin{matrix}- \frac{6}{7} & - \frac{3}{7} & - \frac{2}{7}\\\frac{2}{7} & - \frac{6}{7} & \frac{3}{7}\\\frac{3}{7} & - \frac{2}{7} & - \frac{6}{7}\end{matrix}\right]\left[\begin{matrix}3\\0\\4\end{matrix}\right] = \left[\begin{matrix}- \frac{26}{7}\\\frac{18}{7}\\- \frac{15}{7}\end{matrix}\right],
# \end{align*}
# gives
# \begin{align*}
#     x_{3} &= \frac{1}{- \frac{5}{7}} \left(- \frac{15}{7} \right) = 3, \\
#     x_{2} &= \frac{1}{-3} \left(\frac{18}{7} - \left( - \frac{1}{7} \right) \left( 3 \right) \right) = -1, \\
#     x_{1} &= \frac{1}{-7} \left(- \frac{26}{7} - \left( -8 \right) \left( -1 \right) - \left( - \frac{11}{7} \right) \left( 3 \right) \right) = 1.
# \end{align*}
# ````
# 
# `````

# In[5]:


def qr_householder_latex(A):
    m, n = A.shape
    Q, R = eye(m), A.copy()
    for j in range(n):
        e = zeros(m - j, 1)
        e[0] = 1
        u = R[j:,j]
        signr = sign(u[0])
        u = u + sign(u[0]) * u.norm() * e
        v = u / u.norm()
        H = eye(m)
        H[j:,j:] = eye(m - j) - 2 * v * v.T

        print()
        print(rf"Column $j = {j+1}$:")
        print(r"\begin{align*}")
        if signr > 0:
            print(rf"    \mathbf{{u}} &= \mathbf{{r}}_{{{j+1}}} + \operatorname{{sign}}(r_{{{j+1}{j+1}}}) \| \mathbf{{r}}_{{{j+1}}} \| \mathbf{{e}} = {latex(R[j:,j].T)}^T + {latex(R[j:,j].norm())} {latex(e.T)}^T = {latex(u.T)}^T, \\")
        else:
            print(rf"    \mathbf{{u}} &= \mathbf{{r}}_{{{j+1}}} + \operatorname{{sign}}(r_{{{j+1}{j+1}}}) \| \mathbf{{r}}_{{{j+1}}} \| \mathbf{{e}} = {latex(R[j:,j].T)}^T - {latex(R[j:,j].norm())} {latex(e.T)}^T = {latex(u.T)}^T, \\")
        print(rf"    \mathbf{{v}} &= \frac{{\mathbf{{u}}}}{{\| \mathbf{{u}} \|}} = \frac{{{latex(u.T)}^T}}{{{latex(u.norm())}}}, \\")
        print(rf"    H &= I_{m-j} - 2\mathbf{{vv}}^T = I_{m-j} - \frac{{2}}{{{latex(u.norm()**2)}}}{latex(v)}{latex(v.T)} \\")
        print(rf"      &= I_{m-j} - {latex(2 / (u.norm()**2))}{latex(v * v.T)} = {latex(eye(m-j) - 2 * v * v.T)},")
        print(r"\end{align*}")
        if j > 0:
            print()
            print(f"Adding the first {j} rows and columns of the identity matrix to $H$")
            print()
            print(r"\begin{align*}")
            print(rf"    H &= {latex(H)}.")
            print(r"\end{align*}")
            
        print()
        print("Updating $R$ and $Q$")
        print(r"\begin{align*}")
        print(rf"    R &= H R = {latex(H)}{latex(R)} = {latex(H * R)}, \\")
        
        R = H * R
        
        print(rf"    Q &= Q H = {latex(Q)}{latex(H)} = {latex(Q * H)}.")
        Q = Q * H
        
        print(r"\end{align*}")
    
    return Q, R


(b)
A = Matrix([[6, 6, 1], [3, 6, 1], [2, 1, 1]])
b = Matrix([3, 0, 4])

Q, R = qr_householder_latex(A)

print()
print(r"Solve $R \mathbf{{x}} = Q^T \mathbf{{b}}$")
print()
print(r"\begin{align*}")
print(rf"    {latex(R)} \mathbf{{x}} = {latex(Q.T)}{latex(b)} = {latex(Q.T * b)},")
print(r"\end{align*}")
print("gives")

x = back_substitution_latex(R, Q.T * b)

