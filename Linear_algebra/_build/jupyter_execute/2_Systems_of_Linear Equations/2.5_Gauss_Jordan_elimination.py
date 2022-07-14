#!/usr/bin/env python
# coding: utf-8

# (gauss-jordan-elimination-section)=
# # Gauss-Jordan elimination
# 
# **Gauss-Jordan elimination (GJE)** is similar to [Gaussian elimination](gaussian-elimination-section) with the difference that the augmented matrix is row reduced so that the values of the pivot elements are 1 and are the only non-zero element in the column. This allows the solution to be read from the final augmented matrix without the need to perform back substitution. A matrix in this form is said to be in reduced row echelon form.
# 
# ::::{admonition} Definition: Reduced Row Echelon Form (RREF)
# :class: note
# :name: rref-definition
# 
# A matrix is said to be in **Reduced Row Echelon Form (RREF)** if it satisfies the following conditions
# 
# - it is in row echelon form;
# - the leading entry in each non-zero row has a value of 1;
# - the leading entry in each non-zero row is the only non-zero element in its column.
# ::::
# 
# For example the following matrices are in reduced row echelon form:
# \begin{align*}
#   &\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, &
#   &\begin{pmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix}, &
#   &\begin{pmatrix} 1 & 0 & 2 & 0 \\ 0 & 1 & 3 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}
# \end{align*}
# 
# 
# The method of Gauss-Jordan elimination is summarised by the steps below.
# 
# :::::{admonition} Definition: Gauss-Jordan elimination
# :class: note
# :name: gje-definition
# 
# To row reduce an $m \times n$ matrix $A$ to reduced row echelon form using Gauss-Jordan elimination we do the following: 
# 
# 1. Initalise the pivot row to $i=1$ and pivot column to $k=1$ 
# 2. If $a_{ik} = 0$ perform a row swap with a row beneath the pivot row $i$ with a non-zero element in the pivot column $k$. If no such rows exist set $k = k + 1$ and repeat step 2.
# 3. Divide the pivot row $i$ by the value of the pivot element $a_{ik}$.
# 4. For each row $j = 1 \ldots m$ where $i \neq j$ subtract the pivot row $i$ multiplied by $a_{ik}$ from row $j$. 
# 5. Set $i = 1 + 1$ and $k = k + 1$ and repeat steps 2 to 4 until $i > m$ or $k > n$.
# :::::
# 
# :::::{admonition} Example 2.6
# :class: seealso
# :name: gje-example
# 
# Use Gauss-Jordan elimination to solve the following system of linear equations
# 
# \begin{align*}
#     3x_1 + x_2 - 2 x_3 &= 1, \\
#     x_1 - x_2 + 2x_3 &= 3, \\
#     2x_1 - 3x_2 + 7x_3 &= 4.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
#     & \left( \begin{array}{ccc|c}
#         3 & 1 & -2 & 1 \\
#         1 & -1 & 2 & 3 \\
#         2 & -3 & 7 & 4 
#     \end{array} \right)
#     \begin{array}{l} R_1 \leftrightarrow R_2 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & -1 & 2 & 3 \\
#         3 & 1 & -2 & 1 \\
#         2 & -3 & 7 & 4 
#     \end{array} \right)
#     \begin{array}{l} \\  R_2 - 3R_1 \\  R_3 - 2R_1 \end{array} \\ \\
#     \longrightarrow \quad & 
#     \left( \begin{array}{ccc|c}
#         1 & -1 & 2 & 3 \\
#         0 & 4 & -8 & -8 \\
#         0 & -1 & 3 & -2 
#     \end{array} \right)
#     \begin{array}{l} \\  \dfrac{1}{4} R_2 \\ \phantom{x} \end{array} \\ \\
#     \longrightarrow \quad & 
#     \left( \begin{array}{ccc|c}
#         1 & -1 & 2 & 3 \\
#         0 & 1 & -2 & -2 \\
#         0 & -1 & 3 & -2 
#     \end{array} \right)
#     \begin{array}{l}  R_1 + R_2\\ \\  R_3 + R_2 \end{array} \\ \\
#     \longrightarrow \quad & 
#     \left( \begin{array}{ccc|c}
#         1 & 0 & 0 & 1 \\
#         0 & 1 & -2 & -2 \\
#         0 & 0 & 1 & -4 
#     \end{array} \right)
#     \begin{array}{l} \\  R_2 + 2R_3 \\ \phantom{x}  \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & 0 & 1 \\
#         0 & 1 & 0 & -10 \\
#         0 & 0 & 1 & -4 
#     \end{array} \right)
# \end{align*}
# Therefore the solution is $x_1 = 1$, $x_2 = -10$ and $x_3 = -4$.
# 
# ::::
# :::::
# 
# ## Python code
# 
# The SymPy command for calculating the reduced row echelon form of a matrix `A` is `A.rref()[0]`. The Python code below solves the linear system from [example 2.6](gje-example).

# In[1]:


from sympy import *

# Define linear system
A = Matrix([[3, 1, -2], [1, -1, 2], [2, -3, 7]])
b = Matrix([[1], [3], [4]])

# Form augmented matrix
Ab = A.row_join(b)
print("Augmented matrix")
display(Ab)

# Row reduce augmented matrix
Ab = Ab.rref()[0]
print("Reduced row echelon form")
display(Ab)

# Extract solution
x = Ab[:,-1]
print("Solution")
display(x)


# (gj-matrix-inverse-section)=
# ## Calculating a matrix inverse using Gauss-Jordan elimination
# 
# Gauss-Jordan elimination allows us to calculate the inverse of matrices which is much more computationally efficient than the [adjoint-determinant formula](adjoint-determinant-formula-definition). To show how we can use ERO to calculate an inverse of a matrix we first need to consider elementary matrices.
# 
# ::::{admonition} Elementary matrix
# :class: note
# :name: elementary-matrix-definition
#     
# An **elementary matrix**, $E$, is an $n\times n$ matrix that is obtained by applying a single elementary row operation to the identity matrix $I_n$.
# ::::
# 
# Since we have three types of elementary row operations there are three types of elementary matrices. Consider examples of the three types for $I_3$:
# 
# - swap row $1$ and row $2$: $E_1 = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$
# - multiply row $2$ by $k$: $E_2 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & k & 0 \\ 0 & 0 & 1 \end{pmatrix}$
# - add $k$ times row 1 to row 3: $E_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ k & 0 & 1 \end{pmatrix}$
# 
# Elementary matrices have an inverse which is obtained by inverting the elementary row operation and applying it to $I$. Consider the inverse operations to those shown above
# 
# - swap row $1$ and row $2$: $E_1^{-1} = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} = E_1$
# - divide row $2$ by $k$: $E_2^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \frac{1}{k} & 0 \\ 0 & 0 & 1 \end{pmatrix}$
# - subtract $k$ times row 1 from row 3: $E_3^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -k & 0 & 1 \end{pmatrix}$
# 
# Since the inverse of an elementary matrix is obtained by applying an elementary row operation to the identity matrix, by definition it must also be an elementary matrix.
# 
# ::::{admonition} Theorem: Multiplication by an elementary matrix
# :class: important
# :name: multiplication-by-an-elementary-matrix-theorem
# 
# If $A$ is an $n\times n$ matrix then the product $EA$, where $E$ is an elementary matrix obtained by performing a single elementary row operation on $I_n$, is equivalent to performing the elementary row operation on $A$.
# ::::
# 
# For example, let $A = \begin{pmatrix} 1 & 0 & 4 \\ 2 & -1 & 3 \\ 0 & 5 & 1 \end{pmatrix}$ and consider the following row operations:
# 
# - $R_1 \leftrightarrow R_2$: $E = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ so 
# 
# $$EA = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 & 4 \\ 2 & -1 & 3 \\ 0 & 5 & 1 \end{pmatrix} = \begin{pmatrix} 2 & -1 & 3 \\ 1 & 0 & 4 \\0 & 5 & 1 \end{pmatrix}$$
# 
# - $-2R_2$: $E = \begin{pmatrix} 1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ so 
# 
# $$EA = \begin{pmatrix} 1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 4 \\ 2 & -1 & 3 \\ 0 & 5 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 4 \\ -4 & 2 & -6 \\ 0 & 5 & 1 \end{pmatrix}$$
# 
# - $ R_3 + 3R_2$: $E = \begin{pmatrix} 1 & 0 & 0  \\ 0 & 1 & 0 \\ 0 & 3 & 1 \end{pmatrix}$ so 
# 
# $$EA = \begin{pmatrix} 1 & 0 & 0  \\ 0 & 1 & 0 \\ 0 & 3 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 & 4 \\ 2 & -1 & 3 \\ 0 & 5 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 4 \\ 2 & -1 & 3 \\ 6 & 2 & 10 \end{pmatrix}$$
# 
# ::::{admonition} Theorem: Expressing an inverse matrix as a product of elementary matrices
# :class: important
# :name: inverse-as-product-of-elementary-matrices-theorem
# 
# If $A$ is an $n\times n$ non-singular matrix which which has been reduced to $I_n$ by use of $k$ elementary row operations $E_1, E_2, \ldots E_k$ then 
# 
# $$A^{-1} = E_kE_{k-1}\ldots E_2E_1.$$
# ::::
# 
# **Proof**
# 
# *If $A$ has been reduced to $I_n$ by application of $k$ elementary row operations then*
# 
# $$I_n  = E_kE_{k-1}\ldots E_2E_1A.$$
# 
# *Multiplying both sides on the right by $A^{-1}$ gives $A^{-1}=E_kE_{k-1}\ldots E_2E_1$.*<div style="text-align: right"> &#9633; </div>
# 
# Combining the theorems for [mulitplication by an elementary matrix](multiplication-by-an-elementary-matrix-theorem) and [expressing an inverse matrix as a product of elementary matrices](inverse-as-product-of-elementary-matrices-theorem) means that if we perform the same elementary row operations to $I$ as we have done to row reduce a non-singular matrix $A$ to $I$ then the results is the inverse of $A$. We do this by forming an augmented matrix $(A\mid I)$ and perform Gauss-Jordan elimination on the left-hand matrix. Once the left-hand matrix has been reduced to $I$ the right-hand matrix is then the inverse of $A$.
# 
# :::::{admonition} Example 2.7
# :class: seealso
# :name: gje-inverse-example
# 
# Use Gauss-Jordan elimination to calculate the inverse of 
# \begin{align*}
#     A = \begin{pmatrix}1 & 0 & 2 \\ 2 & -1 & 3 \\ 1 & 4 & 4 \end{pmatrix}.
# \end{align*}
# 
# ::::{dropdown} Solution
# 
# \begin{align*}
#     & \left( \begin{array}{ccc|ccc} 
#         1 & 0 & 2 & 1 & 0 & 0 \\ 
#         2 & -1 & 3 & 0 & 1 & 0 \\
#         1 & 4 & 4 & 0 & 0 & 1 
#     \end{array} \right)
#     \begin{array}{l} \\  R_2 - 2R_1 \\  R_3 - R_1 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc} 
#         1 & 0 & 2 & 1 & 0 & 0 \\ 
#         0 & -1 & -1 & -2 & 1 & 0 \\
#         0 & 4 & 2 & -1 & 0 & 1 
#     \end{array} \right)
#     \begin{array}{l}  -R_2 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc} 
#         1 & 0 & 2 & 1 & 0 & 0 \\ 
#         0 & 1 & 1 & 2 & -1 & 0 \\
#         0 & 4 & 2 & -1 & 0 & 1 
#     \end{array} \right)
#     \begin{array}{l} \\ \\  R_3 - 4R_2 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc} 
#         1 & 0 & 2 & 1 & 0 & 0 \\ 
#         0 & 1 & 1 & 2 & -1 & 0 \\
#         0 & 0 & -2 & -9 & 4 & 1 
#     \end{array} \right)
#     \begin{array}{l} \\ \\  -\frac{1}{2}R_3 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc} 
#         1 & 0 & 2 & 1 & 0 & 0 \\ 
#         0 & 1 & 1 & 2 & -1 & 0 \\
#         0 & 0 & 1 & \frac{9}{2} & -2 & -\frac{1}{2}
#     \end{array} \right)
#     \begin{array}{l}  R_1 - 2R_3 \\  R_2 - R_3 \\ \phantom{x} \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|ccc} 
#         1 & 0 & 0 & -8 & 4 & 1 \\ 
#         0 & 1 & 0 & -\frac{5}{2} & 1 & \frac{1}{2} \\
#         0 & 0 & 1 & \frac{9}{2} & -2 & - \frac{1}{2}
#     \end{array} \right).
# \end{align*} 
# So the inverse is $A^{-1}=\begin{pmatrix} -8 & 4 & 1 \\ -\frac{5}{2} & 1 & \frac{1}{2} \\ \frac{9}{2} & -2 & -\frac{1}{2} \end{pmatrix}$. Checking the answer
# \begin{align*}
#     A^{-1}A = 
#     \begin{pmatrix} 
#         -8 & 4 & 1 \\ 
#         -\frac{5}{2} & 1 & \frac{1}{2} \\
#         \frac{9}{2} & -2 & -\frac{1}{2} 
#     \end{pmatrix}
#     \begin{pmatrix}
#         1 & 0 & 2 \\ 
#         2 & -1 & 3 \\ 
#         1 & 4 & 4 
#     \end{pmatrix} = 
#     \begin{pmatrix} 
#         1 & 0 & 0 \\ 
#         0 & 1 & 0 \\ 
#         0 & 0 & 1 
#     \end{pmatrix} = I.
# \end{align*}
# ::::
# :::::
# 
# The calculation of a matrix inverse using Gauss-Jordan elimination is more efficient that using the adjoint-determinant formula when dealing with larger matrices (i.e., when $n > 3$) since the steps can be easily programmed into a computer and it does not require the calculation of determinants which can be computationally expensive.
# 
# ## Python code
# 
# The Python code below calculates the inverse of the matrix from [example 2.6](gje-inverse-example).

# In[2]:


# Form augmented matrix
A = Matrix([[1, 0, 2], [2, -1, 3], [1, 4, 4]])
AI = A.row_join(eye(3))

print("Augmented matrix")
display(AI)

# Row reduce augmented matrix
AI = AI.rref()[0]

print("RREF")
display(AI)

# Extract inverse matrix
invA = AI[:,3:]

print("Inverse matrix")
display(invA)

