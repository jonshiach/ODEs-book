#!/usr/bin/env python
# coding: utf-8

# # Boundary value problems exercises
# 
# `````{admonition} Exercise 5.1
# :class: note
# :name: ex5.1
# 
# Determine which of the following BVPs have a unique solution
# 
# (a)  $y'' = - \dfrac{4}{t} y' + \dfrac{2}{t^2 } y - \dfrac{2\ln (t)}{t^3 }, \qquad y(1) = 1/2, \qquad y(2) = \ln (2)$;
# 
# ````{dropdown} Solution
# $p(t) = -\dfrac{4}{t}$, $q(t) = \dfrac{2}{t^2}$ and $r(t) = \dfrac{2\ln(t)}{t^3}$ are all continuous and $q(t) > 0$ for $t \in [1, 2]$ so this boundary value problem has a unique solution.
# ````
# 
# (b)  $y'' = e^t + y\cos(t) - (t + 1) y', \qquad y(0) = 1, \qquad y(2) = \ln(3)$;
# 
# ````{dropdown} Solution
# $p(t) = -(t + 1)$, $q(t) = \cos(t)$ and $r(t) = e^t$ are all continuous for $t\in[0,2]$ but $q(t) < 0$ for $t \in (\pi/2, 2]$ so this boundary value problem does not have a unique solution.
# ````
# 
# (c)  $y'' = (t^3 + 5)y + \sin(t), \qquad y(0) = 0,\qquad y(1) = 1$;
# 
# ````{dropdown} Solution
# $p(t) = 0$, $q(t) = t^3 + 5$ and $r(t) = \sin(t)$ are all continuous and $q(t) > 0$ for $t\in[0,1]$ so this boundary value problem has a unique solution.
# ````
# 
# (d)  $y'' = (5y + \sin(3t)) e^t, \qquad y(0) = 0,\qquad y(1) = 0$.
# 
# ````{dropdown} Solution
# $p(t) = 0$, $q(t) = 5e^t$ and $r(t) = e^t\sin(3t)$ are all continuous and $q(t) > 0$ for $t\in[0,1]$ so this boundary value problem has a unique solution.
# ````
# `````
# 
# `````{admonition} Exercise 5.2
# :class: note
# :name: ex5.2
# 
# Consider the following boundary value problem
# 
# \begin{align*}
#     y'' = 2t, \qquad y(0) = 1, \qquad y(2) = 3.
# \end{align*}
# 
# Using a pen and calculator, calculate the Euler method solutions using a step length of $h=0.4$ and guess values of $y'(0) = 1$ and $y'(0) = -1$
# 
# 
# ````{dropdown} Solution
# Rewriting the ODE as a system of two first-order ODEs
# \begin{align*}
#     y_1' &= y_2, \\
#     y_2' &= 2t.
# \end{align*}
# 
# Solving using the Euler method and $y'(0)=1$
# 
# \begin{align*}
#     \mathbf{t} &= (0, 0.4, 0.8, 1.2, 1.6, 2.0), \\
#     \mathbf{y}_0 &= \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \\
#     \mathbf{y}_1 &= \mathbf{y}_0 + h \mathbf{f}(t_0, \mathbf{y}_0) 
#     = \begin{pmatrix} 1 \\ 1 \end{pmatrix} + 0.4 \begin{pmatrix} 1 \\ 2(0) \end{pmatrix} 
#     = \begin{pmatrix} 1.4 \\ 1 \end{pmatrix}, \\
#     \mathbf{y}_2 &= \mathbf{y}_1 + h \mathbf{f}(t_1, \mathbf{y}_1) 
#     = \begin{pmatrix} 1.4 \\ 1 \end{pmatrix} + 0.4 \begin{pmatrix} 1 \\ 2(0.4) \end{pmatrix} 
#     = \begin{pmatrix} 1.8 \\ 1.32 \end{pmatrix}, \\
#     \mathbf{y}_3 &= \mathbf{y}_2 + h \mathbf{f}(t_2, \mathbf{y}_2) 
#     = \begin{pmatrix} 1.8 \\ 1.32 \end{pmatrix} + 0.4 \begin{pmatrix} 1.32 \\ 2(0.8) \end{pmatrix} 
#     = \begin{pmatrix} 2.328 \\ 1.96 \end{pmatrix}, \\
#     \mathbf{y}_4 &= \mathbf{y}_3 + h \mathbf{f}(t_3, \mathbf{y}_3) 
#     = \begin{pmatrix} 2.328 \\ 1.96 \end{pmatrix} + 0.4 \begin{pmatrix} 1.96 \\ 2(1.2) \end{pmatrix} 
#     = \begin{pmatrix} 3.112 \\ 2.92 \end{pmatrix}, \\
#     \mathbf{y}_5 &= \mathbf{y}_4 + h \mathbf{f}(t_4, \mathbf{y}_4) 
#     = \begin{pmatrix} 3.112 \\ 2.92 \end{pmatrix} + 0.4 \begin{pmatrix} 2.92 \\ 2(1.6) \end{pmatrix} 
#     = \begin{pmatrix} 4.28 \\ 4.2 \end{pmatrix}, \\
# \end{align*}
# 
# Solving using $y'(0)=-1$
# 
# \begin{align*}
#     \mathbf{y}_0 &= \begin{pmatrix} 1 \\ -1 \end{pmatrix}, \\
#     \mathbf{y}_1 &= \mathbf{y}_0 + h \mathbf{f}(t_0, \mathbf{y}_0) 
#     = \begin{pmatrix} 1 \\ -1 \end{pmatrix} + 0.4 \begin{pmatrix} -1 \\ 2(0) \end{pmatrix} 
#     = \begin{pmatrix} 0.6 \\ -1 \end{pmatrix}, \\
#     \mathbf{y}_2 &= \mathbf{y}_1 + h \mathbf{f}(t_1, \mathbf{y}_1) 
#     = \begin{pmatrix} 0.6 \\ -1 \end{pmatrix} + 0.4 \begin{pmatrix} -1 \\ 2(0.4) \end{pmatrix} 
#     = \begin{pmatrix} 0.2 \\ -0.68 \end{pmatrix}, \\
#     \mathbf{y}_3 &= \mathbf{y}_2 + h \mathbf{f}(t_2, \mathbf{y}_2) 
#     = \begin{pmatrix} 0.2 \\ -0.68 \end{pmatrix} + 0.4 \begin{pmatrix} -0.68 \\ 2(0.8) \end{pmatrix} 
#     = \begin{pmatrix} -0.072 \\ -0.04 \end{pmatrix}, \\
#     \mathbf{y}_4 &= \mathbf{y}_3 + h \mathbf{f}(t_3, \mathbf{y}_3) 
#     = \begin{pmatrix} -0.072 \\ -0.04 \end{pmatrix} + 0.4 \begin{pmatrix} -0.04 \\ 2(1.2) \end{pmatrix} 
#     = \begin{pmatrix} -0.088 \\ 0.92 \end{pmatrix}, \\
#     \mathbf{y}_5 &= \mathbf{y}_4 + h \mathbf{f}(t_4, \mathbf{y}_4) 
#     = \begin{pmatrix} -0.088 \\ 0.92 \end{pmatrix} + 0.4 \begin{pmatrix} 0.92 \\ 2(1.6) \end{pmatrix} 
#     = \begin{pmatrix} 0.28 \\ 2.2 \end{pmatrix}, \\
# \end{align*}
# ````
# 
# `````

# `````{admonition} Exercise 5.3
# :class: note
# :name: ex5.3
# 
# Use the Secant method to calculate the next value of $s$ for your solutions to the boundary value problem in [exercise 5.2](ex5.2) and hence calculate the Euler method using this new guess value.
# 
# ````{dropdown} Solution
# 
# Calculate the improved guess value
# 
# \begin{align*}
#     s_2 &= s_1 + g(s_1) \frac{s_1 - s_0}{g(s_1) - g(s_0)} \\
#     &= -1 + (3 - 4.28) \frac{-1 - 1}{(3 - 4.28) - (3 - 0.28)} \\
#     &= 0.36
# \end{align*}
# 
# Solving using the Euler method with $y'(0) = 0.36$
# 
# \begin{align*}
#     \mathbf{y}_0 &= \begin{pmatrix} 1 \\ -1 \end{pmatrix}, \\
#     \mathbf{y}_1 &= \mathbf{y}_0 + h \mathbf{f}(t_0, \mathbf{y}_0) 
#     = \begin{pmatrix} 1 \\ 0.36 \end{pmatrix} + 0.4 \begin{pmatrix} 0.36 \\ 2(0) \end{pmatrix} 
#     = \begin{pmatrix} 1.144 \\ 0.36 \end{pmatrix}, \\
#     \mathbf{y}_2 &= \mathbf{y}_1 + h \mathbf{f}(t_1, \mathbf{y}_1) 
#     = \begin{pmatrix} 1.144 \\ 0.36 \end{pmatrix} + 0.4 \begin{pmatrix} 0.36 \\ 2(0.4) \end{pmatrix} 
#     = \begin{pmatrix} 1.288 \\ 0.68 \end{pmatrix}, \\
#     \mathbf{y}_3 &= \mathbf{y}_2 + h \mathbf{f}(t_2, \mathbf{y}_2) 
#     = \begin{pmatrix} 1.288 \\ 0.68 \end{pmatrix} + 0.4 \begin{pmatrix} 0.68 \\ 2(0.8) \end{pmatrix} 
#     = \begin{pmatrix} 1.56 \\ 1.32 \end{pmatrix}, \\
#     \mathbf{y}_4 &= \mathbf{y}_3 + h \mathbf{f}(t_3, \mathbf{y}_3) 
#     = \begin{pmatrix} 1.56 \\ 1.32 \end{pmatrix} + 0.4 \begin{pmatrix} 1.32 \\ 2(1.2) \end{pmatrix} 
#     = \begin{pmatrix} 2.088 \\ 2.28 \end{pmatrix}, \\
#     \mathbf{y}_5 &= \mathbf{y}_4 + h \mathbf{f}(t_4, \mathbf{y}_4) 
#     = \begin{pmatrix} 2.088 \\ 2.28 \end{pmatrix} + 0.4 \begin{pmatrix} 2.28 \\ 2(1.6) \end{pmatrix} 
#     = \begin{pmatrix} 3 \\ 3.56 \end{pmatrix}, \\
# \end{align*}
# 
# The solutions to this boundary value problem using the Euler method with the shooting method are tabulated below.
# 
# | $t$  |  $y_1$  |  $y_2$  |
# |:----:|:-------:|:-------:|
# | 0.00 |  1.0000 |  0.3600 |
# | 0.40 |  1.1440 |  0.3600 |
# | 0.80 |  1.2880 |  0.6800 |
# | 1.20 |  1.5600 |  1.3200 |
# | 1.60 |  2.0880 |  2.2800 |
# | 2.00 |  3.0000 |  3.5600 |
# ````
# 
# `````

# `````{admonition} Exercise 5.4
# :class: note
# :name: ex5.4
#         
# Calculate the solution of the boundary value problem in [exercise 5.4](ex5.4) using the finite-difference method with a step length $h=0.4$.
# 
# ````{dropdown} Solution
# 
# \begin{align*}
#     y'' &= 2t, \\
#     \frac{y_{i-1} - 2 y_i + y_{i+1}}{h^2} &= 2 t_i \\
#     y_{i-1} - 2y_i + y_{i+1} &= 2 h^2 t_i
# \end{align*}
# 
# which can be written as the matrix equation
# 
# \begin{align*}
#     \begin{pmatrix} 
#         1 & 0 \\
#         1 & -2 & 1 \\
#         & \ddots & \ddots & \ddots \\
#         & & 1 & -2 & 1 \\
#         & & & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix} y_0 \\ y_1 \\ \vdots \\ y_{n-1} \\ y_{n} \end{pmatrix} =
#     \begin{pmatrix} 1 \\ 2 h^2 t_1 \\ \vdots \\ 2 h^2 t_{n-1} \\ 3 \end{pmatrix}
# \end{align*}
# 
# Since $h=0.4$ then $\mathbf{t} = (0, 0.4, 0.8, 1.2, 1.6, 2)$ and
# 
# \begin{align*}
#     \begin{pmatrix} 
#         1 & 0 \\
#         1 & -2 & 1 \\
#         & 1 & -2 & 1 \\
#         & & 1 & -2 & 1 \\
#         & & & 1 & -2 & 1 \\
#         & & & & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix} y_0 \\ y_1 \\ y_2 \\ y_3 \\ y_4 \\ y_5 \end{pmatrix} =
#     \begin{pmatrix} 1 \\ 0.128 \\ 0.256 \\ 0.384 \\ 0.512 \\ 3 \end{pmatrix}
# \end{align*}
# 
# Performing the forward sweep of the Thomas algorithm
# 
# \begin{align*}
#     b_1 &= 1, \\ 
#     b_2 &= b_2 - c_1 \left( \frac{a_2}{b_1} \right) = -2 - 0\left( \frac{1}{1} \right) = -2, \\
#     b_3 &= b_3 - c_2 \left( \frac{a_3}{b_2} \right) = -2 - \left( \frac{1}{-2} \right) = -1.5, \\
#     b_4 &= b_4 - c_3 \left( \frac{a_4}{b_3} \right) = -2 - \left( \frac{1}{-1.5} \right) = -1.333333, \\
#     b_5 &= b_5 - c_4 \left( \frac{a_5}{b_4} \right) = -2 - \left( \frac{1}{-1.333333} \right) = -1.25, \\
#     b_6 &= b_6 - c_5 \left( \frac{a_6}{b_5} \right) = 1 - \left( \frac{0}{-1.25} \right) = 1, \\
#     d_1 &= 1, \\
#     d_2 &= d_2 - d_1 \left( \frac{a_2}{b_1} \right) = 0.128 - 1 \left( \frac{1}{1} \right) = -0.872, \\
#     d_3 &= d_3 - d_2 \left( \frac{a_3}{b_2} \right) = 0.256 - (-0.872) \left( \frac{1}{-2} \right) = -0.18, \\
#     d_4 &= d_4 - d_3 \left( \frac{a_4}{b_3} \right) = 0.384 - (-0.18) \left( \frac{1}{-1.5} \right) = 0.264, \\
#     d_5 &= d_5 - d_4 \left( \frac{a_5}{b_4} \right) = 0.512 - (0.264) \left( \frac{1}{-1.333333} \right) = 0.71, \\
#     d_6 &= d_6 - d_5 \left( \frac{a_6}{b_5} \right) = 3 - (0.71) \left( \frac{0}{-1.25} \right) = 3, \\
# \end{align*}
# 
# Performing the back substitution step
# 
# \begin{align*}
#     y_6 &= \frac{d_6}{b_6} = \frac{3}{1} = 3, \\
#     y_5 &= \frac{d_5 - c_5 y_6}{b_5} = \frac{0.71 - 3}{-1.25} = 1.832, \\
#     y_4 &= \frac{d_4 - c_4 y_5}{b_4} = \frac{0.264 - 1.832}{-1.333333} = 1.176, \\
#     y_3 &= \frac{d_3 - c_3 y_4}{b_3} = \frac{-0.18 - 1.176}{-1.5} = 0.904, \\
#     y_2 &= \frac{d_2 - c_2 y_3}{b_2} = \frac{0.872 - 0.904}{-2} = 0.888, \\
#     y_1 &= \frac{d_1 - c_1 y_2}{b_1} = \frac{1 - 0(0.205992)}{1} = 1, \\
# \end{align*}
# 
# The solutions to this boundary value problem using the finite-difference method are tabulated below.
# 
# | $t$  |  $y$   |
# |:----:|:------:|
# | 0.00 | 0.0000 |
# | 0.40 | 0.8880 |
# | 0.80 | 0.9040 |
# | 1.20 | 0.1760 |
# | 1.60 | 1.8320 |
# | 2.00 | 3.0000 |
# 
# ````
# 
# `````

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

def euler(f, tspan, y0, h):
    nsteps = int((tspan[1] - tspan[0]) / h)
    neq = len(y0)
    t = np.arange(nsteps + 1) * h
    y = np.zeros((nsteps + 1, neq))
    y[0,:] = y0
    for n in range(nsteps):
        y[n+1,:] = y[n,:] + h * f(t[n], y[n,:])
        
    return t, y 


def f(t, y):
    return np.array([y[1], 2 * t])

# Define BVP parameters
tspan = [0, 2]  # boundaries of the t domain
bvals = [1, 3]  # boundary values
h = 0.4         # step length
svals = [1, -1]

# Solve IVP
ysols = []
for s in svals:
    t, y = euler(f, tspan, [bvals[0], s], h)
    ysols.append(y)
    
    print("\n|  t   |   y1    |   y2    |")
    print("|:----:|:-------:|:-------:|")
    for n in range(len(t)):
        print(f"| {t[n]:4.2f} | {y[n,0]:7.4f} | {y[n,1]:7.4f} |")
        
# Calculate next guess
s = svals[-1] - (bvals[1] - ysols[-1][-1,0]) * (svals[-1] - svals[-2]) / ((bvals[1] - ysols[-1][-1,0]) - (bvals[1] - ysols[-2][-1,0]))

# Solve IVP
t, y = euler(f, tspan, [bvals[0], s], h)

print("\n|  t   |   y1    |   y2    |")
print("|:----:|:-------:|:-------:|")
for n in range(len(t)):
    print(f"| {t[n]:4.2f} | {y[n,0]:7.4f} | {y[n,1]:7.4f} |")


# `````{admonition} Exercise 5.5
# :class: note
# :name: ex5.5
# 
# The exact solution to the boundary value problem in [exercise 5.2](ex5.2) is $y = \frac{1}{3} t^3 - \frac{1}{3} t + 1$. Write a Python program to perform the numerical calculations for exercises [5.3](ex5.3) and [5.4](ex5.4) and produce a plot of the numerical solutions and the exact solutions on the same set of axes. Comment on your plot.
# 
# ````{dropdown} Solution
# Code
# 
# ```python
# import numpy as np
# import matplotlib.pyplot as plt
# 
# def euler(f, tspan, y0, h):
#     nsteps = int((tspan[1] - tspan[0]) / h)
#     neq = len(y0)
#     t = np.arange(nsteps + 1) * h
#     y = np.zeros((nsteps + 1, neq))
#     y[0,:] = y0
#     for n in range(nsteps):
#         y[n+1,:] = y[n,:] + h * f(t[n], y[n,:])
#         
#     return t, y 
# 
# 
# def shooting_method(solver, f, tspan, bvals, h, tol=1e-4):
#     s, so, go = 1, 2, 1
#     for _ in range(10):
#         t, y = solver(f, tspan, [bvals[0], s], h)
#         g = bvals[1] - y[-1,0]
#         s, so, go = s - g * (s - so) / (g - go), s, g
#         if abs(s - so) < tol:
#             break
#         
#     return t, y
# 
# 
# def tridiagonal_solver(a, b, c, d):
#     n = len(b)
#     for i in range(1, n):
#         w = a[i] / b[i-1]
#         b[i] -= w * c[i-1]
#         d[i] -= w * d[i-1]
#     
#     x = np.zeros(n)
#     x[-1] = d[-1] / b[-1]
#     for i in range(n - 2, -1, -1):
#         x[i] = (d[i] - c[i] * x[i+1]) / b[i]
# 
#     return x
# 
# 
# def f(t, y):
#     return np.array([y[1], 2 * t])
# 
# 
# def exact(t):
#     return 1 / 3 * t ** 3 - 1 / 3 * t + 1
# 
#     
# # Define BVP parameters
# tspan = [0, 2]  # boundaries of the t domain
# bvals = [1, 3]  # boundary values
# h = 0.4         # step length
# 
# # Solve BVP using the shooting method
# t, y_euler = shooting_method(euler, f, tspan, bvals, h)
#     
# # Solve BVP using the finite-difference method
# n = int((tspan[1] - tspan[0]) / h) + 1
# t = np.arange(n) * h
# a, b, c, d = [np.zeros(n) for _ in range(4)]
# b[::n-1] = 1
# d[::n-1] = bvals
# for i in range(1, n - 1):
#     a[i] = 1
#     b[i] = -2
#     c[i] = 1
#     d[i] = 2 * h ** 2 * t[i]
#         
# y_fdm = tridiagonal_solver(a, b, c, d)
#     
#  # Calculate exact solution
# t_exact = np.linspace(tspan[0], tspan[1], 200)
# y_exact = exact(t_exact)
# 
# # Plot solutions
# fig, ax = plt.subplots(figsize=(8, 6))
# plt.plot(t_exact, y_exact, "k", label="Exact")
# plt.plot(t, y_euler[:,0], "bo-", label="Euler method")
# plt.plot(t, y_fdm, "ro-", label="Finite-difference method")
# plt.xlabel("$t$", fontsize=14)
# plt.ylabel("$y$", fontsize=14)
# plt.legend()
# plt.show()
# 
# from myst_nb import glue
# glue("ex5.5_plot", fig, display=False)
# ```
# 
# Plot
# 
# ```{glue:} ex5.5_plot
# ```
# 
# The finite-difference method gives significantly more accurate solutions than the Euler method. This is because the finite-difference used a second-order approximation whereas the Euler method is only first-order. We would expect a more accurate method such as the RK2 method to give similar solutions to the finite-difference method.
# 
# ````

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

def euler(f, tspan, y0, h):
    nsteps = int((tspan[1] - tspan[0]) / h)
    neq = len(y0)
    t = np.arange(nsteps + 1) * h
    y = np.zeros((nsteps + 1, neq))
    y[0,:] = y0
    for n in range(nsteps):
        y[n+1,:] = y[n,:] + h * f(t[n], y[n,:])
        
    return t, y 


def shooting_method(solver, f, tspan, bvals, h, tol=1e-4):
    s, so, go = 1, 2, 1
    for _ in range(10):
        t, y = solver(f, tspan, [bvals[0], s], h)
        g = bvals[1] - y[-1,0]
        s, so, go = s - g * (s - so) / (g - go), s, g
        if abs(s - so) < tol:
            break
        
    return t, y


def tridiagonal_solver(a, b, c, d):
    n = len(b)
    for i in range(1, n):
        w = a[i] / b[i-1]
        b[i] -= w * c[i-1]
        d[i] -= w * d[i-1]
    
    x = np.zeros(n)
    x[-1] = d[-1] / b[-1]
    for i in range(n - 2, -1, -1):
        x[i] = (d[i] - c[i] * x[i+1]) / b[i]

    return x


def f(t, y):
    return np.array([y[1], 2 * t])


def exact(t):
    return 1 / 3 * t ** 3 - 1 / 3 * t + 1

    
# Define BVP parameters
tspan = [0, 2]  # boundaries of the t domain
bvals = [1, 3]  # boundary values
h = 0.4         # step length

# Solve BVP using the shooting method
t, y_euler = shooting_method(euler, f, tspan, bvals, h)
    
# Solve BVP using the finite-difference method
n = int((tspan[1] - tspan[0]) / h) + 1
t = np.arange(n) * h
a, b, c, d = [np.zeros(n) for _ in range(4)]
b[::n-1] = 1
d[::n-1] = bvals
for i in range(1, n - 1):
    a[i] = 1
    b[i] = -2
    c[i] = 1
    d[i] = 2 * h ** 2 * t[i]
        
y_fdm = tridiagonal_solver(a, b, c, d)
    
# Calculate exact solution
t_exact = np.linspace(tspan[0], tspan[1], 200)
y_exact = exact(t_exact)

# Plot solutions
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(t_exact, y_exact, "k", label="Exact")
plt.plot(t, y_euler[:,0], "bo-", label="Euler method")
plt.plot(t, y_fdm, "ro-", label="Finite-difference method")
plt.xlabel("$t$", fontsize=14)
plt.ylabel("$y$", fontsize=14)
plt.legend()
plt.show()

from myst_nb import glue
glue("ex5.5_plot", fig, display=False)

