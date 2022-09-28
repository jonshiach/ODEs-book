#!/usr/bin/env python
# coding: utf-8

# (applying-erk-methods-to-solve-ivps-section)=
# # Solving initial value problems using explicit Runge-Kutta methods
# 
# Recall that the [general form of an explicit Runge-Kutta method](general-form-of-a-RK-method-section) is
# 
# \begin{align*}
#     y_{n+1} &= y_n + h(b_1k_1 + b_2k_2 + \cdots + b_sk_s), \\
#     k_1 &= f(t_n, y_n), \\
#     k_2 &= f(t_n + c_2h, y_n + ha_{21}k_1), \\
#     k_3 &= f(t_n + c_3h, y_n + h(a_{31}k_1 + a_{32}k_2), \\
#     &\vdots \\
#     k_s &= f(t_n + c_sh, y_n + h(a_{s1}k_1 + a_{s2}k_2 + \cdots + a_{s,s-1}k_{s-1}).
# \end{align*}
# 
# To apply the an explicit Runge-Kutta method to solve an initial value problem we calculate the stage values $k_1, k_2, \dots, k_s$ using the known values of $t_n$ and $y_n$ and the step length $h$. Then the solution over one step $y_{n+1}$ is then calculated using $k_1, k_2, \ldots, k_s$.
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
# 
# ```{dropdown} Solution
# 
# The RK4 method is
# 
# \begin{align*}
#     y_{n+1} &= y_n + \frac{h}{6}(k_1 + 2k_2 + 3k_3 + k_4), \\
#     k_1 &= f(t_n, y_n), \\
#     k_2 &= f(t_n + \frac{1}{2}h, y_n + \frac{1}{2}hk_1), \\
#     k_3 &= f(t_n + \frac{1}{2}h, y_n + \frac{1}{2}hk_2), \\
#     k_4 &= f(t_n + h, y_n + hk_3).
# \end{align*}
# 
# Since $t\in[0,1]$ and $h=0.2$ then the number of steps required is
# 
# $$n = \operatorname{int}\left(\frac{1 - 0}{0.2}\right) = 5, $$
# 
# and the $t$ values are 
# 
# $$\mathbf{t} = (0, 0.2, 0.4, 0.6, 0.8, 1.0).$$
# 
# The ODE function is $f(t, y) = ty$ and the initial value is $y_0 = 1$ so using equation {eq}`rk4-equation`
# 
# \begin{align*}
#     k_1 &= f(t_0, y_0) = (0.0)(1) = 0, \\
#     k_2 &= f(t_0 + \frac{1}{2}h, y_0 + \frac{1}{2}hk_1) \\
#     &= (0.0 + \frac{1}{2}(0.2))(1 + \frac{1}{2}(0.2)(0)) \\
#     &= 0.1, \\
#     k_3 &= f(t_0 + \frac{1}{2}h, y_0 + \frac{1}{2}hk_2) \\
#     &= (0.0 + \frac{1}{2}(0.2))(1 + \frac{1}{2}(0.2)(0.1)) \\
#     &= 0.101, \\
#     k_4 &= f(t_0 + h, y_0 + hk_2) \\
#     &= (0.0 + h)(1 + 0.2(0.1)) \\
#     &= 0.101, \\
#     y_1 &= y_0 + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4) \\
#     &= 1 + \frac{0.2}{6}(0 + 2(0.1) + 2(0.101) + 0.204040) \\
#     &= 1.020201, \\
#     \\
#     k_1 &= f(t_1, y_1) = (0.2)(1.020201) = 0.204040, \\
#     k_2 &= f(t_1 + \frac{1}{2}h, y_1 + \frac{1}{2}hk_1) \\
#     &= (0.2 + \frac{1}{2}(0.2))(1.020201 + \frac{1}{2}(0.2)(0.204040)) \\
#     &= 0.312182, \\
#     k_3 &= f(t_1 + \frac{1}{2}h, y_1 + \frac{1}{2}hk_2) \\
#     &= (0.2 + \frac{1}{2}(0.2))(1.020201 + \frac{1}{2}(0.2)(0.312182)) \\
#     &= 0.315426, \\
#     k_4 &= f(t_1 + h, y_1 + hk_2) \\
#     &= (0.2 + h)(1.020201 + 0.2(0.312182)) \\
#     &= 0.315426, \\
#     y_2 &= y_1 + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4) \\
#     &= 1.020201 + \frac{0.2}{6}(0.204040 + 2(0.312182) + 2(0.315426) + 0.433315) \\
#     &= 1.083287, \\
#     \\
#     k_1 &= f(t_2, y_2) = (0.4)(1.083287) = 0.433315, \\
#     k_2 &= f(t_2 + \frac{1}{2}h, y_2 + \frac{1}{2}hk_1) \\
#     &= (0.4 + \frac{1}{2}(0.2))(1.083287 + \frac{1}{2}(0.2)(0.433315)) \\
#     &= 0.563309, \\
#     k_3 &= f(t_2 + \frac{1}{2}h, y_2 + \frac{1}{2}hk_2) \\
#     &= (0.4 + \frac{1}{2}(0.2))(1.083287 + \frac{1}{2}(0.2)(0.563309)) \\
#     &= 0.569809, \\
#     k_4 &= f(t_2 + h, y_2 + hk_2) \\
#     &= (0.4 + h)(1.083287 + 0.2(0.563309)) \\
#     &= 0.569809, \\
#     y_3 &= y_2 + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4) \\
#     &= 1.083287 + \frac{0.2}{6}(0.433315 + 2(0.563309) + 2(0.569809) + 0.718349) \\
#     &= 1.197217, \\
#     \\
#     k_1 &= f(t_3, y_3) = (0.6)(1.197217) = 0.718330, \\
#     k_2 &= f(t_3 + \frac{1}{2}h, y_3 + \frac{1}{2}hk_1) \\
#     &= (0.6 + \frac{1}{2}(0.2))(1.197217 + \frac{1}{2}(0.2)(0.718330)) \\
#     &= 0.888335, \\
#     k_3 &= f(t_3 + \frac{1}{2}h, y_3 + \frac{1}{2}hk_2) \\
#     &= (0.6 + \frac{1}{2}(0.2))(1.197217 + \frac{1}{2}(0.2)(0.888335)) \\
#     &= 0.900235, \\
#     k_4 &= f(t_3 + h, y_3 + hk_2) \\
#     &= (0.6 + h)(1.197217 + 0.2(0.888335)) \\
#     &= 0.900235, \\
#     y_4 &= y_3 + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4) \\
#     &= 1.197217 + \frac{0.2}{6}(0.718330 + 2(0.888335) + 2(0.900235) + 1.101811) \\
#     &= 1.377126, \\
#     \\
#     k_1 &= f(t_4, y_4) = (0.8)(1.377126) = 1.101701, \\
#     k_2 &= f(t_4 + \frac{1}{2}h, y_4 + \frac{1}{2}hk_1) \\
#     &= (0.8 + \frac{1}{2}(0.2))(1.377126 + \frac{1}{2}(0.2)(1.101701)) \\
#     &= 1.338567, \\
#     k_3 &= f(t_4 + \frac{1}{2}h, y_4 + \frac{1}{2}hk_2) \\
#     &= (0.8 + \frac{1}{2}(0.2))(1.377126 + \frac{1}{2}(0.2)(1.338567)) \\
#     &= 1.359885, \\
#     k_4 &= f(t_4 + h, y_4 + hk_2) \\
#     &= (0.8 + h)(1.377126 + 0.2(1.338567)) \\
#     &= 1.359885, \\
#     y_5 &= y_4 + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4) \\
#     &= 1.377126 + \frac{0.2}{6}(1.101701 + 2(1.338567) + 2(1.359885) + 1.649103) \\
#     &= 1.648717.
# \end{align*}
# ```
# ````
# 
# (rk4-python-code)=
# ## Python code
# 
# The Python code below defines a function called `rk4()` which computes the solution to an initial value problem using the RK4 method. Note that the function is very similar to the function for the [RK2 method](rk2-python-code).

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return t * y


def exact(t):
    return np.exp(t ** 2 / 2)


def rk4(f, tspan, y0, h):
    nsteps = int((tspan[1] - tspan[0]) / h)
    neq = len(y0)
    t = np.arange(nsteps + 1) * h
    y = np.zeros((nsteps + 1, neq))
    y[0,:] = y0
    print(r"\begin{align*}")
    for n in range(nsteps):
        k1 = f(t[n], y[n,:])
        k2 = f(t[n] + 0.5 * h, y[n,:] + 0.5 * h * k1)
        k3 = f(t[n] + 0.5 * h, y[n,:] + 0.5 * h * k2)
        k4 = f(t[n] + h, y[n,:] + h * k3)
        y[n+1,:] = y[n,:] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        print(rf"    k_1 &= f(t_{n}, y_{n}) = ({t[n]:0.1f})({y[n,0]:0.6f}) = {k1[0]:0.6f}, \\")   
        print(rf"    k_2 &= f(t_{n} + \frac{{1}}{{2}}h, y_{n} + \frac{{1}}{{2}}hk_1) \\")
        print(rf"    &= ({t[n]:0.1f} + \frac{{1}}{{2}}({h}))({y[n,0]:0.6f} + \frac{{1}}{{2}}({h})({k1[0]:0.6f})) \\")
        print(rf"    &= {k2[0]:0.6f}, \\")
        print(rf"    k_3 &= f(t_{n} + \frac{{1}}{{2}}h, y_{n} + \frac{{1}}{{2}}hk_2) \\")
        print(rf"    &= ({t[n]:0.1f} + \frac{{1}}{{2}}({h}))({y[n,0]:0.6f} + \frac{{1}}{{2}}({h})({k2[0]:0.6f})) \\")
        print(rf"    &= {k3[0]:0.6f}, \\")
        print(rf"    k_4 &= f(t_{n} + h, y_{n} + hk_2) \\")
        print(rf"    &= ({t[n]:0.1f} + h)({y[n,0]:0.6f} + {h}({k2[0]:0.6f})) \\")
        print(rf"    &= {k3[0]:0.6f}, \\")
        print(rf"    y_{n+1} &= y_{n} + \frac{{h}}{{6}}(k_1 + 2k_2 + 2k_3 + k_4) \\")
        print(rf"    &= {y[n,0]:0.6f} + \frac{{{h}}}{{6}}({k1[0]:0.6f} + 2({k2[0]:0.6f}) + 2({k3[0]:0.6f}) + {k4[0]:0.6f}) \\")
        print(rf"    &= {y[n+1,0]:0.6f}", end="")
        if n < nsteps - 1:
            print(rf", \\")
            print(r"    \\")
        else:
            print(rf".")
    
    print(r"\end{align*}")
    return t, y 

# Define IVP
tspan = [0, 1]  # boundaries of the t domain
y0 = [1]        # solution at the lower boundary
h = 0.2         # step length

# Calculate the solution to the IVP
t, y = rk4(f, tspan, y0, h)


# In[2]:


def rk4(f, tspan, y0, h):
    nsteps = int((tspan[1] - tspan[0]) / h)
    neq = len(y0)
    t = np.arange(nsteps + 1) * h
    y = np.zeros((nsteps + 1, neq))
    y[0,:] = y0
    for n in range(nsteps):
        k1 = f(t[n], y[n,:])
        k2 = f(t[n] + 0.5 * h, y[n,:] + 0.5 * h * k1)
        k3 = f(t[n] + 0.5 * h, y[n,:] + 0.5 * h * k2)
        k4 = f(t[n] + h, y[n,:] + h * k3)
        y[n+1,:] = y[n,:] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        
    return t, y 


# The computed solutions using the fourth-order explicit Runge-Kutta are plotted in {numref}`rk4-example-figure` below. 
# 
# ```{glue:figure} rk4_example_plot 
# :name: rk4-example-figure
# 
# The solutions to the initial value problem $y'=ty$, $t\in[0,1]$, $y(0)=1$ using the RK4 method with $h=0.2$.
# ```

# In[3]:


def f(t, y):
    return t * y


def exact(t):
    return np.exp(t ** 2 / 2)


# Define IVP
tspan = [0, 1]  # boundaries of the t domain
y0 = [1]        # solution at the lower boundary
h = 0.2         # step length

# Calculate the solution to the IVP
t, y = rk4(f, tspan, y0, h)

# Plot solutions
t_exact = np.linspace(tspan[0], tspan[1], 200)
y_exact = exact(t_exact)
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(t_exact, y_exact, "k", label="Exact")
plt.plot(t, y, "bo-", label="RK4")
plt.xlabel("$t$", fontsize=14)
plt.ylabel("$y$", fontsize=14)
plt.legend(fontsize=12)
plt.show()

from myst_nb import glue
glue("rk4_example_plot", fig, display=False)


# Doing a visual comparison of the solutions using the [RK2](rk2-definition) ({numref}`rk2-example-figure`) and [RK4](rk4-definition) ({numref}`rk4-example-figure`) methods it appears that the two solutions are very similar. A loglog plot of the global truncation errors for these methods and the Euler methods is shown in {numref}`rk4-gte-plot-figure`.
# 
# ```{glue:figure} rk4_gte_plot
# :name: rk4-gte-plot-figure
# 
# A loglog plot of the global truncation errors for the solutions of $y'=ty$, $y(0)=1$ using the Euler, RK2 and RK4 methods solutions.
# ```
# 
# Here we see that the fourth-order method is significantly more accurate than the second-order method and approximating the value of $n$ in $e = O(h^n)$ using the method given in equation {eq}`order-approximation-equation` gives $n = 4.09$ which indicates fourth-order convergence as expected.

# In[4]:


def euler(f, tspan, y0, h):
    nsteps = int((tspan[1] - tspan[0]) / h)
    neq = len(y0)
    t = np.arange(nsteps + 1) * h
    y = np.zeros((nsteps + 1, neq))
    y[0,:] = y0
    for n in range(nsteps):
        y[n+1,:] = y[n,:] + h * f(t[n], y[n,:])
        
    return t, y 


def rk2(f, tspan, y0, h):
    nsteps = int((tspan[1] - tspan[0]) / h)
    neq = len(y0)
    t = np.arange(nsteps + 1) * h
    y = np.zeros((nsteps + 1, neq))
    y[0,:] = y0
    for n in range(nsteps):
        k1 = f(t[n], y[n,:])
        k2 = f(t[n] + h, y[n,:] + h * k1)
        y[n+1,:] = y[n,:] + h / 2 * (k1 + k2)
        
    return t, y


def rk4(f, tspan, y0, h):
    nsteps = int((tspan[1] - tspan[0]) / h)
    neq = len(y0)
    t = np.arange(nsteps + 1) * h
    y = np.zeros((nsteps + 1, neq))
    y[0,:] = y0
    for n in range(nsteps):
        k1 = f(t[n], y[n,:])
        k2 = f(t[n] + 0.5 * h, y[n,:] + 0.5 * h * k1)
        k3 = f(t[n] + 0.5 * h, y[n,:] + 0.5 * h * k2)
        k4 = f(t[n] + h, y[n,:] + h * k3)
        y[n+1,:] = y[n,:] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        
    return t, y 

# Calculate solution for decreasing step lengths and plot the solution
hvalues = [0.2, 0.1, 0.05, 0.025]
rk4_errors, rk2_errors, euler_errors = [], [], []
for h in hvalues:
    t, y = rk4(f, tspan, y0, h)
    rk4_errors.append(abs(y_exact[-1] - y[-1,0]))
    t, y = rk2(f, tspan, y0, h)
    rk2_errors.append(abs(y_exact[-1] - y[-1,0]))
    t, y = euler(f, tspan, y0, h)
    euler_errors.append(abs(y_exact[-1] - y[-1,0]))

# Approximate the orders
print(f"\nEuler: {(np.log10(euler_errors[0]) - np.log10(euler_errors[-1])) / (np.log10(hvalues[0]) - np.log10(hvalues[-1])):0.2f}")
print(f"RK2:   {(np.log10(rk2_errors[0]) - np.log10(rk2_errors[-1])) / (np.log10(hvalues[0]) - np.log10(hvalues[-1])):0.2f}")
print(f"RK4:   {(np.log10(rk4_errors[0]) - np.log10(rk4_errors[-1])) / (np.log10(hvalues[0]) - np.log10(hvalues[-1])):0.2f}")


# Plot errors
fig, ax = plt.subplots(figsize=(8, 6))
plt.loglog(hvalues, euler_errors, 'ro-', label="Euler")
plt.loglog(hvalues, rk2_errors, 'go-', label="RK2")
plt.loglog(hvalues, rk4_errors, 'bo-', label="RK4")
plt.xlabel(r"$\log(h)$", fontsize=16)
plt.ylabel(r"$\log(e)$", fontsize=16)
plt.legend()

glue("rk4_gte_plot", fig, display=False)

