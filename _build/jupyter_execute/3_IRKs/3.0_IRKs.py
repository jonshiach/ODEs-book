#!/usr/bin/env python
# coding: utf-8

# (irk-chapter)=
# # Implicit Runge-Kutta Methods
# 
# **Learning outcomes**
# 
# On successful completion of this chapter readers will be able to:
# 
# - determine the [order of an implicit Runge-Kutta method](order-of-irk-section);
# - derive [Gauss-Legendre](gauss-legendre-derivation), [Radau](radau-derivation), [DIRK](dirk-derivation) and [SDIRK](sdirk-derivation) implicit Runge-Kutta methods;
# - apply [implicit Runge-Kutta methods to solve initial value problems](solving-ivps-using-irk-methods-section).
# 
# ---
# 
# ## Implicit Runge-Kutta methods
# 
# Runge-Kutta methods can be either an explicit or implicit methods depending on the functions used to calculate the stage values. We have seen in the [previous chapter on explicit methods](erk-chapter) that they are straightforward to apply, however they are not always suitable for solving ODEs that are [**stiff**](stiffness-section). This is why we need to also consider implicit methods.
# 
# Recall that the [general form of a Runge-Kutta method](rk-definition) to solve a first-order ODE $y'=f(t,y)$ is
# 
# \begin{align*}
#    y_{n+1} &=y_n + h \sum_{i=1}^s b_i k_i,\\
#    k_i &=f(t_n +c_i h,y_n + h \sum_{j=1}^s a_{ij} k_j).
# \end{align*}
# 
# Expanding out the stage value functions we have
# 
# \begin{align*}
#     k_1 &= f(t_n + c_1 h, y_n + h (a_{11} k_1 + a_{12} k_2 + \cdots + a_{1s} k_s), \\
#     k_2 &= f(t_n + c_2 h, y_n + h (a_{21} k_1 + a_{22} k_2 + \cdots + a_{2s} k_s), \\
#     & \vdots \\
#     k_s &= f(t_n + c_1 h, y_n + h (a_{s1} k_1 + a_{s2} k_2 + \cdots + a_{ss} k_s).
# \end{align*}
# 
# The value of $k_1$ appears withing the function on the right-hand side of $k_1$ and similar for the other stage values. This means these functions are implicit functions hence we have an implicit Runge-Kutta method. The Butcher tableau for an implicit method is
# 
# \begin{align*}
#    \begin{array}{c|cccc}
#       c_1  & a_{11}  & a_{12}  & \cdots  & a_{1s} \\
#       c_2  & a_{21}  & a_{22}  & \cdots  & a_{2s} \\
#       \vdots  & \vdots  & \vdots  & \ddots  & \vdots \\
#       c_s  & a_{s1}  & a_{s2}  & \cdots  & a_{ss} \\ \hline
#        & b_1  & b_2  & \cdots  & b_s 
#       \end{array}
# \end{align*}
# 
# Note that the $A$ matrix in the upper right-hand region of an implicit method can have non-zero elements in them main diagonal and upper triangular region whereas the $A$ matrix for an explicit method has non-zero elements in the lower triangular region only.
# 
# (order-of-irk-section)=
# ## Determining the order of an implicit Runge-Kutta method
# 
# One of the differences between implicit and explicit methods is that an implicit method can achieve the same accuracy as an explicit method but using fewer stages. To determine the order of an implicit method we need to consider the **order conditions** that govern the values of $a_{ij}$, $b_i$ and $c_i$.
# 
# ````{admonition} Definition: $B(k)$, $C(k)$ and $D(k)$ order conditions 
# :class: note
# :name: Bk_Ck_Dk_order_conditions
# 
# \begin{align*}
#   B(k): && \sum_{i=1}^s b_i c_i^{j-1} = & \frac{1}{j}, & j&=1\ldots k, \\
#   C(k): && \sum_{j=1}^s a_{ij} c_j^{\ell-1} = & \frac{1}{\ell}c_i^{\ell} , & i&=1 \ldots s, & \ell &=1 \ldots k,\\
#   D(k): && \sum_{i=1}^s b_i c_i^{\ell-1} a_{ij} = & \frac{1}{\ell}b_j (1-c_j^{\ell}), & j&=1 \ldots s, & \ell &=1 \ldots k.
# \end{align*}
# ````
# 
# If $G(k)$ represents the fact that a given implicit method has order $k$ then it can be shown that 
# 
# $$B(k)\; \mathsf{and} \; C\left( \left\lfloor \frac{k}{2} \right\rfloor \right) \; \mathsf{and} \; D \left( \left\lfloor \frac{k}{2} \right\rfloor \right) \Longrightarrow G(k)$$
# 
# So to determine the order of an IRK method we need to do the following
# 
# - Find the highest value of $k$ for which $B(k)$ is satisfied;
# - If $C(\lfloor \frac{k}{2} \rfloor)$ and $D(\lfloor \frac{k}{2} \rfloor)$ are satisfied 
#     - the IRK has order $k$;
# - else 
#     - reduce $k$ by 1 and check $C(\lfloor \frac{k}{2} \rfloor)$ and $D(\lfloor \frac{k}{2} \rfloor)$ again. 
# 
# If no value of $k>0$ satisfies $B(k)$, $C(\lfloor \frac{k}{2} \rfloor)$ and $D(\lfloor \frac{k}{2} \rfloor)$ then it isn't a valid Runge-Kutta method.
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
# 
# ```{dropdown} Solution
# 
# Checking the $B(k)$ order condition:
# 
# \begin{align*}
#   j &=1: & LHS &= b_1 c_1^0 + b_2 c_2^0 = \frac{1}{2}(1)+\frac{1}{2}(1)=1, \\
#   && RHS &= 1,\\
#   j &=2: & LHS &= b_1 c_1^1 + b_2 c_2^1 = \frac{1}{2}\left(\frac{1}{4}\right)+\frac{1}{2}\left(\frac{3}{4}\right)=\frac{1}{2}, \\
#   && RHS &= \frac{1}{2},\\
#   j &=3: & LHS &= b_1 c_1^2 + b_2 c_2^2 = \frac{1}{2}{\left(\frac{1}{4}\right)}^2 +\frac{1}{2}{\left(\frac{3}{4}\right)}^2 = \frac{5}{16}, \\
#   && RHS &= \frac{1}{3}.
# \end{align*}
# 
# So since $LHS=RHS$ up to $j=2$ the $B(2)$ condition is satisfied. Now we need to check whether $C(\lfloor \frac{2}{2} \rfloor)=C(1)$ order condition is satisfied. Note that here $\ell=1$ so we only need to check $i = 1$ and $2$ but if $k \geq 2$ then we would need to check $i = 1, 2, \ldots, s$ for each $\ell = 1, 2, \ldots$.
# 
# \begin{align*}
#   i &= 1, & LHS&=a_{11} c_1^0 + a_{12} c_2^0 =\frac{1}{4}(1)+0(1)=\frac{1}{4}, \\
#   && RHS &= \frac{1}{\ell}c_1^{\ell} =\frac{1}{4},\\
#   i &= 2, & LHS&=a_{21} c_1^0 + a_{22} c_2^0 =\frac{1}{2}(1)+\frac{1}{4}(1)=\frac{3}{4}, \\
#   && RHS &= \frac{1}{\ell}c_2^{\ell} =\frac{3}{4}.
# \end{align*}
# 
# So the $C(1)$ order condition is satisfied. Now we need to check whether the $D(1)$ order condition is satisfied
# 
# \begin{align*}
#   j &= 1, & LHS &= b_1 c_1^0 a_{11} +b_2 c_2^0 a_{21} =\frac{1}{2}(1)\left(\frac{1}{4}\right)+\frac{1}{2}(1)\left(\frac{1}{2}\right)=\frac{3}{8},\\
#   && RHS &= \frac{1}{\ell}b_1 (1-c_1^{\ell})=\frac{1}{2}\left(1-\frac{1}{4}\right)=\frac{3}{8},\\
#   j&=2, & LHS&=b_1 c_1^0 a_{12} +b_2 c_2^0 a_{22} =\frac{1}{2}(1)(0)+\frac{1}{2}(1)\left(\frac{1}{4}\right)=\frac{1}{8},\\
#   && RHS&=\frac{1}{\ell }b_2 (1 - c_2^{\ell})=\frac{1}{2}\left(1-\frac{3}{4}\right)=\frac{1}{8}.
# \end{align*}
# 
# So the $D(k)$ order condition is satisfied up to $k=2$. Therefore since $B(2)$, $C(1)$ and $D(1)$ are all satisfied this IRK method is order 2.
# ``` 
# ````
