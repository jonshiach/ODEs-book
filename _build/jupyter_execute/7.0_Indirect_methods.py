#!/usr/bin/env python
# coding: utf-8

# (indirect-methods-chapter)=
# # 7. Indirect Methods
# 
# **Learning outcomes**
# 
# On successful completion of this chapter readers will be able to:
# 
#    - understand the concept of an indirect method when used to solve a system of linear equations;
#    - apply the Jacobi, Gauss-Seidel and SOR methods to solve a linear system;
#    - use the residual to determine the accuracy of the current estimate of the solution to the linear system;
#    - determine whether an indirect method is convergent for a particular linear system and analyse the theoretical rate of convergence for indirect methods.
# 
# ## Indirect methods
# 
# Indirect methods for solving systems of linear equations use an iterative approach to repeatedly update estimates of the exact solution to the linear system. They are called **indirect methods** since multiple applications of the method is required to calculate a solution unlike [direct methods](direct-methods-chapter) such as Gaussian elimination and LU decomposition which require a single application to calculate the solution. However, direct methods are inefficient for large systems of equations for which we tend to use indirect methods instead. 
# 
# An indirect method for solving a system of linear equations of the form $A \mathbf{x}= \mathbf{b}$ is
# 
# ```{math}
# :label: iteration-matrix-equation
# 
# \mathbf{x}^{(k+1)} =T\mathbf{x}^{(k)} + \mathbf{c},
# ```
# 
# where $\mathbf{x}^{(k)}$ and $\mathbf{x}^{(k+1)}$ are the current and improved estimates of $\mathbf{x}$, $T$ is an **iteration matrix** and $\mathbf{c}$ is some vector. This equation is iterated updating the values of the estimates such that $\mathbf{x}^{(k)} \to \mathbf{x}$ as $k\to \infty$. Note that unlike direct methods which will calculate the exact solution, indirect only calculate an estimate (albeit very close) of the exact solution.
