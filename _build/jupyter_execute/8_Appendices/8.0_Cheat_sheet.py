#!/usr/bin/env python
# coding: utf-8

# # Cheat Sheet
# 
# ## Initial value problems
# 
# 
# ````{glossary}
# Ordinary Differential Equation (ODE)
#     An [ODE](ode-section) is an equation of the for 
#     
#     $$y^{(n)} = f(t, y, y', y'', \ldots, y^{(n-1)}),$$
#     
#     where $y(t)$ is a function of the independent variable $t$. 
# 
# Initial Value Problem (IVP)    
#     An [initial value problem](ivp-definition) is an ODE where the solution at some initial state is known
#     
#     $$y' = f(t, y), \qquad t \in [a, b], \qquad y(a) = \alpha.$$
# 
# The Taylor series
#     The [Taylor series](taylor-series-section) is a series expansion of a function $f(t)$
#     
#     $$f(t + h) = \sum_{n=0}^\infty \frac{h^n}{n!}f^{(n)}(t).$$
# 
# Truncating the Taylor series
#     [Truncating the Taylor series](taylor-series-section) is where all terms after the $n$th derivative in the Taylor series are omitted. 
#     
#     $$f(t + h) \approx f(t) + hf'(t) + \frac{h^2}{2!} f''(t) + \cdots + \frac{h^n}{n!} f^{(n)}(t).$$
# 
# The Euler method
#     The [Euler method](euler-method-section) is a first-order accurate numerical method for solving an initial value problem of the form $y' = f(t, y)$, $t\in [a, b]$, $t_0 = \alpha$
#     
#     $$y_{n+1} = y_n + h f(t_n, y_n),$$
#     
#     $t_n$ is a value of $t$ at step $n$, $y_n = y(t_n)$ and $h = t_{n+1} - t_n$ is the step length.
#     
# Local Truncation Error (LTE)
#     The [local truncation error](local-truncation-error-section) is the error in the calculation of a single step of a numerical method assuming that the previous values are exact.
#     
# Global Truncation Error (GTE)
#     The [global truncation error](global-truncation-error-section) is the error that has accumulated over all previous steps of a numerical method assuming the initial solution was known to be exact.
#     
# Big-O notation
#     $f(h) = O(h^n)$ means that as $h \to 0$ then $f(h) \to 0$ at least as fast as $h^n \to 0$.
# 
# Order of a method
#     The [order](global-truncation-error-section) of a method is the degree of $O(h^n)$ for the global truncation error of the method.
#     
# Reducing higher order ODE to first-order ODEs
#     An $n$th order ODE $y^{(n)} = f(t, y, y', y'', \ldots, y^{(n-1)}$ can be written as a system of $n$ first order ODES such that
#     
#     \begin{align*}
#         y_1' &= y_2, \\
#         y_2' &= y_3, \\
#         & \vdots \\
#         y_n' &= f(t, y_1, y_2, \ldots, y_n).
#     \end{align*}
# ````
# ---
# 
# ## Explicit Runge-Kutta methods
# 
# ````{glossary}
# General form of a Runge-Kutta method
#     The [general form of a Runge-Kutta method](general-form-of-a-RK-method-section) is
#     
#     \begin{align*}
#         y_{n+1} &= y_n + h\sum_{i=1}^s b_i k_i, \\
#         k_i &= f(t_n + c_ih, y_n + h \sum_{j=1}^s a_{ij} k_i,
#     \end{align*}
#     
#     where $k_i$ are intermediate stage valeus.
#     
# Butcher tableau
#     Runge-Kutta methods can be represented using a [Butcher tableau](butcher-tableau-section) such that
#     
#     \begin{align*}
#         \begin{array}{c|c}
#             \mathbf{c} & A \\ \hline
#             & \mathbf{b}^\mathrm{T}
#         \end{array}
#     \end{align*}
#     
#     where $[A]_{ij} = a_{ij}$, $\mathbf{b} = (b_1, \ldots, b_s)^\mathrm{T}$ and $\mathbf{c} = (c_1, \ldots, c_s)^\mathrm{T}$.
#     
# Explicit Runge-Kutta method
#     An [explicit Runge-Kutta method](explicit-and-implicit-rk-methods-section) is a method where $c_1 = 0$, $a_{ij} = 0$ where $i \leq j$ such that the stage values are explicit functions.
#     
# Order conditions of a Runge-Kutta method
#     Comparing the $n$th order Taylor series expansion of $y' = f(t, y)$ to that of the general form of a Runge-Kutta method gives the [order conditions](rk2-derivation-section) which need to be satisfied for an $n$th order Runge-Kutta method.
#   
# The row sum condition
#     The values of $a_{ij}$ and $c_i$ must satisfy the [row sum condition](row-sum-condition) which is $c_i = \displaystyle_{j=1}^s a_{ij}$.
#     
# The second-order explicit Runge-Kutta method (RK2)
#     *The* [second-order explicit Runge-Kutta method](rk2-derivation-example) has the Butcher tableau
#     
#     \begin{align*}
#         \begin{array}{c|cc}
#             0 & 0 \\ 
#             1 & 1 \\ \hline
#             & \frac{1}{2} & \frac{1}{2}
#         \end{array}
#     \end{align*}
#     
# The fourth-order explicit Runge-Kutta method (RK4)
#     *The* [fourth-order explicit Runge-Kutta method](rk4-definition) has the Butcher tableau
#     
#     \begin{align*}
#         \begin{array}{c|cccc}
#             0 & 0 \\
#             \frac{1}{2} & \frac{1}{2} \\
#             \frac{1}{2} & 0 & \frac{1}{2} \\ 
#             1 & 0 & 0 & 1 \\ \hline
#             & \frac{1}{6} & \frac{1}{3} & \frac{1}{3} & \frac{1}{6}
#         \end{array}
#     \end{align*}
# ````

# ---
# ## Implicit Runge-Kutta methods
# 
# ````{glossary}
# Implicit Runge-Kutta methods (IRK)
#     An [implicit Runge-Kutta method](irk-chapter) is where the stage values are implicit functions.
#     
# Order of an implicit Runge-Kutta method
#     Implicit Runge-Kutta methods can have a higher order of accuracy for the same number of stages as an explicit Runge-Kutta method. The [order of an implicit Runge-Kutta methods](order-of-irk-section) is the highest value of $k$ for which the order conditions $B(k)$, $C(\lfloor \frac{k}{2} \rfloor)$ and $D(\lfloor \frac{k}{2} \rfloor)$ are satisfied where
#     
#     \begin{align*}
#         B(k): && \sum_{i=1}^s b_i c_i^{j-1} = & \frac{1}{j}, & j&=1\ldots k, \\
#         C(k): && \sum_{j=1}^s a_{ij} c_j^{\ell-1} = & \frac{1}{\ell}c_i^{\ell} , & i&=1 \ldots s, & \ell &=1 \ldots k,\\
#         D(k): && \sum_{i=1}^s b_i c_i^{\ell-1} a_{ij} = & \frac{1}{\ell}b_j (1-c_j^{\ell}), & j&=1 \ldots s, & \ell &=1 \ldots k.
#     \end{align*}
#     
# Gauss-Legendre implicit Runge-Kutta methods
#     An $s$-stage [Gauss-Legendre](gauss-legendre-derivation) implicit Runge-Kutta method has order $k = 2s$ and are derived by setting $c_i$ to be the roots of the Legendre polynomial 
#     
#     $$P_n(t) = \displaystyle\sum_{k=0}^n \binom{n}{k} \binom{n+k}{k} (t - 1)^k,$$
#     
#     and $b_i$ and $a_{ij}$ are chosen to satisfy the $B(k)$ and $C(\lfloor \frac{k}{2} \rfloor)$ order conditions. For 
#     
# Radau IA implicit Runge-Kutta method
#     An $s$-stage [Radau IA](radau-derivation) implicit Runge-Kutta method has order $k = 2s - 1$ and are derived by setting $c_i$ to be the roots of $P_s(t) + P_{s-1}(t)$ and the values of $b_i$ and $a_{ij}$ are chosen to satisfy the order condition $D(k)$.
#     
# Radau IIA implicit Runge-Kutta method 
#     An $s$-stage [Radau IIA](radau-derivation) implicit Runge-Kutta method has order $k = 2s - 1$  are derived by setting $c_i$ to be the roots of $P_s(t) - P_{s-1}(t)$ and the values of $b_i$ and $a_{ij}$ are chosen to satisfy the order condition $C(k)$.
#     
# Diagonally Implicit Runge-Kutta (DIRK) methods
#     An [DIRK](dirk-derivation) method is an implicit Runge-Kutta method where $a_{ij} = 0$ where $i < j$ and is derived by satisfying the $B(k)$ and $C(\lfloor \frac{k}{2} \rfloor)$ and 
#     
#     $$\mathbf{b}^T A \mathbf{c} = \frac{1}{k!}.$$
#     
#     The stage values of a DIRK method can be calculated sequentially.
#     
# Singly Diagonally Implicit Runge-Kutta (SDIRK) methods
#     An [SDIRK](sdirk-derivation) method an implicit Runge-Kutta method where $a_{ij} = 0$ where $i < j$ and is derived by satisfying the $B(k)$, $C(\lfloor \frac{k}{2} \rfloor)$ and $D(\lfloor \frac{k}{2} \rfloor)$ order conditions.
#     
# Computing the stage values of an implicit Runge-Kutta method
#     [Computing the stage values](solving-ivps-using-irk-methods-section) of an implicit Runge-Kutta method requires the solution to a system of nonlinear equations. This is typically done using Newton's method but can also be done using the Gauss-Seidel method.
# ````

# ---
# ## Stability
# 
# ````{glossary}
# 
# Stability
#     A method is [stable](stability-definition) if the local truncation errors do not increase from one step to the next.
#     
# Stiffness
#     An ODE is [stiff](stiffness-definition) if it requires a very small value of the step length $h$ in order for a method to remain stable.
#     
# Stiffness ratio
#     The [stiffness ratio](stiffness-ratio-definition) gives a measure to whether an system of ODEs is stiff and is calculated using
#     
#     \begin{align*}
#         S = \frac{\max_i(|\lambda_i|)}{\min_i(|\lambda_i|)}.
#     \end{align*}
#     
#     If $S$ is large then the system is considered stiff.
#     
# Test ODE
#     The stability of numerical methods for solving ODEs can be analysed by considering the simple [test ODE](stability-functions-section) $y' = \lambda \lambda y$.
# 
# Stability function
#     The [stability function](stability-function-definition) $R(z)$ for a method is the change of the solution over a single step of the method when used to solve the test ODE
#     
#     $$y_{n+1} = R(z) y_n.$$
#     
# Absolute stability
#     A method is considered [absolutely stable](absolute-stability-section) if $|R(z)| \leq 1$ for $z \in \mathbb{C}$.
#     
# Region of absolute stability
#     The [region of absolute stability](region-of-absolute-stability-definition) is the set of values of $z$ for which the method is absolutely stable. 
#     
# Interval of absolute stability
#     The [interval of absolute stability](interval-of-absolute-stability-section) is the range of values of $h$ for which a method is absolutely stable.
# 
# Stability function of an explicit Runge-Kutta method
#     The [stability function of an explicit Runge-Kutta method](erk-rz-section) can be determined using
#     
#     \begin{align*}
#         R(z)=1+\sum_{k=0}^{\infty} \mathbf{b}^T A^k \mathbf{e}\,z^{k+1} =1+\mathbf{b}^T \mathbf{e}\,z+\mathbf{b}^T A\mathbf{e}\,z^2 +\mathbf{b}^T A^2 \mathbf{e}\,z^3 + \cdots
#     \end{align*}
#     
# Order of an explicit Runge-Kutta method
#     The order of an explicit Runge-Kutta method is the order of the highest term in the stability function for that method that agrees with the series expansion of $e^z$
#     
#     \begin{align*}
#         e^z = \sum_{k=0}^{\infty} \frac{1}{k!} z^k = 1 + z + \frac{1}{2!}z^2 + \frac{1}{3!}z^3 + \frac{1}{4!}z^4 + \cdots
#     \end{align*}
#     
# Stability function of an implicit Runge-Kutta method
#     The [stability function of an implicit Runge-Kutta method](implicit-rz-section) can be determined using
#     
#     \begin{align*}
#         R(z) = \frac{\det (I - zA + z\mathbf{e}\mathbf{b}^T)}{\det(I - zA)}.
#     \end{align*}
#     
# A-stability
#     An implicit method is considered [A-stable](A-stability) if its region of absolute stability includes all points on the left-hand side of the complex plane.
#     
# Conditions for A-stability
#     For a method to be A-stable it must satisfied the following [conditions](a-stability-theorem)
#     
#     - All roots of the denominator of $R(z)$ have positive real parts
#     - $E(y)=Q(iy)Q(-iy)-P(iy)P(-iy) \geq 0$ for all $y\in \mathbb{R}$
# 
# ````

# ---
# ## Boundary Value Problems
# 
# ```{glossary}
# Two point Boundary Value Problem (BVP)
#     A [two point boundary value problem](bvp-section) is an ODE where the solutions at the lower and upper boundaries of the domain are known
#     
#     $$y'' = f(t, y), \qquad t \in [a, b], \qquad y(a) = \alpha, \qquad y(b) = \beta.$$
#     
# Uniqueness of solutions to a BVP
#     A BVP may have a [unique solution, infinitely many solutions or no solutions](existence-and-uniqueness-of-bvp-solutions-section). A BVP of the form $y'' = p(t) y' + q(t) y + r(t)$ has a unique solution if the following conditions are satisfied
#     
#     - $p(t)$, $q(t)$ and $r(t)$ are continuous on $[a, b]$;
#     - $q(t) > 0$ for all $t\in [a,b]$.
#     
# The shooting method
#     The [shooting method](shooting-method-section) for solving a BVP uses estimates of the initial value of $y'(a)$ and compares the numerical solution for $y(b)$ to the known solution $y(b)=\beta$ and changes the estimates accordingly. 
#     
# The secant method
#     The [secant method](secant-method-section) is a root finding method that can be used to calculate improved estimates in the shooting method. If $s_{i}$ and $s_{i-1}$ are current and previous guess values of $y'(a)$ then an improved guess value is
#     
#     \begin{align*}
#         s_{i+1} = s_i - g(s_i)\frac{s_i - s_{i-1}}{g(s_i) - g(s_{i-1})}.
#     \end{align*}
#     
#     where $g(s) = y'(a) - y_n$ and $y_n$ is the numerical solution for $y(b)$. 
#     
# Finite-difference approximations
#     A [finite-difference approximation](finite-difference-method-section) is an approximation of a derivative derived from the Taylor series.
# 
# Finite-difference methods
#     The [finite-difference method](finite-difference-method-section) uses finite-difference approximations to approximate a BVP using a system of linear equations (usually tridiagonal).
#    
# The Thomas algorithm
#     The [Thomas algorithm](thomas-algorithm-section) is an efficient method for solving tridiagonal systems of linear equations.
# 
# ```

# ---
# ## Direct methods
# 
# ```{glossary}
# System of linear equations
#     A [system of linear equations](systems-of-linear-equations-section) is a set of linear equations of the form $A \mathbf{x} = \mathbf{b}$ where the solution vector $\mathbf{x}$ satisfies all equations in the system.
#     
# Direct methods
#     [Direct methods](direct-methods-chapter) solve a system of linear equations using a single application of the method.
#     
# LU decomposition
#     [LU decomposition](lu-section) factorises a square matrix $A$ into a lower and upper triangular matrix $L$ and $U$ such that $A = LU$
#     \begin{align*}
#         u_{ij} &= a_{ij} - \sum_{k=1}^{i-1} \ell_{ik}u_{kj}, & i &= 1, \ldots, j, \\
#         \ell_{ij} &= \dfrac{1}{u_{jj}} \left(a_{ij} - \displaystyle \sum_{k=1}^{j-1} \ell_{ik}u_{kj}\right), & i &= j+1, \ldots, n.
#     \end{align*}
#  
# Crout's method
#     The solution of a system of linear equations $A \mathbf{x} = \mathbf{b}$ can be calculated using [Crout's method](crouts-method-section) where $L \mathbf{y} = \mathbf{b}$ is solved for $\mathbf{y}$ by forward substitution and $U \mathbf{x} = \mathbf{y}$ is solved for $\mathbf{x}$ by back substitution.
#     
# Partial pivoting
#     [Partial pivoting](partial-pivoting-section) uses row swaps to ensure that the pivot elements $a_{jj}$ have a larger absolute value that the elements in the column beneath it. 
#     
# Permutation matrix
#     The permutation matrix is calculated by performing the same row swaps as used in partial pivoting to the identity matrix. 
#     
# LUP decomposition
#     [LUP decomposition](lup-decomposition-section) factorises a square matrix $A$ into a lower and upper triangular matrices $L$ and $U$ and the permutation matrix $P$ such that $PA = LU$.
#     
# Crout's method with LUP decomposition
#     The solution of a system of linear equations $A \mathbf{x} = \mathbf{b}$ can be calculated using [Crout's method](lup-decomposition-section) where $L \mathbf{y} = P \mathbf{b}$ is solved for $\mathbf{y}$ by forward substitution and $U \mathbf{x} = \mathbf{y}$ is solved for $\mathbf{x}$ by back substitution.
#     
# Positive definite matrix
#     A matrix is [positive definite](cholesky-section) if it is symmetric and the determinants of all upper left square matrices are all positive.
#     
# Cholesky decomposition
#     [Cholesky decomposition](cholesky-definition) factorises a positive definite matrix $A$ into a lower triangular matrix $L$ such that $A = LL^\mathrm{T}$
#     \begin{align*}
#         \ell_{jj} &= \sqrt{a_{jj} - \sum_{k=1}^{j-1} \ell_{jk}^2 }, & j &= 1, \ldots, n,\\
#         \ell_{ij} &= \dfrac{1}{\ell_{jj} }\left(a_{ij} -\displaystyle \sum_{k=1}^{i-1} \ell_{ik} \ell_{jk} \right), & i &= j + 1,\ldots ,n.
#     \end{align*}
#     
# The Cholesky-Crout method
#     The solution of a system of linear equations $A \mathbf{x} = \mathbf{b}$ where $A$ is positive definite can be calculated using the [Cholesky-Crout's method](cholesky-crout-method-section) where $L \mathbf{y} = \mathbf{b}$ is solved for $\mathbf{y}$ by forward substitution and $L^\mathrm{T} \mathbf{x} = \mathbf{y}$ is solved for $\mathbf{x}$ by back substitution.
#     
# Orthogonal vectors
#     A set of vectors $\lbrace \mathbf{v}_1 ,\mathbf{v}_2 ,\mathbf{v}_3 ,\dots \rbrace$ is said to be [orthogonal](qr-section) if $\mathbf{v}_i \cdot \mathbf{v}_j =0$ for $i\not= j$. 
# 
# Orthonormal vectors
#     A set of orthogonal vectors is [orthonormal](qr-section) if the vectors are all unit vectors.
#     
# QR decomposition 
#     [QR decomposition](qr-section) factorises an $m \times n$ matrix $A$ into an orthogonal matrix $Q$ and an upper triangular matrix $R$ such that $A = QR$.
#     
# The Gram-Schmidt process
#     The [Gram-Schmidt](qr-gram-schmidt-section) process applied to a set of $n$ independent vectors $(\mathbf{a}_1 ,\mathbf{a}_2 ,\dots ,\mathbf{a}_n)$ produces a set of $n$ orthogonal vectors $(\mathbf{u}_1 ,\mathbf{u}_2 ,\dots ,\mathbf{u}_n)$ by subtracting the projection of $\mathbf{a}_i$ onto $\mathbf{u}_j$ for $j = 1, \ldots, i = 1$.
#     
# QR decomposition using the Gram-Schmidt process
#     The QR decomposition of a matrix $A$ calculated using the [Gram-Schmidt process](qr-gramschmidt-definition) is
# 
#     For $j = 1, \ldots, n$
#     \begin{align*}
#         r_{ij} &=\mathbf{q}_i \cdot \mathbf{a}_j , \qquad i = 1,\dots ,j-1,\\
#         \mathbf{u}_j &= \mathbf{a}_j - \sum_{i=1}^{j-1} r_{ij} \mathbf{q}_i ,\\
#         r_{jj} &= \| \mathbf{u}_j \|,\\
#         \mathbf{q}_j &=\frac{\mathbf{u}_j }{r_{jj}}.
#     \end{align*}
# 
# Crout's method with QR decomposition
#     The solution of a system of linear equations $A \mathbf{x} = \mathbf{b}$ where $A$ is positive definite can be calculated using the [Crout's method with QR decomposition](qr-crout-section) by solving $Rx = Q^\mathrm{T} \mathbf{b}$ using back substitution.
#     
# Householder transformations
#     [Householder transformations](qr-householder-section) reflect a vector about a line that passes through the origin.
#     
# QR decomposition using Householder transformations
#     The QR decomposition a matrix $A$ calculated using [Householder transformations](qr-householder-definition) uses the following steps.
# 
#     For $j = 1, \ldots, n$
# 
#     - $\mathbf{e} = (1, \underbrace{0, \ldots, 0}_{m-j})^T$;
#     - $\mathbf{u} = (r_{jj}, r_{j+1,j}, \ldots, r_{m,j})^T$;
#     - $\mathbf{u} = \mathbf{u} + \operatorname{sign}(r_{jj})\|\mathbf{u}\|\mathbf{e}$;
#     - $\mathbf{v} = \dfrac{\mathbf{u}}{\| \mathbf{u} \|}$;
#     - $H = \begin{pmatrix}
#             I_{j-1} & 0 \\
#             0 & I_{m-j+1} - 2 \mathbf{v}\mathbf{v}^T
#         \end{pmatrix}$;
#     - $R = H R$;
#     - $Q = Q H$.
# ```

# ---
# ## Indirect methods
# 
# ```{glossary}
# Indirect method
#     [Indirect methods](indirect-methods-chapter) is multiple applications of the method to calculate the solution to a system of linear equations. An estimate is made of the solution $\mathbf{x}^{(0)}$ and an indirect method is applied to calculate the improved estimate $\mathbf{x}^{(1)}$. The method is applied repeatedly until two successive estimates agree to some tolerance.
#   
# Jacobi method
#     The [Jacobi method](jacobi-method-section) for calculating the solution to a system of linear equations $A \mathbf{x} = \mathbf{b}$ is 
#     \begin{align*}
#         x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j = 1}^{i-1} a_{ij} x_j^{(k)} - \sum_{j = i+1}^n a_{ij} x_j^{(k)} \right).
#     \end{align*}
# 
# Gauss-Seidel method
#     The [Gauss-Seidel method](gauss-seidel-method-section) for calculating the solution to a system of linear equations $A \mathbf{x} = \mathbf{b}$ is 
#     \begin{align*}
#         x_i^{(k+1)} = \frac{1}{a_{ii} }\left(b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{(k+1)} -\sum_{j=i+1}^n a_{ij} x_j^{(k)} \right).
#     \end{align*}
#     
# The SOR method
#     The [SOR method](sor-method-section) for calculating the solution to a system of linear equations $A \mathbf{x} = \mathbf{b}$ is
#     
#     \begin{align*}
#         x_i^{(k+1)} =(1 - \omega) x_i^{(k)} + \frac{\omega}{a_{ii} }\left(b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{(k+1)} -\sum_{j=i+1}^n a_{ij} x_j^{(k)} \right),
#     \end{align*}
#     
#     where $\omega \in [0, 2]$ is a relaxation parameter.
#     
# Iteration matrix
#     The [iteration matrix](indirect-methods-chapter) for a method is the matrix $T$ such that $\mathbf{x}^{(k+1)} = T\mathbf{x}^{(k)} + \mathbf{c}$ where $\mathbf{x}^{(k)}$ and $\mathbf{x}^{(k+1)}$ are current and next estimates of the solution. The iteration matrices for the indirect methods are
#     
#     \begin{align*}
#         \textsf{Jacobi}: && T_J &= - D^{-1}(L + U),\\
#         \textsf{Gauss-Seidel}: && T_{GS} &=-(L+D)^{-1} U, \\
#         \textsf{SOR}: && T_{SOR} &=(D+\omega L)^{-1} ((1-\omega )D-\omega U),
#     \end{align*}
#     
#     where $A = L + D + U$ and $L$, $D$, and $U$ are lower, diagonal and upper triangular elements of $A$. 
#     
# Spectral radius
#     The [spectral radius](spectral-radius-definition) of a matrix is the largest absolute eigenvalue of the matrix.
#     
# Convergence of direct methods
#     A direct method will [converge](convergence-of-indirect-methods-section) to a solution if the spectral radius of the iteration matrix is less than 1. The smaller the spectral radius of the convergence matrix, the faster the convergence.
#     
# Optimum value of the relaxation parameter
#     The [optimum value of the relaxation parameter](optimum-relaxation-parameter-section) for the SOR method is the value of $\omega$ such that the spectral radius of the iteration matrix is minimised. If the coefficient matrix $A$ has all real eigenvalues then the optimum value of $\omega$ is
#     
#     \begin{align*}
#         \omega_{opt} = 1+{\left(\frac{\rho (T_J )}{1+\sqrt{1-\rho (T_J )^2 }}\right)}^2,
#     \end{align*}
#     
#     where $\rho(T_J)$ is the spectral radius of the Jacobi method iteration matrix.
# ```
