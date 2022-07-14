#!/usr/bin/env python
# coding: utf-8

# # Chapter summary
# 
# - A numerical method is [stable](stability-definition) if the local truncation errors do not increase from one step to the next.
# - A system of ODEs is [stiff](stiffness-section) if it requires a numerical method to use a small step length in order to remain stable.
# - If the [stiffness ratio](stiffness-ratio-definition) which is the ratio of the largest to smallest eigenvalues of the coefficient matrix of a system of ODEs is *large* then the system is considered to be stiff. 
# - The stability of a method is analysed by considering the simple test equation $y' =\lambda y$.
# - The [stability function](stability-function-definition) of a method is the amount by which the solution to the test equation changes over a single step of length.
# - A numerical method is [absolutely stable](stability-function-definition) is the absolute value of the stability function is less than 1.
# - The [region of absolute stability](region-of-absolute-stability-definition) is the set of all values in the complex plane where a numerical method is absolutely stable.
# - The [interval of absolute stability](interval-of-absolute-stability-definition) is the range of values of $z = h \lambda$ for which a numerical method is absolutely stable.
# - The [stability function of an explicit Runge-Kutta method](erk-rz-section) is a polynomial function of $z$ the coefficients of which are calculated using the values of $a_{ij$ and $b_i$.
# - The order of an explicit Runge-Kutta method can be found by determining the highest order term in the stability function that is the same as the series expansion of $e^z$.
# - The stability function for [implicit methods](implicit-rz-section) are a fraction of two polynomial functions of $z$.
# - Implicit methods can be [A-stable](a-stability-definition) which means the region of absolute stability contains the whole left-hand side of the complex plane meaning that there is no limit placed on the value of the step length for a method to remain stable.
