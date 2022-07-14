#!/usr/bin/env python
# coding: utf-8

# # Chapter Summary
# 
# - [Runge-Kutta methods](rk-definition) are **single step methods** that use intermediate **stage** values to advance the solution over a small step of length $h$ using known values of $t_n$ and $y_n$ to calculate $y_{n+1} = y(t_n+h)$;
# - Runge-Kutta methods are commonly expressed in tabular form called a [Butcher tableau](butcher-tableau-definition);
# - There are two types of Runge-Kutta methods: explicit and implicit methods.
# - [Explicit Runge-Kutta methods](explicit-and-implicit-rk-methods-section) are more straightforward to calculate but can be inefficient for some types of ODEs;
# - [Implicit Runge-Kutta methods](explicit-and-implicit-rk-methods-section) are less straightforward to calculate but are more efficient for some types of ODEs;
# - The coefficients of a Runge-Kutta methods are chosen to satisfy the **order conditions** which are derived by comparing the [Taylor series expansion](taylor-series-definition) to the general form of the [Runge-Kutta method](rk-definition) to the equivalent Taylor series expansion of the first-order ODE $y' = f(t,y)$.
