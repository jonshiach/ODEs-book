#!/usr/bin/env python
# coding: utf-8

# # Initial Value Problems
# 
# ``````{div} full-width
# 
# - **Initial Value Problem:** an ODE of the form $y' = f(t, y)$ over the domain $t \in [a, b]$ with initial solution $y(a) = \alpha$.
# 
# - **The Taylor series:**
# \begin{align*}
#     f(t+h) &= \sum_{n = 0}^\infty \frac{h^n}{n!}f^{(n)}(t) = f(t) + hf'(t) + \frac{h^2}{2!}f''(t) + \frac{h^3}{3!}f'''(t) + \cdots
# \end{align*}
# 
# ````{admonition} Example 1.1
# :class: seealso
# :name: taylor-series-example
# 
# Use the first, second, third and fourth-order Taylor series expansions to calculate the value of $\cos\left(\frac{\pi}{3} + h\right)$ where $h=0.2$.
# ````
# 
# - **The Euler method:**
# \begin{align*}
# y_{n+1} = y_n + h f(t_n ,y_n).
# \end{align*}
# 
# ````{admonition} Example 1.2
# :class: seealso
# :name: euler-example
# 
# Calculate the solution to the following initial value problem using the Euler method with $h = 0.2$
# 
# $$y' = ty, \qquad t\in [0,1], \qquad y(0)=1,$$
# 
# and compare the computed solution to the exact solution which is $y = \exp\left(\dfrac{t^2}{2}\right)$.
# ````
# 
# - **The second-order Runge-Kutta (RK2) method:** 
# \begin{align*}
#     y_{n+1} &= y_n + \frac{h}{2}(k_1 + k_2),\\
#     k_1 &= f(t_n, y_n), \\
#     k_2 &= f(t_n + h, y_n + h k_1).
# \end{align*} 
# 
# ````{admonition} Example 1.3
# :class: seealso
# :name: rk2-example
# 
# Calculate the solution to the initial value problem from [example 1.2](euler-example) using the RK2 method with a step length of $h = 0.2$
# 
# \begin{align*}
#     y'=ty, \qquad t\in [0,1], \qquad y(0)=1,
# \end{align*}
# 
# and compare the computed solution to the exact solution which is $y = \exp\left(\dfrac{t^2}{2}\right)$.
# ````
# 
# - **Writing higher order ODES as a system of first-order ODEs:** given $y^{(n)} = f(t, y, y', \ldots, y^{(n-1)})$ let $y_1=y$, $y_2 = y'$, $y_3 = y''$ etc. then
# \begin{align*}
#     y_1' &= y_2,\\
#     y_2' &= y_3,\\
#     &\vdots \\
#     y_n' &= f(t, y_1 , y_2 , y_3 , \ldots, y_n).
# \end{align*}
# 
# ````{admonition} Example 1.4
# :class: seealso
# :name: higher-order-odes-example
# 
# Rewrite the following ODE as a system of first-order ODEs
# 
# \begin{align*}
#     y''' + yy'' -2y' + ty'' - 10 = 0.
# \end{align*}
# ````
# 
# `````{admonition} Example 1.5
# :class: seealso
# :name: higher-order-ode-ivp-example
# 
# Calculate solution to the following initial value problem using the Euler method with $h=0.2$
# 
# \begin{align*}
#     y'' + y = 0, \qquad t \in [0,10], \qquad y(0) = 2, \qquad y'(0) = 0
# \end{align*}
# 
# and compare the computed solution to the exact solution which is $y = 2\cos(t)$.
# `````
# 
# ``````
