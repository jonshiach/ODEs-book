#!/usr/bin/env python
# coding: utf-8

# (taylor-series-section)=
# # The Taylor Series
# 
# The **Taylor series** named after English mathematician [Brook Taylor](https://en.wikipedia.org/wiki/Brook_Taylor) is a series expansion of a function.
# 
# ````{admonition} Definition: The Taylor series
# :class: note
# :name: taylor-series-definition
# 
# Let $f(t)$ be a differentiable function of the variable $t$ then the value $f(t+h)$ where $h$ is some small value can be written using the Taylor series
# 
# \begin{align*}
#     f(t+h) &= \sum_{n = 0}^\infty \frac{h^n}{n!}f^{(n)}(t) \\
#     &= f(t) + hf'(t) + \frac{h^2}{2!}f''(t) + \frac{h^3}{3!}f'''(t) + \cdots
# \end{align*}
# ````
# 
# We can use the Taylor series to approximate the value of $f(t)$ where the smaller the value of $h$ the closer the approximation $f(t+h)$ is to actual value $f(t)$. The problem with we have is that we cannot sum an infinite number of terms so instead we only consider the first $n$ terms in the summation
# 
# \begin{align*}
#     f(t+h) &= \underbrace{f(t) + hf'(t) + \frac{h^2}{2!}f''(t) \cdots + \frac{h^n}{n!}f^{(n)}(t)}_{\mathrm{first }\,n\,\mathrm{ terms}} \\
#     & \qquad + \underbrace{\frac{h^{n+1}}{(n+1)!}f^{(n+1)}(t) + \frac{h^{n+2}}{(n+2)!}f^{(n+2)}(t) + \cdots}_{\mathrm{Highter\,Order\,Terms \,(HOT)}}
# \end{align*}
# 
# It is important to note that since we are omitting the higher order terms in the truncation of the Taylor series we only have an **approximation** of $f(t+h)$. When we omit the Higher-Order Terms (HOT) from the Taylor series we say we have **truncated** the Taylor series. So if for example we omit all terms higher than fourth-order we have the **fourth-order Taylor series expansion** of $f(t+h)$.
# 
# $$f(t+h) = f(t) + hf' (t)+\frac{h^2}{2}f'' (t) + \frac{h^3}{3!}f^{''')}(t) + \frac{h^4}{4!}f^{(4)} + \mathrm{HOT}.$$
# 
# ````{admonition} Example 1.1
# :class: seealso
# :name: taylor-series-example
# 
# Use the first, second, third and fourth-order Taylor series expansions to calculate the value of $\cos\left(\frac{\pi}{3} + h\right)$ where $h=0.2$.
# 
# ```{dropdown} Solution
# 
# Here $t=\frac{\pi}{3}$, $h=0.2$, $f(t) = \cos(t)$ and $f'(t) = -\sin(t)$ so the first-order expansion is
# 
# \begin{align*}
#     \cos(t + h) &\approx \cos(t) - h \sin(t) \\
#     \cos\left(\frac{\pi}{3} + 0.2 \right) &\approx \cos\left(\frac{\pi}{3}\right) - 0.2 \sin\left(\frac{\pi}{3}\right)
#     \\
#     &= 0.5 - 0.173205 = 0.326795.
# \end{align*}
# 
# We know that the exact value is $\cos(\frac{\pi}{3} + 0.2) = 0.317980\ldots$ so the error in the first-order Taylor series approximation is $|0.317980 - 0.326795| = 0.008814$.
# 
# The second derivative of $f(t) = \cos(t)$ is $f''(t) = \dfrac{\mathrm{d}}{\mathrm{d}t}(-\sin(t)) = -\cos(t)$ so the second-order expansion is
# 
# \begin{align*}
#     \cos(t + h) &\approx \underbrace{\cos(t) - h \sin(t)}_{\mathrm{first\,order\,expansion}} - \frac{h^2}{2!} \cos(t).
# \end{align*}
# 
# The first two terms in the second-order expansion is the first-order expansion which we have already calculated so
# 
# \begin{align*}
#     \cos\left(\frac{\pi}{3} + 0.2 \right) &\approx 0.326795 - \frac{0.2^2}{2} \cos\left(\frac{\pi}{3}\right) \\
#     &= 0.326795 - 0.010000 = 0.316795.
# \end{align*}
# 
# Doing similar for the third and fourth-order expansions 
# 
# \begin{align*}
#     \mathrm{3rd\,order}: && \cos\left(\frac{\pi}{3} + 0.2 \right) &\approx 0.316795 + \frac{0.2^3}{6} \sin\left(\frac{\pi}{3}\right) \\
#     &&& = 0.316795 + 0.001155 = 0.317950, \\
#     \mathrm{4th\,order}: && \cos(\left(\frac{\pi}{3} + 0.2 \right) &\approx 0.317950 + \frac{0.2^4}{6} \cos\left(\frac{\pi}{3}\right) \\
#     &&& = 0.317950 + 0.000033 = 0.317983.
# \end{align*}
# 
# The Taylor series approximations and the errors have been tabulated below. Note that as we include more terms in the Taylor series expansion the error tends to zero. 
# 
# | $n$ | Taylor series approximation |  error   |
# |:---:|:-------------:|:--------:|
# |  0  |    0.500000   | 1.82e-01 |
# |  1  |    0.326795   | 8.81e-03 |
# |  2  |    0.316795   | 1.19e-03 |
# |  3  |    0.317950   | 3.10e-05 |
# |  4  |    0.317983   | 2.35e-06 |
# ```
# ````
# 
# ## Using Python to calculate a Taylor series approximation
# 
# The code below calculates the Taylor series approximation of $\cos(t + h)$ using the first $n$ terms of the series. Note that since the derivative of $\cos(t)$ is $-\sin(t)$ so if $n$ is even then $f^{(n)}(t) = \pm \cos$ and when $n$ is odd $f^{(n)}(t) = \pm \sin(t)$. To calculate this we can use an `if` statement that checks whether the current value of $n$ is even or odd and calculates the value $f(t)$ accordingly and change the sign of $f^{(n)}(t)$ when $n$ is odd. 

# In[1]:


import numpy as np

t = np.pi / 3  # variable
h = 0.2        # step length
nmax = 4       # highest order term retained
sign = 1       # sign for the nth term
approx = 0     # value of the approximation

print("|  n  | approximation |  error   |")
print("|:---:|:-------------:|:--------:|")
for n in range(nmax + 1):
    if n % 2 == 0:
        f = np.cos(t)
    else:
        f = np.sin(t)
        sign = -sign 
    
    approx += sign * h ** n / np.math.factorial(n) * f
    print(f"|  {n}  |    {approx:7.6f}   | {abs(np.cos(t + h) - approx):7.2e} |")

