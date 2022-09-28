#!/usr/bin/env python
# coding: utf-8

# # Implicit Runge-Kutta (IRK) Methods
# 
# ``````{div} full-width
# 
# - **Order of an IRK method:** a $k$th order IRK method must satisfy the $B(k)$, $C(\lfloor \frac{k}{2} \rfloor)$ and $D(\lfloor \frac{k}{2} \rfloor)$ order conditions.
# \begin{align*}
#   B(k): && \sum_{i=1}^s b_i c_i^{j-1} = & \frac{1}{j}, & j&=1\ldots k, \\
#   C(k): && \sum_{j=1}^s a_{ij} c_j^{\ell-1} = & \frac{1}{\ell}c_i^{\ell} , & i&=1 \ldots s, & \ell &=1 \ldots k,\\
#   D(k): && \sum_{i=1}^s b_i c_i^{\ell-1} a_{ij} = & \frac{1}{\ell}b_j (1-c_j^{\ell}), & j&=1 \ldots s, & \ell &=1 \ldots k.
# \end{align*}
# 
# ````{admonition} Example 3.1
# :class: seealso
# 
# Determine the order of the following IRK method
# 
# \begin{align*}
#     \begin{array}{c|cc}
#           \frac{1}{4} & \frac{1}{4} & 0 \\
#           \frac{3}{4} & \frac{1}{2} & \frac{1}{4} \\ \hline
#           & \frac{1}{2} & \frac{1}{2}
#     \end{array}
# \end{align*}
# ````
# 
# - **Legendre polynomials:** $P_n(t)=\displaystyle\sum_{k=0}^n \binom{n}{k}\binom{n+k}{k}(t-1)^k$
# 
# 
# - **Gauss-Legendre IRK methods:** an $s$ stage method has order $k = 2s$. The $c_i$ values are the roots of the Legendre polynomial $P_s(t)$ and $a_{ij}$ and $b_i$ satisfy the $C(\lfloor \frac{k}{2} \rfloor)$ order condition.
# 
# `````{admonition} Example 3.2
# :class: seealso
# :name: fourth-order-Gauss-Legendre-method-example
# 
# Derive a fourth-order Gauss-Legendre method.
# `````
# 
# - **Radau IA IRK methods:** an $s$ stage method has order $k = 2s - 1$. The $c_i$ values are the roots of $0 = P_s(t) + P_{s-1}(t)$ and the values of $a_{ij}$ and $b_i$ satisfy the $D(k)$ order condition.
# 
# - **Radau IIA IRK methods:** an $s$ stage method has order $k = 2s - 1$. The $c_i$ values are the roots of $0 = P_s(t) - P_{s-1}(t)$ and the values of $a_{ij}$ and $b_i$ satisfy the $C(k)$ order condition.
# 
# ````{admonition} Example 3.3
# :class: seealso
# :name: radau-derivation-example
# 
# Derive a third-order Radau IA method.
# ````
# 
# - **Diagonally Implicit Runge-Kutta (DIRK) methods** have an $A$ matrix that is lower triangular with non-zero elements on the main diagonal. The coefficients of a $k$th-order DIRK method are chosen to satisfy the $B(k)$ and $C(\lfloor \frac{k}{2} \rfloor)$ order conditions along with $\mathbf{b}^T A\mathbf{c}=\dfrac{1}{k!}$.
# 
# `````{admonition} Example 3.4
# :class: seealso
# 
# Derive a 2-stage third-order DIRK method.
# `````
# 
# - **Singly Diagonally Implicit Runge-Kutta (SDIRK)** a DIRK method with the condition $a_{ii} = c_i$. 
# 
# ````{admonition} Example 3.5
# :class: seealso
# :name: sdirk-derivation-example
# 
# Derive a 2-stage third-order SDIRK method.
# ````
# 
# - **Solving IVPs using IRK methods:** the IRK method is rewritten in the form
# 
# \begin{align*}
#    y_{n+1} &= y_n + h \sum_{i=1}^s b_i f(t_n + c_i h, Y_i),\\
#    Y_i &= y_n + h \sum_{j=1}^s a_{ij} f(t_n + c_j h, Y_j).
# \end{align*}
# 
# ````{admonition} Example 3.6
# :class: seealso
# :name: irk-example-1
# 
# The third-order Radau IA implicit Runge-Kutta method is defined by the following Butcher tableau
# 
# \begin{align*}
#    \begin{array}{c|cc}
#       0 & \frac{1}{4} & -\frac{1}{4} \\
#       \frac{2}{3} & \frac{1}{4} & \frac{5}{12} \\ \hline
#       & \frac{1}{4} & \frac{3}{4}
#     \end{array}
# \end{align*}
# 
# Use this method to calculate the solution of the following initial value problem using a step length of $h=0.2$ and a convergence tolerance of $tol=10^{-4}$.
# 
# \begin{align*}
#     y' = ty, \qquad t\in [0,1], \qquad y(0)=1.
# \end{align*}
# ````
# 
# 
# ``````
