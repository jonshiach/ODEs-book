#!/usr/bin/env python
# coding: utf-8

# # Chapter summary
# 
# - A [two-point boundary value problem](bvp-definition) is defined by a second-order ODE where the solutions at the lower and upper boundaries are known.
# - A boundary value problem can have a unique solution, an infinitely number of solutions or no solutions.
# - The [shooting method](shooting-method-section) uses a guess of the value for $y'(0)$ and adjusts the guess by comparing the computed solution at the upper boundary to the known solution.
# - The [Secant method](secant-method-section) is used to calculate improved estimates of the guess value.
# - The [finite-difference method](finite-difference-method-section) uses finite-difference approximations of the derivatives in the ODE to derive a linear system of equations that approximates the solution to the boundary value problem.
# - The higher the order of the finite-difference approximations, the higher the value of $h$ can be to achieve the same accuracy.
