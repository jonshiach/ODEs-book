#!/usr/bin/env python
# coding: utf-8

# (finite-difference-method-section)=
# # The finite-difference method
# 
# The **finite-difference method** for solving a boundary value problem replaces the derivatives in the ODE with **finite-difference approximations** derived from the Taylor series. This results in linear system of algebraic equations that can be solved to give an approximation of the solution to the BVP.
# 
# The derivatives of $y_i$ are approximated using values of neighbouring nodes $y_{i+1}$, $y_{i-1}$ etc. using expressions derived by truncating the [Taylor series](taylor-series-definition) and rearranging to make the derivative term the subject. Some common finite-difference approximations are listed in the table below.
# 
# | Finite-difference approximation                | Order  | Name                 |
# |:-----------------------------------------------|:-------|:---------------------|
# | $y' = \dfrac{y_{i+1} - y_i}{h}$                | first  | forward difference   |
# | $y' = \dfrac{y_i - y_{i-1}}{h}$                | first  | backward difference  |
# | $y' = \dfrac{y_{i+1} - y_{i-1}}{2h}$           | second | central difference   |
# | $y'' = \dfrac{y_{i-1} - 2 y_i + y_{i+1}}{h^2}$ | second | symmetric difference |
# 
# The solution to a boundary value problem using then finite-difference method is determined by approximating the derivatives in the ODE using finite-differences. Consider the following boundary value problem
# 
# \begin{align*}
#     y'' = f(t,y), \qquad t \in [a, b], \qquad y(a) = \alpha, \qquad y(b) = \beta.
# \end{align*}
# 
# Using the symmetric difference to approximate $y''$ in the ODE we have
# 
# \begin{align*}
#     y_{i-1} - 2y_i + y_{i+1} = h^2 f(t_i ,y_i).
# \end{align*}
# 
# Since we know that $y_0 = \alpha$ and $y_n = \beta$ then the first and last equations become we have a system of $n$ equations
# 
# \begin{align*}
#     y_0 &= \alpha, \\
#     y_0 - 2y_1 + y_2 &= h^2 f(t_1, y_1), \\
#     y_1 - 2y_1 + y_3 &= h^2 f(t_2, y_2), \\
#     & \vdots \\
#     y_{n-3} - 2y_{n-2} + y_{n-1} &= h^2 f(t_{n-2}, y_{n-2}), \\
#     y_{n-2} - 2y_{n-1} + y_{n} &= h^2 f(t_{n-1}, y_{n-1}), \\
#     y_{n} &= \beta,
# \end{align*}
# 
# which can be written as the matrix equation
# 
# \begin{align*}
#     \begin{pmatrix}
#         1 & 0 &  &  \\
#         1 & -2 & 1 &  & & \\
#         & 1 & -2 & 1 & & \\
#         & & \ddots & \ddots & \ddots & \\
#         & & & 1 & -2 & 1 \\
#         & & & & 1 & -2 & 1 \\
#         & & & & & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix} y_0 \\ y_1 \\ y_2 \\ \vdots \\ y_{n-2} \\ y_{n-1} \\ y_n \end{pmatrix} =
#     \begin{pmatrix} \alpha \\ f(t_1, y_1) \\ f(t_2, y_2) \\ \vdots \\ f(t_{n-2},y_{n-2}) \\ f(t_{n-1}, y_{n-1}) \\ \beta \end{pmatrix}.
# \end{align*}
# 
# Once the linear system is defined it can be solved using LU decomposition.
# 
# ## The Thomas algorithm
# 
# The coefficient matrix for the linear system that results from the application of the second-order symmetric finite-difference approximation of $y''$ is [tridiagonal](https://en.wikipedia.org/wiki/Tridiagonal_matrix) (the only non-zero elements are on the main, lower and upper diagonals). The usual methods for solving linear systems of equations such as Gaussian elimination and LU decomposition could be applied here, however there is a more efficient method that can solve tridiagonal systems called the [**Thomas algorithm**](https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm). 
# 
# ````{admonition} Definition: The Thomas algorithm
# :class: note
# :name: thomas-method-definition
# 
# Given a tridiagonal linear system of equations of the form
# 
# \begin{align*}
#     \begin{pmatrix} 
#         b_1 & c_1 \\
#         a_2 & b_2 & c_2 \\
#         & a_3 & b_3 & \ddots \\
#         & & \ddots & \ddots & c_{n-1} \\
#         & & & a_n & b_n
#     \end{pmatrix}
#     \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ \vdots \\ x_n \end{pmatrix} =
#     \begin{pmatrix} d_1 \\ d_2 \\ d_3 \\ \vdots \\ d_n \end{pmatrix},
# \end{align*}
# 
# the solution can be found by performing a forward sweep on the $b_i$ and $d_i$ coefficients
# 
# \begin{align*}
#     b_i &= b_i - c_{i-1} \left( \frac{a_i}{b_{i-1}} \right), & i = 2, 3, \ldots, n, \\
#     d_i &= d_i - d_{i-1} \left( \frac{a_i}{b_{i-1}} \right), & i = 2, 3, \ldots, n, 
# \end{align*}
# 
# the solution is then found using back substitution
# 
# \begin{align*}
#     x_n &= \frac{d_n}{b_n}, \\
#     x_i &= \frac{d_i - c_i x_{i+1}}{b_i}, \qquad i = n-1, n-2, \ldots, 1.
# \end{align*}
# ````
# 
# ````{admonition} Example 5.4
# :class: seealso
# :name: bvp-finite-difference-example
# 
# Use the finite-difference method to solve the boundary below using a step length of $h = 0.2$
# 
# \begin{align*}
#     y'' - y' - y = 0, \qquad y(0) = 0, \qquad y(1) = 2.
# \end{align*}
# 
# **Solution**
# 
# Using a forward difference to approximate $y'$ and a symmetric difference to approximate $y''$ we have
# 
# \begin{align*}
#     \frac{y_{i-1} -2y_i +y_{i+1} }{h^2 }-\frac{y_{i+1} -y_i }{h}-y_i = 0,
# \end{align*}
# 
# which can be simplified to
# 
# \begin{align*}
#     y_{i-1} +(h-h^2 -2)y_i +(1-h)y_{i+1} = 0.
# \end{align*}
# 
# This gives the following system of linear equations
# 
# \begin{align*}
#     y_0 &= 0, \\
#     y_0 + (h - h^2 - 2) y_1 + (1 - h) y_2 &= 0, \\
#     y_1 + (h - h^2 - 2) y_2 + (1 - h) y_3 &= 0, \\
#     &\vdots \\
#     y_{n-2} + (h - h^2 - 2) y_{n-1} + (1 - h) y_n &= 0, \\
#     y_n &= 2.
# \end{align*}
# 
# which we can write the linear system as the matrix equation
# 
# \begin{align*}
#     \begin{pmatrix}
#         1 & 0 & &  &  & \\
#         1 & h-h^2 -2 & 1-h &  &  & \\
#         &  \ddots  & \ddots  & \ddots  & \\
#         &  & 1 & h-h^2 -2 & 1-h \\
#         &  &  & 0 & 1
#     \end{pmatrix} 
#     \begin{pmatrix} y_0 \\ y_1 \\ \vdots \\ y_{n-1} \\ y_n \end{pmatrix}  =
#     \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \\ 2  \end{pmatrix}.
# \end{align*}
# 
# If we use a step length of $h=0.2$ we have
# 
# \begin{align*}
#     \mathbf{t} = (0, 0.2, 0.4, 0.6, 0.8, 1),
# \end{align*}
# 
# and
# 
# \begin{align*}
#     \begin{pmatrix}
#         1 & 0 \\
#         1 & -1.84 & 0.8 \\
#         & 1 & -1.84 & 0.8 \\
#         & & 1 & -1.84 & 0.8 \\
#         & & & 1 & -1.84 & 0.8 \\
#         & & & & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix} y_0 \\ y_1 \\ y_2 \\ y_3 \\ y_4 \\ y_5 \end{pmatrix} = 
#     \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 2 \end{pmatrix}.
# \end{align*}
# 
# Performing the forward sweep of the Thomas algorithm
# 
# \begin{align*}
#     b_1 &= 1, \\ 
#     b_2 &= b_2 - c_1 \left( \frac{a_2}{b_1} \right) = -1.84 - 0.8 \left( \frac{1}{1} \right) = -2.64, \\
#     b_3 &= b_3 - c_2 \left( \frac{a_3}{b_2} \right) = -1.84 - 0.8 \left( \frac{1}{-2.64} \right) = -1.405217, \\
#     b_4 &= b_4 - c_3 \left( \frac{a_4}{b_3} \right) = -1.84 - 0.8 \left( \frac{1}{-1.405217} \right) = -1.270693, \\
#     b_5 &= b_5 - c_4 \left( \frac{a_5}{b_4} \right) = -1.84 - 0.8 \left( \frac{1}{-1.270693} \right) = -1.210422, \\
#     b_6 &= b_6 - c_5 \left( \frac{a_6}{b_5} \right) = 1 - 0.8 \left( \frac{0}{-1.210422} \right) = 1, \\
#     d_1 &= 0, \\
#     d_2 &= d_2 - d_1 \left( \frac{a_2}{b_1} \right) = 0 - 0 \left( \frac{1}{1} \right) = 0, \\
#     d_3 &= d_3 - d_2 \left( \frac{a_3}{b_2} \right) = 0 - 0 \left( \frac{1}{-2.64} \right) = 0, \\
#     d_4 &= d_4 - d_3 \left( \frac{a_4}{b_3} \right) = 0 - 0 \left( \frac{1}{-1.405217} \right) = 0, \\
#     d_5 &= d_5 - d_4 \left( \frac{a_5}{b_4} \right) = 0 - 0 \left( \frac{1}{-1.270693} \right) = 0, \\
#     d_6 &= d_6 - d_5 \left( \frac{a_6}{b_5} \right) = 2 - 0 \left( \frac{0}{-1.270693} \right) = 2, \\
# \end{align*}
# 
# Performing the back substitution
# 
# \begin{align*}
#     y_6 &= \frac{d_6}{b_6} = \frac{2}{1} = 2, \\
#     y_5 &= \frac{d_5 - c_5 y_6}{b_5} = \frac{0 - 0.8(2)}{-1.210422} = 1.321853, \\
#     y_4 &= \frac{d_4 - c_4 y_5}{b_4} = \frac{0 - 0.8(1.321853)}{-1.270693} = 0.832209, \\
#     y_3 &= \frac{d_3 - c_3 y_4}{b_3} = \frac{0 - 0.8(0.832209)}{-1.405217} = 0.473782, \\
#     y_2 &= \frac{d_2 - c_2 y_3}{b_2} = \frac{0 - 0.8(0.473782)}{-2.64} = 0.205992, \\
#     y_1 &= \frac{d_1 - c_1 y_2}{b_1} = \frac{0 - 0(0.205992)}{1} = 0, \\
# \end{align*}
# 
# 
# The solutions to this boundary value problem using the finite-difference method are tabulated below.
# 
# | $t$  |  $y$   | Exact  |  Error   |
# |:----:|:------:|:------:|:--------:|
# | 0.00 | 0.0000 | 0.0000 | 0.00e+00 |
# | 0.20 | 0.2060 | 0.2213 | 1.53e-02 |
# | 0.40 | 0.4738 | 0.5014 | 2.76e-02 |
# | 0.60 | 0.8322 | 0.8658 | 3.36e-02 |
# | 0.80 | 1.3219 | 1.3494 | 2.76e-02 |
# | 1.00 | 2.0000 | 2.0000 | 0.00e+00 |
# 
# ````
# 
# ## Python code
# 
# The code below calculates the solution to the boundary value problem in  [example 5.4](bvp-finite-difference-example). The coefficient arrays `a`, `b` and `c` along with the constant vector `d` are defined for this problem and the `tridiagonal_solver()` function is used to solve the linear system. Note that the values in `a`, `b`, `c` and `d` are specific to the problem being solved and will need to be changed when solving other boundary value problems.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

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
    
    
def exact(t):
    return (2 * np.exp((1 - np.sqrt(5)) * (t - 1) / 2) * (np.exp(np.sqrt(5) * t) -1)) / (np.exp(np.sqrt(5)) - 1)
 

# Define BVP parameters
tspan = [0, 1]  # boundaries of the t domain
bvals = [0, 2]  # boundary values
h = 0.2         # step length

# Define linear system
n = int((tspan[1] - tspan[0]) / h) + 1
t = np.arange(n) * h
a, b, c, d = [np.zeros(n) for _ in range(4)]
b[::n-1] = 1
d[::n-1] = bvals
for i in range(1, n - 1):
    a[i] = 1
    b[i] = h - h ** 2 - 2
    c[i] = 1 - h
    d[i] = 0
        
# Solve linear system
y = tridiagonal_solver(a, b, c, d)

# Print table of solution values
print("|  t   |   y    | Exact  |  Error   |")
print("|:----:|:------:|:------:|:--------:|")
for n in range(len(t)):
    print(f"| {t[n]:4.2f} | {y[n]:6.4f} | {exact(t[n]):6.4f} | {abs(exact(t[n]) - y[n]):6.2e} |")
    
# Plot solution
t_exact = np.linspace(0, tspan[1], 200)
y_exact = exact(t_exact)
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(t_exact, y_exact, "k-", label="Exact")
plt.plot(t, y, "bo-", label=f"Finite-difference method")
plt.xlabel("$t$", fontsize=14)
plt.ylabel("$y$", fontsize=14)
plt.legend(fontsize=12)
plt.show()


# In[2]:


from myst_nb import glue
glue("bvp_fdm_plot", fig, display=False)


# ## Accuracy vs number of nodes
# 
# The solutions seen in [example 5.4](bvp-finite-difference-example) seem to show that the finite-difference method produces reasonably accurate results for this boundary value problem. One way to improve on the accuracy of our solution is to increase the number of nodes used.
# 
# Consider the solution of the following BVP using the finite-difference method
# 
# \begin{align*}
#     y'' + 3ty' + 7y = \cos (2t), \qquad y(0) = 1, \qquad y(3) = 0.
# \end{align*}
# 
# Using forward and symmetric differences to approximate $y'$ and $y''$ respectively gives
# 
# \begin{align*}
#     \frac{y_{i-1} - 2y_i + y_{i+1}}{h^2} + 3t_i \left( \frac{y_{i+1} - y_i}{h}\right) + 7y_i &= \cos(2t_i) \\
#     y_{i-1} + (7h^2 - 3ht_i - 2)y_i + (1 + 3ht_i)y_{i+1} &= h^2 \cos(2t_i).
# \end{align*}
# 
# So the linear system is
# 
# \begin{align*}
#     \begin{pmatrix} 
#         1 & 0 \\
#         1 & 7h^2 - 3ht_1 - 2 & 1 + 3ht_1 \\
#         & \ddots & \ddots & \ddots \\
#         && 1 & 7h^2 - 3ht_{N-1} - 2 & 1 + 3ht_{N-1} \\
#         &&& 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix} y_0 \\ y_1 \\ \vdots \\ y_{N-1} \\ y_N \end{pmatrix} \\
#     = \begin{pmatrix} 1 \\ h^2 \cos(2t_1) \\ \vdots \\ h^2 \cos(2t_{N-1}) \\ 0 \end{pmatrix}.
# \end{align*}
# 
# The solution of this BVP is shown in {numref}`bvp-fdm-accuracy-figure-1` for $h=0.05$ and $h = 0.005$. Since we used a first-order approximation for $y'$ the error for this method is $O(h)$ and we expect the solution using $h=0.005$ to be more accurate. 
# 
# ```{glue:figure} bvp_fdm_accuracy_plot_1
# :name: "bvp-fdm-accuracy-figure-1"
# 
# Solutions to the boundary value problem $y'' + 3ty' + 7y = \cos (2t)$, $t \in [0,3]$, $y(0) = 1$, $y(3) = 0$ using first-order finite-difference approximations with $h=0.05$ and $h=0.005$.
# ```
# 
# To obtain a more accurate solution, instead of increasing the number of nodes we could use the [central difference approximation](finite-difference-method-section) (which is second-order accurate) to approximate $y'$
# 
# \begin{align*}
#     \frac{y_{i-1} - 2y_i + y_{i+1}}{h^2} + 3t_i\left( \frac{y_{i+1} - y_{i-1}}{2h} \right) + 7y_i &= \cos(2t_i) \\
#     (2 - 3ht_i)y_{i-1} + (14h^2 - 4)y_i + (2 + 3ht_i)y_{i+1} &= 2h^2 \cos(2t_i).
# \end{align*}
# 
# So the linear system for the second-order finite-difference method is
# 
# \begin{align*}
#     \begin{pmatrix} 
#         1 & 0 \\
#         2 - 3ht_1 & 14h^2 - 4 & 2 + 3ht_1 \\
#         & \ddots & \ddots & \ddots \\
#         && 2 - 3ht_{N-1} & 14h^2 - 4 & 2 + 3ht_{N-1} \\
#         &&& 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix} y_0 \\ y_1 \\ \vdots \\ y_{N-1} \\ y_N \end{pmatrix} \\
#     = \begin{pmatrix} 1 \\ 2h^2 \cos(2t_1) \\ \vdots \\ 2h^2 \cos(2t_{N-1}) \\ 0 \end{pmatrix}.
# \end{align*}
# 
# The solution using the second-order finite difference method with $h=0.05$ has been plotted against the first-order solution using $h=0.05$ and $h=0.005$ in {numref}`bvp-fdm-accuracy-figure-2`. The second order solution gives good agreement with the first order solution using 10 times fewer nodes.
# 
# ```{glue:figure} bvp_fdm_accuracy_plot_2
# :name: "bvp-fdm-accuracy-figure-2"
# 
# Solutions to the boundary value problem $y'' + 3ty' + 7y = \cos (2t)$, $t \in [0,3]$, $y(0) = 1$, $y(3) = 0$ using first-order and second-order finite-difference approximations with $h=0.05$ and $h=0.005$.
# ```

# In[3]:


# Define BVP parameters
tspan = [0, 3]         # boundaries of the t domain
bvals = [1, 0]         # boundary values
hvals = [0.05, 0.005]  # step lengths

tsol, ysol = [], []
for h in hvals:

    # Define linear system (first-order)
    n = int((tspan[1] - tspan[0]) / h) + 1
    t = np.arange(n) * h
    a, b, c, d = [np.zeros(n) for _ in range(4)]
    b[::n-1] = 1
    d[::n-1] = bvals
    for i in range(1, n-1):
        a[i] = 1
        b[i] = 7 * h ** 2 - 3 * h * t[i] - 2
        c[i] = 1 + 3 * h * t[i]
        d[i] = h ** 2 * np.cos(2 * t[i])

    # Solve linear system
    y = tridiagonal_solver(a, b, c, d)
    ysol.append(y)
    tsol.append(t)

# Solve using second-order method
# Define linear system (second-order)
h = hvals[0]
n = int((tspan[1] - tspan[0]) / h) + 1
t = np.arange(n) * h
a, b, c, d = [np.zeros(n) for _ in range(4)]
b[::n-1] = 1
d[::n-1] = bvals
for i in range(1, n - 1):
    a[i] = 2 - 3 * h * t[i]
    b[i] = 14 * h ** 2 - 4
    c[i] = 2 + 3 * h * t[i]
    d[i] = 2 * h ** 2 * np.cos(2 * t[i])

# Solve linear system
y = tridiagonal_solver(a, b, c, d)
ysol.append(y)
tsol.append(t)

# Plot solution (first-order only)
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(tsol[0], ysol[0], "b-", label=f"first-order ($h={hvals[0]})$")
plt.plot(tsol[1], ysol[1], "r-", label=f"first-order ($h={hvals[1]})$")
plt.xlabel("$t$", fontsize=14)
plt.ylabel("$y$", fontsize=14)
plt.legend(fontsize=12)
plt.show()

from myst_nb import glue
glue("bvp_fdm_accuracy_plot_1", fig, display=False)

# Plot solution (first and second-order)
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(tsol[0], ysol[0], "b-", label=f"first-order ($h={hvals[0]}$)")
plt.plot(tsol[1], ysol[1], "r-", label=f"first-order ($h={hvals[1]}$)")
plt.plot(tsol[2], ysol[2], "g-", label=f"second-order ($h={h}$)")
plt.xlabel("$t$", fontsize=14)
plt.ylabel("$y$", fontsize=14)
plt.legend(fontsize=12)
plt.show()

glue("bvp_fdm_accuracy_plot_2", fig, display=False)

