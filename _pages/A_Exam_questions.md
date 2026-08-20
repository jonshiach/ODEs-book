# Examination Questions

The following are example examination questions that are similar in style and scope to the ones that you can expect to see in your examination. You are advised to work through these in preparation for the examination. The examination takes place in a PC lab where you will be permitted access to Python (Jupyter Notebook or Spyder), MATLAB and Excel. You are advised to familiarise yourself with one or more to help you answer the questions.

---

## Explicit Runge-Kutta Methods

```````{exercise} Exam Question 1
:label: erk-exam-1

(a) An explicit Runge-Kutta method is expressed using the Butcher tableau below.

$$ \begin{align*}
   \begin{array}{c|cccc}
   0 & 0 \\
   \frac{1}{4} & \frac{1}{4} \\
   \frac{1}{2} & 0 & \frac{1}{2} \\
   1 & 1 & -2 & 2 \\ \hline
   & \frac{1}{6} & 0 & \frac{2}{3} & \frac{1}{6}
   \end{array}
\end{align*} $$

Use this Runge-Kutta method with a step length of $h = 0.2$ to solve the following IVP

$$ \begin{align*}
   y' &= t - 2 y, & t &\in [0, 1], & y(0) &= 2.  
\end{align*} $$

<div style="text-align: right">[10 marks]</div>

``````{dropdown} Solution
$$ \begin{align*}
   \mathbf{t} &= (0, 0.2, 0.4, 0.6, 0.8, 1), \\
   \mathbf{y} &= (2, 1.3584, 0.9612, 0.7279, 0.6045, 0.5547).
\end{align*} $$

`````{tab-set}
````{tab-item} Python
```python
import numpy as np

def f(t, y): 
return t - 2 * y

h = 0.2
nsteps = 5

t = np.arange(0, 1 + h, h)
y = np.zeros(t.shape)

for n in range(nsteps):
k1 = f(t[n], y[n])
k2 = f(t[n] + 1/4 * h, y[n] + 1/4 * h * k1)
k3 = f(t[n] + 1/2 * h, y[n] + 1/2 * h * k2)
k4 = f(t[n] + h, y[n] + h * (k1 - 2 * k2 + 2 * k3))

y[n+1] = y[n] + h / 6 * (k1 + 4 * k3 + k4)

print(t)
print(y)
```
````

````{tab-item} MATLAB
```matlab
f = @(t, y) t - 2 * y;

nsteps = 5;
h = 0.2;

t = 0 : h : 1;
y = zeros(size(t));
y(1) = 2;

for n = 1 : nsteps
k1 = f(t(n), y(n));
k2 = f(t(n) + 1/4 * h, y(n) + 1/4 * h * k1);
k3 = f(t(n) + 1/2 * h, y(n) + 1/2 * h * k2);
k4 = f(t(n) + h, y(n) + h * (k1 - 2 * k2 + 2 * k3));

y(n+1) = y(n) + h / 6 * (k1 + 4 * k3 + k4);
end

t
y
```
````
`````

Note: solutions may also be calculated using a pen and calculator or using Excel.
``````

(b) The exact solution to the IVP from part (a) is $y(t) = \frac{1}{9}(3t + 19 e^{-3t} - 1)$. Calculate the global truncation error for the numerical solution to the IVP for $y(1)$ using the Runge-Kutta method from part (a) with $h = 0.2$ and $h = 0.1$. Use your global truncation errors to estimate the order accuracy of this Runge-Kutta method.

<div style="text-align: right">[10 marks]</div>

``````{dropdown} Solution
The exact solution is $y(1) = 0.554504$ and numerical solutions are $y(1, h= 0.2) = 0.554686$ and $y(1,h = 0.1) = 0.554514$ so the GTE are

$$ \begin{align*}
   E(h = 0.2) = |0.554504 - 0.554686| = 1.82 \times 10^{-4}, \\
   E(h = 0.1) = |0.554504 - 0.554515| = 9.60 \times 10^{-5},
\end{align*} $$

therefore

$$ \text{order} \approx \frac{\log \left( \dfrac{E(h1)}{E(h2)}\right)}{\log \left( \dfrac{h_1}{h_2}\right)} = \frac{\log \left( \dfrac{1.82 \times 10^{-4}}{9.60 \times 10^{-5}} \right)}{\log \left( \dfrac{0.2}{0.1} \right)} = 4.24. $$
``````

(c) Explain in words how step size control is implemented within a Runge-Kutta method.

<div style="text-align: right">[5 marks]</div>

```{dropdown} Solution

```

```````

```````{exercise}
:label: erk-exam-2

(a) The order conditions for a fourth-order explicit Runge-Kutta method are:

$$ \begin{align*}
b_1 + b_2 + b_3 + b_4 &= 1, \\
b_2c_2 + b_3c_3 + b_4c_4 &= \frac12, \\
b_2c_2^2 + b_3c_3^2 + b_4c_4^2 &= \frac13, \\
b_2c_2^3 + b_3c_3^3 + b_4c_4^3 &= \frac14, \\
b_3a_{32}c_2 + b_4a_{42}c_2 + b_4a_{43}c_3 &= \frac{1}{6}, \\
b_3a_{32}c_2c_3 + b_4a_{42}c_2c_4 + b_4a_{43}c_3c_4 &= \frac18, \\
b_3a_{32}c_2^2 + b_4a_{42}c_2^2 + b_4a_{43}c_3^2 &= \frac{1}{12}, \\
b_4a_{43}a_{32}c_2 &= \frac{1}{24}, \\
c_2 &= a_{21}, \\
c_3 &= a_{31} + a_{32}, \\
c_4 &= a_{41} + a_{42} + a_{43}.
\end{align*} $$

Derive a fourth-order explicit Runge-Kutta method with $c_2 = \frac13$, $c_3 = \frac23$ and $c_4=1$. Write down your method in the form of a Butcher tableau.
<div style="text-align: right">[10 marks]</div>

``````{dropdown} Solution

$$ \begin{array}{c|cccc}
  0 & 0 \\
  \frac13 & \frac13 \\
  \frac23 & -\frac13 & 1 \\
  1 & 1 & -1 & 1 \\
  \hline
  & \frac18 & \frac38 & \frac38 & \frac18
\end{array} $$

`````{tab-set}
````{tab-item} Python
```python
import sympy as sp

b1, b2, b3, b4, a21, a31, a32, a41, a42, a43 = sp.symbols("b1, b2, b3, b4, a21, a31, a32, a41, a42, a43")

c2 = sp.Rational(1,3)
c3 = sp.Rational(2,3)
c4 = 1

eq1 = b1 + b2 + b3 + b4 - 1
eq2 = b2 * c2 + b3 * c3 + b4 * c4 - sp.Rational(1,2)
eq3 = b2 * c2**2 + b3 * c3**2 + b4 * c4**2 - sp.Rational(1,3)
eq4 = b2 * c2**3 + b3 * c3**3 + b4 * c4**3 - sp.Rational(1,4)
eq5 = b3 * a32 * c2 + b4 * a42 * c2 + b4 * a43 * c3 - sp.Rational(1,6)
eq6 = b3 * a32 * c2 * c3 + b4 * a42 * c2 * c4 + b4 * a43 * c3 * c4 - sp.Rational(1,8)
eq7 = b3 * a32 * c2**2 + b4 * a42 * c2**2 + b4 * a43 * c3**2 - sp.Rational(1,12)
eq8 = b4 * a43 * a32 * c2 - sp.Rational(1,24)
eq9 = c2 - a21
eq10 = c3 - a31 - a32
eq11 = c4 - a41 - a42 - a43

sp.solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10, eq11))
```
````
`````
``````

(b) &emsp; Use your method from part (a) to solve the following initial value problem using a step length of $h = 0.1$. 

$$ y' = -3ty, \qquad t \in [0, \tfrac12], \qquad y(0) = 1. $$

Present the solution as a table of $t$ and $y$ values correct to 6 decimal places.
<div style="text-align: right">[10 marks]</div>

``````{dropdown} Solution

| $t$ | $y$ |
|:--:|:--:|
| 0.0 | 1.000000 |
| 0.1 | 0.985112 |
| 0.2 | 0.941764 |
| 0.3 | 0.873714 |
| 0.4 | 0.786625 |
| 0.5 | 0.687286 |

`````{tab-set}
````{tab-item} Python
```python
import numpy as np

def rk4(f, tspan, y0, h):

    nsteps = int((tspan[1] - tspan[0]) / h)
    t = np.arange(0, tspan[1] + h, h)
    y = np.zeros(t.shape)
    y[0] = y0

    for n in range(nsteps):
        k1 = f(t[n], y[n])
        k2 = f(t[n] + 1/3 * h, y[n] + 1/3 * h * k1)
        k3 = f(t[n] + 2/3 * h, y[n] + h * (-1/3 * k1 + k2))
        k4 = f(t[n] + h, y[n] + h * (k1 - k2 + k3))

        y[n+1] = y[n] + h / 8 * (k1 + 3 * k2 + 3 * k3 + k4)

    return t, y


def f(t, y): 
    return -3 * t * y


h = 0.1
y0 = 1
tspan = [0, 1/2]

t, y = rk4(f, tspan, y0, h)

print(f"t = {t}")
print(f"y = {y}")
```
````

``````

(c) &emsp; The exact solution of the IVP from part (b) is $y = e^{-(3t^2)/2}$. Compute the global truncation errors for your Runge-Kutta method for $y(\frac12)$ with step lengths $h=0.1$ and $h = 0.05$. Use the global truncation errors to estimate the order of accuracy of your Runge-Kutta method from part (a).

<div style="text-align: right">[5 marks]</div>

``````{dropdown} Solution

The numerical solutions using the two step lengths are

$$ \begin{align*}
  y_5(h = 0.1) &= 3.47 \times 10^{-6}, \\
  y_5(h = 0.05) &= 1.97 \times 10^{-7},
\end{align*} $$

so the order estimate is

$$ \text{order} = \frac{\log \left( \frac{3.47 \times 10^{-6}}{1.97 \times 10^{-7}} \right)}{ \log \left( \frac{0.1}{0.05} \right)} = 4.14.$$

`````{tab-set}
````{tab-item}
```python
def exact(t):
    return np.exp(-3 * t**2 / 2)


h = 0.1
t, y = rk4(f, tspan, y0, h)
E1 = abs(exact(1/2) - y[-1])
print(f"E(h={h}) = {E1}")

h = 0.05
t, y = rk4(f, tspan, y0, h)
E2 = abs(exact(1/2) - y[-1])
print(f"E(h={h}) = {E2}")

order = np.log(E1 / E2) / np.log(0.1 / 0.05)
print(f"order = {order}")
```
````
`````

``````
```````

---

## Implicit Runge-Kutta Methods

````{exercise}
:label: irk-exam-1

(a) The $B(k)$ and $C(k)$ order conditions for a Runge-Kutta method are

$$ \begin{align*}
   B(k):&& \sum_{i=1}^s b_i c_i^{j-1} &= \frac{1}{j}, & j &= 1 \ldots k, \\
   C(k):&& \sum_{j=1}^s a_{ij}c_j^{\ell - 1} &= \frac{1}{\ell} c_i^\ell, & i &= 1 \ldots s, & \ell &= 1 \ldots k,
\end{align*} $$

and the $n$-order Legendre polynomial is

$$ \begin{align*}
   P_n(x) = \sum_{i=0}^n {n \choose i} {n + i \choose i} (x - 1)^i,
\end{align*} $$

where ${n \choose i}$ is the Binomial coefficient.

An $s$-stage Radau IIA method has order $2s - 1$, the $c_i$ values are the roots of $P_s(x) - P_{s-1}(x)$ and the $a_{ij}$ and $b_i$ coefficients are chosen to satisfy the $B(2s)$ and $C(s)$ order conditions respectively.

Derive a third-order Radau IIA method expressing your solution as a Butcher tableau.

<div style="text-align: right">[10 marks]</div>

```{dropdown} Solution

A third-order Radau IIA method has $s = 2$ stages. The values of $c_1$ and $c_2$ are the roots of $P_2(x) - P_1(x) = 0$

$$ \begin{align*}
   0 &= P_2(x) - P_1(x) \\
   &= 1 + {2 \choose 1}{3 \choose 1}(x - 1) + {2 \choose 2}{4 \choose 2}(x - 1)^2 - 1 - {1 \choose 1}{2 \choose 1} (x - 1) \\
   &= 6x^2 - 8x + 2 \\
   &= (3x - 1)(x - 1)
\end{align*} $$

so $c_1 = \frac{1}{3}$ and $c_2 = 1$. The $b_1$ and $b_2$ values satisfy the $B(2)$ order conditions

$$ \begin{align*}
   b_1 + b_2 &= 1, \\
   \frac{1}{3}b_1 + b_2 &= \frac{1}{2},
\end{align*} $$

so $b_1 = \frac{3}{4}$ and $b_2 = \frac{1}{4}$. The $A$ values satisfy the $C(1)$ order conditions

$$ \begin{align*}
   a_{11} + a_{12} &= \frac{1}{3}, \\
   a_{21} + a_{22} &= 1, \\
   \frac{1}{3}a_{11} + a_{12} &= \frac{1}{18}, \\
   \frac{1}{3}a_{21} + a_{22} &= \frac{1}{2}.
\end{align*} $$

Subtracting the third equation from the first gives $a_{11} = \frac{5}{12}$ so $a_{12} = -\frac{1}{12}$. Subtracting the fourth equation from the second gives $a_{21} = \frac{3}{4}$ and $a_{22} = \frac{1}{4}$. So the Butcher tableau for the third-order Radau IIA method is

$$ \begin{array}{c|cc}
   \frac{1}{3} & \frac{5}{12} & -\frac{1}{12} \\
   1 & \frac{3}{4} & \frac{1}{4} \\
   \hline
   & \frac{3}{4} & \frac{1}{4}
\end{array} $$
```

(b) A 2-stage SDIRK method is given below

$$ \begin{align*}
   \begin{array}{c|cc}
      \frac{1}{8} & \frac{1}{8} & 0 \\
      \frac{7}{8} & \frac{3}{4} & \frac{1}{8} \\ \hline
      & \frac{1}{2} & \frac{1}{2}
      \end{array}
\end{align*} $$

Write the stability function of this method and determine whether it is A-stable or not. You may find the following formulae useful:

$$ \begin{align*}
   R(z) &= \frac{\det(I - zA + z\mathbf{eb}^\mathsf{T})}{\det(I - zA)}, \\
   E(y) &= |Q(iy)|^2 - |P(iy)|^2.
\end{align*} $$

<div style="text-align: right">[10 marks]</div>

```{dropdown} Solution

The stability function for this DIRK method is

$$ \begin{align*}
   R(z) &= \frac{\det
   \left(
   \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - z
   \begin{pmatrix} \frac18 & 0 \\ \frac34 & \frac18 \end{pmatrix} + z
   \begin{pmatrix} \frac12 & \frac12 \\ \frac12 & \frac12 \end{pmatrix}
   \right)
   }{\det
   \left(
   \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - z
   \begin{pmatrix} \frac18 & 0 \\ \frac34 & \frac18 \end{pmatrix}
   \right)
   } \\
   &= \frac{\det
   \begin{pmatrix} 1 + \frac{3}{8}z & \frac{1}{2}z \\ -\frac14 z & 1 + \frac{3}{8}z \end{pmatrix}
   }{\det
   \begin{pmatrix} 1 - \frac18 z & 0 \\ -\frac34 z & 1 - \frac18 z \end{pmatrix}
   }
   = \frac{1 + \frac34 z + \frac{17}{64}z^2}{1 - \frac14 z + \frac{1}{64}z^2}
\end{align*} $$

The roots of the denominator are

$$ \begin{align*}
   z &= \frac{\frac14 \pm \sqrt{\frac{1}{16} - \frac{1}{16}}}{\frac{1}{32}} = 8,
\end{align*} $$

which is positive so the first condition for A-stability is satisfied. 

$$ \begin{align*}
   E(y) &= |Q(iy)|^2 - |P(iy)|^2 \\
   &= \left| 1 - \frac14 iy - \frac{1}{64}y^2 \right|^2 - \left| 1 + \frac34 iy - \frac{17}{64}y^2 \right|^2 \\
   &= \left( 1 - \frac{1}{64}y^2 \right)^2 + \left( -\frac{1}{4}y \right)^2 - \left( 1 - \frac{17}{64}y^2 \right)^2 - \left( \frac{3}{4}y \right)^2 \\
   &= 1 - \frac{1}{32}y^2 + \frac{1}{4096}y^4 + \frac{1}{16}y^2 - 1 + \frac{17}{32}y^2 - \frac{289}{4096}y^4 - \frac{9}{16}y^2 \\
   &= - \frac{9}{128}y^4
\end{align*} $$

Since $E(y) < 0$ for all $y \in \mathbb{R}$ so this DIRK method is non A-stable.
```

(c) Explain what is meant by a stiff system of equations. What methods would be most suitable for solving stiff and non-stiff problems?

<div style="text-align: right">[5 marks]</div>

```{dropdown} Solution


```
````

````{exercise}
:label: irk-exam-2

(a) The $B(k)$ and $C(k)$ order conditions for an $s$-stage Runge-Kutta method are

$$ \begin{align*}
  B(k): && \sum_{i=1}^s b_ic_i^{j - 1} &= \frac{1}{j}, & j &= 1, \ldots, k, \\
  C(k): && \sum_{j=1}^s a_{ij}c_j^{\ell - 1} &= \frac{1}{\ell} c_i^\ell, & i &= 1, \ldots, s, & \ell &= 1, \ldots, k,
\end{align*} $$

and the Legendre polynomial is

$$ P_n(x) = \sum_{i=0}^n {n \choose i}{n+i \choose i} (x - 1)^i, $$

where  ${n \choose i}$ is the Binomial coefficient.

Given that an $s$-stage Gauss-Legendre implicit Runge-Kutta method has order $2s$ where the $c_i$ coefficients are the roots of the Legendre polynomial $P_s(x)$ and the $b_i$ and $a_{ij}$ coefficients satisfy the $B(s)$ and $C(s)$ order conditions, derive a fourth-order Gauss-Legendre method.

<div style="text-align: right">[10 marks]</div>

``````{dropdown} Solution
A fourth-order Gauss-Legendre method has $s = 2$ stages. The $c_i$ values are the roots of $P_2(x)$

$$ \begin{align*}
  P_3(x) &= 1 + {2 \choose 1}{3 \choose 1}(x - 1) + {2 \choose 2}{4 \choose 2}(x - 1)^2  \\
  &= 1 + 6(x - 1) + 6 (x^2 - 2x + 1) \\
  &= 6x^2 - 6x + 1,
\end{align*} $$

using Python or MATLAB to compute the roots of $P_3(x)$ results in 

$$ c_1 = \frac12 - \frac{\sqrt{3}}{6}, \qquad c_2 = \frac12 + \frac{\sqrt{3}}{6}.$$

The $b_i$ and $a_{ij}$ satisfy the $B(2)$ and $c(2)$ order conditions

$$ \begin{align*}
  b_1 + b_2 &= 1, \\
  b_1c_1 + b_2c_2 &= \frac12, \\
  a_{11} + a_{12} &= c_1, \\
  a_{21} + a_{22} &= c_2, \\
  a_{11}c_1 + a_{12}c_2 &= \frac12 c_1^2, \\
  a_{21}c_1 + a_{22}c_2 &= \frac12 c_2^2.
\end{align*} $$

Solving using Python or MATLAB gives

$$ \begin{array}{c|cc}
  \frac12 - \frac{\sqrt{3}}{6} & \frac14 & \frac14 - \frac{\sqrt{3}}{6} \\
  \frac12 + \frac{\sqrt{3}}{6} & \frac14 + \frac{\sqrt{3}}{6} & \frac14 \\
  \hline
  & \frac12 & \frac12
\end{array} $$

`````{tab-set}
````{tab-item} Python
```python
x = sp.symbols('x')
c = sp.solve(6 * x**2 - 6 * x + 1)

c1 = c[0]
c2 = c[1]

print(c1, c2)

b1, b2, a11, a12, a21, a22 = sp.symbols("b1, b2, a11, a12, a21, a22")

eq1 = b1 + b2 - 1
eq2 = b1 * c1 + b2 * c2 - sp.Rational(1,2)
eq3 = a11 + a12 - c1
eq4 = a21 + a22 - c2
eq5 = a11 * c1 + a12 * c2 - c1**2 / 2
eq6 = a21 * c1 + a22 * c2 - c2**2 / 2

sp.solve((eq1, eq2, eq3, eq4, eq5, eq6))
```
````
`````

``````

(b) Another implicit method has the following Butcher tableau: 

$$ \begin{array}{c|cc}
  \frac12 & \frac12 & 0 \\
  \frac32 & -\frac12 & 2 \\
  \hline
  & -\frac12 & \frac32
\end{array} $$

State with reasons whether it is A-stable or not. You may find the following useful:

$$ \begin{align*}
  R(z) &= \frac{\det(I - zA + z\mathbf{eb}^\mathsf{T})}{\det(I - zA)}, \\
  E(y) &= |Q(iy)|^2 - |P(iy)|^2,
\end{align*} $$

where $R(z) = P(z) / Q(z)$ and $i^2 = -1$. 

<div style="text-align: right">[10 marks]</div>

```{dropdown} Solution

The stability function is

$$ \begin{align*}
  R(z) &= \frac{
    \det \left( 
      \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - z
      \begin{pmatrix} \frac12 & 0 \\ -\frac12 & 2 \end{pmatrix} + z
      \begin{pmatrix} -\frac12 & \frac32 \\ -\frac12 & \frac32 \end{pmatrix}
    \right)
  }{
    \det \left(
        \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - z
        \begin{pmatrix} \frac12 & 0 \\ -\frac12 & 2 \end{pmatrix}
    \right)
  } \\
  &= \frac{\det
    \begin{pmatrix} 1 - z & \frac32 z \\ 0 & 1 - \frac12 z\end{pmatrix}
    }{ \det
    \begin{pmatrix} 1 - \frac12 z & 0 \\ \frac12 z & 1 - 2z \end{pmatrix}
    }
  = \frac{1 - \frac32 z + \frac12 z^2}{1 - \frac52 z + z^2}.
\end{align*} $$

A method is A-stable if

- the roots of $Q(z)$ have positive real parts and
- $E(y) \geq 0$ for all $y \in \mathbb{R}$. 

Checking the roots of $Q(z)$

$$ \begin{align*}
  z &= \frac{\frac52 \pm \sqrt{\frac{25}{4} - 4}}{2}
  = \frac54 \pm \frac34=\frac12, 2
\end{align*} $$

So the first condition is satisfied. Checking $E(y) \ge 0$

$$ \begin{align*}
  E(y) &= \left| 1 - \frac52 iy - y^2 \right|^2 - \left| 1 - \frac32 iy - \frac12 y^2 \right|^2 \\
  &= (1 - y^2)^2 + \left( -\frac52 y \right)^2 - \left( 1 - \frac12 y^2 \right)^2 - \left( -\frac32 y \right)^2 \\
  &= 1 - 2y^2 + y^4 + \frac{25}{4}y^2 - 1 + y^2 - \frac14 y^4 - \frac94 y^2 \\
  &= 3y^2 + \frac34 y^4,
\end{align*} $$

so $E(y) > 0$ for all $y \in \mathbb{R}$ so the second condition is satisfied and this is an A-stable method.
```

(c) What are the advantages and disadvantages of using an A-stable implicit Runge-Kutta method over an explicit Runge-Kutta method. In what situation would you choose to implement one over the other?

<div style="text-align: right">[5 marks]</div>

```{dropdown}

```
````

---

## Matrix Decomposition Methods

````{exercise}
:label: matrix-decomposition-exam-1

(a) Use LUP decomposition to solve the following system of equations

$$ \begin{align*}
   2x_1 + 2x_2 +  x_3 &= 11, \\
   4x_1 +  x_2 + 3x_3 &= 46, \\
   -3x_1 - 5x_2 + 4x_3 &= 14.
\end{align*} $$

<div style="text-align: right">[10 marks]</div>

```{dropdown} Solution

Performing partial pivoting on the coefficient matrix

$$ \begin{align*}
   & \begin{pmatrix}
   2 & 2 & 1 \\
   4 & 1 & 3 \\ 
   -3 & -5 & 4
   \end{pmatrix}
   \begin{matrix} R_1 \leftrightarrow R_2 \\ \phantom{x} \\ \phantom{x} \end{matrix} &
   \longrightarrow
   & \begin{pmatrix}
   4 & 1 & 3 \\ 
   2 & 2 & 1 \\
   -3 & -5 & 4
   \end{pmatrix}
   \begin{matrix}  \\ R_2 \leftrightarrow R_3 \\ \phantom{x} \end{matrix} \\
   \longrightarrow
   & \begin{pmatrix}
   4 & 1 & 3 \\ 
   -3 & -5 & 4 \\
   2 & 2 & 1 
   \end{pmatrix} = PA.
\end{align*} $$

Performing the same row swaps on $I_3$

$$ \begin{align*}
   & \begin{pmatrix}
   1 & 0 & 0 \\
   0 & 1 & 0 \\
   0 & 0 & 1
   \end{pmatrix}
   \begin{matrix} R_1 \leftrightarrow R_2 \\ \phantom{x} \\ \phantom{x} \end{matrix} &
   \longrightarrow
   & \begin{pmatrix}
   0 & 1 & 0 \\
   1 & 0 & 0 \\
   0 & 0 & 1
   \end{pmatrix}
   \begin{matrix}  \\ R_2 \leftrightarrow R_3 \\ \phantom{x} \end{matrix} \\
   \longrightarrow
   & \begin{pmatrix}
   0 & 1 & 0 \\
   0 & 0 & 1 \\
   1 & 0 & 0
   \end{pmatrix} = P.
\end{align*} $$

Computing the LU decomposition of $PA$

$$ \begin{align*}
   j &= 1: & u_{11} &= a_{11} = 4, \\
   && \ell_{21} &= \frac{1}{u_{11}}a_{21} = \frac14(-3) = -\frac34, \\
   && \ell_{31} &= \frac{1}{u_{11}}a_{31} = \frac14(2) = \frac12, \\
   j &= 2: & u_{12} &= a_{12} = 1, \\
   && u_{22} &= a_{22} - \ell_{21}u_{12} = -5 - \left(-\frac34\right)(1) = -\frac{17}{4}, \\
   && \ell_{32} &= \frac{1}{u_{22}}(a_{32} - \ell_{31}u_{12}) = -\frac{4}{17} \left( 2 - \frac12(1) \right) = -\frac{6}{17}, \\
   j &= 3: & u_{13} &= a_{13} = 3, \\
   && u_{23} &= a_{23} - \ell_{21}u_{13} = 4 - \left( -\frac34 \right)(3) = \frac{25}{4}, \\
   && u_{33} &= a_{33} - \ell_{31}u_{13} - \ell_{32}u_{23} = 1 - \frac12(3) - \left( -\frac{25}{4} \right) = \frac{29}{17},
\end{align*} $$

therefore

$$ \begin{align*}
   L &=
   \begin{pmatrix}
   1 & 0 & 0 \\
   -\frac34 & 1 & 0 \\
   \frac12 & -\frac{6}{17} & 1
   \end{pmatrix}, &
   U &= 
   \begin{pmatrix}
   4 & 1 & 3 \\
   0 & -\frac{17}{4} & \frac{25}{4} \\
   0 & 0 & \frac{29}{17}
   \end{pmatrix}, &
   P &= 
   \begin{pmatrix}
   0 & 1 & 0 \\
   0 & 0 & 1 \\
   1 & 0 & 0 
   \end{pmatrix}.
\end{align*} $$

Solving $L\mathbf{y} = P \mathbf{b}$ 

$$ \begin{align*}
   \begin{pmatrix}
      1 & 0 & 0 \\
      -\frac34 & 1 & 0 \\
      \frac12 & -\frac{6}{17} & 1
   \end{pmatrix}
   \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix}
   &= 
   \begin{pmatrix}
      0 & 1 & 0 \\
      0 & 0 & 1 \\
      1 & 0 & 0 
   \end{pmatrix}
   \begin{pmatrix} 11 \\ 46 \\ 14 \end{pmatrix}
   =
   \begin{pmatrix} 46 \\ 14 \\ 11 \end{pmatrix}
   \quad \implies \quad
   \begin{aligned}
      y_1 &= 46 \\
      y_2 &= 14 - (-\tfrac34)(46) = \tfrac{97}{2}, \\
      y_3 &= 11 - \tfrac12(46) - (-\tfrac{6}{17}) = \tfrac{87}{17}.
   \end{aligned}
\end{align*} $$

Solving $U \mathbf{x} = \mathbf{y}$

$$ \begin{align*}
   \begin{pmatrix}
      4 & 1 & 3 \\
      0 & -\frac{17}{4} & \frac{25}{4} \\
      0 & 0 & \frac{29}{17}
   \end{pmatrix}
   \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix}
   &= 
   \begin{pmatrix} 46 \\ \frac{97}{2} \\ \frac{87}{17} \end{pmatrix}
   \quad \implies \quad
   \begin{aligned}
   x_3 &= \tfrac{17}{29} (\tfrac{87}{17}) = 3, \\
   x_2 &= -\tfrac{17}{4} (\tfrac{97}{2} - \tfrac{25}{4}(3)) = -7, \\
   x_1 &= \tfrac{1}{4} (46 - (-7) - 3(3)) = 11.
   \end{aligned}
\end{align*} $$

```

(b) The Gram-Schmidt method for computing the QR decomposition of the matrix $A$ is:

- for $j = 1 \ldots n$
  - $r_{ij} = \mathbf{q}_i \cdot \mathbf{a}_j, \qquad i = 1, \ldots, j - 1$
  - $\mathbf{u}_j = \mathbf{a}_i - \displaystyle\sum_{i=1}^{j - 1} r_{ij} \mathbf{q}_i$
  - $r_{jj} = \| \mathbf{u}_j \|$
  - $\mathbf{q}_j = \dfrac{\mathbf{u}_i}{r_{jj}}$

Calculate the QR decomposition of the following matrix using the Gram-Schmidt process and verify that your decomposition is an orthogonal matrix.

$$ \begin{align*}
  A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 1 & 3 & 4 \end{pmatrix}
\end{align*} $$

<div style="text-align: right">[10 marks]</div>

```{dropdown} Solution

$$ \begin{align*}
  j &= 1; & \mathbf{u}_1 &= \mathbf{a}_1 = 
  \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \\
  && r_{11} &= \| \mathbf{u}_1 \| = \sqrt{3}, \\
  && \mathbf{q}_1 &= \frac{\mathbf{u}_1}{r_{11}} = \frac{1}{\sqrt{3}}
  \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = 
  \begin{pmatrix} \frac{\sqrt{3}}{3} \\ \frac{\sqrt{3}}{3} \\ \frac{\sqrt{3}}{3} \end{pmatrix}, \\
  j &= 2: & r_{12} &= \mathbf{q}_1 \cdot \mathbf{a}_2 =
  \begin{pmatrix} \frac{\sqrt{3}}{3} \\ \frac{\sqrt{3}}{3} \\ \frac{\sqrt{3}}{3} \end{pmatrix}
  \cdot
  \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = 2\sqrt{3}, \\
  && \mathbf{u}_2 &= \mathbf{a}_2 - r_{12} \mathbf{q}_1 =
  \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} - 2 \sqrt{3}
  \begin{pmatrix} \frac{\sqrt{3}}{3} \\ \frac{\sqrt{3}}{3} \\ \frac{\sqrt{3}}{3} \end{pmatrix}
  =
  \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix}, \\
  && r_{22} &= \| \mathbf{u}_2 \| = \sqrt{2}, \\
  && \mathbf{q}_2 &= \frac{\mathbf{u}_2}{r_{22}} = \frac{\sqrt{2}}{2}
  \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix}
  =
  \begin{pmatrix} -\frac{\sqrt{2}}{2} \\ 0 \\ \frac{\sqrt{2}}{2}\end{pmatrix}, \\
  j &=3 & r_{13} &= \mathbf{q}_1 \cdot \mathbf{a}_3 
  =
  \begin{pmatrix} \frac{\sqrt{3}}{3} \\ \frac{\sqrt{3}}{3} \\ \frac{\sqrt{3}}{3} \end{pmatrix} \cdot
  \begin{pmatrix} 1 \\ 3 \\ 4 \end{pmatrix} 
  = \frac{8\sqrt{3}}{3}, \\
  && r_{23} &= \mathbf{q}_2 \cdot \mathbf{a}_3
  =
  \begin{pmatrix} -\frac{\sqrt{2}}{2} \\ 0 \\ \frac{\sqrt{2}}{2}\end{pmatrix} \cdot
  \begin{pmatrix} 1 \\ 3 \\ 4 \end{pmatrix} 
  =
  \frac{3\sqrt{2}}{2}, \\
  && \mathbf{u}_3 &= \mathbf{a}_3 - r_{13} \mathbf{q}_1 - r_{23} \mathbf{q}_2
  =
  \begin{pmatrix} 1 \\ 3 \\ 4 \end{pmatrix} - \frac{8\sqrt{3}}{3}
  \begin{pmatrix} \frac{\sqrt{3}}{3} \\ \frac{\sqrt{3}}{3} \\ \frac{\sqrt{3}}{3} \end{pmatrix} - \frac{3\sqrt{2}}{2}
  \begin{pmatrix} -\frac{\sqrt{2}}{2} \\ 0 \\ \frac{\sqrt{2}}{2}\end{pmatrix}
  =
  \begin{pmatrix} -\frac16 \\ \frac13 \\ -\frac16 \end{pmatrix}, \\
  && r_{33} &= \| \mathbf{u}_3 \| = \frac{\sqrt{6}}{6}, \\
  && \mathbf{q}_3 &= \frac{\mathbf{u}_3}{r_{33}} = \sqrt{6}
  \begin{pmatrix} -\frac16 \\ \frac13 \\ -\frac16 \end{pmatrix}
  =
  \begin{pmatrix} -\frac{\sqrt{6}}{6} \\ \frac{\sqrt{6}}{3} \\ -\frac{\sqrt{6}}{6} \end{pmatrix},
\end{align*} $$

therefore

$$ \begin{align*}
  Q &= 
  \begin{pmatrix}
    \frac{\sqrt{3}}{3} & -\frac{\sqrt{2}}{2} & -\frac{\sqrt{6}}{6} \\
    \frac{\sqrt{3}}{3} & 0 & \frac{\sqrt{6}}{3} \\
    \frac{\sqrt{3}}{3} & \frac{\sqrt{2}}{2} & -\frac{\sqrt{6}}{6}
  \end{pmatrix}, &
  R &=
  \begin{pmatrix}
    \sqrt{3} & 2 \sqrt{3} & \frac{8\sqrt{3}}{3} \\
    0 & \sqrt{2} & \frac{3\sqrt{2}}{2} \\
    0 & 0 & \frac{\sqrt{6}}{6}
  \end{pmatrix}.
\end{align*} $$
```

(c) Explain how LU decomposition used in the calculation of the stage values of an implicit Runge-Kutta method. What advantages does it have for this application over other methods for solving systems of linear equations?

<div style="text-align: right">[5 marks]</div>

```{dropdown} Solution
LU decomposition is commonly used to compute the solution to the linear system required by Newton's method to solve for the stages values. Since we assume the Jacobian matrix is constant for all Newton iterations, the LU decomposition only needs to be computed once per step, whereas other solution methods for linear systems such as Gaussian elimination would need to be re-computed for each iteration.
```
````
