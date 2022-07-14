#!/usr/bin/env python
# coding: utf-8

# # Systems of linear equations exercises

# :::::{admonition} Exercise 2.1
# :class: note
# :name: ex2.1
# 
# Solve the following linear system of equations using the inverse of the coefficient matrix.
# 
# (a)
# \begin{align*}
#      - 4 x_{1} + 2 x_{2} &= -22, \\
#      3 x_{1} + 4 x_{2} &= 11.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
#     \det
#     \left( \begin{array}{cc}
#          -4 & 2 \\
#          3 & 4 \\
#     \end{array} \right)
#     &= -22, \\
#     \operatorname{adj}
#     \left( \begin{array}{cc}
#          -4 & 2 \\
#          3 & 4 \\
#     \end{array} \right)
#     &= 
#     \left( \begin{array}{cc}
#          4 & -2 \\
#          -3 & -4 \\
#     \end{array} \right)
# , \\
#     \therefore A^{-1} &= \frac{1}{-22}
#     \left( \begin{array}{cc}
#          4 & -2 \\
#          -3 & -4 \\
#     \end{array} \right)
# \ = 
#     \left( \begin{array}{cc}
#          - \frac{2}{11} & \frac{1}{11} \\
#          \frac{3}{22} & \frac{2}{11} \\
#     \end{array} \right)
# ,\end{align*}
# 
# therefore
# \begin{align*}
#     \mathbf{{x}} = 
#     \left( \begin{array}{cc}
#          - \frac{2}{11} & \frac{1}{11} \\
#          \frac{3}{22} & \frac{2}{11} \\
#     \end{array} \right)
#     \left( \begin{array}{cc}
#          -22 \\
#          11 \\
#     \end{array} \right)
#     =
#     \left( \begin{array}{cc}
#          5 \\
#          -1 \\
#     \end{array} \right)
# \end{align*}
# ::::
# 
# (b)
# \begin{align*}
#      - 4 x_{1} + 2 x_{2} &= 6, \\
#      - x_{1} - 3 x_{2} &= -2.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
#     \det
#     \left( \begin{array}{cc}
#          -4 & 2 \\
#          -1 & -3 \\
#     \end{array} \right)
#     &= 14, \\
#     \operatorname{adj}
#     \left( \begin{array}{cc}
#          -4 & 2 \\
#          -1 & -3 \\
#     \end{array} \right)
#     &= 
#     \left( \begin{array}{cc}
#          -3 & -2 \\
#          1 & -4 \\
#     \end{array} \right)
# , \\
#     \therefore A^{-1} &= \frac{1}{14}
#     \left( \begin{array}{cc}
#          -3 & -2 \\
#          1 & -4 \\
#     \end{array} \right)
# \ = 
#     \left( \begin{array}{cc}
#          - \frac{3}{14} & - \frac{1}{7} \\
#          \frac{1}{14} & - \frac{2}{7} \\
#     \end{array} \right)
# ,\end{align*}
# 
# therefore
# \begin{align*}
#     \mathbf{{x}} = 
#     \left( \begin{array}{cc}
#          - \frac{3}{14} & - \frac{1}{7} \\
#          \frac{1}{14} & - \frac{2}{7} \\
#     \end{array} \right)
#     \left( \begin{array}{cc}
#          6 \\
#          -2 \\
#     \end{array} \right)
#     =
#     \left( \begin{array}{cc}
#          -1 \\
#          1 \\
#     \end{array} \right)
# \end{align*}
# ::::
# 
# (c)
# \begin{align*}
#      - 4 x_{1} - 4 x_{2} - 2 x_{3} &= 16, \\
#      3 x_{1} + 4 x_{3} &= -8, \\
#      x_{1} &= 0.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
#     \det
#     \left( \begin{array}{ccc}
#          -4 & -4 & -2 \\
#          3 & 0 & 4 \\
#          1 & 0 & 0 \\
#     \end{array} \right)
#     &= -16, \\
#     \operatorname{adj}
#     \left( \begin{array}{ccc}
#          -4 & -4 & -2 \\
#          3 & 0 & 4 \\
#          1 & 0 & 0 \\
#     \end{array} \right)
#     &= 
#     \left( \begin{array}{ccc}
#          0 & 0 & -16 \\
#          4 & 2 & 10 \\
#          0 & -4 & 12 \\
#     \end{array} \right)
# , \\
#     \therefore A^{-1} &= \frac{1}{-16}
#     \left( \begin{array}{ccc}
#          0 & 0 & -16 \\
#          4 & 2 & 10 \\
#          0 & -4 & 12 \\
#     \end{array} \right)
# \ = 
#     \left( \begin{array}{ccc}
#          0 & 0 & 1 \\
#          - \frac{1}{4} & - \frac{1}{8} & - \frac{5}{8} \\
#          0 & \frac{1}{4} & - \frac{3}{4} \\
#     \end{array} \right)
# ,\end{align*}
# 
# therefore
# \begin{align*}
#     \mathbf{{x}} = 
#     \left( \begin{array}{ccc}
#          0 & 0 & 1 \\
#          - \frac{1}{4} & - \frac{1}{8} & - \frac{5}{8} \\
#          0 & \frac{1}{4} & - \frac{3}{4} \\
#     \end{array} \right)
#     \left( \begin{array}{ccc}
#          16 \\
#          -8 \\
#          0 \\
#     \end{array} \right)
#     =
#     \left( \begin{array}{ccc}
#          0 \\
#          -3 \\
#          -2 \\
#     \end{array} \right)
# \end{align*}
# ::::
# 
# (d)
# \begin{align*}
#      4 x_{1} - 4 x_{3} &= 8, \\
#      4 x_{1} -  x_{2} +  x_{3} &= -4, \\
#      3 x_{1} +  x_{2} + 2 x_{3} &= -12.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
#     \det
#     \left( \begin{array}{ccc}
#          4 & 0 & -4 \\
#          4 & -1 & 1 \\
#          3 & 1 & 2 \\
#     \end{array} \right)
#     &= -40, \\
#     \operatorname{adj}
#     \left( \begin{array}{ccc}
#          4 & 0 & -4 \\
#          4 & -1 & 1 \\
#          3 & 1 & 2 \\
#     \end{array} \right)
#     &= 
#     \left( \begin{array}{ccc}
#          -3 & -4 & -4 \\
#          -5 & 20 & -20 \\
#          7 & -4 & -4 \\
#     \end{array} \right)
# , \\
#     \therefore A^{-1} &= \frac{1}{-40}
#     \left( \begin{array}{ccc}
#          -3 & -4 & -4 \\
#          -5 & 20 & -20 \\
#          7 & -4 & -4 \\
#     \end{array} \right)
# \ = 
#     \left( \begin{array}{ccc}
#          \frac{3}{40} & \frac{1}{10} & \frac{1}{10} \\
#          \frac{1}{8} & - \frac{1}{2} & \frac{1}{2} \\
#          - \frac{7}{40} & \frac{1}{10} & \frac{1}{10} \\
#     \end{array} \right)
# ,\end{align*}
# 
# therefore
# \begin{align*}
#     \mathbf{{x}} = 
#     \left( \begin{array}{ccc}
#          \frac{3}{40} & \frac{1}{10} & \frac{1}{10} \\
#          \frac{1}{8} & - \frac{1}{2} & \frac{1}{2} \\
#          - \frac{7}{40} & \frac{1}{10} & \frac{1}{10} \\
#     \end{array} \right)
#     \left( \begin{array}{ccc}
#          8 \\
#          -4 \\
#          -12 \\
#     \end{array} \right)
#     =
#     \left( \begin{array}{ccc}
#          -1 \\
#          -3 \\
#          -3 \\
#     \end{array} \right)
# \end{align*}
# ::::
# :::::

# In[1]:


from sympy import *
 
def print_matrix(A):
    m, n = A.shape
    cols = "c" * m
    print(rf"    \left( \begin{{array}}{{{cols}}}")
    for i in range(m):
        print("        ", end="")
        for j in range(n - 1):
            print(rf" {latex(A[i,j])} &", end="")
        print(rf" {latex(A[i,-1])} \\")
    print(r"    \end{array} \right)")
    
    
def print_system(A, b):
    m, n = A.shape
    print(r"\begin{align*}")
    for i in range(m):
        string = "    "
        j = 0
        if A[i,j] == 1:
            string += rf" x_{{{j + 1}}}"
        elif A[i,j] == -1:
            string += rf" - x_{{{j + 1}}}"
        elif A[i,j] > 0:
            string += rf" {latex(A[i,j])} x_{{{j + 1}}}"
        elif A[i,j] < 0:
            string += rf" - {latex(-A[i,j])} x_{{{j + 1}}}"
            
        for j in range(1, n):
            if A[i,j] == 0:
                continue
            elif A[i,j] == 1:
                string += rf" +  x_{{{j + 1}}}"
            elif A[i,j] == -1:
                string += rf" -  x_{{{j + 1}}}"
            elif A[i,j] > 0:
                string += rf" + {latex(A[i,j])} x_{{{j + 1}}}"
            elif A[i,j] < 0:
                string += rf" - {latex(-A[i,j])} x_{{{j + 1}}}"
                
        string += rf" &= {latex(b[i])}"
        if i < m - 1:
            string += r", \\"
        else:
            string += "."
        print(string)
    print(r"\end{align*}")
    print()
    

def matrix_inverse_solve(A, b):
    print("::::{dropdown} Solution")
    print(r"\begin{align*}")
    print(r"    \det")
    print_matrix(A)
    print(rf"    &= {latex(A.det())}, \\")
    print(r"    \operatorname{adj}")
    print_matrix(A)
    print(rf"    &= ")
    print_matrix(A.adjugate())
    print(r", \\")
    print(rf"    \therefore A^{{-1}} &= \frac{{1}}{{{latex(A.det())}}}")
    print_matrix(A.adjugate())
    print("\\ = ")
    print_matrix(A.inv())
    print(r",\end{align*}")
    print("\ntherefore")
    print(r"\begin{align*}")
    print(r"    \mathbf{{x}} = ")
    print_matrix(A.inv())
    print_matrix(b)
    print("    =")
    print_matrix(A.inv() * b)
    print(r"\end{align*}")
    print("::::")
 

print(":::::{admonition} Exercise 2.1")
print(":class: note")
print(":name: ex2.1")
print()
print("Solve the following linear system of equations using the inverse of the coefficient matrix.")     

print("\n(a)")
A = Matrix([[-4, 2], [3, 4]])
b = Matrix([[-22], [11]])
print_system(A, b)
matrix_inverse_solve(A, b)

print("\n(b)")
A = Matrix([[-4, 2], [-1, -3]])
b = Matrix([[6], [-2]])
print_system(A, b)
matrix_inverse_solve(A, b)

print("\n(c)")
A = Matrix([[-4, -4, -2], [3, 0, 4], [1, 0, 0]])
b = Matrix([[16], [-8], [0]])
print_system(A, b)
matrix_inverse_solve(A, b)

print("\n(d)")
A = Matrix([[4, 0, -4], [4, -1, 1], [3, 1, 2]])
b = Matrix([[8], [-4], [-12]])
print_system(A, b)
matrix_inverse_solve(A, b)

print(":::::")


# :::::{admonition} Exercise 2.2
# :class: note
# :name: ex2.2
# 
# Solve the following linear system of equations using Cramer's rule.
# 
# (a)
# \begin{align*}
#      x_{1} + 4 x_{2} &= -20, \\
#      - 4 x_{1} +  x_{2} &= -5.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
#     x_{1} &= \frac{\det \left(\begin{matrix}-20 & 4\\-5 & 1\end{matrix}\right)}{\det \left(\begin{matrix}1 & 4\\-4 & 1\end{matrix}\right)} = \frac{0}{17} = 0, \\ \\
#     x_{2} &= \frac{\det \left(\begin{matrix}1 & -20\\-4 & -5\end{matrix}\right)}{\det \left(\begin{matrix}1 & 4\\-4 & 1\end{matrix}\right)} = \frac{-85}{17} = -5, \\ \\
# \end{align*}
# ::::
# 
# (b)
# \begin{align*}
#      x_{1} +  x_{2} &= 4, \\
#      + 4 x_{2} &= 12.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
#     x_{1} &= \frac{\det \left(\begin{matrix}4 & 1\\12 & 4\end{matrix}\right)}{\det \left(\begin{matrix}1 & 1\\0 & 4\end{matrix}\right)} = \frac{4}{4} = 1, \\ \\
#     x_{2} &= \frac{\det \left(\begin{matrix}1 & 4\\0 & 12\end{matrix}\right)}{\det \left(\begin{matrix}1 & 1\\0 & 4\end{matrix}\right)} = \frac{12}{4} = 3, \\ \\
# \end{align*}
# ::::
# 
# (c)
# \begin{align*}
#      3 x_{1} - 4 x_{2} - 4 x_{3} &= 21, \\
#      - 2 x_{1} -  x_{2} -  x_{3} &= 8, \\
#      4 x_{1} -  x_{2} + 3 x_{3} &= -14.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
#     x_{1} &= \frac{\det \left(\begin{matrix}21 & -4 & -4\\8 & -1 & -1\\-14 & -1 & 3\end{matrix}\right)}{\det \left(\begin{matrix}3 & -4 & -4\\-2 & -1 & -1\\4 & -1 & 3\end{matrix}\right)} = \frac{44}{-44} = -1, \\ \\
#     x_{2} &= \frac{\det \left(\begin{matrix}3 & 21 & -4\\-2 & 8 & -1\\4 & -14 & 3\end{matrix}\right)}{\det \left(\begin{matrix}3 & -4 & -4\\-2 & -1 & -1\\4 & -1 & 3\end{matrix}\right)} = \frac{88}{-44} = -2, \\ \\
#     x_{3} &= \frac{\det \left(\begin{matrix}3 & -4 & 21\\-2 & -1 & 8\\4 & -1 & -14\end{matrix}\right)}{\det \left(\begin{matrix}3 & -4 & -4\\-2 & -1 & -1\\4 & -1 & 3\end{matrix}\right)} = \frac{176}{-44} = -4, \\ \\
# \end{align*}
# ::::
# 
# (d)
# \begin{align*}
#      4 x_{1} + 4 x_{2} +  x_{3} &= 5, \\
#      - 2 x_{1} +  x_{2} +  x_{3} &= -1, \\
#      - 5 x_{1} - 4 x_{2} + 2 x_{3} &= -14.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
#     x_{1} &= \frac{\det \left(\begin{matrix}5 & 4 & 1\\-1 & 1 & 1\\-14 & -4 & 2\end{matrix}\right)}{\det \left(\begin{matrix}4 & 4 & 1\\-2 & 1 & 1\\-5 & -4 & 2\end{matrix}\right)} = \frac{0}{33} = 0, \\ \\
#     x_{2} &= \frac{\det \left(\begin{matrix}4 & 5 & 1\\-2 & -1 & 1\\-5 & -14 & 2\end{matrix}\right)}{\det \left(\begin{matrix}4 & 4 & 1\\-2 & 1 & 1\\-5 & -4 & 2\end{matrix}\right)} = \frac{66}{33} = 2, \\ \\
#     x_{3} &= \frac{\det \left(\begin{matrix}4 & 4 & 5\\-2 & 1 & -1\\-5 & -4 & -14\end{matrix}\right)}{\det \left(\begin{matrix}4 & 4 & 1\\-2 & 1 & 1\\-5 & -4 & 2\end{matrix}\right)} = \frac{-99}{33} = -3, \\ \\
# \end{align*}
# ::::
# :::::

# In[2]:


def cramers_rule(A, b):
    print(r"::::{dropdown} Solution")
    print(r"\begin{align*}")
    for i in range(len(b)):
        Ai = A.copy()
        Ai[:,i] = b
        print(rf"    x_{{{i+1}}} &= \frac{{\det {latex(Ai, mat_delim='(')}}}{{\det {latex(A, mat_delim='(')}}}", end="")
        print(rf" = \frac{{{latex(Ai.det())}}}{{{latex(A.det())}}} = {latex(Ai.det() / A.det())}, \\ \\")

    print(r"\end{align*}")
    print(r"::::")


print(":::::{admonition} Exercise 2.2")
print(":class: note")
print(":name: ex2.2")
print()
print("Solve the following linear system of equations using Cramer's rule.")     

print("\n(a)")
A = Matrix([[1, 4], [-4, 1]])
b = Matrix([[-20], [-5]])
print_system(A, b)
cramers_rule(A, b)

print("\n(b)")
A = Matrix([[1, 1], [0, 4]])
b = Matrix([[4], [12]])
print_system(A, b)
cramers_rule(A, b)

print("\n(c)")
A = Matrix([[3, -4, -4], [-2, -1, -1], [4, -1, 3]])
b = Matrix([[21], [8], [-14]])
print_system(A, b)
cramers_rule(A, b)

print("\n(d)")
A = Matrix([[4, 4, 1], [-2, 1, 1], [-5, -4, 2]])
b = Matrix([[5], [-1], [-14]])
print_system(A, b)
cramers_rule(A, b)

print(":::::")


# :::::{admonition} Exercise 2.3
# :class: note
# :name: ex2.3
# 
# Solve the following linear system of equations using Gaussian elimination.
# 
# (a)
# \begin{align*}
#      - x_{1} + 3 x_{2} &= -2, \\
#      - 2 x_{1} +  x_{2} &= 1.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{cc|c}
#          -1 & 3 & -2 \\
#          -2 & 1 & 1 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - 2 R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|c}
#          -1 & 3 & -2 \\
#          0 & -5 & 5 \\
#     \end{array} \right)
# \end{align*}
# 
# therefore 
# \begin{align*}
#     x_{2} &= \frac{1}{-5} \left( 5\right) = -1, \\
#     x_{1} &= \frac{1}{-1} \left( -2 - 3 \left( -1 \right)\right) = -1.
# \end{align*}
# ::::
# 
# (b)
# \begin{align*}
#      3 x_{1} +  x_{2} + 2 x_{3} &= 11, \\
#      4 x_{1} - 4 x_{3} &= -4, \\
#      4 x_{1} - 2 x_{2} +  x_{3} &= 13.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{ccc|c}
#          3 & 1 & 2 & 11 \\
#          4 & 0 & -4 & -4 \\
#          4 & -2 & 1 & 13 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - \frac{4}{3} R_{1} \\ R_{3} - \frac{4}{3} R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#          3 & 1 & 2 & 11 \\
#          0 & - \frac{4}{3} & - \frac{20}{3} & - \frac{56}{3} \\
#          0 & - \frac{10}{3} & - \frac{5}{3} & - \frac{5}{3} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} - \frac{5}{2} R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#          3 & 1 & 2 & 11 \\
#          0 & - \frac{4}{3} & - \frac{20}{3} & - \frac{56}{3} \\
#          0 & 0 & 15 & 45 \\
#     \end{array} \right)
# \end{align*}
# 
# therefore 
# \begin{align*}
#     x_{3} &= \frac{1}{15} \left( 45\right) = 3, \\
#     x_{2} &= \frac{1}{- \frac{4}{3}} \left( - \frac{56}{3} - \left( - \frac{20}{3} \right) \left( 3 \right)\right) = -1, \\
#     x_{1} &= \frac{1}{3} \left( 11 - 1 \left( -1 \right) - 2 \left( 3 \right)\right) = 2.
# \end{align*}
# ::::
# 
# (c)
# \begin{align*}
#      - x_{1} - 5 x_{2} - 2 x_{3} &= -17, \\
#      2 x_{1} - 2 x_{2} - 3 x_{3} &= -14, \\
#      3 x_{1} -  x_{2} + 4 x_{3} &= -13.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{ccc|c}
#          -1 & -5 & -2 & -17 \\
#          2 & -2 & -3 & -14 \\
#          3 & -1 & 4 & -13 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} + 2 R_{1} \\ R_{3} + 3 R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#          -1 & -5 & -2 & -17 \\
#          0 & -12 & -7 & -48 \\
#          0 & -16 & -2 & -64 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} - \frac{4}{3} R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#          -1 & -5 & -2 & -17 \\
#          0 & -12 & -7 & -48 \\
#          0 & 0 & \frac{22}{3} & 0 \\
#     \end{array} \right)
# \end{align*}
# 
# therefore 
# \begin{align*}
#     x_{3} &= \frac{1}{\frac{22}{3}} \left( 0\right) = 0, \\
#     x_{2} &= \frac{1}{-12} \left( -48 - \left( -7 \right) \left( 0 \right)\right) = 4, \\
#     x_{1} &= \frac{1}{-1} \left( -17 - \left( -5 \right) \left( 4 \right) - \left( -2 \right) \left( 0 \right)\right) = -3.
# \end{align*}
# ::::
# 
# (d)
# \begin{align*}
#      - x_{1} - 5 x_{2} - 2 x_{3} &= -26, \\
#      2 x_{1} - 2 x_{2} - 3 x_{3} &= -19, \\
#      3 x_{1} -  x_{2} - 4 x_{3} &= -20.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{ccc|c}
#          -1 & -5 & -2 & -26 \\
#          2 & -2 & -3 & -19 \\
#          3 & -1 & -4 & -20 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} + 2 R_{1} \\ R_{3} + 3 R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#          -1 & -5 & -2 & -26 \\
#          0 & -12 & -7 & -71 \\
#          0 & -16 & -10 & -98 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} - \frac{4}{3} R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#          -1 & -5 & -2 & -26 \\
#          0 & -12 & -7 & -71 \\
#          0 & 0 & - \frac{2}{3} & - \frac{10}{3} \\
#     \end{array} \right)
# \end{align*}
# 
# therefore 
# \begin{align*}
#     x_{3} &= \frac{1}{- \frac{2}{3}} \left( - \frac{10}{3}\right) = 5, \\
#     x_{2} &= \frac{1}{-12} \left( -71 - \left( -7 \right) \left( 5 \right)\right) = 3, \\
#     x_{1} &= \frac{1}{-1} \left( -26 - \left( -5 \right) \left( 3 \right) - \left( -2 \right) \left( 5 \right)\right) = 1.
# \end{align*}
# ::::
# 
# (e)
# \begin{align*}
#      3 x_{1} - 5 x_{2} - 4 x_{3} -  x_{4} &= 28, \\
#      - 4 x_{2} + 3 x_{3} - 4 x_{4} &= 41, \\
#      2 x_{1} + 3 x_{2} + 3 x_{3} - 3 x_{4} &= 11, \\
#      - 2 x_{1} + 2 x_{2} - 5 x_{3} - 4 x_{4} &= -21.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{cccc|c}
#          3 & -5 & -4 & -1 & 28 \\
#          0 & -4 & 3 & -4 & 41 \\
#          2 & 3 & 3 & -3 & 11 \\
#          -2 & 2 & -5 & -4 & -21 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} - \frac{2}{3} R_{1} \\ R_{4} + \frac{2}{3} R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|c}
#          3 & -5 & -4 & -1 & 28 \\
#          0 & -4 & 3 & -4 & 41 \\
#          0 & \frac{19}{3} & \frac{17}{3} & - \frac{7}{3} & - \frac{23}{3} \\
#          0 & - \frac{4}{3} & - \frac{23}{3} & - \frac{14}{3} & - \frac{7}{3} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} + \frac{19}{12} R_{2} \\ R_{4} - \frac{1}{3} R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|c}
#          3 & -5 & -4 & -1 & 28 \\
#          0 & -4 & 3 & -4 & 41 \\
#          0 & 0 & \frac{125}{12} & - \frac{26}{3} & \frac{229}{4} \\
#          0 & 0 & - \frac{26}{3} & - \frac{10}{3} & -16 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ \phantom{x} \\ R_{4} + \frac{104}{125} R_{3} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|c}
#          3 & -5 & -4 & -1 & 28 \\
#          0 & -4 & 3 & -4 & 41 \\
#          0 & 0 & \frac{125}{12} & - \frac{26}{3} & \frac{229}{4} \\
#          0 & 0 & 0 & - \frac{1318}{125} & \frac{3954}{125} \\
#     \end{array} \right)
# \end{align*}
# 
# therefore 
# \begin{align*}
#     x_{4} &= \frac{1}{- \frac{1318}{125}} \left( \frac{3954}{125}\right) = -3, \\
#     x_{3} &= \frac{1}{\frac{125}{12}} \left( \frac{229}{4} - \left( - \frac{26}{3} \right) \left( -3 \right)\right) = 3, \\
#     x_{2} &= \frac{1}{-4} \left( 41 - 3 \left( 3 \right) - \left( -4 \right) \left( -3 \right)\right) = -5, \\
#     x_{1} &= \frac{1}{3} \left( 28 - \left( -5 \right) \left( -5 \right) - \left( -4 \right) \left( 3 \right) - \left( -1 \right) \left( -3 \right)\right) = 4.
# \end{align*}
# ::::
# 
# (f)
# \begin{align*}
#      2 x_{1} - 3 x_{2} - 3 x_{3} + 4 x_{4} &= -1, \\
#      4 x_{1} - 5 x_{2} +  x_{3} - 5 x_{4} &= 42, \\
#      3 x_{1} + 3 x_{2} -  x_{3} - 5 x_{4} &= 20, \\
#      x_{1} +  x_{3} + 3 x_{4} &= -4.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{cccc|c}
#          2 & -3 & -3 & 4 & -1 \\
#          4 & -5 & 1 & -5 & 42 \\
#          3 & 3 & -1 & -5 & 20 \\
#          1 & 0 & 1 & 3 & -4 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - 2 R_{1} \\ R_{3} - \frac{3}{2} R_{1} \\ R_{4} - \frac{1}{2} R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|c}
#          2 & -3 & -3 & 4 & -1 \\
#          0 & 1 & 7 & -13 & 44 \\
#          0 & \frac{15}{2} & \frac{7}{2} & -11 & \frac{43}{2} \\
#          0 & \frac{3}{2} & \frac{5}{2} & 1 & - \frac{7}{2} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} - \frac{15}{2} R_{2} \\ R_{4} - \frac{3}{2} R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|c}
#          2 & -3 & -3 & 4 & -1 \\
#          0 & 1 & 7 & -13 & 44 \\
#          0 & 0 & -49 & \frac{173}{2} & - \frac{617}{2} \\
#          0 & 0 & -8 & \frac{41}{2} & - \frac{139}{2} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ \phantom{x} \\ R_{4} - \frac{8}{49} R_{3} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|c}
#          2 & -3 & -3 & 4 & -1 \\
#          0 & 1 & 7 & -13 & 44 \\
#          0 & 0 & -49 & \frac{173}{2} & - \frac{617}{2} \\
#          0 & 0 & 0 & \frac{625}{98} & - \frac{1875}{98} \\
#     \end{array} \right)
# \end{align*}
# 
# therefore 
# \begin{align*}
#     x_{4} &= \frac{1}{\frac{625}{98}} \left( - \frac{1875}{98}\right) = -3, \\
#     x_{3} &= \frac{1}{-49} \left( - \frac{617}{2} - \frac{173}{2} \left( -3 \right)\right) = 1, \\
#     x_{2} &= \frac{1}{1} \left( 44 - 7 \left( 1 \right) - \left( -13 \right) \left( -3 \right)\right) = -2, \\
#     x_{1} &= \frac{1}{2} \left( -1 - \left( -3 \right) \left( -2 \right) - \left( -3 \right) \left( 1 \right) - 4 \left( -3 \right)\right) = 4.
# \end{align*}
# ::::
# :::::
# 

# In[3]:


def print_augmented_matrix(A):
    m, n = A.shape
    cols = "c" * (n - 1)
    cols += "|c"
    print(rf"    \left( \begin{{array}}{{{cols}}}")
    for i in range(m):
        print("        ", end="")
        for j in range(n - 1):
            print(rf" {latex(A[i,j])} &", end="")
        print(rf" {latex(A[i,-1])} \\")
    print(r"    \end{array} \right)")
    
        
def gelim(A):
    m, n = A.shape
    
    print(r"::::{dropdown} Solution")
    print(r"\begin{align*}")
    print(r"&", end="")
    print_augmented_matrix(A)
    
    for i in range(m - 1):
        for j in range(i, n):
            if A[i,j] != 0:
                pivotcol = j
                break         
         
        string = r"    \begin{matrix} \phantom{x} \\"
        for j in range(i):
            string += r" \phantom{x} \\"
            
        for j in range(i + 1, m):
            if A[j,pivotcol] / A[i,pivotcol] > 0:
                if A[j,pivotcol] / A[i,pivotcol] == 1:
                    string += rf" R_{{{j+1}}} - R_{{{i + 1}}}"
                else:
                    string += rf" R_{{{j+1}}} - {latex(A[j,pivotcol] / A[i,pivotcol])} R_{{{i + 1}}}"    
            elif A[j,pivotcol] / A[i,pivotcol] < 0:
                if A[j,pivotcol] / A[i,pivotcol] == -1:
                    string += rf" R_{{{j+1}}} + R_{{{i + 1}}}"
                else:
                    string += rf" R_{{{j+1}}} + {latex(-A[j,pivotcol] / A[i,pivotcol])} R_{{{i + 1}}}"
            elif A[j,pivotcol] / A[i,pivotcol] == 0:
                string += r" \phantom{x}"
            A[j,:] -= A[j,pivotcol] / A[i,pivotcol] * A[i,:]
            
            if j < m - 1:
                string += r" \\"
        string += r" \end{matrix} \\[1em]"
        print(string)
        print(r"    \longrightarrow \quad &")
        print_augmented_matrix(A)
    print(r"\end{align*}")
                
    return A


def back_substitution(A):
    m, n = A.shape
    x = A[:,-1]
    print(r"\begin{align*}")
    for i in range(m - 1, -1, -1):
        string = rf"    x_{{{i+1}}} &= \frac{{1}}{{{latex(A[i,i])}}} \left( {latex(A[i,-1])}"
            
        for j in range(i + 1, n - 1):
            if A[i,j] >= 0:
                string += rf" - {latex(A[i,j])} \left( {latex(x[j])} \right)"
            else:
                string += rf" - \left( {latex(A[i,j])} \right) \left( {latex(x[j])} \right)"
            x[i] -= A[i,j] * x[j]
        
        x[i] /= A[i,i]
        
        string += rf"\right) = {latex(x[i])}"
            
        if i > 0:
            string += r", \\"
        else:
            string += "."
        print(string)
    print(r"\end{align*}")
    
    
print(":::::{admonition} Exercise 2.3")
print(":class: note")
print(":name: ex2.3")
print()
print("Solve the following linear system of equations using Gaussian elimination.")    
print("\n(a)")
A = Matrix([[-1, 3], [-2, 1]])
b = Matrix([[-2], [1]])

print_system(A, b)
Ab = A.row_join(b)
Ab = gelim(Ab)
print()
print(rf"therefore ")
back_substitution(A)
print(r"::::")
    
print("\n(b)")
A = Matrix([[3, 1, 2], [4, 0, -4], [4, -2, 1]])
b = Matrix([[11], [-4], [13]])
print_system(A, b)
Ab = A.row_join(b)
Ab = gelim(Ab)
print()
print(rf"therefore ")
back_substitution(A)
print(r"::::")

print("\n(c)")
A = Matrix([[-1, -5, -2], [2, -2, -3], [3, -1, 4]])
b = Matrix([[-17], [-14], [-13]])
print_system(A, b)
Ab = A.row_join(b)
Ab = gelim(Ab)

print()
print(rf"therefore ")
back_substitution(A)
print(r"::::")

print("\n(d)")
A = Matrix([[-1, -5, -2], [2, -2, -3],  [3, -1, -4]])
b = Matrix([[-26], [-19], [-20]])
print_system(A, b)
Ab = A.row_join(b)
Ab = gelim(Ab)
print()
print(rf"therefore ")
back_substitution(A)
print(r"::::")

print("\n(e)")
A = Matrix([[3, -5, -4, -1], [0, -4, 3, -4], [2, 3, 3, -3], [-2, 2, -5, -4]])
b = Matrix([[28], [41], [11], [-21]])
print_system(A, b)
Ab = A.row_join(b)
Ab = gelim(Ab)

print()
print(rf"therefore ")
back_substitution(A)
print(r"::::")

print("\n(f)")
A = Matrix([[2, -3, -3, 4], [4, -5, 1, -5], [3, 3, -1, -5], [1, 0, 1, 3]])
b = Matrix([[-1], [42], [20], [-4]])
print_system(A, b)
Ab = A.row_join(b)
Ab = gelim(Ab)

print()
print(rf"therefore ")
back_substitution(A)
print(r"::::")

print(":::::")


# :::::{admonition} Exercise 2.4
# :class: note
# :name: ex2.4
# 
# Solve the linear system of equations from [exercise 2.3](ex2.3) using Gaussian elimination with partial pivoting.
# 
# (a)
# \begin{align*}
#      - x_{1} + 3 x_{2} &= -2, \\
#      - 2 x_{1} +  x_{2} &= 1.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{cc|cc}
#          -1 & 3 & -2 \\
#          -2 & 1 & 1 \\
#     \end{array} \right)
#     \begin{matrix} R_{1} \leftrightarrow R_{2} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|cc}
#          -2 & 1 & 1 \\
#          -1 & 3 & -2 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - \frac{1}{2} R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|cc}
#          -2 & 1 & 1 \\
#          0 & \frac{5}{2} & - \frac{5}{2} \\
#     \end{array} \right)
# \end{align*}
# 
# therefore 
# \begin{align*}
#     x_{2} &= \frac{1}{\frac{5}{2}} \left( - \frac{5}{2}\right) = -1, \\
#     x_{1} &= \frac{1}{-2} \left( 1 - 1 \left( -1 \right)\right) = -1.
# \end{align*}
# ::::
# 
# (b)
# \begin{align*}
#      3 x_{1} +  x_{2} + 2 x_{3} &= 11, \\
#      4 x_{1} - 4 x_{3} &= -4, \\
#      4 x_{1} - 2 x_{2} +  x_{3} &= 13.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{ccc|ccc}
#          3 & 1 & 2 & 11 \\
#          4 & 0 & -4 & -4 \\
#          4 & -2 & 1 & 13 \\
#     \end{array} \right)
#     \begin{matrix} R_{1} \leftrightarrow R_{2} \\ \phantom{x} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          4 & 0 & -4 & -4 \\
#          3 & 1 & 2 & 11 \\
#          4 & -2 & 1 & 13 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - \frac{3}{4} R_{1} \\ R_{3} - R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          4 & 0 & -4 & -4 \\
#          0 & 1 & 5 & 14 \\
#          0 & -2 & 5 & 17 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} \leftrightarrow R_{3} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          4 & 0 & -4 & -4 \\
#          0 & -2 & 5 & 17 \\
#          0 & 1 & 5 & 14 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} + \frac{1}{2} R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          4 & 0 & -4 & -4 \\
#          0 & -2 & 5 & 17 \\
#          0 & 0 & \frac{15}{2} & \frac{45}{2} \\
#     \end{array} \right)
# \end{align*}
# 
# therefore 
# \begin{align*}
#     x_{3} &= \frac{1}{\frac{15}{2}} \left( \frac{45}{2}\right) = 3, \\
#     x_{2} &= \frac{1}{-2} \left( 17 - 5 \left( 3 \right)\right) = -1, \\
#     x_{1} &= \frac{1}{4} \left( -4 - 0 \left( -1 \right) - \left( -4 \right) \left( 3 \right)\right) = 2.
# \end{align*}
# ::::
# 
# (c)
# \begin{align*}
#      - x_{1} - 5 x_{2} - 2 x_{3} &= -17, \\
#      2 x_{1} - 2 x_{2} - 3 x_{3} &= -14, \\
#      3 x_{1} -  x_{2} + 4 x_{3} &= -13.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{ccc|ccc}
#          -1 & -5 & -2 & -17 \\
#          2 & -2 & -3 & -14 \\
#          3 & -1 & 4 & -13 \\
#     \end{array} \right)
#     \begin{matrix} R_{1} \leftrightarrow R_{3} \\ \phantom{x} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          3 & -1 & 4 & -13 \\
#          2 & -2 & -3 & -14 \\
#          -1 & -5 & -2 & -17 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - \frac{2}{3} R_{1} \\ R_{3} + \frac{1}{3} R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          3 & -1 & 4 & -13 \\
#          0 & - \frac{4}{3} & - \frac{17}{3} & - \frac{16}{3} \\
#          0 & - \frac{16}{3} & - \frac{2}{3} & - \frac{64}{3} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} \leftrightarrow R_{3} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          3 & -1 & 4 & -13 \\
#          0 & - \frac{16}{3} & - \frac{2}{3} & - \frac{64}{3} \\
#          0 & - \frac{4}{3} & - \frac{17}{3} & - \frac{16}{3} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} - \frac{1}{4} R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          3 & -1 & 4 & -13 \\
#          0 & - \frac{16}{3} & - \frac{2}{3} & - \frac{64}{3} \\
#          0 & 0 & - \frac{11}{2} & 0 \\
#     \end{array} \right)
# \end{align*}
# 
# therefore 
# \begin{align*}
#     x_{3} &= \frac{1}{- \frac{11}{2}} \left( 0\right) = 0, \\
#     x_{2} &= \frac{1}{- \frac{16}{3}} \left( - \frac{64}{3} - \left( - \frac{2}{3} \right) \left( 0 \right)\right) = 4, \\
#     x_{1} &= \frac{1}{3} \left( -13 - \left( -1 \right) \left( 4 \right) - 4 \left( 0 \right)\right) = -3.
# \end{align*}
# ::::
# 
# (d)
# \begin{align*}
#      - x_{1} - 5 x_{2} - 2 x_{3} &= -26, \\
#      2 x_{1} - 2 x_{2} - 3 x_{3} &= -19, \\
#      3 x_{1} -  x_{2} - 4 x_{3} &= -20.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{ccc|ccc}
#          -1 & -5 & -2 & -26 \\
#          2 & -2 & -3 & -19 \\
#          3 & -1 & -4 & -20 \\
#     \end{array} \right)
#     \begin{matrix} R_{1} \leftrightarrow R_{3} \\ \phantom{x} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          3 & -1 & -4 & -20 \\
#          2 & -2 & -3 & -19 \\
#          -1 & -5 & -2 & -26 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - \frac{2}{3} R_{1} \\ R_{3} + \frac{1}{3} R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          3 & -1 & -4 & -20 \\
#          0 & - \frac{4}{3} & - \frac{1}{3} & - \frac{17}{3} \\
#          0 & - \frac{16}{3} & - \frac{10}{3} & - \frac{98}{3} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} \leftrightarrow R_{3} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          3 & -1 & -4 & -20 \\
#          0 & - \frac{16}{3} & - \frac{10}{3} & - \frac{98}{3} \\
#          0 & - \frac{4}{3} & - \frac{1}{3} & - \frac{17}{3} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} - \frac{1}{4} R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          3 & -1 & -4 & -20 \\
#          0 & - \frac{16}{3} & - \frac{10}{3} & - \frac{98}{3} \\
#          0 & 0 & \frac{1}{2} & \frac{5}{2} \\
#     \end{array} \right)
# \end{align*}
# 
# therefore 
# \begin{align*}
#     x_{3} &= \frac{1}{\frac{1}{2}} \left( \frac{5}{2}\right) = 5, \\
#     x_{2} &= \frac{1}{- \frac{16}{3}} \left( - \frac{98}{3} - \left( - \frac{10}{3} \right) \left( 5 \right)\right) = 3, \\
#     x_{1} &= \frac{1}{3} \left( -20 - \left( -1 \right) \left( 3 \right) - \left( -4 \right) \left( 5 \right)\right) = 1.
# \end{align*}
# ::::
# 
# (e)
# \begin{align*}
#      3 x_{1} - 5 x_{2} - 4 x_{3} -  x_{4} &= 28, \\
#      - 4 x_{2} + 3 x_{3} - 4 x_{4} &= 41, \\
#      2 x_{1} + 3 x_{2} + 3 x_{3} - 3 x_{4} &= 11, \\
#      - 2 x_{1} + 2 x_{2} - 5 x_{3} - 4 x_{4} &= -21.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{cccc|cccc}
#          3 & -5 & -4 & -1 & 28 \\
#          0 & -4 & 3 & -4 & 41 \\
#          2 & 3 & 3 & -3 & 11 \\
#          -2 & 2 & -5 & -4 & -21 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} - \frac{2}{3} R_{1} \\ R_{4} + \frac{2}{3} R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          3 & -5 & -4 & -1 & 28 \\
#          0 & -4 & 3 & -4 & 41 \\
#          0 & \frac{19}{3} & \frac{17}{3} & - \frac{7}{3} & - \frac{23}{3} \\
#          0 & - \frac{4}{3} & - \frac{23}{3} & - \frac{14}{3} & - \frac{7}{3} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} \leftrightarrow R_{3} \\ \phantom{x} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          3 & -5 & -4 & -1 & 28 \\
#          0 & \frac{19}{3} & \frac{17}{3} & - \frac{7}{3} & - \frac{23}{3} \\
#          0 & -4 & 3 & -4 & 41 \\
#          0 & - \frac{4}{3} & - \frac{23}{3} & - \frac{14}{3} & - \frac{7}{3} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} + \frac{12}{19} R_{2} \\ R_{4} + \frac{4}{19} R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          3 & -5 & -4 & -1 & 28 \\
#          0 & \frac{19}{3} & \frac{17}{3} & - \frac{7}{3} & - \frac{23}{3} \\
#          0 & 0 & \frac{125}{19} & - \frac{104}{19} & \frac{687}{19} \\
#          0 & 0 & - \frac{123}{19} & - \frac{98}{19} & - \frac{75}{19} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ \phantom{x} \\ R_{4} + \frac{123}{125} R_{3} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          3 & -5 & -4 & -1 & 28 \\
#          0 & \frac{19}{3} & \frac{17}{3} & - \frac{7}{3} & - \frac{23}{3} \\
#          0 & 0 & \frac{125}{19} & - \frac{104}{19} & \frac{687}{19} \\
#          0 & 0 & 0 & - \frac{1318}{125} & \frac{3954}{125} \\
#     \end{array} \right)
# \end{align*}
# 
# therefore 
# \begin{align*}
#     x_{4} &= \frac{1}{- \frac{1318}{125}} \left( \frac{3954}{125}\right) = -3, \\
#     x_{3} &= \frac{1}{\frac{125}{19}} \left( \frac{687}{19} - \left( - \frac{104}{19} \right) \left( -3 \right)\right) = 3, \\
#     x_{2} &= \frac{1}{\frac{19}{3}} \left( - \frac{23}{3} - \frac{17}{3} \left( 3 \right) - \left( - \frac{7}{3} \right) \left( -3 \right)\right) = -5, \\
#     x_{1} &= \frac{1}{3} \left( 28 - \left( -5 \right) \left( -5 \right) - \left( -4 \right) \left( 3 \right) - \left( -1 \right) \left( -3 \right)\right) = 4.
# \end{align*}
# ::::
# 
# (f)
# \begin{align*}
#      2 x_{1} - 3 x_{2} - 3 x_{3} + 4 x_{4} &= -1, \\
#      4 x_{1} - 5 x_{2} +  x_{3} - 5 x_{4} &= 42, \\
#      3 x_{1} + 3 x_{2} -  x_{3} - 5 x_{4} &= 20, \\
#      x_{1} +  x_{3} + 3 x_{4} &= -4.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{cccc|cccc}
#          2 & -3 & -3 & 4 & -1 \\
#          4 & -5 & 1 & -5 & 42 \\
#          3 & 3 & -1 & -5 & 20 \\
#          1 & 0 & 1 & 3 & -4 \\
#     \end{array} \right)
#     \begin{matrix} R_{1} \leftrightarrow R_{2} \\ \phantom{x} \\ \phantom{x} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          4 & -5 & 1 & -5 & 42 \\
#          2 & -3 & -3 & 4 & -1 \\
#          3 & 3 & -1 & -5 & 20 \\
#          1 & 0 & 1 & 3 & -4 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - \frac{1}{2} R_{1} \\ R_{3} - \frac{3}{4} R_{1} \\ R_{4} - \frac{1}{4} R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          4 & -5 & 1 & -5 & 42 \\
#          0 & - \frac{1}{2} & - \frac{7}{2} & \frac{13}{2} & -22 \\
#          0 & \frac{27}{4} & - \frac{7}{4} & - \frac{5}{4} & - \frac{23}{2} \\
#          0 & \frac{5}{4} & \frac{3}{4} & \frac{17}{4} & - \frac{29}{2} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} \leftrightarrow R_{3} \\ \phantom{x} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          4 & -5 & 1 & -5 & 42 \\
#          0 & \frac{27}{4} & - \frac{7}{4} & - \frac{5}{4} & - \frac{23}{2} \\
#          0 & - \frac{1}{2} & - \frac{7}{2} & \frac{13}{2} & -22 \\
#          0 & \frac{5}{4} & \frac{3}{4} & \frac{17}{4} & - \frac{29}{2} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} + \frac{2}{27} R_{2} \\ R_{4} - \frac{5}{27} R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          4 & -5 & 1 & -5 & 42 \\
#          0 & \frac{27}{4} & - \frac{7}{4} & - \frac{5}{4} & - \frac{23}{2} \\
#          0 & 0 & - \frac{98}{27} & \frac{173}{27} & - \frac{617}{27} \\
#          0 & 0 & \frac{29}{27} & \frac{121}{27} & - \frac{334}{27} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ \phantom{x} \\ R_{4} + \frac{29}{98} R_{3} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          4 & -5 & 1 & -5 & 42 \\
#          0 & \frac{27}{4} & - \frac{7}{4} & - \frac{5}{4} & - \frac{23}{2} \\
#          0 & 0 & - \frac{98}{27} & \frac{173}{27} & - \frac{617}{27} \\
#          0 & 0 & 0 & \frac{625}{98} & - \frac{1875}{98} \\
#     \end{array} \right)
# \end{align*}
# 
# therefore 
# \begin{align*}
#     x_{4} &= \frac{1}{\frac{625}{98}} \left( - \frac{1875}{98}\right) = -3, \\
#     x_{3} &= \frac{1}{- \frac{98}{27}} \left( - \frac{617}{27} - \frac{173}{27} \left( -3 \right)\right) = 1, \\
#     x_{2} &= \frac{1}{\frac{27}{4}} \left( - \frac{23}{2} - \left( - \frac{7}{4} \right) \left( 1 \right) - \left( - \frac{5}{4} \right) \left( -3 \right)\right) = -2, \\
#     x_{1} &= \frac{1}{4} \left( 42 - \left( -5 \right) \left( -2 \right) - 1 \left( 1 \right) - \left( -5 \right) \left( -3 \right)\right) = 4.
# \end{align*}
# ::::
# :::::

# In[4]:


def gelimpp(A):
    m, n = A.shape
    
    print(r"::::{dropdown} Solution")
    print(r"\begin{align*}")
    print(r"&", end="")
    print_augmented_matrix(A)
    
    for i in range(m - 1):
        for j in range(i, n):
            if A[i,j] != 0:
                pivotcol = j
                break
                
        maxpivot, pivotrow = abs(A[i, pivotcol]), i
        for j in range(i + 1, m):
            if abs(A[j,pivotcol]) > maxpivot:
                maxpivot, pivotrow = abs(A[j,pivotcol]), j
               
        if pivotrow != i:
            string = r"    \begin{matrix}"
            for j in range(m):
                if i == j:
                    string += rf" R_{{{i+1}}} \leftrightarrow R_{{{pivotrow + 1}}}"
                else:
                    string += r" \phantom{x}"
                if j < m - 1:
                    string += r" \\"
              
            string += r" \end{matrix} \\[1em]"
            print(string)
            print(r"    \longrightarrow \quad &")  
            A[i,:], A[pivotrow,:] = A[pivotrow,:], A[i,:]
            print_augmented_matrix(A)
                
         
        string = r"    \begin{matrix} \phantom{x} \\"
        for j in range(i):
            string += r" \phantom{x} \\"
            
        for j in range(i + 1, m):
            if A[j,pivotcol] / A[i,pivotcol] > 0:
                if A[j,pivotcol] / A[i,pivotcol] == 1:
                    string += rf" R_{{{j+1}}} - R_{{{i + 1}}}"
                else:
                    string += rf" R_{{{j+1}}} - {latex(A[j,pivotcol] / A[i,pivotcol])} R_{{{i + 1}}}"    
            elif A[j,pivotcol] / A[i,pivotcol] < 0:
                if A[j,pivotcol] / A[i,pivotcol] == -1:
                    string += rf" R_{{{j+1}}} + R_{{{i + 1}}}"
                else:
                    string += rf" R_{{{j+1}}} + {latex(-A[j,pivotcol] / A[i,pivotcol])} R_{{{i + 1}}}"
            elif A[j,pivotcol] / A[i,pivotcol] == 0:
                string += r" \phantom{x}"
            A[j,:] -= A[j,pivotcol] / A[i,pivotcol] * A[i,:]
            
            if j < m - 1:
                string += r" \\"
        string += r" \end{matrix} \\[1em]"
        print(string)
        print(r"    \longrightarrow \quad &")
        print_augmented_matrix(A)
    print(r"\end{align*}")
    print()
    print(rf"therefore ")
    back_substitution(A)
    print(r"::::") 
    
    return A


print(":::::{admonition} Exercise 2.5")
print(":class: note")
print(":name: ex2.5")
print()
print("Solve the linear system of equations from [exercise 2.3](ex2.3) using Gaussian elimination with partial pivoting.")    
print("\n(a)")
A = Matrix([[-1, 3], [-2, 1]])
b = Matrix([[-2], [1]])
Ab = A.row_join(b)
print_system(A, b)
Ab = gelimpp(Ab)

print("\n(b)")
A = Matrix([[3, 1, 2], [4, 0, -4], [4, -2, 1]])
b = Matrix([[11], [-4], [13]])
Ab = A.row_join(b)
print_system(A, b)
Ab = gelimpp(Ab)

print("\n(c)")
A = Matrix([[-1, -5, -2], [2, -2, -3], [3, -1, 4]])
b = Matrix([[-17], [-14], [-13]])
Ab = A.row_join(b)
print_system(A, b)
Ab = gelimpp(Ab)

print("\n(d)")
A = Matrix([[-1, -5, -2], [2, -2, -3],  [3, -1, -4]])
b = Matrix([[-26], [-19], [-20]])
Ab = A.row_join(b)
print_system(A, b)
Ab = gelimpp(Ab)

print("\n(e)")
A = Matrix([[3, -5, -4, -1], [0, -4, 3, -4], [2, 3, 3, -3], [-2, 2, -5, -4]])
b = Matrix([[28], [41], [11], [-21]])
Ab = A.row_join(b)
print_system(A, b)
Ab = gelimpp(Ab)

print("\n(f)")
A = Matrix([[2, -3, -3, 4], [4, -5, 1, -5], [3, 3, -1, -5], [1, 0, 1, 3]])
b = Matrix([[-1], [42], [20], [-4]])
Ab = A.row_join(b)
print_system(A, b)
Ab = gelimpp(Ab)

print(":::::")


# :::::{admonition} Exercise 2.5
# :class: note
# :name: ex2.5
# 
# Solve the linear system of equations from [exercise 2.3](ex2.3) using Gauss-Jordan elimination.
# 
# (a)
# \begin{align*}
#      - x_{1} + 3 x_{2} &= -2, \\
#      - 2 x_{1} +  x_{2} &= 1.
# \end{align*}
# 
# ::::{dropdown} Solution 
# \begin{align*}
# &    \left( \begin{array}{cc|cc}
#          -1 & 3 & -2 \\
#          -2 & 1 & 1 \\
#     \end{array} \right)
#     \begin{matrix} - R_{1} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|cc}
#          1 & -3 & 2 \\
#          -2 & 1 & 1 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} + 2 R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|cc}
#          1 & -3 & 2 \\
#          0 & -5 & 5 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ - \frac{1}{5} R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|cc}
#          1 & -3 & 2 \\
#          0 & 1 & -1 \\
#     \end{array} \right)
#     \begin{matrix} R_{1} + 3 R_{2} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|cc}
#          1 & 0 & -1 \\
#          0 & 1 & -1 \\
#     \end{array} \right)
# \end{align*}
# 
# therefore  $x_{1} = -1$ and $x_{2} = -1$.
# ::::
# 
# (b)
# \begin{align*}
#      3 x_{1} +  x_{2} + 2 x_{3} &= 11, \\
#      4 x_{1} - 4 x_{3} &= -4, \\
#      4 x_{1} - 2 x_{2} +  x_{3} &= 13.
# \end{align*}
# 
# ::::{dropdown} Solution 
# \begin{align*}
# &    \left( \begin{array}{ccc|ccc}
#          3 & 1 & 2 & 11 \\
#          4 & 0 & -4 & -4 \\
#          4 & -2 & 1 & 13 \\
#     \end{array} \right)
#     \begin{matrix} \frac{1}{3} R_{1} \\ \phantom{x} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & \frac{1}{3} & \frac{2}{3} & \frac{11}{3} \\
#          4 & 0 & -4 & -4 \\
#          4 & -2 & 1 & 13 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - 4 R_{1} \\ R_{3} - 4 R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & \frac{1}{3} & \frac{2}{3} & \frac{11}{3} \\
#          0 & - \frac{4}{3} & - \frac{20}{3} & - \frac{56}{3} \\
#          0 & - \frac{10}{3} & - \frac{5}{3} & - \frac{5}{3} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ - \frac{3}{4} R_{2} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & \frac{1}{3} & \frac{2}{3} & \frac{11}{3} \\
#          0 & 1 & 5 & 14 \\
#          0 & - \frac{10}{3} & - \frac{5}{3} & - \frac{5}{3} \\
#     \end{array} \right)
#     \begin{matrix} R_{1} - \frac{1}{3} R_{2} \\ \phantom{x} \\ R_{3} + \frac{10}{3} R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 0 & -1 & -1 \\
#          0 & 1 & 5 & 14 \\
#          0 & 0 & 15 & 45 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ \frac{1}{15} R_{3} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 0 & -1 & -1 \\
#          0 & 1 & 5 & 14 \\
#          0 & 0 & 1 & 3 \\
#     \end{array} \right)
#     \begin{matrix} R_{1} + R_{3} \\ R_{2} - 5 R_{3} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 0 & 0 & 2 \\
#          0 & 1 & 0 & -1 \\
#          0 & 0 & 1 & 3 \\
#     \end{array} \right)
# \end{align*}
# 
# therefore  $x_{1} = 2$, $x_{2} = -1$ and $x_{3} = 3$.
# ::::
# 
# (c)
# \begin{align*}
#      - x_{1} - 5 x_{2} - 2 x_{3} &= -17, \\
#      2 x_{1} - 2 x_{2} - 3 x_{3} &= -14, \\
#      3 x_{1} -  x_{2} + 4 x_{3} &= -13.
# \end{align*}
# 
# ::::{dropdown} Solution 
# \begin{align*}
# &    \left( \begin{array}{ccc|ccc}
#          -1 & -5 & -2 & -17 \\
#          2 & -2 & -3 & -14 \\
#          3 & -1 & 4 & -13 \\
#     \end{array} \right)
#     \begin{matrix} - R_{1} \\ \phantom{x} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 5 & 2 & 17 \\
#          2 & -2 & -3 & -14 \\
#          3 & -1 & 4 & -13 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - 2 R_{1} \\ R_{3} - 3 R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 5 & 2 & 17 \\
#          0 & -12 & -7 & -48 \\
#          0 & -16 & -2 & -64 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ - \frac{1}{12} R_{2} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 5 & 2 & 17 \\
#          0 & 1 & \frac{7}{12} & 4 \\
#          0 & -16 & -2 & -64 \\
#     \end{array} \right)
#     \begin{matrix} R_{1} - 5 R_{2} \\ \phantom{x} \\ R_{3} + 16 R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 0 & - \frac{11}{12} & -3 \\
#          0 & 1 & \frac{7}{12} & 4 \\
#          0 & 0 & \frac{22}{3} & 0 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ \frac{3}{22} R_{3} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 0 & - \frac{11}{12} & -3 \\
#          0 & 1 & \frac{7}{12} & 4 \\
#          0 & 0 & 1 & 0 \\
#     \end{array} \right)
#     \begin{matrix} R_{1} + \frac{11}{12} R_{3} \\ R_{2} - \frac{7}{12} R_{3} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 0 & 0 & -3 \\
#          0 & 1 & 0 & 4 \\
#          0 & 0 & 1 & 0 \\
#     \end{array} \right)
# \end{align*}
# 
# therefore  $x_{1} = -3$, $x_{2} = 4$ and $x_{3} = 0$.
# ::::
# 
# (d)
# \begin{align*}
#      - x_{1} - 5 x_{2} - 2 x_{3} &= -26, \\
#      2 x_{1} - 2 x_{2} - 3 x_{3} &= -19, \\
#      3 x_{1} -  x_{2} - 4 x_{3} &= -20.
# \end{align*}
# 
# ::::{dropdown} Solution 
# \begin{align*}
# &    \left( \begin{array}{ccc|ccc}
#          -1 & -5 & -2 & -26 \\
#          2 & -2 & -3 & -19 \\
#          3 & -1 & -4 & -20 \\
#     \end{array} \right)
#     \begin{matrix} - R_{1} \\ \phantom{x} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 5 & 2 & 26 \\
#          2 & -2 & -3 & -19 \\
#          3 & -1 & -4 & -20 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - 2 R_{1} \\ R_{3} - 3 R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 5 & 2 & 26 \\
#          0 & -12 & -7 & -71 \\
#          0 & -16 & -10 & -98 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ - \frac{1}{12} R_{2} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 5 & 2 & 26 \\
#          0 & 1 & \frac{7}{12} & \frac{71}{12} \\
#          0 & -16 & -10 & -98 \\
#     \end{array} \right)
#     \begin{matrix} R_{1} - 5 R_{2} \\ \phantom{x} \\ R_{3} + 16 R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 0 & - \frac{11}{12} & - \frac{43}{12} \\
#          0 & 1 & \frac{7}{12} & \frac{71}{12} \\
#          0 & 0 & - \frac{2}{3} & - \frac{10}{3} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ - \frac{3}{2} R_{3} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 0 & - \frac{11}{12} & - \frac{43}{12} \\
#          0 & 1 & \frac{7}{12} & \frac{71}{12} \\
#          0 & 0 & 1 & 5 \\
#     \end{array} \right)
#     \begin{matrix} R_{1} + \frac{11}{12} R_{3} \\ R_{2} - \frac{7}{12} R_{3} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 0 & 0 & 1 \\
#          0 & 1 & 0 & 3 \\
#          0 & 0 & 1 & 5 \\
#     \end{array} \right)
# \end{align*}
# 
# therefore  $x_{1} = 1$, $x_{2} = 3$ and $x_{3} = 5$.
# ::::
# 
# (e)
# \begin{align*}
#      3 x_{1} - 5 x_{2} - 4 x_{3} -  x_{4} &= 28, \\
#      - 4 x_{2} + 3 x_{3} - 4 x_{4} &= 41, \\
#      2 x_{1} + 3 x_{2} + 3 x_{3} - 3 x_{4} &= 11, \\
#      - 2 x_{1} + 2 x_{2} - 5 x_{3} - 4 x_{4} &= -21.
# \end{align*}
# 
# ::::{dropdown} Solution 
# \begin{align*}
# &    \left( \begin{array}{cccc|cccc}
#          3 & -5 & -4 & -1 & 28 \\
#          0 & -4 & 3 & -4 & 41 \\
#          2 & 3 & 3 & -3 & 11 \\
#          -2 & 2 & -5 & -4 & -21 \\
#     \end{array} \right)
#     \begin{matrix} \frac{1}{3} R_{1} \\ \phantom{x} \\ \phantom{x} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          1 & - \frac{5}{3} & - \frac{4}{3} & - \frac{1}{3} & \frac{28}{3} \\
#          0 & -4 & 3 & -4 & 41 \\
#          2 & 3 & 3 & -3 & 11 \\
#          -2 & 2 & -5 & -4 & -21 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} - 2 R_{1} \\ R_{4} + 2 R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          1 & - \frac{5}{3} & - \frac{4}{3} & - \frac{1}{3} & \frac{28}{3} \\
#          0 & -4 & 3 & -4 & 41 \\
#          0 & \frac{19}{3} & \frac{17}{3} & - \frac{7}{3} & - \frac{23}{3} \\
#          0 & - \frac{4}{3} & - \frac{23}{3} & - \frac{14}{3} & - \frac{7}{3} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ - \frac{1}{4} R_{2} \\ \phantom{x} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          1 & - \frac{5}{3} & - \frac{4}{3} & - \frac{1}{3} & \frac{28}{3} \\
#          0 & 1 & - \frac{3}{4} & 1 & - \frac{41}{4} \\
#          0 & \frac{19}{3} & \frac{17}{3} & - \frac{7}{3} & - \frac{23}{3} \\
#          0 & - \frac{4}{3} & - \frac{23}{3} & - \frac{14}{3} & - \frac{7}{3} \\
#     \end{array} \right)
#     \begin{matrix} R_{1} + \frac{5}{3} R_{2} \\ \phantom{x} \\ R_{3} - \frac{19}{3} R_{2} \\ R_{4} + \frac{4}{3} R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          1 & 0 & - \frac{31}{12} & \frac{4}{3} & - \frac{31}{4} \\
#          0 & 1 & - \frac{3}{4} & 1 & - \frac{41}{4} \\
#          0 & 0 & \frac{125}{12} & - \frac{26}{3} & \frac{229}{4} \\
#          0 & 0 & - \frac{26}{3} & - \frac{10}{3} & -16 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ \frac{12}{125} R_{3} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          1 & 0 & - \frac{31}{12} & \frac{4}{3} & - \frac{31}{4} \\
#          0 & 1 & - \frac{3}{4} & 1 & - \frac{41}{4} \\
#          0 & 0 & 1 & - \frac{104}{125} & \frac{687}{125} \\
#          0 & 0 & - \frac{26}{3} & - \frac{10}{3} & -16 \\
#     \end{array} \right)
#     \begin{matrix} R_{1} + \frac{31}{12} R_{3} \\ R_{2} + \frac{3}{4} R_{3} \\ \phantom{x} \\ R_{4} + \frac{26}{3} R_{3} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          1 & 0 & 0 & - \frac{102}{125} & \frac{806}{125} \\
#          0 & 1 & 0 & \frac{47}{125} & - \frac{766}{125} \\
#          0 & 0 & 1 & - \frac{104}{125} & \frac{687}{125} \\
#          0 & 0 & 0 & - \frac{1318}{125} & \frac{3954}{125} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ \phantom{x} \\ - \frac{125}{1318} R_{4} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          1 & 0 & 0 & - \frac{102}{125} & \frac{806}{125} \\
#          0 & 1 & 0 & \frac{47}{125} & - \frac{766}{125} \\
#          0 & 0 & 1 & - \frac{104}{125} & \frac{687}{125} \\
#          0 & 0 & 0 & 1 & -3 \\
#     \end{array} \right)
#     \begin{matrix} R_{1} + \frac{102}{125} R_{4} \\ R_{2} - \frac{47}{125} R_{4} \\ R_{3} + \frac{104}{125} R_{4} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          1 & 0 & 0 & 0 & 4 \\
#          0 & 1 & 0 & 0 & -5 \\
#          0 & 0 & 1 & 0 & 3 \\
#          0 & 0 & 0 & 1 & -3 \\
#     \end{array} \right)
# \end{align*}
# 
# therefore  $x_{1} = 4$, $x_{2} = -5$, $x_{3} = 3$ and $x_{4} = -3$.
# ::::
# 
# (f)
# \begin{align*}
#      2 x_{1} - 3 x_{2} - 3 x_{3} + 4 x_{4} &= -1, \\
#      4 x_{1} - 5 x_{2} +  x_{3} - 5 x_{4} &= 42, \\
#      3 x_{1} + 3 x_{2} -  x_{3} - 5 x_{4} &= 20, \\
#      x_{1} +  x_{3} + 3 x_{4} &= -4.
# \end{align*}
# 
# ::::{dropdown} Solution 
# \begin{align*}
# &    \left( \begin{array}{cccc|cccc}
#          2 & -3 & -3 & 4 & -1 \\
#          4 & -5 & 1 & -5 & 42 \\
#          3 & 3 & -1 & -5 & 20 \\
#          1 & 0 & 1 & 3 & -4 \\
#     \end{array} \right)
#     \begin{matrix} \frac{1}{2} R_{1} \\ \phantom{x} \\ \phantom{x} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          1 & - \frac{3}{2} & - \frac{3}{2} & 2 & - \frac{1}{2} \\
#          4 & -5 & 1 & -5 & 42 \\
#          3 & 3 & -1 & -5 & 20 \\
#          1 & 0 & 1 & 3 & -4 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - 4 R_{1} \\ R_{3} - 3 R_{1} \\ R_{4} - R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          1 & - \frac{3}{2} & - \frac{3}{2} & 2 & - \frac{1}{2} \\
#          0 & 1 & 7 & -13 & 44 \\
#          0 & \frac{15}{2} & \frac{7}{2} & -11 & \frac{43}{2} \\
#          0 & \frac{3}{2} & \frac{5}{2} & 1 & - \frac{7}{2} \\
#     \end{array} \right)
#     \begin{matrix} R_{1} + \frac{3}{2} R_{2} \\ \phantom{x} \\ R_{3} - \frac{15}{2} R_{2} \\ R_{4} - \frac{3}{2} R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          1 & 0 & 9 & - \frac{35}{2} & \frac{131}{2} \\
#          0 & 1 & 7 & -13 & 44 \\
#          0 & 0 & -49 & \frac{173}{2} & - \frac{617}{2} \\
#          0 & 0 & -8 & \frac{41}{2} & - \frac{139}{2} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ - \frac{1}{49} R_{3} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          1 & 0 & 9 & - \frac{35}{2} & \frac{131}{2} \\
#          0 & 1 & 7 & -13 & 44 \\
#          0 & 0 & 1 & - \frac{173}{98} & \frac{617}{98} \\
#          0 & 0 & -8 & \frac{41}{2} & - \frac{139}{2} \\
#     \end{array} \right)
#     \begin{matrix} R_{1} - 9 R_{3} \\ R_{2} - 7 R_{3} \\ \phantom{x} \\ R_{4} + 8 R_{3} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          1 & 0 & 0 & - \frac{79}{49} & \frac{433}{49} \\
#          0 & 1 & 0 & - \frac{9}{14} & - \frac{1}{14} \\
#          0 & 0 & 1 & - \frac{173}{98} & \frac{617}{98} \\
#          0 & 0 & 0 & \frac{625}{98} & - \frac{1875}{98} \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ \phantom{x} \\ \frac{98}{625} R_{4} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          1 & 0 & 0 & - \frac{79}{49} & \frac{433}{49} \\
#          0 & 1 & 0 & - \frac{9}{14} & - \frac{1}{14} \\
#          0 & 0 & 1 & - \frac{173}{98} & \frac{617}{98} \\
#          0 & 0 & 0 & 1 & -3 \\
#     \end{array} \right)
#     \begin{matrix} R_{1} + \frac{79}{49} R_{4} \\ R_{2} + \frac{9}{14} R_{4} \\ R_{3} + \frac{173}{98} R_{4} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cccc|cccc}
#          1 & 0 & 0 & 0 & 4 \\
#          0 & 1 & 0 & 0 & -2 \\
#          0 & 0 & 1 & 0 & 1 \\
#          0 & 0 & 0 & 1 & -3 \\
#     \end{array} \right)
# \end{align*}
# 
# therefore  $x_{1} = 4$, $x_{2} = -2$, $x_{3} = 1$ and $x_{4} = -3$.
# ::::
# :::::

# In[5]:


def gjelim(A):
    m, n = A.shape
    
    print(r"::::{dropdown} Solution ")
    print(r"\begin{align*}")
    print(r"&", end="")
    print_augmented_matrix(A)
    
    for i in range(m):
        for j in range(i, n):
            if A[i,j] != 0:
                pivot = j
                break
    
        if A[i,pivot] != 1:
            print(r"    \begin{matrix}", end="")
            for j in range(m):
                if j == i:
                    if A[i,pivot] == -1:
                        print(rf" - R_{{{j+1}}}", end="")
                    elif A[i,pivot] != 1:
                        print(rf" {latex(1 / A[i,pivot])} R_{{{j+1}}}", end="")
                else:
                    print(r" \phantom{x}", end="")
                if j < m - 1:
                    print(r" \\", end="")
            print(r" \end{matrix} \\[1em]")
            print(r"    \longrightarrow \quad &")
            
            A[i,:] /= A[i,pivot]
            print_augmented_matrix(A)
         
        print(r"    \begin{matrix}", end="")
        for j in range(m):
            if i != j:
                if A[j,pivot] > 0:
                    if A[j,pivot] == 1:
                        print(rf" R_{{{j+1}}} - R_{{{i + 1}}}", end="")
                    else:
                        print(rf" R_{{{j+1}}} - {latex(A[j,pivot])} R_{{{i + 1}}}", end="")    
                elif A[j,pivot] < 0:
                    if A[j,pivot] == -1:
                        print(rf" R_{{{j+1}}} + R_{{{i + 1}}}", end="")
                    else:
                        print(rf" R_{{{j+1}}} + {latex(-A[j,pivot])} R_{{{i + 1}}}", end="")
                elif A[j,pivot] == 0:
                    print(r" \phantom{x}", end="")
                A[j,:] -= A[j, pivot] * A[i,:]
            if i == j:
                print(r" \phantom{x}", end="")
            if j < m - 1:
                print(r" \\", end="")
        print(r" \end{matrix} \\[1em]")
        print(r"    \longrightarrow \quad &")
        print_augmented_matrix(A)
    print(r"\end{align*}")
    print()
    print(rf"therefore ", end="")
    for i in range(m - 1):
        print(rf" $x_{{{i+1}}} = {latex(A[i,-1])}$", end="")
        if i < m - 2:
            print(",", end ="")
    print(rf" and $x_{{{m}}} = {latex(A[-1,-1])}$.")
    print("::::")

    return A
        
print(":::::{admonition} Exercise 2.4")
print(":class: note")
print(":name: ex2.4")
print()
print("Solve the linear system of equations from [exercise 2.3](ex2.3) using Gauss-Jordan elimination.")    
print("\n(a)")

A = Matrix([[-1, 3], [-2, 1]])
b = Matrix([[-2], [1]])
Ab = A.row_join(b)
print_system(A, b)
Ab = gjelim(Ab)

print("\n(b)")
A = Matrix([[3, 1, 2], [4, 0, -4], [4, -2, 1]])
b = Matrix([[11], [-4], [13]])
Ab = A.row_join(b)
print_system(A, b)
Ab = gjelim(Ab)

print("\n(c)")
A = Matrix([[-1, -5, -2], [2, -2, -3], [3, -1, 4]])
b = Matrix([[-17], [-14], [-13]])
Ab = A.row_join(b)
print_system(A, b)
Ab = gjelim(Ab)

print("\n(d)")
A = Matrix([[-1, -5, -2], [2, -2, -3],  [3, -1, -4]])
b = Matrix([[-26], [-19], [-20]])
Ab = A.row_join(b)
print_system(A, b)
Ab = gjelim(Ab)

print("\n(e)")
A = Matrix([[3, -5, -4, -1], [0, -4, 3, -4], [2, 3, 3, -3], [-2, 2, -5, -4]])
b = Matrix([[28], [41], [11], [-21]])
Ab = A.row_join(b)
print_system(A, b)
Ab = gjelim(Ab)

print("\n(f)")
A = Matrix([[2, -3, -3, 4], [4, -5, 1, -5], [3, 3, -1, -5], [1, 0, 1, 3]])
b = Matrix([[-1], [42], [20], [-4]])
Ab = A.row_join(b)
print_system(A, b)
Ab = gjelim(Ab)

print(":::::")


# :::::{admonition} Exercise 2.6
# :class: note
# :name: ex2.6
# 
# Use Gauss-Jordan elimination to calculate the inverse of the coefficient matrices from [exercise 2.1](ex2.1).
# 
# 
# (a)
# \begin{align*}
#     \left( \begin{array}{cc}
#          -4 & 2 \\
#          3 & 4 \\
#     \end{array} \right)
# \end{align*}
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{cc|cc}
#          -4 & 2 & 1 & 0 \\
#          3 & 4 & 0 & 1 \\
#     \end{array} \right)
#     \begin{matrix} - \frac{1}{4} R_{1} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|cc}
#          1 & - \frac{1}{2} & - \frac{1}{4} & 0 \\
#          3 & 4 & 0 & 1 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - 3 R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|cc}
#          1 & - \frac{1}{2} & - \frac{1}{4} & 0 \\
#          0 & \frac{11}{2} & \frac{3}{4} & 1 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \frac{2}{11} R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|cc}
#          1 & - \frac{1}{2} & - \frac{1}{4} & 0 \\
#          0 & 1 & \frac{3}{22} & \frac{2}{11} \\
#     \end{array} \right)
#     \begin{matrix} R_{1} + \frac{1}{2} R_{2} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|cc}
#          1 & 0 & - \frac{2}{11} & \frac{1}{11} \\
#          0 & 1 & \frac{3}{22} & \frac{2}{11} \\
#     \end{array} \right)
# \end{align*}
# 
# therefore 
# \begin{align*}
# A^{{-1}} = 
#     \left( \begin{array}{cc}
#          - \frac{2}{11} & \frac{1}{11} \\
#          \frac{3}{22} & \frac{2}{11} \\
#     \end{array} \right)
# . \end{align*}
# ::::
# 
# (b)
# \begin{align*}
#     \left( \begin{array}{cc}
#          -4 & 2 \\
#          -1 & -3 \\
#     \end{array} \right)
# \end{align*}
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{cc|cc}
#          -4 & 2 & 1 & 0 \\
#          -1 & -3 & 0 & 1 \\
#     \end{array} \right)
#     \begin{matrix} - \frac{1}{4} R_{1} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|cc}
#          1 & - \frac{1}{2} & - \frac{1}{4} & 0 \\
#          -1 & -3 & 0 & 1 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} + R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|cc}
#          1 & - \frac{1}{2} & - \frac{1}{4} & 0 \\
#          0 & - \frac{7}{2} & - \frac{1}{4} & 1 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ - \frac{2}{7} R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|cc}
#          1 & - \frac{1}{2} & - \frac{1}{4} & 0 \\
#          0 & 1 & \frac{1}{14} & - \frac{2}{7} \\
#     \end{array} \right)
#     \begin{matrix} R_{1} + \frac{1}{2} R_{2} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|cc}
#          1 & 0 & - \frac{3}{14} & - \frac{1}{7} \\
#          0 & 1 & \frac{1}{14} & - \frac{2}{7} \\
#     \end{array} \right)
# \end{align*}
# 
# therefore 
# \begin{align*}
# A^{{-1}} = 
#     \left( \begin{array}{cc}
#          - \frac{3}{14} & - \frac{1}{7} \\
#          \frac{1}{14} & - \frac{2}{7} \\
#     \end{array} \right)
# . \end{align*}
# ::::
# 
# (c)
# \begin{align*}
#     \left( \begin{array}{ccc}
#          -4 & -4 & -2 \\
#          3 & 0 & 4 \\
#          1 & 0 & 0 \\
#     \end{array} \right)
# \end{align*}
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{ccc|ccc}
#          -4 & -4 & -2 & 1 & 0 & 0 \\
#          3 & 0 & 4 & 0 & 1 & 0 \\
#          1 & 0 & 0 & 0 & 0 & 1 \\
#     \end{array} \right)
#     \begin{matrix} - \frac{1}{4} R_{1} \\ \phantom{x} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 1 & \frac{1}{2} & - \frac{1}{4} & 0 & 0 \\
#          3 & 0 & 4 & 0 & 1 & 0 \\
#          1 & 0 & 0 & 0 & 0 & 1 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - 3 R_{1} \\ R_{3} - R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 1 & \frac{1}{2} & - \frac{1}{4} & 0 & 0 \\
#          0 & -3 & \frac{5}{2} & \frac{3}{4} & 1 & 0 \\
#          0 & -1 & - \frac{1}{2} & \frac{1}{4} & 0 & 1 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ - \frac{1}{3} R_{2} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 1 & \frac{1}{2} & - \frac{1}{4} & 0 & 0 \\
#          0 & 1 & - \frac{5}{6} & - \frac{1}{4} & - \frac{1}{3} & 0 \\
#          0 & -1 & - \frac{1}{2} & \frac{1}{4} & 0 & 1 \\
#     \end{array} \right)
#     \begin{matrix} R_{1} - R_{2} \\ \phantom{x} \\ R_{3} + R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 0 & \frac{4}{3} & 0 & \frac{1}{3} & 0 \\
#          0 & 1 & - \frac{5}{6} & - \frac{1}{4} & - \frac{1}{3} & 0 \\
#          0 & 0 & - \frac{4}{3} & 0 & - \frac{1}{3} & 1 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ - \frac{3}{4} R_{3} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 0 & \frac{4}{3} & 0 & \frac{1}{3} & 0 \\
#          0 & 1 & - \frac{5}{6} & - \frac{1}{4} & - \frac{1}{3} & 0 \\
#          0 & 0 & 1 & 0 & \frac{1}{4} & - \frac{3}{4} \\
#     \end{array} \right)
#     \begin{matrix} R_{1} - \frac{4}{3} R_{3} \\ R_{2} + \frac{5}{6} R_{3} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 0 & 0 & 0 & 0 & 1 \\
#          0 & 1 & 0 & - \frac{1}{4} & - \frac{1}{8} & - \frac{5}{8} \\
#          0 & 0 & 1 & 0 & \frac{1}{4} & - \frac{3}{4} \\
#     \end{array} \right)
# \end{align*}
# 
# therefore 
# \begin{align*}
# A^{{-1}} = 
#     \left( \begin{array}{ccc}
#          0 & 0 & 1 \\
#          - \frac{1}{4} & - \frac{1}{8} & - \frac{5}{8} \\
#          0 & \frac{1}{4} & - \frac{3}{4} \\
#     \end{array} \right)
# . \end{align*}
# ::::
# 
# (d)
# \begin{align*}
#     \left( \begin{array}{ccc}
#          4 & 0 & -4 \\
#          4 & -1 & 1 \\
#          3 & 1 & 2 \\
#     \end{array} \right)
# \end{align*}
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{ccc|ccc}
#          4 & 0 & -4 & 1 & 0 & 0 \\
#          4 & -1 & 1 & 0 & 1 & 0 \\
#          3 & 1 & 2 & 0 & 0 & 1 \\
#     \end{array} \right)
#     \begin{matrix} \frac{1}{4} R_{1} \\ \phantom{x} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 0 & -1 & \frac{1}{4} & 0 & 0 \\
#          4 & -1 & 1 & 0 & 1 & 0 \\
#          3 & 1 & 2 & 0 & 0 & 1 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - 4 R_{1} \\ R_{3} - 3 R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 0 & -1 & \frac{1}{4} & 0 & 0 \\
#          0 & -1 & 5 & -1 & 1 & 0 \\
#          0 & 1 & 5 & - \frac{3}{4} & 0 & 1 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ - R_{2} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 0 & -1 & \frac{1}{4} & 0 & 0 \\
#          0 & 1 & -5 & 1 & -1 & 0 \\
#          0 & 1 & 5 & - \frac{3}{4} & 0 & 1 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} - R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 0 & -1 & \frac{1}{4} & 0 & 0 \\
#          0 & 1 & -5 & 1 & -1 & 0 \\
#          0 & 0 & 10 & - \frac{7}{4} & 1 & 1 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ \frac{1}{10} R_{3} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 0 & -1 & \frac{1}{4} & 0 & 0 \\
#          0 & 1 & -5 & 1 & -1 & 0 \\
#          0 & 0 & 1 & - \frac{7}{40} & \frac{1}{10} & \frac{1}{10} \\
#     \end{array} \right)
#     \begin{matrix} R_{1} + R_{3} \\ R_{2} + 5 R_{3} \\ \phantom{x} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 0 & 0 & \frac{3}{40} & \frac{1}{10} & \frac{1}{10} \\
#          0 & 1 & 0 & \frac{1}{8} & - \frac{1}{2} & \frac{1}{2} \\
#          0 & 0 & 1 & - \frac{7}{40} & \frac{1}{10} & \frac{1}{10} \\
#     \end{array} \right)
# \end{align*}
# 
# therefore 
# \begin{align*}
# A^{{-1}} = 
#     \left( \begin{array}{ccc}
#          \frac{3}{40} & \frac{1}{10} & \frac{1}{10} \\
#          \frac{1}{8} & - \frac{1}{2} & \frac{1}{2} \\
#          - \frac{7}{40} & \frac{1}{10} & \frac{1}{10} \\
#     \end{array} \right)
# . \end{align*}
# ::::
# :::::

# In[6]:


def print_augmented_matrix(A):
    m, n = A.shape
    cols = "c" * m + "|" + "c" * m
    print(rf"    \left( \begin{{array}}{{{cols}}}")
    for i in range(m):
        print("        ", end="")
        for j in range(n - 1):
            print(rf" {latex(A[i,j])} &", end="")
        print(rf" {latex(A[i,-1])} \\")
    print(r"    \end{array} \right)")
 
  
def print_standalone_matrix(A):
    m, n = A.shape
    cols = "c" * m
    print(r"\begin{align*}")
    print(rf"    \left( \begin{{array}}{{{cols}}}")
    for i in range(m):
        print("        ", end="")
        for j in range(n - 1):
            print(rf" {latex(A[i,j])} &", end="")
        print(rf" {latex(A[i,-1])} \\")
    print(r"    \end{array} \right)")
    print(r"\end{align*}")
          
def gjelim_inverse(A):
    m, n = A.shape
    
    A = A.row_join(eye(A.shape[0]))

    print(r"::::{dropdown} Solution")
    print(r"\begin{align*}")
    print(r"&", end="")
    print_augmented_matrix(A)
    
    for i in range(m):
        for j in range(i, n):
            if A[i,j] != 0:
                pivot = j
                break
    
        if A[i,pivot] != 1:
            print(r"    \begin{matrix}", end="")
            for j in range(m):
                if j == i:
                    if A[i,pivot] == -1:
                        print(rf" - R_{{{j+1}}}", end="")
                    elif A[i,pivot] != 1:
                        print(rf" {latex(1 / A[i,pivot])} R_{{{j+1}}}", end="")
                else:
                    print(r" \phantom{x}", end="")
                if j < m - 1:
                    print(r" \\", end="")
            print(r" \end{matrix} \\[1em]")
            print(r"    \longrightarrow \quad &")
            
            A[i,:] /= A[i,pivot]
            print_augmented_matrix(A)
         
        print(r"    \begin{matrix}", end="")
        for j in range(m):
            if i != j:
                if A[j,pivot] > 0:
                    if A[j,pivot] == 1:
                        print(rf" R_{{{j+1}}} - R_{{{i + 1}}}", end="")
                    else:
                        print(rf" R_{{{j+1}}} - {latex(A[j,pivot])} R_{{{i + 1}}}", end="")    
                elif A[j,pivot] < 0:
                    if A[j,pivot] == -1:
                        print(rf" R_{{{j+1}}} + R_{{{i + 1}}}", end="")
                    else:
                        print(rf" R_{{{j+1}}} + {latex(-A[j,pivot])} R_{{{i + 1}}}", end="")
                elif A[j,pivot] == 0:
                    print(r" \phantom{x}", end="")
                A[j,:] -= A[j, pivot] * A[i,:]
            if i == j:
                print(r" \phantom{x}", end="")
            if j < m - 1:
                print(r" \\", end="")
        print(r" \end{matrix} \\[1em]")
        print(r"    \longrightarrow \quad &")
        print_augmented_matrix(A)
    print(r"\end{align*}")
    print()
    print(rf"therefore ")
    print(r"\begin{align*}")
    print(r"A^{{-1}} = ")
    print_matrix(A[:,n:])
    print(r". \end{align*}")
    print("::::")

    return A


print(":::::{admonition} Exercise 2.6")
print(":class: note")
print(":name: ex2.6")
print()
print("Use Gauss-Jordan elimination to calculate the inverse of the coefficient matrices from [exercise 2.1](ex2.1).")
print()    
print("\n(a)")
A = Matrix([[-4, 2], [3, 4]])
print_standalone_matrix(A)
AI = gjelim_inverse(A)

print("\n(b)")
A = Matrix([[-4, 2], [-1, -3]])
print_standalone_matrix(A)
AI = gjelim_inverse(A)

print("\n(c)")
A = Matrix([[-4, -4, -2], [3, 0, 4], [1, 0, 0]])
print_standalone_matrix(A)
AI = gjelim_inverse(A)

print("\n(d)")
A = Matrix([[4, 0, -4], [4, -1, 1], [3, 1, 2]])
print_standalone_matrix(A)
AI = gjelim_inverse(A)

print(":::::")


# :::::{admonition} Exercise 2.7
# :class: note
# :name: ex2.7
# 
# For the following linear systems of equations, determine the rank of the coefficient matrix and the augmented matrix and classify the system is consistent, inconsistent or indeterminate and calculate the solution (if possible).
# 
# 
# (a)
# \begin{align*}
#      x_{1} -  x_{2} + 2 x_{3} &= 2, \\
#      2 x_{1} +  x_{2} + 4 x_{3} &= 7, \\
#      4 x_{1} +  x_{2} +  x_{3} &= 4.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{ccc|ccc}
#          1 & -1 & 2 & 2 \\
#          2 & 1 & 4 & 7 \\
#          4 & 1 & 1 & 4 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - 2 R_{1} \\ R_{3} - 4 R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & -1 & 2 & 2 \\
#          0 & 3 & 0 & 3 \\
#          0 & 5 & -7 & -4 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} - \frac{5}{3} R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & -1 & 2 & 2 \\
#          0 & 3 & 0 & 3 \\
#          0 & 0 & -7 & -9 \\
#     \end{array} \right)
# \end{align*}
# 
# therefore $\rho(A) = 3$ and $\rho((A|\mathbf{b})) = 3$ so this system has a unique solution
# 
# \begin{align*}
#     x_{3} &= \frac{1}{-7} \left( -9\right) = \frac{9}{7}, \\
#     x_{2} &= \frac{1}{3} \left( 3 - 0 \left( \frac{9}{7} \right)\right) = 1, \\
#     x_{1} &= \frac{1}{1} \left( 2 - \left( -1 \right) \left( 1 \right) - 2 \left( \frac{9}{7} \right)\right) = \frac{3}{7}.
# \end{align*}
# ::::
# 
# (b)
# \begin{align*}
#      x_{1} -  x_{2} + 2 x_{3} &= 3, \\
#      2 x_{1} - 3 x_{2} + 7 x_{3} &= 4, \\
#      - x_{1} + 3 x_{2} - 8 x_{3} &= 1.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{ccc|ccc}
#          1 & -1 & 2 & 3 \\
#          2 & -3 & 7 & 4 \\
#          -1 & 3 & -8 & 1 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - 2 R_{1} \\ R_{3} + R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & -1 & 2 & 3 \\
#          0 & -1 & 3 & -2 \\
#          0 & 2 & -6 & 4 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} + 2 R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & -1 & 2 & 3 \\
#          0 & -1 & 3 & -2 \\
#          0 & 0 & 0 & 0 \\
#     \end{array} \right)
# \end{align*}
# 
# therefore $\rho(A) = 2$ and $\rho((A|\mathbf{b})) = 2$. Since $\rho(A) = \rho((A|\mathbf{b})) < 3$ then this system has infintely many solutons. Let $r = x_3$
# 
# \begin{align*}
#     x_2 &= \frac{1}{-1}(-2 - 3r) = 2 + 3r, \\
#     x_1 &= 3 + 2 + 3r - 2r = 5 + r.
# \end{align*}
# ::::
# 
# (c)
# \begin{align*}
#      x_{1} +  x_{2} - 2 x_{3} &= 1, \\
#      2 x_{1} -  x_{2} +  x_{3} &= 9, \\
#      x_{1} + 4 x_{2} - 7 x_{3} &= 2.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{ccc|ccc}
#          1 & 1 & -2 & 1 \\
#          2 & -1 & 1 & 9 \\
#          1 & 4 & -7 & 2 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - 2 R_{1} \\ R_{3} - R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 1 & -2 & 1 \\
#          0 & -3 & 5 & 7 \\
#          0 & 3 & -5 & 1 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} + R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc}
#          1 & 1 & -2 & 1 \\
#          0 & -3 & 5 & 7 \\
#          0 & 0 & 0 & 8 \\
#     \end{array} \right)
# \end{align*}
# 
# therefore $\rho(A) = 2$ and $\rho((A|\mathbf{b})) = 3$. Since $\rho(A) < \rho((A|\mathbf{b}))$ then this is an inconsistent system and does not have a solution.
# ::::
# :::::

# In[7]:


def rank(A):
    m, n = A.shape
    
    print(r"::::{dropdown} Solution")
    print(r"\begin{align*}")
    print(r"&", end="")
    print_augmented_matrix(A)
    
    for i in range(m - 1):
        for j in range(i, n):
            if A[i,j] != 0:
                pivotcol = j
                break         
         
        string = r"    \begin{matrix} \phantom{x} \\"
        for j in range(i):
            string += r" \phantom{x} \\"
            
        for j in range(i + 1, m):
            if A[j,pivotcol] / A[i,pivotcol] > 0:
                if A[j,pivotcol] / A[i,pivotcol] == 1:
                    string += rf" R_{{{j+1}}} - R_{{{i + 1}}}"
                else:
                    string += rf" R_{{{j+1}}} - {latex(A[j,pivotcol] / A[i,pivotcol])} R_{{{i + 1}}}"    
            elif A[j,pivotcol] / A[i,pivotcol] < 0:
                if A[j,pivotcol] / A[i,pivotcol] == -1:
                    string += rf" R_{{{j+1}}} + R_{{{i + 1}}}"
                else:
                    string += rf" R_{{{j+1}}} + {latex(-A[j,pivotcol] / A[i,pivotcol])} R_{{{i + 1}}}"
            elif A[j,pivotcol] / A[i,pivotcol] == 0:
                string += r" \phantom{x}"
            A[j,:] -= A[j,pivotcol] / A[i,pivotcol] * A[i,:]
            
            if j < m - 1:
                string += r" \\"
        string += r" \end{matrix} \\[1em]"
        print(string)
        print(r"    \longrightarrow \quad &")
        print_augmented_matrix(A)
    print(r"\end{align*}")
    print()
    print(rf"therefore $\rho(A) = {latex(A[:,:m].rank())}$ and $\rho((A|\mathbf{{b}})) = {latex(A.rank())}$.")
    print("::::")
    
    return A
    
print(":::::{admonition} Exercise 2.7")
print(":class: note")
print(":name: ex2.7")
print()
print("For the following linear systems of equations, determine the rank of the coefficient matrix and the augmented matrix and classify the system is consistent, inconsistent or indeterminate and calculate the solution (if possible).")
print()    

print("\n(a)")
A = Matrix([[1, -1, 2], [2, 1, 4], [4, 1, 1]])
b = Matrix([[2], [7], [4]])
Ab = A.row_join(b)
print_system(A, b)
Ab = rank(Ab)
back_substitution(Ab)

print("\n(b)")
A = Matrix([[1, -1, 2], [2, -3, 7], [-1, 3, -8]])
b = Matrix([[3], [4], [1]])
Ab = A.row_join(b)
print_system(A, b)
rank(Ab)

print("\n(c)")
A = Matrix([[1, 1, -2], [2, -1, 1], [1, 4, -7]])
b = Matrix([[1], [9], [2]])
Ab = A.row_join(b)
print_system(A, b)
rank(Ab)

print(":::::")


# :::::{admonition} Exercise 2.8
# :class: note
# :name: ex2.8
# 
# Solve the following systems of homogeneous linear equations.
# 
# (a)
# \begin{align*}
#      3 x_{1} + 2 x_{2} + 7 x_{3} &= 0, \\
#      4 x_{1} - 3 x_{2} - 2 x_{3} &= 0, \\
#      5 x_{1} + 9 x_{2} + 23 x_{3} &= 0.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{ccc|c}
#          3 & 2 & 7 & 0 \\
#          4 & -3 & -2 & 0 \\
#          5 & 9 & 23 & 0 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - \frac{4}{3} R_{1} \\ R_{3} - \frac{5}{3} R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#          3 & 2 & 7 & 0 \\
#          0 & - \frac{17}{3} & - \frac{34}{3} & 0 \\
#          0 & \frac{17}{3} & \frac{34}{3} & 0 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} + R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#          3 & 2 & 7 & 0 \\
#          0 & - \frac{17}{3} & - \frac{34}{3} & 0 \\
#          0 & 0 & 0 & 0 \\
#     \end{array} \right)
# \end{align*}
# 
# Let $x_3 =r$ then
# \begin{align*}
#     x_2 &= \frac{1}{-\frac{17}{3}}\left( \frac{34}{3}r \right) = -2r, \\
#     x_1 &= \frac{1}{3}(-2(-2r) - 7r) = -r.
# \end{align*}
# ::::
# 
# (b)
# \begin{align*}
#      2 x_{1} + 3 x_{2} -  x_{3} &= 0, \\
#      x_{1} -  x_{2} - 2 x_{3} &= 0, \\
#      3 x_{1} +  x_{2} + 3 x_{3} &= 0.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
# &    \left( \begin{array}{ccc|c}
#          2 & 3 & -1 & 0 \\
#          1 & -1 & -2 & 0 \\
#          3 & 1 & 3 & 0 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ R_{2} - \frac{1}{2} R_{1} \\ R_{3} - \frac{3}{2} R_{1} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#          2 & 3 & -1 & 0 \\
#          0 & - \frac{5}{2} & - \frac{3}{2} & 0 \\
#          0 & - \frac{7}{2} & \frac{9}{2} & 0 \\
#     \end{array} \right)
#     \begin{matrix} \phantom{x} \\ \phantom{x} \\ R_{3} - \frac{7}{5} R_{2} \end{matrix} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#          2 & 3 & -1 & 0 \\
#          0 & - \frac{5}{2} & - \frac{3}{2} & 0 \\
#          0 & 0 & \frac{33}{5} & 0 \\
#     \end{array} \right)
# \end{align*}
# 
# Let $x_3 = r$ then
# \begin{align*}
#     x_2 &= \frac{1}{-\frac{5}{2}} \left(\frac{3}{2}r \right) = -\frac{3}{5}r, \\
#     x_1 &= \frac{1}{2} \left( -3\left(-\frac{3}{5}r\right) + r \right) = \frac{7}{5}r.
# \end{align*}
# ::::
# :::::

# In[8]:


print(":::::{admonition} Exercise 2.8")
print(":class: note")
print(":name: ex2.8")
print()
print("Solve the following systems of homogeneous linear equations.")

print("\n(a)")
A = Matrix([[3, 2, 7], [4, -3, -2], [5, 9, 23]])
b = zeros(3, 1)
Ab = A.row_join(b)
print_system(A, b)
Ab = gelim(Ab)
print("::::")

print("\n(b)")
A = Matrix([[2, 3, -1], [1, -1, -2], [3, 1, 3]])
b = zeros(3, 1)
Ab = A.row_join(b)
print_system(A, b)
Ab = gelim(Ab)
print("::::")

print(":::::")


# :::::{admonition} Exercise 2.9
# :class: note
# :name: ex2.9 
#     
# Determine the values of $k$ for which the following system of linear equations
# 
# \begin{align*}
#     x_1 + x_2 + 3x_3 &= 1, \\
#     4x_1 + 3x_2 + kx_3 &= 2, \\
#     2x_1 + x_2 + 2x_3 &= 3,
# \end{align*}
# 
# has:
# 
# (a) a unique solution.
# 
# ::::{dropdown} Solution
# \begin{align*}
#     & \left( \begin{array}{ccc|c} 
#         1 & 1 & 3 & 1 \\
#         4 & 3 & k & 2 \\
#         2 & 1 & 2 & 3 
#     \end{array} \right)
#     \begin{array}{l} \phantom{x} \\ R_2 - 4 R_1 \\ R_3 - 2 R_1 \end{array} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c} 
#         1 & 1 & 3 & 1 \\
#         0 & -1 & k - 12 & -2 \\
#         0 & -1 & -4 & 1 
#     \end{array} \right)
#     \begin{array}{l} \phantom{x} \\ R_2 \leftrightarrow R_3 \\ \phantom{x} \end{array} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c} 
#         1 & 1 & 3 & 1 \\
#         0 & -1 & -4 & 1 \\
#         0 & -1 & k - 12 & -2 
#     \end{array} \right)
#     \begin{array}{l} \phantom{x} \\ \phantom{x} \\ R_3 - R_2 \end{array} \\[1em]
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c} 
#         1 & 1 & 3 & 1 \\
#         0 & -1 & -4 & 1 \\
#         0 & 0 & k - 8 & -3
#     \end{array} \right).
# \end{align*}
# 
# For a homogeneous system to have a unique solution, each column must have a pivot. Therefore this system has a solution when $k \neq 8$.
# ::::
# 
# (b) a non-trivial solution
# 
# ::::{dropdown} Solution
# The row echelon form of the coefficient matrix is
# \begin{align*}
#     \begin{pmatrix}
#         1 & 1 & 3 \\
#         0 & -1 & -4 \\
#         0 & 0 & k - 8
#     \end{pmatrix}.
# \end{align*}
# 
# When $k=8$ the last row are all zeros so this system will have infinitely many solutions.
# 
# ::::
# 
# :::::
