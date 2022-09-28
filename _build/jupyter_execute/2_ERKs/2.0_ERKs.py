#!/usr/bin/env python
# coding: utf-8

# (erk-chapter)=
# # Explicit Runge-Kutta Methods
# 
# **Learning Outcomes**
# 
# On successful completion of this chapter readers will be able to:
# 
# - identify a [Runge-Kutta method](rk-definition) and express it using a [Butcher tableau](butcher-tableau-definition);
# - distinguish between [explicit and implicit](explicit-and-implicit-rk-methods-section) Runge-Kutta methods;
# - [derive](rk2-derivation-section) an explicit Runge-Kutta method;
# - apply [explicit Runge-Kutta methods to solve an initial value problem](applying-erk-methods-to-solve-ivps-section).
# 
# ---
# (general-form-of-a-RK-method-section)=
# ## General form of a Runge-Kutta method
# 
# Runge-Methods are the most popular family of methods used to solve Ordinary Differential Equations (ODEs). They are known as **single step methods** because they update the solution for the next step $y_{n+1}$ using information from the single step $y_n$. The other type of method for solving ODEs are [**linear multistep methods**](https://en.wikipedia.org/wiki/Linear_multistep_method) that calculate $y_{n+1}$ using information from multiple steps $y_n ,y_{n-1} ,y_{n-2} ,\ldots $
#    
# ````{admonition} Definition: General form of a Runge-Kutta method
# :class: note
# :name: rk-definition
# 
# The general form of a Runge-Kutta method for solving the initial value problem $y' =f(t,y)$, $t \in [a, b]$, $y_0 = y(a)$ is
# 
# ```{math}
# :label: rk-equation
# \begin{align}
#     y_{n+1} &=y_n +h\sum_{i=1}^s b_i k_i,\\
#     k_i &=f(t_n +c_i h,y_n +h\sum_{j=1}^s a_{ij} k_j ),
# \end{align}
# ```
# 
# where
# - $t_n$ is some value of the independent variable $t$;
# - $y_n=y(t_n)$ is the value of the function $y$ at $t=t_n$;
# - $h=t_{n+1}-t_n$ is the **step length**;
# - $s$ is the number of **stages** of the method;
# - $k_i$ are intermediate **stage values** used to calculate $y_{n+1}$;
# - $a_{ij}$, $b_i$ and $c_i$ are coefficients that define a particular Runge-Kutta method.
# 
# ````
# 
# (butcher-tableau-section)=
# ### Butcher tableau
# 
# Runge-Kutta methods are often summarised in a **Butcher tableau** named after the New Zealand mathematician [John Butcher](https://en.wikipedia.org/wiki/John_C._Butcher).
# 
# ````{admonition} Definition: Butcher Tableau
# :class: note
# :name: butcher-tableau-definition
# 
# A Butcher tableau is a table of values containing the coefficients $a_{ij}$, $b_i$ and $c_i$ for a Runge-Kutta method
# 
# \begin{align*}
#     \begin{array}{c|c}
#         \mathbf{c} & A \\ \hline
#         & \mathbf{b}^T
#     \end{array}
# \end{align*}
# 
# where $A$ is a matrix of $a_{ij}$ coefficients and $\mathbf{b}$ and $\mathbf{c}$ are column vectors containing the $b_i$ and $c_i$ coefficients
# 
# \begin{align*}
#     A &= \begin{pmatrix}
#         a_{11} & a_{12} & \cdots & a_{1s} \\
#         a_{21} & a_{22} & \cdots & a_{2s} \\
#         \vdots & \vdots & \ddots & \vdots \\
#         a_{s1} & a_{2s} & \cdots & a_{ss}
#     \end{pmatrix}, &
#     \mathbf{b} &= \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_s \end{pmatrix}, &
#     \mathbf{c} &= \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_s \end{pmatrix},
# \end{align*}
# 
# i.e.,
# 
# \begin{align*}
#     \begin{array}{c|cccc}
#         c_1  & a_{11}  & a_{12}  & \cdots  & a_{1s} \\
#         c_2  & a_{21}  & a_{22}  & \cdots  & a_{2s} \\
#         \vdots  & \vdots  & \vdots  & \ddots  & \vdots \\
#         c_s  & a_{s1}  & a_{s2}  & \cdots  & a_{ss} \\ \hline
#         & b_1  & b_2  & \cdots  & b_s 
#     \end{array}
# \end{align*}
# ````
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
# 
# ````{dropdown} Solution
# 
# The general form of a two-stage Runge-Kutta method is
# 
# ```{math}
# :label: butcher-tableau-example-equation-2
# 
# \begin{align*}
#     y_{n+1} &= y_n + h(b_1 k_1 + b_2 k_2), \\
#     k_1 &= f(t_n + c_1 h, y_n + h(a_{11}k_1 + a_{12}k_2)), \\
#     k_2 &= f(t_n + c_2 h, y_n + h(a_{21}k_1 + a_{22}k_2)). 
# \end{align*}
# ```
# 
# Comparing equations {eq}`butcher-tableau-example-equation-1` and {eq}`butcher-tableau-example-equation-2` we can see that $a_{11} = a_{12} = a_{22} = 0$, $b_1 = b_2 = 1$, $c_1 = 0$ and $c_2 = 1$ therefore the Butcher tableau for this method is
# 
# \begin{align*}
#     \begin{array}{c|cc}
#         0 & 0 & 0 \\
#         1 & 1 & 0 \\ \hline
#         & \frac{1}{2} & \frac{1}{2}
#     \end{array}
# \end{align*}
# ````
# `````
# 
# (explicit-and-implicit-rk-methods-section)=
# ## Explicit and implicit Runge-Kutta methods
# 
# Expanding out the stage values from equation {eq}`rk-equation` we see that the stage values of a general Runge-Kutta method are
# 
# \begin{align*}
#     k_1 &=f(t_n +c_1 h,y_n +h(a_{11} k_1 +a_{12} k_2 +\cdots +a_{1s} k_s ),\\
#     k_2 &=f(t_n +c_2 h,y_n +h(a_{21} k_1 +a_{22} k_2 +\cdots +a_{2s} k_s ),\\
#     &\vdots \\
#     k_s &=f(t_n +c_s h,y_n +h(a_{s1} k_1 +a_{s2} k_s +\cdots +a_{ss} k_s ).
# \end{align*} 
# 
# The first equation where we are calculating $k_1$ includes $k_1$ on the right-hand side and in the second equation where we are calculating $k_2$ includes $k_2$ on the right-hand side and so on. These are examples of [**implicit functions**](https://en.wikipedia.org/wiki/Implicit_function) and Runge-Kutta methods where the stage values are expressed using implicit functions are known as **Implicit Runge-Kutta (IRK)** methods. To calculate the solution of the stage values of an IRK method involves solving a system of equations ([see Implicit Runge-Kutta Methods](irk-chapter)).
# 
# If the summation in the stage value $k_i$ in equation {eq}`rk-equation` is altered so the upper limit to the sum is $i-1$, i.e.,
# 
# \begin{align*}
#     k_i = f(t_n + c_1 h,y_n + h\sum_{j=1}^{i-1} a_{ij} k_j)
# \end{align*}
# 
# and let $c_1 = 0$ then we have the following equations for calculating the stage values
# 
# \begin{align*}
#     k_1 &=f(t_n ,y_n),\\
#     k_2 &=f(t_n +c_2 h,y_n +ha_{21} k_1 ),\\
#     k_3 &=f(t_n +c_3 h,y_n +h(a_{31} k_1 +a_{32} k_2 )),\\
#     &\vdots \\
#     k_s &=f(t_n +c_s h,y_n +h(a_{s1} k_1 +a_{s2} k_s +\cdots +a_{s,s-1} k_{s-1} )).
# \end{align*}
# 
# These stage values are **explicit functions** where the subject of the equation does not appear on the right-hand side. Runge-Kutta methods where the stages values are calculated using explicit functions are known as **Explicit Runge Kutta (ERK)** methods. These are easier to compute than implicit Runge-Kutta methods because the stage values can be calculated sequentially in order, i.e., $k_1$ can be calculated using $t_n$ and $y_n$ and then used to calculate $k_2$ and so on. However for some ODEs explicit methods require a very small value for the step length and and we must then use implicit methods (see the chapter on [Stability)](stability-chapter) for more detail).
# 
# ### Butcher tableau for explicit and implicit Runge-Kutta methods
# 
# Explicit and implicit Runge-Kutta methods can be easily distinguished by looking at their Butcher tableaux. The $A$ matrix in the top right region of a Butcher tableau for an explicit method is lower-triangular whereas for an implicit method the main-diagonal and upper triangular elements are non-zero.
# 
# ````{grid}
# :gutter: 3
# 
# ```{grid-item-card} Explicit Runge-Kutta method
# \begin{align*}
#     \begin{array}{c|ccccc}
#         0 &  &  &  &  & \\
#         c_2  & a_{21}  &  &  &  & \\
#         c_3  & a_{31}  & a_{32}  &  &  & \\
#         \vdots  & \vdots  & \vdots  & \ddots  &  & \\
#         c_s  & a_{s1}  & a_{s2}  & \cdots  & a_{s,s-1}  & \\ \hline
#         & b_1  & b_2  & \cdots  & b_{s-1}  & b_s 
#     \end{array}
# \end{align*}
# 
# ```
# 
# ```{grid-item-card} Implicit Runge-Kutta method
# \begin{align*}
#     \begin{array}{c|ccccc}
#         c_1  & a_{11}  & a_{12}  & a_{13}  & \cdots  & a_{1s} \\
#         c_2  & a_{21}  & a_{22}  & a_{23}  & \cdots  & a_{2s} \\
#         c_3  & a_{31}  & a_{32}  & a_{33}  & \cdots  & a_{3s} \\
#         \vdots  & \vdots  & \vdots  & \vdots  & \ddots  & \vdots \\
#         c_s  & a_{s1}  & a_{s2}  & a_{s3}  & \cdots  & a_{ss} \\ \hline
#          & b_1  & b_2  & b_3  & \cdots  & b_s 
#     \end{array}
# \end{align*}
# ```
# 
# ````
