#!/usr/bin/env python
# coding: utf-8

# # Cramer's rule
# 
# **Cramer's rule** is an explicit rule for calculating the solution to a system of linear equations using determinants.
# 
# ::::{admonition} Theorem: Cramer's rule
# :class: important
# :name: cramers-rule-theorem
# 
# The solution to a non-singular linear system of equations of the form $A\mathbf{x}=\mathbf{b}$ can be calculated using Cramer's rule which is
# 
# :::{math}
# :label: cramers-rule-equation
# 
# x_i = \frac{\det(A_i)}{\det(A)},
# :::
# 
# where $A_i$ is a matrix obtained by replacing column $i$ of $A$ with $\mathbf{b}$.
# 
# ::::
# 
# **Proof**
# 
# *Consider the solution to the linear system $A\mathbf{x} = \mathbf{b}$ where $A$ is non-singular then the solution for the first variable $x_1$ is*
# 
# \begin{align*}
#     x_1 = \det 
#     \begin{pmatrix} 
#         x_1 & 0 & \cdots & 0 \\
#         x_2 & 1 & \cdots & 0 \\
#         \vdots & \vdots & \ddots & \vdots \\
#         x_n & 0 & \cdots & 1
#     \end{pmatrix} = \det(X_1).
# \end{align*}
# 
# *Since $\mathbf{x} = A^{-1}\mathbf{b}$ and $I = A^{-1}A$ then the matrix $X_1$ can be written as*
# 
# \begin{align*}
#     X_1 = \begin{pmatrix} A^{-1}\mathbf{b} & A^{-1} \mathbf{a}_2 & \cdots & A^{-1} \mathbf{a}_n \end{pmatrix},
# \end{align*}
# 
# *where $\mathbf{a}_i$ is the $i$th column of $A$. Since $A_1$ in equation {eq}`cramers-rule-equation` is $A_1 = \begin{pmatrix} \mathbf{b} & \mathbf{a}_2 & \cdots & \mathbf{a}_n \end{pmatrix}$ then $X_1 = A^{-1}A_1$. Using the property of determinant where the determinant of a product of two matrices is equal to the product of the determinants  then*
# 
# \begin{align*}
#     x_1 = \det(X_1) = \det(A^{-1}A_1) = \det(A^{-1})\det(A_1) = \frac{\det(A_1)}{\det(A)}.
# \end{align*}
# 
# *Doing similar for the other variables completes the proof.* <div style="text-align: right"> &#9633; </div>
# 
# 
# :::::{admonition} Example 2.3
# :class: seealso
# :name: cramers-rule-example
# 
# Solve the following systems of linear equations using Cramer's rule
# 
# ::::{grid}
# 
# :::{grid-item}
# (i) &emsp; $\begin{array}{rl}
#     3x_1 - 2x_2 &= -4, \\
#     x_1 - 3x_2 &= 1.
# \end{array}$
# :::
# 
# :::{grid-item}
# (ii) &emsp; $\begin{array}{rl}
#     -2x_1 - 3x_2 - x_3 &= -5, \\
#     -4x_1 + 4x_2 + 3x_3 &= -20, \\
#     -3x_1 &= -12.
# \end{array}$
# :::
# 
# ::::
# 
# ::::{dropdown} Solution
# 
# (i) $A = \begin{pmatrix} 3 & -2 \\ 1 & -3 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} -4 \\ 1 \end{pmatrix}$
# 
# \begin{align*}
#     x_1 &= \frac{
#     \begin{vmatrix} -4 & -2 \\ 1 & -3 \end{vmatrix}}
#     {\begin{vmatrix} 3 & -2 \\ 1 & -3 \end{vmatrix}} = \frac{14}{-7} = -2,  \\
#     \\
#     x_2 &= \frac{\begin{vmatrix} 3 & -4 \\ 1 & 1 \end{vmatrix}}{-7} = 
#     \frac{7}{-7} = -1.
# \end{align*}
# 
# Check solution:
# 
# \begin{align*}
#     A\mathbf{x} = \begin{pmatrix} 3 & -2 \\ 1 & -3 \end{pmatrix}
#     \begin{pmatrix} -2 \\ -1 \end{pmatrix} =
#     \begin{pmatrix} -4 \\ 1 \end{pmatrix} = \mathbf{b}.
# \end{align*}
# 
# (ii) $A = \begin{pmatrix} -2 & -3 & -1 \\ -4 & 4 & 3 \\ -3 & 0 & 0 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} -5 \\ -20 \\ -12 \end{pmatrix}$
# 
# \begin{align*}
#     x_1 &= \frac{
#     \begin{vmatrix}-5 & -3 & -1 \\ -20 & 4 & 3 \\ -12 & 0 & 0 \end{vmatrix}}
#     {\begin{vmatrix} -2 & -3 & -1 \\ -4 & 4 & 3 \\ -3 & 0 & 0 \end{vmatrix}}
#     = \frac{-12
#     \begin{vmatrix} -3 & -1 \\ 4 & 3 \end{vmatrix}}
#     {-3\begin{vmatrix} -3 & -1 \\ 4 & 3 \end{vmatrix}} \\
#     &= \frac{-12(-5)}{-3(-5)} = \frac{60}{15} = 4,\\ \\
#     x_2 &= \frac{
#     \begin{vmatrix} -2 & -5 & -1 \\ -4 & -20 & 3 \\ -3 & -12 & 0 \end{vmatrix}}{15} 
#     = \frac{-\begin{vmatrix} -4 & -20 \\ -3 & -12 \end{vmatrix} 
#     - 3\begin{vmatrix}-2 & -5 \\ -3 & -12 \end{vmatrix}}{15}  \\
#     &= \frac{12 - 3(9)}{15} = \frac{-15}{15} = -1, \\ \\
#     x_3 &= \frac{
#     \begin{vmatrix} -2 & -3 & - 5 \\ -4 & 4 & -20 \\ -3 & 0 & -12 \end{vmatrix}}{15}
#     =\frac{-3\begin{vmatrix} -3 & -5 \\ 4 & -20 \end{vmatrix} - 
#     12\begin{vmatrix} -2 & -3 \\ -4 & 4 \end{vmatrix}}{15} \\
#     & = \frac{-3(80) - 12(-20)}{15} = \frac{0}{15} = 0.
# \end{align*}
# 
# Check solution:
# 
# \begin{align*}
#     A\mathbf{x} = 
#     \begin{pmatrix} -2 & -3 & -1 \\ -4 & 4 & 3 \\ -3 & 0 & 0 \end{pmatrix}
#     \begin{pmatrix} 4 \\ -1 \\ 0 \end{pmatrix} =
#     \begin{pmatrix} -5 \\ -20 \\ -12 \end{pmatrix} = \mathbf{b}.
# \end{align*}
# 
# ::::
# 
# :::::
