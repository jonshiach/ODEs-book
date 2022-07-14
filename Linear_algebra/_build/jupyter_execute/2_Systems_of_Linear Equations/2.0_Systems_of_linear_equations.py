#!/usr/bin/env python
# coding: utf-8

# (systems-of-linear-equations-chapter)=
# # Systems of Linear Equations
# 
# **Learning outcomes**
# 
# On successful completion of this chapters students will be able to:
# 
# - [define a linear system of equations](system-of-linear-equation-definition) and write them as a matrix equation;
# - calculate the solution to a system of linear equations using the [inverse matrix](solution-using-inverse-matrix-theorem) and [Cramer's rule](cramers-rule-theorem);
# - use [Gaussian elimination](ge-definition) to row reduce a matrix to [row echelon form](ref-definition) and calculate the solution to a linear system of equations using back substitution;
# - use [partial pivoting](ge-pp-definition) to reduce the risk of rounding errors whilst performing Gaussian elimination;
# - use [Gauss-Jordan elimination](gje-definition) to row reduce a matrix to [reduced row echelon form](rref-definition) and use it to solver a system of linear equations
# - use Gauss-Jordan elimination to calculate the [inverse of a matrix](gj-matrix-inverse-section);
# - identity when a system of linear equations is [consistent](consistent-system-theorem), [inconsistent](inconsistent-system-theorem) or [indeterminate](indeterminate-system-theorem);
# - solve a [homogeneous system of linear equations](homogeneous-system-definition).
# 
# ---
# ## Definition
# 
# 
# ::::{admonition} Definition: System of linear equations
# :class: note
# :name: system-of-linear-equation-definition
# 
# A **system of linear equations** is a collection of one or more linear equations expressed using the same set of variables. For example,
# 
# \begin{align*}
#     a_{11} x_1+a_{12} x_2+\cdots +a_{1n}x_n &=b_1, \\
#     a_{21} x_1+a_{22} x_2+\cdots+a_{2n}x_n &=b_2, \\
#     &\vdots \\
#     a_{m1} x_1+a_{m2} x_2+\cdots+a_{mn}x_n &=b_m,
# \end{align*}
# where $x_1, x_2, \ldots, x_n$ are **variables**, $a_{11}, a_{12}, \ldots, a_{mn}$ are **coefficients** and $b_1, b_2, \ldots, b_n$ are **constant** terms.
# ::::
# 
# In general we would know the values of $a_{ij}$ and $b_i$ and we would like to find out what the values of $x_i$ are.
# 
# Linear systems are often represented using the matrix notation $A \mathbf{x} = \mathbf{b}$, where $A$ is an $m \times n$ matrix containing the coefficient terms known as the **coefficient matrix**, $\mathbf{x}$ is a $m \times 1$ matrix containing the variables known as the **variable vector** and $\mathbf{b}$ is a $m \times 1$ matrix containing the constant terms known as the **constant vector** (vectors are introduced in [here](vectors-chapter) but for now simply consider them as matrices with a single column), i.e.,
# 
# \begin{align*}
#     \begin{array}{cccc}
#         A & \mathbf{x} & = & \mathbf{b} \\[4pt]
#         \underbrace{\begin{pmatrix} 
#             a_{11} & a_{12} & \cdots & a_{1n} \\
#             a_{21} & a_{22} & \cdots & a_{2n} \\
#             \vdots & \vdots & \ddots & \vdots \\
#             a_{m1} & a_{m2} & \cdots & a_{mn}
#         \end{pmatrix}}_{\text{coefficient matrix}} &
#         \underbrace{
#             \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}
#         }_{\text{variable vector}} & = &
#         \underbrace{
#             \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_m \end{pmatrix}
#         }_{\text{constant vector}}
#     \end{array}
# \end{align*}
# 
# :::::{admonition} Example 2.1
# :class: seealso
# :name: system-of-linear-equations-matrix-form-example
# 
# Write the following linear system of equations as a matrix equation
# \begin{align*}
#     2x_1 + x_2 &= 4, \\
#     4x_1 + 3x_2 &= 10.
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
#     \begin{pmatrix} 
#         2 & 1 \\ 
#         4 & 3 
#     \end{pmatrix}
#     \begin{pmatrix}
#         x_1 \\ x_2 
#     \end{pmatrix} = 
#     \begin{pmatrix} 
#         4 \\ 10 
#     \end{pmatrix}.
# \end{align*}
# ::::
# :::::
# 
# (solving-linear-systems-using-algebra-section)=
# ## Solving linear systems using algebra
# 
# One way which we can solve systems of linear equations is using simple algebra. The usual approach is to try to solve for each unknown in turn by eliminating all of the other unknowns. For example, consider the linear system of equations from [example 2.1](system-of-linear-equations-matrix-form-example)
# 
# \begin{align*}
#     2x_1 + x_2 &= 4, \\
#     4x_1 + 3x_2 &= 10.
# \end{align*}
# 
# we could eliminate $x_2$ be subtracting 3 times the first equation from the second to give
# 
# $$ -2 x_1 = -2,$$
# 
# which is easily solved to give $x_1 = 1$. Now that we know the value of $x_1$ we can substitute it into any equation in the system to give $x_2$. Substituting $x_1 = 1$ into the first equation gives
# 
# $$ 2(1) + x_2 = 4, $$
# 
# so $x_2 = 2$. The solution should satisfy all equations in the system to checking that it also satisfies the second equation
# 
# $$ 4(1) + 3(2) = 10, $$
# 
# so we know that $x_1 = 1$ and $x_2 = 2$ is the solution. Whilst this approach is simple to implement for small systems of linear equations the algebra will soon become unwieldy for larger systems which is why we use the methods that are covered in this chapter.
