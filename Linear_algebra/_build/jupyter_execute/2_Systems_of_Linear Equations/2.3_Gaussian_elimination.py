#!/usr/bin/env python
# coding: utf-8

# (gaussian-elimination-section)=
# # Gaussian elimination
# 
# **Gaussian elimination (GE)** is an algorithm for solving systems of linear equations. It is the most common method used in practice since it can by easily programmed into a computer and applied to larger systems. Consider the following method for solving a linear system of three equations in three unknowns:
# 
# \begin{align*}
#     3x_1 + x_2 - 2x_3 &= 1, \\
#     x_1 - x_2 + 2x_3 &= 3, \\
#     2x_1 - 3x_2 + 7x_3 &= 4.
# \end{align*}
# 
# Swap the first two equations around
# 
# \begin{align*} 
#     x_1 - x_2 + 2x_3 &= 3, \\
#     3x_1 + x_2 - 2x_3 &= 1, \\
#     2x_1 - 3x_2 + 7x_3 &= 4.
# \end{align*}
# 
# Subtract 3 times the first equation from the second equation and 2 times the first equation from the third equation
# 
# \begin{align*} 
#     x_1 - x_2 + 2x_3 &= 3, \\
#     4x_2 - 8x_3 &= -8, \\
#     - x_2 + 3x_3 &= -2.
# \end{align*}
# 
# Multiply the second equation by $\frac{1}{4}$
# 
# \begin{align*} 
#     x_1 - x_2 + 2x_3 &= 3, \\
#     x_2 - 2 x_3 &= -2, \\
#     - x_2 + 3x_3 &= -2.
# \end{align*}
# 
# Add the first equation to the second
# 
# \begin{align*} 
#     x_1 - x_2 + 2x_3 &= 3, \\
#     x_2 - 2 x_3 &= -2, \\
#     x_3 &= -4.
# \end{align*}
# 
# Here the third equation gives the solution to $x_3=-4$. We can substitute the value of $x_3$ into the other two to find the solutions of $x_2$ and $x_1$
# 
# \begin{align*}
#     x_2 - 2(-4) &= -2 &
#     \therefore x_2 &= -10, \\
#     x_1 - (-10) + 2(-4) &= 3 &
#     \therefore x_1 &= 1.
# \end{align*} 
# 
# In this method, we used three types of operations on the equations in the system. These operations are known as **Elementary Row Operations (EROs)**.
# 
# ::::{admonition} Definition: Elementary Row Operations (EROs)
# :class: note
# :name: ero-definition
# 
# The three operations that can be applied to a linear system of equations without changing the solution are
# 
# - Type I: swap any two rows of the system;
# - Type II: multiply one row by a non-zero scalar;
# - Type III: replace a single row by itself plus a multiple of another row.
# ::::
# 
# In the solution to the linear system of equations shown above we used a type I row operation in step 1, a type II row operation in step 3 and type III row operations in steps 2 and 4.
# 
# We can represent the linear system using matrices for convenience. We begin by expressing the linear system using an augmented matrix consisting of the concatenation of $A$ and $\mathbf{x}$ so any EROs that are applied to the augmented matrix are applied to the coefficients and the constant terms at the same time.
# 
# ::::{admonition} Definition: Augemented matrix
# :class: note
# :name: augmented-matrix-definition
# 
# The **augmented matrix** is a representation of a system of linear equations $A\mathbf{x}=\mathbf{b}$ such that the $m\times n$ coefficient matrix $A$ and right-hand side constant vector $\mathbf{b}$ are combined into a single $m\times (n+1)$ matrix $(A \mid \mathbf{b})$. 
# ::::
# 
# When writing the augmented matrix we often draw a partition separating $A$ and $\mathbf{b}$ (although this is not strictly necessary), i.e.,
# 
# \begin{align*}
#     \left(
#     \begin{array}{cccc|c}
#         a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\
#         a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\
#         \vdots & \vdots & \ddots & \vdots & \vdots \\
#         a_{m1} & a_{m2} & \cdots & a_{mn} & b_n
#     \end{array}
#     \right).
# \end{align*}
# 
# Elementary row operations are applied to the augmented matrix so that we reduce it to what is known as row echelon form where the solution of the system can be easily calculated. 
# 
# ::::{admonition} Definition: Row Echelon Form (REF)
# :class: note
# :name: ref-definition
# 
# A matrix is said to be in **Row Echelon Form (REF)** if the following conditions are satisfied:
# 
# - any non-zero rows are above any all-zero rows;
# - in each non-zero row, with the exception of the first row, the **pivot element** (the first non-zero element in the row) is to the right of the pivot element in the row above;
# ::::
# 
# For example, the following matrices are in row echelon form and the red numbers are the pivot elements
# 
# \begin{align*}
#     &\begin{pmatrix} \color{red}{1} & 2 \\ 0 & \color{red}{3} \end{pmatrix}, &
#     &\begin{pmatrix} \color{red}{1} & 2 & 3 \\ 0 & 0 & \color{red}{4} \end{pmatrix}, &
#     &\begin{pmatrix} 0 & \color{red}{1} & 3\\ 0 & 0 & \color{red}{4} \\ 0 & 0 & 0\end{pmatrix}.
# \end{align*}
# 
# Note that the elements below the pivot elements are all zero.
# 
# ## Row reduction
# 
# The process of transforming a matrix into row echelon form using elementary row operations is known as **row reduction**. For example, we will use Gaussian elimination to solve the following system of linear equations
# 
# \begin{align*}
#     3x_1 + x_2 - 2x_3 &= 1, \\
#     x_1 - x_2 + 2x_3 &= 3, \\
#     2x_1 - 3x_2 + 7x_3 &= 4.
# \end{align*}
# 
# Expressing this using an augmented matrix, we have
# 
# \begin{align*}
#     \left( \begin{array}{ccc|c}
#         \color{red}{3} & 1 & -2 & 1 \\
#         \color{blue}{1} & -1 & 2 & 3 \\
#         \color{blue}{2} & -3 & 7 & 4
#     \end{array} \right) .
# \end{align*}
# 
# The first pivot element is in row 1 column 1 which has a value of 3. We need to apply row operations so that the elements in the column beneath the pivot element are zero. To do so we add a multiple of the pivot row to each of the rows beneath (a [type III](ero-definition) row operation). Since the pivot element is 3 and the first non-zero element in row 2 is 1, to reduce this to zero we subtract row 1 multiplied by $\frac{1}{3}$ from row 2.
# 
# \begin{align*}
#     \left( \begin{array}{ccc|c}
#         \color{red}{ 3} & 1 & -2 & 1 \\
#         \color{blue}{ 1 - \frac{1}{3}(3)} & -1 - \frac{1}{3}(1) & 2 - \frac{1}{3}(-2) & 3 - \frac{1}{3}(1) \\
#         \color{blue}{ 2} & -3 & 7 & 4
#     \end{array} \right) &
#     \longrightarrow
#     \left( \begin{array}{ccc|c}
#         \color{red}{ 3} & 1 & -2 & 1 \\
#         \color{blue}{ 0} & -\frac{4}{3} & \frac{8}{3} & \frac{8}{3} \\
#         \color{blue}{ 2} & -3 & 7 & 4
#     \end{array} \right) .
# \end{align*}
# 
# We also need to do the same to row 3. Since the element row 3 column 1 has a value of 2, we need to subtract row 1 multiplied by $\frac{2}{3}$ from row 3. 
# 
# \begin{align*}
#     \left( \begin{array}{ccc|c}
#         \color{red}{3} & 1 & -2 & 1 \\
#         \color{blue}{0} & -\frac{4}{3} & \frac{8}{3} & \frac{8}{3} \\
#         \color{blue}{2 - \frac{2}{3}(3)} & -3 - \frac{2}{3}(1) & 7 - \frac{2}{3}(-2) & 4 - \frac{2}{3}(1)
#     \end{array} \right) 
#     \longrightarrow  
#     \left( \begin{array}{ccc|c}
#         \color{red}{3} & 1 & -2 & 1 \\
#         \color{blue}{0} & -\frac{4}{3} & \frac{8}{3} & \frac{8}{3} \\
#         \color{blue}{0} & -\frac{11}{3} & \frac{25}{3} & \frac{10}{3}
#     \end{array} \right) .
# \end{align*}
# 
# Note that these two row operations could have been done simultaneously since changing the values in row 2 does not affect row 3 and vice-versa. Column 1 is now in row echelon form so we move to the next pivot element in row 2 which is $-\frac{4}{3}$.
# 
# \begin{align*}
#     \left( \begin{array}{ccc|c}
#         3 & 1 & -2 & 1 \\
#         0 & \color{red}{-\frac{4}{3}} & \frac{8}{3} & \frac{8}{3} \\
#         0 & \color{blue}{-\frac{11}{3}} & \frac{25}{3} & \frac{10}{3}
#     \end{array} \right) .
# \end{align*}
# 
# The element in row 3 column 2 has a value of $-\frac{11}{3}$ and the pivot element has a value of $-\frac{4}{3}$ so we need to subtract row 2 multiplied by $-\frac{11}{3} / -\frac{4}{3} = \frac{11}{4}$ from row 3.
# 
# \begin{align*}
#     \left( \begin{array}{ccc|c}
#         3 & 1 & -2 & 1 \\
#         0 & \color{red}{-\frac{4}{3}} & \frac{8}{3} & \frac{8}{3} \\
#         0 & \color{blue}{-\frac{11}{3} + \frac{11}{4}(-\frac{4}{3})} & \frac{25}{3} + \frac{11}{4}(\frac{8}{3}) & \frac{10}{3} +\frac{11}{4}(\frac{8}{3})
#     \end{array} \right) 
#     \longrightarrow
#     \left( \begin{array}{ccc|c}
#         3 & 1 & -2 & 1 \\
#         0 & \color{red}{-\frac{4}{3}} & \frac{8}{3} & \frac{8}{3} \\
#         0 & \color{blue}{0} & 1 & -4
#     \end{array} \right) .
# \end{align*}
# 
# Now the augmented matrix is in row echelon form. We can convert back to matrix form and express the linear system as three separate equations.
# \begin{align*}
#     \begin{pmatrix} 
#         3 & 1 & -2 \\
#         0 & -\frac{4}{3} & \frac{8}{3} \\
#         0 & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} &= \
#     \begin{pmatrix} 1 \\ \frac{8}{3} \\ -4 \end{pmatrix}  
#     \implies
#     \begin{array}{rcl}
#         3x_1 + x_2 - 2x_3 &=& 1, \\
#         -\frac{4}{3} x_2 - \frac{8}{3} x_3 &=& \frac{8}{3}, \\
#         x_3 &=& -4.
#     \end{array}
# \end{align*}
# 
# Since we have reduced the coefficient matrix to row echelon form we have a solution for the final variable. We can then substitute known values of the variables into the preceding equation to solve for the preceding variable. We continue in this way until we have solutions for all of the variables in the system. This step is known as **back substitution**. So for our system the final equation gives $x_3=-4$ so substitution into the second equation gives
# 
# \begin{align*}
#     -\frac{4}{3} x_2 + \frac{8}{3} (-4) &= \frac{8}{3} \\
#     -\frac{4}{3} x_2 &= \frac{40}{3} \\
#     \therefore x_2 &= -10,
# \end{align*}
# 
# and substituting $x_2$ and $x_3$ into the first equation gives
# 
# \begin{align*}
#     3x_1 + (-10) - 2(-4) &= 1 \\
#     3x_1 &= 3 \\
#     \therefore x_1 &= 1.
# \end{align*}
# 
# In the interest of brevity, the following notation is used to denote the three types of EROs
# 
# -  Type I: swap row $i$ and row $j$: $R_i \leftrightarrow R_j$ ;
# -  Type II: multiply row $i$ by the non-zero scalar $k$: $kR_i$;
# -  Type III: add $k$ times row $j$ to row $i$:  $R_i + kR_j$.
# 
# Since the EROs do not change the solution to the system of equations, it does not matter which EROs are applied to row reduce the augmented matrix. A common approach is to ensure the pivot elements have a value of 1 which can decrease the number of fractional values thus simplifying the calculations. For example, consider the following row reduction of the same augmented matrix as before.
# 
# \begin{align*}
#     & \left( \begin{array}{ccc|c}
#         3 & 1 & -2 & 1 \\
#         1 & -1 & 2 & 3 \\
#         2 & -3 & 7 & 4
#     \end{array} \right)
#     \begin{array}{l} R_1 \leftrightarrow R_2 \\ \phantom{x} \\ \phantom{x} \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & -1 & 2 & 3 \\
#         3 & 1 & -2 & 1 \\
#         2 & -3 & 7 & 4
#     \end{array} \right) 
#     \begin{array}{l} \\ R_2 - 3 R_1 \\ R_3 - 2 R_1 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & -1 & 2 & 3 \\
#         0 & 4 & -8 & -8 \\
#         0 & -1 & 3 & -2
#     \end{array} \right) 
#     \begin{array}{l} \\ \dfrac{1}{4}R_2 \\ \phantom{x} \end{array}  \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & -1 & 2 & 3 \\
#         0 & 1 & -2 & -2 \\
#         0 & -1 & 3 & -2
#     \end{array} \right) 
#     \begin{array}{l} \\ \\ R_3 + R_2 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & -1 & 2 & 3 \\
#         0 & 1 & -2 & -2 \\
#         0 & 0 & 1 & -4
#     \end{array} \right)
# \end{align*}
# 
# Solving using back substitution gives $x_1 = 1$, $x_2 = -10$ and $x_3 = -4$ which was the same solution as we saw before.
# 
# :::::{admonition} Definition: Gaussian elimination
# :class: note
# :name: ge-definition
# 
# To row reduce an $m \times n$ matrix $A$ to reduced row echelon form using Gaussian elimnation we do the following: 
# 
# 1. Initalise the pivot row to $i=1$ and pivot column to $k=1$ 
# 2. If $a_{ik} = 0$ perform a row swap with a row beneath the pivot row $i$ with a non-zero element in the pivot column $k$. If no such rows exist set $k = k + 1$ and repeat step 2.
# 3. For each row $j = i+1 \ldots m$ beneath the pivot row subtract the pivot row $i$ multiplied by $\dfrac{a_{jk}}{a_{ik}}$ from row $j$. 
# 4. Set $i = 1 + 1$ and $k = k + 1$ and repeat steps 2 and 3 until $i > m$ or $k > n$.
# :::::
# 
# :::::{admonition} Example 2.4
# :class: seealso
# :name: ge-example
# 
# Use Gaussian-elimination to solve the following systems of linear equations:
# 
# ::::{grid}
# 
# :::{grid-item}
# (i) &emsp; $\begin{array}{rl}
#     x_1 + 2x_2 &= 7, \\ 
#     3x_1 - 4x_2 &= 1.
#     \end{array}$
# :::
# 
# :::{grid-item}
# (ii) &emsp; $\begin{array}{rl}
#     x_1 + x_3 &= 3, \\ 
#     -2x_1 + x_2 + 3x_3 &= 3, \\
#     -x_1 + 2x_2 + 4x_3 &= 5.
#     \end{array}$
# :::
# 
# ::::
# 
# ::::{dropdown} Solution
# 
# (i) 
# \begin{align*}
#     & \left( \begin{array}{cc|c} 1 & 2 & 7 \\ 3 & -4 & 1 \end{array} \right)
#     \begin{array}{l} \\ R_2 - 3R_1 \end{array} &
#     \longrightarrow \quad &
#     & \left( \begin{array}{cc|c} 1 & 2 & 7 \\ 0 & -10 & -20 \end{array} \right)
# \end{align*}
# 
# Solving for $x_1$ and $x_2$ using back substitution
# 
# \begin{align*}
#     -10x_2 &= -20 & \therefore x_2 &= \frac{-20}{-10} = 2, \\
#     x_1 + 2x_2 &= 7 & \therefore x_1 &= 7 - 2x_2 = 7 - 2(2) = 3.
# \end{align*}
# 
# This solution can be easily verified by substituting it back into the original system.
# 
# (ii) 
# \begin{align*}
#     & \left( \begin{array}{ccc|c}
#         1 & 0 & 1 & 3 \\
#         -2 & 1 & 3 & 3 \\
#         -1 & 2 & 4 & 5
#     \end{array} \right)
#     \begin{array}{l} \\ R_2 + 2R_1 \\ R_3 + R_1 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & 1 & 3 \\
#         0 & 1 & 5 & 9 \\
#         0 & 2 & 5 & 8
#     \end{array} \right)
#     \begin{array}{l} \\ \\ R_3 - 2R_2 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         1 & 0 & 1 & 3 \\
#         0 & 1 & 5 & 9 \\
#         0 & 0 & -5 & -10
#     \end{array} \right)
# \end{align*}
# 
# Solving for $x_1$, $x_2$ and $x_3$ using back substitution
# 
# \begin{align*}
#     -5x_3 &= -10 & \therefore x_3 &= \frac{-10}{-5} = 2, \\
#     x_2 + 5x_3 &= 9 & \therefore x_2 &= 9 - 5x_3 = 9 - 5(2) = -1, \\
#     x_1 + x_3 &= 3 & \therefore x_1 &= 3 - x_3 = 3 - 2 = 1.
# \end{align*}
# ::::
# :::::
