#!/usr/bin/env python
# coding: utf-8

# # Initial Value Problems Chapter Summary
# 
# - An [Initial Value Problem (IVP)](ivp-definition) is expressed as an ODE where the solution at the lower bound of the domain is known.
# - The [Euler method](euler-method-definition) is derived by truncating the [Taylor series](taylor-series-definition) after the first-order term. It advances the solution over a small step of length $h$ using known values of $t_n$ and $y_n$ to calculate the solution at $y_{n+1} =y(t_n +h)$.
# - The [Local Truncation Error](lte-definition) is the error accrued by a method over a single step assuming the solution at the start of the step is known to be exact.
# - The [Global Truncation Error](gte-definition) is the error accrued over all previous steps of a method assuming the initial solution is known to be exact.
# - The global truncation error for an $n$th order method is $O(h^{n})$ which means as $h$ tends to zero, the error will tend to zero at least as fast as $h^n$.
# - The [Euler method](euler-method-definition) is first-order accurate so the solutions tend to be inaccurate unless using a very small value of the step length $h$.
# - The [second-order Runge-Kutta (RK2) method](rk2-definition) uses two intermediate stage values that are then used to calculate the solution over the full step.
# - [Higher-order ODEs](higher-order-odes-section) can be rewritten as a system of first-order ODEs which can be solved using numerical solution methods.
