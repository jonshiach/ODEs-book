#!/usr/bin/env python
# coding: utf-8

# # Explicit Runge-Kutta Methods
# 
# ``````{div} full-width
# 
# - **General form of a Runge-Kutta method:**
# \begin{align*}
#     y_{n+1} &=y_n +h\sum_{i=1}^s b_i k_i,\\
#     k_i &=f(t_n +c_i h,y_n +h\sum_{j=1}^s a_{ij} k_j ),
# \end{align*}
# 
# - **Butcher tableau:** a Butcher tableau is a table of values containing the coefficients $a_{ij}$, $b_i$ and $c_i$ for a Runge-Kutta method
# \begin{align*}
#     \begin{array}{c|cccc}
#         c_1 & a_{11} & a_{12} & \cdots & a_{1s} \\
#         c_2 & a_{21} & a_{22} & \cdots & a_{2s} \\
#         \vdots & \vdots & \vdots & \ddots & \vdots \\
#         c_2 & a_{s1} & a_{2s} & \cdots & a_{ss} \\ \hline
#         & b_1 & b_2 & \cdots & b_s
#     \end{array}
# \end{align*}
# 
# `````{admonition} Example 2.1
# :class: seealso
# :name: butcher-tableau-example
# 
# Express the second-order Runge-Kutta method given below as a Butcher tableau
# 
# ````{math}
# :label: butcher-tableau-example-equation-1
# 
# \begin{align*}
#     y_{n+1} &= y_n + \frac{h}{2}(k_1 + k_2), \\
#     k_1 &= f(t_n, y_n), \\
#     k_2 &= f\left( t_n + h, y_n + hk_1 \right).
# \end{align*}
# ````
# `````
# 
# - **Order conditions for a second-order ERK method:** 
# \begin{align*}
#     b_1 +b_2 &=1,\\
#     c_2 b_2 &=\frac{1}{2},\\
#     a_{21} b_2 &=\frac{1}{2}
# \end{align*}
# 
# ````{admonition} Example 2.2
# :class: seealso
# :name: rk2-derivation-example
# 
# Derive a second-order Runge-Kutta method where $c_2 = 1$.
# ````
# 
# - **Order conditions for a fourth-order ERK method:**
# 
# \begin{align*}
#     b_1 + b_2 + b_3 + b_4 &= 1,\\
#     b_2 c_2 + b_3 c_3 + b_4 c_4 &=  \frac{1}{2},\\
#     b_2 c_2^2 + b_3 c_3^2 + b_4 c_4^2 &= \frac{1}{3},\\
#     b_2 c_2^3 + b_3 c_3^3 + b_4 c_4^3 &= \frac{1}{4},\\
#     b_3 c_3 a_{32} c_2 + b_4 c_4 (a_{42} c_2 + a_{43} c_3 ) &= \frac{1}{8},\\
#     b_3 a_{32} + b_4 a_{42} &= b_2 (1-c_2 ),\\
#     b_4 a_{43} &= b_3 (1 - c_3 ),\\
#     0 &= b_4 (1-c_4 ).
# \end{align*}
# 
# - **The row sum condition:**
# \begin{align*}
#     c_i =\sum_{j=1}^{s} a_{ij},
# \end{align*}
# 
# ````{admonition} Example 2.3
# :class: seealso
# 
# Derive a fourth-order Runge-Kutta method where $c_2 = c_3 = \frac{1}{2}$, $c_4 =1$ and $b_2 = \frac{1}{3}$.
# ````
# 
# - **The fourth-order Runge-Kutta (RK4) method:**
# \begin{align*}
#     y_{n + 1} &= y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4), \\
#     k_1 &= f(t_n, y_n), \\
#     k_2 &= f(t_n + \frac{1}{2}h, y_n + \frac{1}{2}hk_1), \\
#     k_3 &= f(t_n + \frac{1}{2}h, y_n + \frac{1}{2}hk_2), \\
#     k_4 &= f(t_n + h, y_n + hk_3).
# \end{align*}
# 
# ````{admonition} Example 2.4
# :class: seealso
# :name: rk4-example
# 
# Calculate the solution to the following initial value problem using the [RK4 method](rk4-definition) with $h = 0.2$
# 
# \begin{align*}
#     y'=ty, \qquad t\in [0,1], \qquad y(0)=1,
# \end{align*}
# 
# and compare the computed solution to the exact solution which is $y = \exp\left(\dfrac{t^2}{2}\right)$.
# ````
# 
# ``````
