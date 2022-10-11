#!/usr/bin/env python
# coding: utf-8

# # Implicit Runge-Kutta Methods Exercises
# 
# `````{admonition} Exercise 3.1
# :class: note
# :name: ex3.1
# 
# Show that the Radau IA below is a third-order method.
# 
# \begin{align*}
#     \begin{array}{c|cc}
#       0 & 0 & 0 \\
#       \tfrac{2}{3} & \tfrac{1}{3} & \tfrac{1}{3} \\ \hline
#       & \tfrac{1}{4} & \tfrac{3}{4}
#     \end{array}
# \end{align*}
# 
# ````{dropdown} Solution
# 
# $B(k)$:
# \begin{align*}
#     j &= 1: & LHS &= b_1 c_1^0 + b_2 c_2^0 = \tfrac{1}{4} + \tfrac{3}{4} = 1, \\
#     && RHS &= 1, \\
#     j &= 2: & LHS &= b_1 c_1^1 + b_2 c_2^1 = \tfrac{1}{4}(0) + \tfrac{3}{4} ( \tfrac{2}{3} ) = \tfrac{1}{2}, \\
#     && RHS &= \tfrac{1}{2}, \\
#     j &= 3: & LHS &= b_1 c_1^2 + b_2 c_2^2 = \tfrac{1}{4}(0) + \tfrac{3}{4} ( \tfrac{4}{9} ) = \tfrac{1}{3}, \\
#     && RHS &= \tfrac{1}{3}, \\
#     j &= 4: & LSH &= b_1 c_1^3 + b_2 c_3^3 = \tfrac{1}{4}(0) + \tfrac{3}{4} ( \tfrac{8}{27} ) = \tfrac{2}{9}, \\
#     && RHS &= \tfrac{1}{4}.
# \end{align*}
# 
# So $B(3)$ is satisfied. Checking $C(1)$:
# \begin{align*}
#     i &= 1: & LHS &= a_{11} c_1^0 + a_{12} c_2^0 = 0 + 0 = 0, \\
#     && RHS &= \tfrac{1}{1} c_1^1 = 0, \\
#     i &= 2: & LHS &= a_{21} c_1^0 + a_{22} c_2^0 = \tfrac{1}{3} + \tfrac{1}{3} = \tfrac{2}{3}, \\
#     && RHS &= \tfrac{1}{1} c_2^1 = \tfrac{2}{3}.
# \end{align*}
# 
# So $C(1)$ is satisfied, checking $D(1)$:
# 
# \begin{align*}
#     j &= 1: & LHS &= b_1 c_1^0 a_{11} + b_2 c_2^0 a_{21} = \tfrac{1}{4} (1)(0) + \tfrac{3}{4} (1) ( \tfrac{1}{3} ) = \tfrac{1}{4}, \\
#     && RHS &= \tfrac{1}{1}b_1(1 - c_1^1) = \tfrac{1}{4}(1 - 0) = \tfrac{1}{4}, \\
#     j &= 2: & LHS &= b_1 c_1^0 a_{12} + b_2 c_2^0 a_{22} = \tfrac{1}{4} (1)(0) + \tfrac{3}{4} (1) ( \tfrac{1}{3} ) = \tfrac{1}{4}, \\
#     && RHS &= \tfrac{1}{1} b_2 (1 - c_2^1) = \tfrac{3}{4} ( 1 - \tfrac{2}{3} ) = \tfrac{1}{4}.
# \end{align*}
# 
# Since $B(3)$, $C(1)$ and $D(1)$ are satisfied then this implicit method is a third-order method.
# ````
# `````
# 
# `````{admonition} Exercise 3.2
# :class: note
# :name: ex3.2
# 
# Determine the order of the following IRK method.
# \begin{align*}
#   \begin{array}{c|ccc}
#      0 & 0 & 0 & 0 \\
#      \frac{1}{2} & \frac{1}{4} & \frac{1}{4} & 0 \\
#      1 & 0 & 1 & 0 \\ \hline
#      & \frac{1}{6} & \frac{2}{3} & \frac{1}{6}
#   \end{array}
# \end{align*}
# 
# ````{dropdown} Solution
# Check $B(k)$
# 
# \begin{align*}
#     j &= 1: & LHS &= b_1 c_1^0 + b_2 c_2^0 + b_3 c_3^0 = \tfrac{1}{6} + \tfrac{2}{3} + \tfrac{1}{6} = 1, \\
#     && RHS &= 1, \\
#     j &= 2: & LHS &= b_1 c_1^1 + b_2 c_2^1 + b_3 c_3^1 = \tfrac{1}{6}(0) + \tfrac{2}{3}(\tfrac{1}{2}) + \tfrac{1}{6}(1) = \tfrac{1}{2}, \\
#     && RHS &= \tfrac{1}{2}, \\ 
#     j &= 3: & LHS &= b_1 c_1^2 + b_2 c_2^2 + b_3 c_3^2 = \tfrac{1}{6}(0) + \tfrac{2}{3}(\tfrac{1}{4}) + \tfrac{1}{6}(1) = \tfrac{1}{3}, \\
#     && RHS &= \tfrac{1}{3}, \\
#     j &= 4: & LHS &= b_1 c_1^3 + b_2 c_2^3 + b_3 c_3^3 = \tfrac{1}{6}(0) + \tfrac{2}{3}(\tfrac{1}{8}) + \tfrac{1}{6}(1) = \tfrac{1}{4}, \\
#     && RHS &= \tfrac{1}{4}, \\
#     j &= 5: & LHS &= b_1 c_1^4 + b_2 c_2^4 + b_3 c_3^4 = \tfrac{1}{6}(0) + \tfrac{2}{3}(\tfrac{1}{16}) + \tfrac{1}{6}(1) = \tfrac{5}{24}, \\
# \end{align*}
# 
# So $B(4)$ is satisfied, checking $C(2)$:
# 
# \begin{align*}
#     \ell &= 1, & i &= 1, & LHS &= a_{11} c_1^0 + a_{12} c_2^0 + a_{13} c_3^0 = 0 + 0 + 0 = 0, \\
#     &&&& RHS &= \tfrac{1}{1} c_1^1 = 0, \\
#     && i &= 2, & LHS &= a_{21} c_1^0 + a_{22} c_2^0 + a_{23} c_3^0 = \tfrac{1}{4} + \tfrac{1}{4} + 0 = \tfrac{1}{2} \\
#     &&&& RHS &= \tfrac{1}{1} c_2^1 = \tfrac{1}{2}, \\
#     && i &= 3, & LHS &= a_{31} c_1^0 + a_{32} c_2^0 + a_{33} c_3^0 = 0 + 1 + 0 = 1, \\
#     &&&& RHS &= \tfrac{1}{1} c_3^1 = 1, \\
#     \ell &= 2, & i &= 1 & LHS &= a_{11} c_1^1 + a_{12} c_2^1 + a_{13} c_3^1 = 0 + 0 + 0 = 0, \\
#     &&&& RHS &= \tfrac{1}{2} c_1^2 = \tfrac{1}{2}(0) = 0, \\
#     && i &= 2, & LHS &= a_{21} c_1^1 + a_{22} c_2^1 + a_{23} c_3^1 = \tfrac{1}{4}(0) + \tfrac{1}{4}(\tfrac{1}{2}) + 0(1) = \tfrac{1}{8}, \\
#     &&&& RHS &= \tfrac{1}{2} c_2^2 = \tfrac{1}{2} (\tfrac{1}{4}) = \tfrac{1}{8}, \\
#     && i &= 3, & LHS &= a_{31} c_1^1 + a_{32} c_2^1 + a_{33} c_3^1 = 0(1) + 1(\tfrac{1}{2}) + 0(1) = \tfrac{1}{2}, \\
#     &&&& RHS &= \tfrac{1}{2} c_3^2 = \tfrac{1}{2}(1) = \tfrac{1}{2}.
# \end{align*}
# 
# So $C(2)$ is satisfied, checking $D(2)$
# 
# \begin{align*}
#     \ell &= 1, & j &= 1, & LHS &= b_1 c_1^0 a_{11} + b_2 c_2^0 a_{21} + b_3 c_3^0 a_{31} 
#     = \tfrac{1}{6}(1)(0) + \tfrac{2}{3}(1)(\tfrac{1}{4}) + \tfrac{1}{6}(1)(0) = \tfrac{1}{6}, \\
#     &&&& RHS &= \tfrac{1}{1} b_1 (1 - c_1^1) = \tfrac{1}{6} (1 - 0) = \tfrac{1}{6}, \\
#     && j &= 2, & LHS &= b_1 c_1^0 a_{12} + b_2 c_2^0 a_{22} + b_3 c_3^0 a_{32} 
#     = \tfrac{1}{6}(1)(0) + \tfrac{2}{3}(1)(\tfrac{1}{4}) + \tfrac{1}{6}(1)(1) = \tfrac{1}{3}, \\
#     &&&& RHS &= \tfrac{1}{1} b_2 (1 - c_2^1) = \tfrac{2}{3} (1 - \tfrac{1}{2}) = \tfrac{1}{3}, \\
#     && j &= 3, & LHS &= b_1 c_1^0 a_{13} + b_2 c_2^0 a_{23} + b_3 c_3^0 a_{33} 
#     = \tfrac{1}{6}(1)(0) + \tfrac{2}{3}(1)(0) + \tfrac{1}{6}(1)(0) = 0, \\
#     &&&& RHS &= \tfrac{1}{1} b_3 (1 - c_3^1) = \tfrac{1}{6} (1 - 1) = 0, \\
#     \ell &= 2, & j &= 1, & LHS &= b_1 c_1^1 a_{11} + b_2 c_2^1 a_{21} + b_3 c_3^1 a_{31} 
#     = \tfrac{1}{6}(0)(0) + \tfrac{2}{3}(\tfrac{1}{2})(\tfrac{1}{4}) + \tfrac{1}{6}(1)(0) = \tfrac{1}{12}, \\
#     &&&& RHS &= \tfrac{1}{2} b_1 (1 - c_1^2) = \tfrac{1}{2}(\tfrac{1}{6})(1 - 0) = \tfrac{1}{12}, \\
#     && j &= 2, & LHS &= b_1 c_1^1 a_{12} + b_2 c_2^1 a_{22} + b_3 c_3^1 a_{32} 
#     = \tfrac{1}{6}(0)(0) + \tfrac{2}{3}(\tfrac{1}{2})(\tfrac{1}{4}) + \tfrac{1}{6}(1)(1) = \tfrac{1}{4}, \\
#     &&&& RHS &= \tfrac{1}{2} b_2 (1 - c_2^2) = \tfrac{1}{2} (\tfrac{2}{3})(1 - \tfrac{1}{4}) = \tfrac{1}{4}, \\
#     && j &= 3, & LHS &= b_1 c_1^1 a_{13} + b_2 c_2^1 a_{23} + b_3 c_3^1 a_{33} 
#     = \tfrac{1}{6}(0)(0) + \tfrac{2}{3}(\tfrac{1}{2})(0) + \tfrac{1}{6}(1)(0) = 0, \\
#     &&&& RHS &= \tfrac{1}{2} b_3 (1 - c_3^2) = \tfrac{1}{2} (\tfrac{1}{6}) (1 - 1) = 0.
# \end{align*}
# 
# Since $B(4)$, $C(2)$ and $D(2)$ are satisfied then this is a fourth-order method. 
# ````
# 
# `````
# 
# `````{admonition} Exercise 3.3
# :class: note
# :name: ex3.3
# 
# Derive a third-order Radau IIA method.
# 
# ````{dropdown} Solution
# Since $k=3$ then the method has $s = \frac{k + 1}{2} = 2$ stages. The values of $c_1$ and $c_2$ are the roots of $P_2(t) - P_1(t)$
# 
# \begin{align*}
#     0 &= (6t^2 - 6t + 1) - (2t - 1) = 6t^2 - 8t + 2, \\
#     \therefore t &= \frac{2 \pm 1}{3},
# \end{align*}
# 
# so $c_1 = \frac{1}{3}$ and $c_2 = 1$. The values of $b_i$ satisfy the [$B(4)$ order conditions](Bk_Ck_Dk_order_conditions)
# 
# \begin{align*}
#     b_1 + b_2 &= 0, \\
#     \tfrac{1}{3} b_1 + b_2 &= \tfrac{1}{2}, \\
#     \tfrac{1}{9} b_1 + b_2 &= \tfrac{1}{3},
# \end{align*}
# 
# which is solved to give $b_1 = \frac{3}{4}$ and $b_2 = \frac{1}{4}$. The values of $a_{ij}$ satisfy the [$C(2)$ order conditions](Bk_Ck_Dk_order_conditions)
# 
# \begin{align*}
#     a_{11} + a_{12} &= \tfrac{1}{3}, \\
#     a_{21} + a_{22} &= 1, \\
#     \tfrac{1}{3} a_{11} + a_{12} &= \tfrac{1}{18}, \\
#     \tfrac{1}{3} a_{21} + a_{22} &= \tfrac{1}{2},
# \end{align*}
# 
# Subtracting the third equation from the first gives $\frac{2}{3} a_{11} = \frac{4}{18}$ so $a_{11} = \frac{5}{12}$ and substituting this into the first equation gives $a_{12} = -\frac{1}{12}$. Subtracting the fourth equation from the second gives $\frac{2}{3} a_{21} = \frac{1}{2}$ so $a_{21} = \frac{3}{4}$ and substituting this into the second equation gives $a_{22} = \frac{1}{4}$. So the fourth-order Radau II method is
# 
# \begin{align*}
#     \begin{array}{c|cc}
#         \frac{1}{3} & \frac{5}{12} & -\frac{1}{12} \\
#         1 & \frac{3}{4} & \frac{1}{4} \\
#         \hline
#         & \frac{3}{4} & \frac{!}{4}
#     \end{array}
# \end{align*}
# 
# Python code
# 
# ```python
# from sympy import *
# init_printing()
# 
# # Define Legendre polynomial
# def P(n):
#     t = Symbol("t")
#     P = 0
#     for k in range(n + 1):
#         P += binomial(n, k) * binomial(n + k, k) * (t - 1) ** k
# 
#     return P
# 
# 
# # Define symbolic variables
# a11, a12, a21, a22, b1, b2, c1, c2 = symbols("a11, a12, a21, a22, b1, b2, c1, c2")
# 
# # Calculate c values
# c1, c2 = solve(P(2) - P(1))
# display(solve(P(2) - P(1)))
# 
# # Define order conditions
# eq1 = b1 + b2 - 1
# eq2 = b1 * c1 + b2 * c2 - Rational(1,2)
# eq3 = a11 + a12 - c1
# eq4 = a21 + a22 - c2
# eq5 = a11 * c1 + a12 * c2 - Rational(1,2) * c1 ** 2
# eq6 = a21 * c1 + a22 * c2 - Rational(1,2) * c2 ** 2
# 
# # Solve order conditions
# solve((eq1, eq2, eq3, eq4, eq5, eq6))
# ```
# 
# Output:
# 
# ```{glue:math} ex3.3_output_1
# :label: ex3.3-output-1
# ```
# 
# ```{glue:math} ex3.3_output_2
# :label: ex3.3-output-2
# ```
# 
# ````
# 
# `````

# In[1]:


from sympy import *
from myst_nb import glue
init_printing()

# Define Legendre polynomial
def P(n):
    t = Symbol("t")
    P = 0
    for k in range(n + 1):
        P += binomial(n, k) * binomial(n + k, k) * (t - 1) ** k

    return P


# Define symbolic variables
a11, a12, a21, a22, b1, b2, c1, c2 = symbols("a11, a12, a21, a22, b1, b2, c1, c2")

# Calculate c values
c1, c2 = solve(P(2) - P(1))
display(solve(P(2) - P(1)))

# Define order conditions
eq1 = b1 + b2 - 1
eq2 = b1 * c1 + b2 * c2 - Rational(1,2)
eq3 = a11 + a12 - c1
eq4 = a21 + a22 - c2
eq5 = a11 * c1 + a12 * c2 - Rational(1,2) * c1 ** 2
eq6 = a21 * c1 + a22 * c2 - Rational(1,2) * c2 ** 2

# Solve order conditions
solve((eq1, eq2, eq3, eq4, eq5, eq6))

glue("ex3.3_output_1", solve(P(2) - P(1)), display=False)
glue("ex3.3_output_2", solve((eq1, eq2, eq3, eq4, eq5, eq6)))


# `````{admonition} Exercise 3.4
# :class: note
# :name: ex3.4
# 
# Using pen and paper and working to 6 decimal places, calculate the first step of the third-order Radau IIA method derived in [exercise 3.3](ex3.3) to solve the following initial value problem using a step length of $h=0.4$ and a convergence tolerance of $tol = 10^{-4}$
# 
# \begin{align*}
#   y' =t - y, \qquad t \in [0,2], \qquad y(0) = 1.
# \end{align*}
# 
# ````{dropdown} Solution
# The Butcher tableau for the Radau IIA method is
# 
# \begin{align*}
#     \begin{array}{c|cc}
#         \frac{1}{3} & \frac{5}{12} & -\frac{1}{12} \\
#         1 & \frac{3}{4} & \frac{1}{4} \\
#         \hline
#         & \frac{3}{4} & \frac{1}{4}
#     \end{array}
# \end{align*}
# 
# The stage values are
# 
# \begin{align*}
#     Y_1 &= y_n + h (\tfrac{5}{12} f(t_n + \tfrac{1}{3} h, Y_1) - \tfrac{1}{12} f(t_n + h, Y_2)) \\
#     Y_2 &= y_n + h (\tfrac{3}{4} f(t_n + \tfrac{1}{3} h, Y_1) + \tfrac{1}{4} f(t_n + h, Y_2)),
# \end{align*}
# 
# and since $f(t,y) = t - y $ then
# 
# \begin{align*}
#     Y_1 &= y_n + h (\tfrac{5}{12} (t_n + \tfrac{1}{3} h - Y_1) - \tfrac{1}{12} (t_n + h - Y_2)) \\
#     Y_2 &= y_n + h (\tfrac{3}{4} (t_n + \tfrac{1}{3} h - Y_1) + \tfrac{1}{4} (t_n + h - Y_2)).
# \end{align*}
# 
# For this problem $y(0) = 1$ and $h = 0.4$. Using starting estimates of $Y_1 = Y_2 = 1$ 
# 
# \begin{align*}
#     k &= 1, & Y_1 &= 1 + 0.4 (\tfrac{5}{12} (0 + \tfrac{1}{3} (0.4) - 1) - \tfrac{1}{12} (0 + 0.4 - 1)) \\
#     && &= 0.875556, \\
#     && Y_2 &= 1 + 0.4 (\tfrac{3}{4} (0 + \tfrac{1}{3} (0.4) - 0.875556) + \tfrac{1}{4} (0 + 0.4 - 1)) \\
#     && &= 0.717333, \\
#     k &= 2, & Y_1 &= 1 + 0.4 (\tfrac{5}{12}( 0 + \tfrac{1}{3} (0.4) - 0.875556) - \tfrac{1}{12} (0 + 0.4 - 0.717333)) \\
#     && &= 0.886874, \\
#     && Y_2 &= 1 + 0.4 (\tfrac{3}{4} (0 + \tfrac{1}{3} (0.4) - 0.886874) + \tfrac{1}{4} (0 + 0.4 - 0.717333)) \\
#     && &= 0.742204, \\
#     k &= 3, & Y_1 &= 1 + 0.4 (\tfrac{5}{12} (0 + \tfrac{1}{3} (0.4) - 0.886874) - \tfrac{1}{12} (0 + 0.4 - 0.742204)) \\
#     && &= 0.885817, \\
#     && Y_2 &= 1 + 0.4 (\frac{3}{4} (0 + \tfrac{1}{3} (0.4) - 0.885817) + \tfrac{1}{4} (0 + 0.4 - 0.742204)) \\
#     && &= 0.740035, \\
#     k &= 4, & Y_1 &= 1 + 0.4 (\tfrac{5}{12} (0 + \tfrac{1}{3} (0.4) - 0.885817) - \tfrac{1}{12} (0 + 0.4 - 0.740035)) \\
#     && &= 0.885921, \\
#     && Y_2 &= 1 + 0.4 (\tfrac{3}{4} (0 + \tfrac{1}{3} (0.4) - 0.885921) + \tfrac{1}{4} (0 + 0.4 - 0.740035)) \\
#     && &= 0.740220, \\
#     k &= 5, & Y_1 &= 1 + 0.4 (\tfrac{5}{12} (0 + \tfrac{1}{3} (0.4) - 0.885921) - \tfrac{1}{12} (0 + 0.4 - 0.740220)) \\
#     && &= 0.885909, \\
#     && Y_2 &= 1 + 0.4 (\tfrac{3}{4} (0 + \tfrac{1}{3} (0.4) - 0.885909) + \tfrac{1}{4} (0 + 0.4 - 0.740220)) \\
#     && &= 0.740205.
# \end{align*}
# 
# After 4 iterations $\max(|0.885909 - 0.885921|, |0.740205 - 0.640220|) = 1.5\times 10^{-5} < 10^{-4}$ so $Y_1 = 0.885909$ and $Y_2 = 0.740205$ are accurate enough for our needs. The solution over the first step is
# 
# \begin{align*}
#     y_1 &= y_0 + h (\tfrac{3}{4} (t_0 + \tfrac{1}{3}(0.4) - Y_1) + \tfrac{1}{4} (t_0 + 0.4 - Y_2)), \\
#     &= 1 + 0.4 (\tfrac{3}{4} (0 + \frac{1}{3}(0.4) - 0.885909) + \frac{1}{4} (0 + 0.4 - 0.740205)), \\
#     &= 0.740207.
# \end{align*}
# 
# `````

# `````{admonition} Exercise 3.5
# :class: note
# :name: ex3.5
# 
# The exact solution to the IVP in [exercise 3.4](ex3.4) is $y = t + 2e^{-t} - 1$. Write a program to this initial value problem over the full domain and produce a table comparing the numerical and exact solutions. Plot the numerical solutions and exact solutions on the same set of axes.
# 
# ````{dropdown} Solution
# Code
# 
# ```python
# import numpy as np
# import matplotlib.pyplot as plt
# 
# def radauIIA(f, tspan, y0, h):
#     nsteps = int((tspan[1] - tspan[0]) / h)
#     neq = len(y0)
#     t = np.arange(nsteps + 1) * h
#     y = np.zeros((nsteps + 1, neq))
#     y[0,:] = y0
#     for n in range(nsteps):
#         Y1, Y2, Y1o, Y2o = np.ones(neq), np.ones(neq), np.ones(neq), np.ones(neq)
#         for k in range(10):
#             Y1 = y[n,:] + h * (5/12 * f(t[n] + 1/3 * h, Y1) - 1/12 * f(t[n] + h, Y2))
#             Y2 = y[n,:] + h * (3/4 * f(t[n] + 1/3 * h, Y1) + 1/4 * f(t[n] + h, Y2))
#             if max(np.amax(abs(Y1 - Y1o)), np.amax(abs(Y2 - Y2o))) < tol:
#                 break
#             Y1o, Y2o = Y1, Y2
# 
#         y[n+1,:] = y[n,:] + h * (3/4 * f(t[n] + 1/3 * h, Y1) + 1/4 * f(t[n] + h, Y2))
#         
#     return t, y
# 
# 
# def f(t, y):
#     return t - y
# 
# 
# def exact(t):
#     return t + 2 * np.exp(-t) - 1
# 
# 
# # Define IVP
# tspan = [0, 2]  # boundaries of the t domain
# y0 = [1]        # solution at the lower boundary
# h = 0.4         # step length
# tol = 1e-4      # convergence tolerance
# 
# # Solve IVP using the Radau IIA method
# t, y = radauIIA(f, tspan, y0, h)
# 
# # Output solution table
# print("|  t  |    IRK    |   Exact   |   Error   |")
# print("|:---:|:---------:|:---------:|:---------:|")
# for n in range(len(t)):
#     print(f"| {t[n]:3.1f} | {y[n,0]:9.6f} | {exact(t[n]):9.6f} | {abs(exact(t[n]) - y[n,0]):9.2e} |")
# 
# # Plot solutions
# t_exact = np.linspace(tspan[0], tspan[1], 200)
# y_exact = exact(t_exact)
# fig, ax = plt.subplots(figsize=(8, 6))
# plt.plot(t_exact, y_exact, "k", label="Exact")
# plt.plot(t, y, "bo-", label="Radua IIA")
# plt.xlabel("$t$", fontsize=14)
# plt.ylabel("$y$", fontsize=14)
# plt.legend(fontsize=12)
# plt.show()
# ```
# 
# Output
# 
# ```
# |  t  |    IRK    |   Exact   |   Error   |
# |:---:|:---------:|:---------:|:---------:|
# | 0.0 |  1.000000 |  1.000000 |  0.00e+00 |
# | 0.4 |  0.740207 |  0.740640 |  4.33e-04 |
# | 0.8 |  0.698075 |  0.698658 |  5.83e-04 |
# | 1.2 |  0.801801 |  0.802388 |  5.87e-04 |
# | 1.6 |  1.003268 |  1.003793 |  5.25e-04 |
# | 2.0 |  1.270232 |  1.270671 |  4.39e-04 |
# ```
# 
# Plot
# 
# ```{glue:figure} ex3.5_plot
# ```
# 
# ````
# `````

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

def radauIIA(f, tspan, y0, h):
    nsteps = int((tspan[1] - tspan[0]) / h)
    neq = len(y0)
    t = np.arange(nsteps + 1) * h
    y = np.zeros((nsteps + 1, neq))
    y[0,:] = y0
    for n in range(nsteps):
        Y1, Y2, Y1o, Y2o = np.ones(neq), np.ones(neq), np.ones(neq), np.ones(neq)
        for k in range(10):
            Y1 = y[n,:] + h * (5/12 * f(t[n] + 1/3 * h, Y1) - 1/12 * f(t[n] + h, Y2))
            Y2 = y[n,:] + h * (3/4 * f(t[n] + 1/3 * h, Y1) + 1/4 * f(t[n] + h, Y2))
            if max(np.amax(abs(Y1 - Y1o)), np.amax(abs(Y2 - Y2o))) < tol:
                break
            Y1o, Y2o = Y1, Y2

        y[n+1,:] = y[n,:] + h * (3/4 * f(t[n] + 1/3 * h, Y1) + 1/4 * f(t[n] + h, Y2))
        
    return t, y


def f(t, y):
    return t - y


def exact(t):
    return t + 2 * np.exp(-t) - 1


# Define IVP
tspan = [0, 2]  # boundaries of the t domain
y0 = [1]        # solution at the lower boundary
h = 0.4         # step length
tol = 1e-4      # convergence tolerance

# Solve IVP using the Radau IIA method
t, y = radauIIA(f, tspan, y0, h)

# Output solution table
print("|  t  |    IRK    |   Exact   |   Error   |")
print("|:---:|:---------:|:---------:|:---------:|")
for n in range(len(t)):
    print(f"| {t[n]:3.1f} | {y[n,0]:9.6f} | {exact(t[n]):9.6f} | {abs(exact(t[n]) - y[n,0]):9.2e} |")

# Plot solutions
t_exact = np.linspace(tspan[0], tspan[1], 200)
y_exact = exact(t_exact)
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(t_exact, y_exact, "k", label="Exact")
plt.plot(t, y, "bo-", label="Radua IIA")
plt.xlabel("$t$", fontsize=14)
plt.ylabel("$y$", fontsize=14)
plt.legend(fontsize=12)
plt.show()


# In[3]:


from myst_nb import glue
glue("ex3.5_plot", fig, display=False)

