#!/usr/bin/env python
# coding: utf-8

# # Chapter summary
# 
# - Indirect methods use an iterative approach to improve an estimate of the solution to a system of linear equations. The methods are iterated until the estimates have achieved the required accuracy.
# - The [Jacobi method](jacobi-method-section) is uses information from the previous iteration only to update the estimates.
# - The [Gauss-Seidel method](gauss-seidel-method-section) uses values of estimates already calculated in a given iteration to update the estimates. This means that the Gauss-Seidel method will converge to a solution faster than the Jacobi method.
# - An indirect method will [converge](convergence-of-indirect-methods-section) to the exact solution if the value of the spectral radius (the largest absolute eigenvalue) of the iteration matrix for a linear system is less than 1. 
# - The smaller the value of the spectral radius, the faster the method will converge to the exact solution.
# - The [SOR method](sor-method-section) uses a relaxation parameter to adjust how much estimates will change over a single iteration. The value of the relaxation parameter is chosen to minimise the spectral radius.
