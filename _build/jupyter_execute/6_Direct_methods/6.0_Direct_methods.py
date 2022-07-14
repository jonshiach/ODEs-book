#!/usr/bin/env python
# coding: utf-8

# (direct-methods-chapter)=
# # Direct Methods
# 
# **Learning outcomes**
# 
# On successful completion of this chapter readers will be able to:
# 
# -  apply [LU decomposition](lu-definition) to factorise a square matrix into a product of a lower triangular and upper triangular matrices.
# -  apply [Crout's method](crouts-method-section) for solving a system of linear equations using LU decomposition;
# -  solve a system of linear equations using [LU decomposition with partial pivoting](partial-pivoting-section);
# -  apply [Cholesky decomposition](cholesky-definition) to factorise a positive definite matrix into a product of a lower triangular matrix and its transpose;
# -  solve a system of linear equations using the [Cholesky-Crout method](cholesky-crout-method-section);
# -  apply [QR decomposition](qr-section) to factorise an $m\times n$ matrix into the product of an orthogonal matrix and an upper triangular matrix using the [Gram-Schmidt process](qr-gramschmidt-definition) and [Householder transformations](qr-householder-definition);
# -  Solve a [system of linear equations using QR decomposition](qr-crout-section). 
# 
# ---
# ## Systems of linear equations
# 
# [Systems of linear equations](https://en.wikipedia.org/wiki/System_of_linear_equations) appear often in the topics of numerical analysis and numerical solutions to differential equations. Examples include the solution of the [stage values of an implicit Runge-Kutta method](solving-ivps-using-irk-methods-section) and the solution to a boundary value problem using the [finite-difference method](finite-difference-method-section). The methods that are applied to solve systems of linear equations fall into one of two categories: **direct methods** that use an algebraic approach and [**indirect methods**](indirect-methods-chapter) that use an iterative approach. On this chapter we will look at some common direct methods.
# 
# A system of linear equations with $m$ equations and $n$ unknowns is expressed as
# 
# \begin{align*}
#     a_{11} x_1 +a_{12} x_2 +\cdots +a_{1n} x_n &=b_1 ,\\
#     a_{21} x_1 +a_{22} x_2 +\cdots +a_{2n} x_n &=b_2 ,\\
#     &\vdots \\
#     a_{m1} x_1 +a_{m2} x_2 +\cdots +a_{mn} x_n &=b_n ,
# \end{align*}
# 
# where $x_i$ are the unknown variables, $a_{ij}$ are coefficients and $b_i$ are constant terms. It is often more convenient to express a system of linear equations as a matrix equation 
# 
# \begin{align*}
#     A \mathbf{x} = \mathbf{b},
# \end{align*}
# where $A$ is the **coefficient matrix**, $\mathbf{x}$ is the **variable vector** and $b$ is the **constant vector**
# 
# \begin{align*}
#     A &= \begin{pmatrix}
#         a_{11}  & a_{12}  & \cdots  & a_{1n} \\
#         a_{21}  & a_{22}  & \cdots  & a_{2n} \\
#         \vdots  & \vdots  & \ddots  & \vdots \\
#         a_{m1}  & a_{m2}  & \cdots  & a_{mn} 
#     \end{pmatrix},& 
#     \mathbf{x} &= \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_m \end{pmatrix}, &
#     \mathbf{b} &= \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_m \end{pmatrix}.
# \end{align*}
# 
# The solution (if it exists) is the vector $\mathbf{x}$ for which the equation $A\mathbf{x} = \mathbf{b}$ is satisfied. The solution to a linear system may be one of the following
# 
# - The system has infinitely many solutions. This usually occurs when the number of unknown variables exceeds the number of equations in the system.
# - The system has a single unique solution.
# - The system has no solution. This usually occurs where one equation in the system contradicts another such that not value of the variables could satisfy both.
