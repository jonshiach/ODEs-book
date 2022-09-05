#!/usr/bin/env python
# coding: utf-8

# # Chapter summary
# 
# - [LU decomposition](lu-definition) factorises a square matrix in the product of a lower triangular matrix $L$ and an upper triangular matrix $U$.
# - [Crout's method](crouts-method-section) is used to solve a system of linear equations using LU decomposition by apply forward and back substitution.
# - [Partial pivoting](partial-pivoting-section) ensures that the pivot element has a larger absolute value than the elements in the column below the pivot. This eliminates the problems caused when the pivot element is small resulting in computational rounding errors;
# - [Cholesky decomposition](cholesky-definition) can be applied to factorise a [positive definite matrix](positive-definite-example) into the product of a lower triangular matrix $L$ and its transpose. Cholesky decomposition of a matrix requires fewer operations than the equivalent LU decomposition.
# - [QR decomposition](qr-section) can be applied to factorise an $m\times n$ matrix into the product of an [orthogonal matrix](orthogonal-matrix-definition) $Q$ and an upper triangular matrix $R$. 
# - QR decomposition can be calculated using the [Gram-Schmidt process](qr-gramschmidt-definition) where an orthonormal basis is determined by recursively subtracting the vector projection of non-orthogonal vectors onto known basis vectors.
# - QR decomposition can also be calculated using [Householder transformations](qr-householder-definition) which recursively applies a linear transformation to the columns of $A$ to reflect them onto the basis vectors $\mathbf{e}$.
# - QR decomposition can be used to calculate a solution to an overdetermined system when the number of equations is bigger than the number of unknowns.
# - The advantage of using decomposition methods for solving systems of linear equations is that a change in the constant values do not require a recalculation of the decomposition as opposed to Gaussian elimination.
