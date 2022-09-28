#!/usr/bin/env python
# coding: utf-8

# # Stability
# 
# ``````{div} full-width
# 
# - **Stability:** method is considered **stable** if $|\tau_{n+1} - \tau_n | \leq 1$ where $\tau_n = |y_n - \bar{y_n}|$ is the local truncation error, $y_n$ and $\bar{y_n}$ are the computed and exact solutions.
# 
# - **Stiffness:** an ODE is considered stiff if a numerical method requires a very small step length $h$ in order for the method to be stable.
# 
# - **Stiffness ratio:** $S = \dfrac{\max_i(|\lambda_i|)}{\min_i(|\lambda_i|)}$. If $S$ is large the ODE is stiff.
# 
# ````{admonition} Example 4.1
# :class: seealso
# 
# Determine the stiffness ration of the following ODE
# 
# $$ y'' + 1001 y' + 1000 y = 0.$$
# ````
# 
# - **Stability function $R(z)$:** is the rate of growth over a single step of the method when applied to calculate the solution of an ODE of the form $y'=\lambda t$ where $z = h \lambda$, i.e., $y_{n+1} = R(z)y_n$
# 
# - **Absolute stability:** a method is considered to be absolutely stable if $|R(z)| \leq 1$ for $z\in \mathbb{C}$.
# 
# - **Region of absolute stability:** the set of $z\in \mathbb{C}$ for which a method is absolutely stable.
# 
# - **Stability function of an ERK method:** $R(z) = 1+\displaystyle\sum_{k=0}^{\infty} \mathbf{b}^T A^k \mathbf{e}\,z^{k+1}$
# 
# - **Order of an ERK method:** the maximum degree that the stability function agrees with $\exp(z) = \displaystyle\sum_{n=0}^\infty \frac{z^n}{n!}$
# 
# `````{admonition} Example 4.2
# :class: seealso
# :name: erk-stability-example
# 
# An explicit Runge-Kutta method is defined by the following Butcher tableau
# 
# \begin{align*}\begin{array}{c|cccc}
# 0 &  &  &  & \\
# \frac{1}{2} & \frac{1}{2} &  &  & \\
# \frac{3}{4} & 0 & \frac{3}{4} &  & \\
# 1 & \frac{2}{9} & \frac{1}{3} & \frac{4}{9} & \\ 
# \hline
# & \frac{7}{24} & \frac{1}{4} & \frac{1}{3} & \frac{1}{8}
# \end{array}\end{align*}
# 
# &emsp; (i) &emsp; Determine the stability function for this Runge-Kutta method and hence find its order;
# 
# &emsp; (ii) &emsp; plot the region of absolute stability and that of an explicit method on the same order on the same set of axes;
# 
# &emsp; (iii) &emsp; comment on the region of absolute stability of the two methods.
# `````
# 
# - **Stability function of an IRK method:** $R(z) = \dfrac{\det (I - zA + z\mathbf{e}\mathbf{b}^T)}{\det(I - zA)}$ where $\mathbf{e}\mathbf{b}^\mathrm{T}$ is a diagonal matrix with the elements of $\mathbf{b}$ on the main diagonal.
# 
# - **A-stability:** the region of absolute stability includes all points in the left-hand complex plane. The conditions for A-stability are:
# 
#     - All roots of $\det(I - zA)$ have positive real parts;
#     - $Q(iy)Q(-iy)-P(iy)P(-iy) \geq 0$ for all $y\in \mathbb{R}$.
# 
# `````{admonition} Example 4.3
# :class: seealso
# :name: a-stability-example
# 
# An implicit Runge-Kutta method is defined by the following Butcher tableau
# 
# \begin{align*}
#     \begin{array}{c|cc}
#     \frac{1}{3} & \frac{5}{12} & -\frac{1}{12} \\
#     1 & \frac{3}{4} & \frac{1}{4} \\ \hline
#     & \frac{3}{4} & \frac{1}{4}
#     \end{array}
# \end{align*}
# 
# Determine whether this method is A-stable and plot the region of absolute stability.
# `````
# 
# ``````
