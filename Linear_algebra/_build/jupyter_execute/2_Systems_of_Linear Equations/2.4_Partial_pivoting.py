#!/usr/bin/env python
# coding: utf-8

# (partial-pivoting-section)=
# # Partial pivoting
# 
# In most practical applications of row reduction to solve a linear system we use computers to perform the calculations. Computers use floating point numbers to compute arithmetic operations which are not exact and can be prone to rounding errors. Consider the following linear system of equations
# 
# \begin{align}
#   \begin{pmatrix}0.0001 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \end{pmatrix}= 
#   \begin{pmatrix}1 \\ 2 \end{pmatrix}.
# \end{align}
# 
# Using Gaussian elimination but rounding all calculations to 4 decimal place accuracy we have
# 
# \begin{align*}
#     & \left( \begin{array}{cc|c} 
#         0.0001 & 1 & 1 \\
#         1 & 1 & 2 
#     \end{array} \right)
#     \begin{array}{l} \\  R_2 - 1000R_1 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|c} 
#         0.0001 & 1 & 1 \\
#         0 & -9999 & -9998 
#     \end{array} \right)
#     \begin{array}{l} \\  -\frac{1}{9999}R_2 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|c} 
#         0.0001 & 1 & 1 \\
#         0 & 1 & 1.0000
#     \end{array} \right).
# \end{align*}
# 
# So $x_2= 1.000$ and using back substitution we have $x_1 = 0$. However, checking our solution with the original system we see that this does not satisfy the second equation $x_1 + x_2 = 2$. The problem is that our first pivot element of 0.0001 was small compared with the value below which produced large values when adding multiples of the pivot row to the other rows. 
# 
# To overcome this we can perform a row swap so that the pivot element is larger than the value below
# 
# \begin{align*}
#     & \left(\begin{array}{cc|c} 
#         0.0001 & 1 & 1 \\
#         1 & 1 & 2 
#     \end{array} \right)
#     \begin{array}{l} R_1 \leftrightarrow R_2 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|c} 
#         1 & 1 & 2 \\
#         0.0001 & 1 & 1 
#     \end{array} \right)
#     \begin{array}{l} \\  R_2 - 0.0001 R_1 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|c} 
#         1 & 1 & 2 \\
#         0 & 0.9999 & 0.9998
#     \end{array} \right)
# \end{align*}
# 
# So $x_2 = 1.000$ as before but using back substitution we now have $x_1 = 1.000$ which is consistent with the original system. This process is called *partial pivoting* and it's where we perform a row swap to ensure that the pivot element has a larger absolute value from the elements in the column beneath the pivot.
# 
# :::::{admonition} Definition: Gaussian elimination with partial pivoting
# :class: note
# :name: ge-pp-definition
# 
# To row reduce an $m \times n$ matrix $A$ to reduced row echelon form using Gauss-Jordan elimination with partial pivoting we do the following: 
# 
# 1. Initalise the pivot row to $i=1$ and pivot column to $k=1$
# 2. Swap the pivot row $i$ with the row below which has the largest absolute value element in the pivot column $k$ which is greater than the absolute value of the pivot element $|a_{ik}|$. 
# 3. If $a_{ik} = 0$ then set $k = k + 1$ and repeat step 2.
# 4. For each row $j = i+1 \ldots m$ beneath the pivot row subtract the pivot row $i$ multiplied by $\dfrac{a_{jk}}{a_{ik}}$ from row $j$. 
# 5. Set $i = 1 + 1$ and $k = k + 1$ and repeat steps 2 to 4 until $i > m$ or $k > n$.
# :::::
# 
# :::::{admonition} Example 2.5
# :class: seealso
# :name: partial-pivoting-example
# 
# Solve the system of linear equations using Gaussian elimination with partial pivoting. 
# 
# \begin{align*}
#     \begin{array}{rcl}
#         x_1 - x_2 + 3x_3 &=& 13, \\
#         4x_1 - 2x_2 + x_3 &=& 15, \\
#         -3x_1 - x_2 + 4x_3 &=& 8.
#     \end{array}
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
#     & \left(\begin{array}{ccc|c} 
#         1 & -1 & 3 & 13 \\
#         4 & -2 & 1 & 15\\
#         -3 & -1 & 4 & 8
#     \end{array} \right) 
#     \begin{array}{l} R_1 \leftrightarrow R_2 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         4 & -2 & 1 & 15\\ 
#         1 & -1 & 3 & 13 \\
#         -3 & -1 & 4 & 8
#     \end{array} \right)
#     \begin{array}{l} \\  R_2 - \frac{1}{4}R_1 \\[1pt]  R_3 + \frac{3}{4}R_1 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         4 & -2 & 1 & 15\\ 
#         0 & -\frac{1}{2} & \frac{11}{4} & \frac{37}{4} \\
#         0 & -\frac{5}{2} & \frac{19}{4} & \frac{77}{4}
#     \end{array} \right)
#     \begin{array}{l} \\ R_2 \leftrightarrow R_3 \\ \phantom{x} \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         4 & -2 & 1 & 15\\ 
#         0 & -\frac{5}{2} & \frac{19}{4} & \frac{77}{4} \\
#         0 & -\frac{1}{2} & \frac{11}{4} & \frac{37}{4}
#     \end{array} \right)
#     \begin{array}{l} \\ \\ R_3 - \frac{1}{5}R_2 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         4 & -2 & 1 & 15\\ 
#         0 & -\frac{5}{2} & \frac{19}{4} & \frac{77}{4} \\
#         0 & 0 & \frac{9}{5} & \frac{27}{5}
#     \end{array} \right)
#     \begin{array}{l} \\ \\ R_3 - \frac{1}{5}R_2 \end{array}
# \end{align*}
# Solving for $x_3$, $x_2$ and $x_1$ using back substitution
# \begin{align*}
#     x_3 &= \frac{5}{9}\left( \frac{27}{5} \right) = 3, \\
#     x_2 &= -\frac{2}{5} \left( \frac{77}{4} - \frac{19}{4}(3)\right) = -2, \\
#     x_1 &= \frac{1}{4}( 15 + 2(-2) - 3) = 2. 
# \end{align*}
#  
# ::::
# :::::
