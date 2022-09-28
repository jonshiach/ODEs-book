#!/usr/bin/env python
# coding: utf-8

# (bvp-chapter)=
# # Boundary Value Problems
# 
# **Learning outcomes**
# 
# On successful completion of this chapter readers will be able to:
# 
# - understand the definition of a [two-point boundary value problem](bvp-definition) and the existence and uniqueness of its solutions;
# - apply the [shooting method](shooting-method-section) to solve a boundary value problem;
# - implement the [Secant method](secant-method-section) to calculate estimates of the initial value;
# - implement the [finite-difference method](finite-difference-method-section) to solve boundary value problems;
# - implement the [Thomas algorithm](thomas-method-definition) to solve a tridiagonal system of linear equations.
# 
# ---
# 
# (bvp-section)=
# ## General two-point boundary value problem
# 
# A **Boundary Value Problem (BVP)** is an ODE where the solutions at the boundaries of the domain are known. 
# 
# ````{admonition} Definition: General two-point boundary value problem
# :class: note
# :name: bvp-definition
# 
# A two-point boundary value problem is a second-order ODE where the solutions at the lower and upper boundaries of the domain are known
# 
# ```{math}
# :label: bvp-equation
# 
# y'' = f(t,y),\qquad  t\in [a, b],\qquad y(a) = \alpha ,\qquad y(b) = \beta,
# ```
# 
# for some known values $\alpha$ and $\beta$.
# 
# ````
# 
# (existence-and-uniqueness-of-bvp-solutions-section)=
# ## Existence and uniqueness of solutions to boundary value problems
# 
# If an initial value problem has a solution it will be unique for a particular initial value. This is not true for boundary value problems which can have a unique solution, no solution or an infinite number of solutions. Consider the following boundary value problem
# 
# \begin{align*}
#     y'' + 4y = 0, \qquad y(0) = 1, \qquad y\left(\dfrac{\pi}{4}\right) = 2.
# \end{align*}
# 
# The general solution to the ODE $y'' + 4y = 0$ is 
# 
# \begin{align*}
#     y = c_1 \cos(2 t) + c_2 \sin(2 t),
# \end{align*}
# 
# so substituting the boundary values we have 
# 
# \begin{align*}
#     1 &= c_2 \cos(0) + c_2 \sin(0) = c_1, \\
#     2 &= c_2 \cos\left(\frac{\pi}{2}\right) + c_2 \sin\left(\frac{\pi}{2}\right) = c_2.
# \end{align*}
# 
# Here we can determine the values of $c_1$ and $c_2$ so this boundary value problem has the unique solution
# 
# \begin{align*}
#     y = \cos(t) + 2\sin(t).
# \end{align*}
# 
# Now consider the boundary value problem
# 
# \begin{align*}
#     y'' + 4y = 0, \qquad y(0) = 1, \qquad y(2\pi) = 1.
# \end{align*}
# 
# and substituting the boundary values we have
# 
# \begin{align*}
#     1 &= c_1 \cos(0) + c_2 \sin(0) = c_1, \\
#     1 &= c_1 \cos(2\pi) + c_2 \sin(2\pi) = c_1.
# \end{align*}
# 
# Here we have a solution for $c_1$ but we cannot determine the value of $c_2$ so the solution to the boundary value problem is
# 
# \begin{align*}
#     y = \cos(t) + c_2 \sin(t),
# \end{align*}
# 
# where $c_2$ can be any value. So we have infinitely many solutions. Finally consider the boundary value problem
# 
# \begin{align*}
#     y'' + 4y = 0, \qquad y(0) = 1, \qquad y(2\pi) = 1.
# \end{align*}
# 
# and substituting the boundary values we have
# 
# \begin{align*}
#     1 &= c_1 \cos(0) + c_2 \sin(0) = c_1, \\
#     2 &= c_1 \cos(2\pi) + c_2 \sin(2\pi) = c_1.
# \end{align*}
# 
# Here we have $c_1 = 1$ and $c_2 = 2$ which is a contradiction so this boundary value problem does not have a solution.
# 
# 
# ````{admonition} Theroem: Uniqueness of the solution to boundary value problems
# :class: important
# 
# A linear boundary value problem of the form
# 
# ```{math}
# :label: bvp-uniqueness-equation 
# 
# y'' = p(t)y' + q(t)y + r(t), \qquad t \in [a,b], \qquad y(a) = \alpha , \qquad y(b) = \beta ,
# ```
# 
# where $p(t)$, $q(t)$ and $r(t)$ are some functions of $t$ then it has a unique solution if the following are satisfied
# 
# - $p(t)$, $q(t)$ and $r(t)$ are continuous on $[a, b]$;
# - $q(t) > 0$ for all $t\in [a,b]$.
# 
# ````
# 
# ````{admonition} Example 5.1
# :class: seealso
# 
# Show that the following boundary value problem has a unique solution
# 
# \begin{align*}
#     y'' = (t^3 +5)y + \sin (t), \qquad t \in [0,1], \qquad y(0) = 0, \qquad y(1) = 1.
# \end{align*}
# 
# ```{dropdown} Solution
# 
# Comparing this boundary value problem to equation {eq}`bvp-uniqueness-equation` we have
# 
# \begin{align*}
#     p(t) &= 0,\\
#     q(t) &= t^3 + 5,\\
#     r(t) &= \sin(t),
# \end{align*}
# 
# which are all continuous on $[0,1]$ and $q(t)\geq $ for all $t\in [0,1]$ so this boundary value problem has a unique solution.
# ```
# 
# ````
