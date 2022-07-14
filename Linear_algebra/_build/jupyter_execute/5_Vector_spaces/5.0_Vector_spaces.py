#!/usr/bin/env python
# coding: utf-8

# (vector-spaces-chapter)=
# # Vector spaces
# 
# **Learning outcomes**
# 
# On successful completion of this chapters students will be able to:
# 
# - identify when a set of objects is a [vector space](vector-space-definition);
# - identify when a subset of a vector space is a [subspace](subspace-definition);
# - determine whether elements of a vector space are [linearly dependent or linearly independent](linear-dependence-definition);
# - identify a [basis](basis-definition), determine the [dimension](vector-space-dimension-definition) of a vector space and represent vectors with respect to a [non-standard basis](change-of-basis-example).
# 
# ---
# ## Definition
# 
# :::{admonition} Definition: Vector space
# :class: note
# :name: vector-space-definition
# 
# A [**vector space**](https://en.wikipedia.org/wiki/Vector_space) over a field $F$ is a non-empty set $V$ of objects called vectors on which the operations below are defined. The notation $V \times V$ denotes the Cartesian product of $V$ with itself and $\to$ denotes a mapping from one set to another.
# 
# - **addition** $(+)$: $V \times V \to V$. For example, given two elements $\mathbf{u}, \mathbf{v} \in V$ we can `add' them together to obtain another element $\mathbf{u} + \mathbf{v} \in V$. 
# - **scalar multiplication** $(\cdot )$: $F \times V \to V$. For example given $\alpha \in F$ and $\mathbf{u} \in V$ we can `multiply' $\mathbf{u}$ by $\alpha$ to obtain another element $\alpha \cdot \mathbf{u} \in V$
# :::
# 
# For example, a field could be the set of all real numbers $\mathbb{R}$ and a vector space be the set of all co-ordinates in $\mathbb{R}^3$. Not all subsets of a field can be classified as a vector space, to do so the set $V$ must satisfy the following axioms. 
# 
# :::{admonition} Theorem: Axioms of a vector space
# :class: important
# :name: vector-space-axioms-theorem
# 
# Let $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$ and $\beta, \alpha \in F$, $V$ is a vector space if all of the following axioms are satisfied
# 
# - A1: Associativity of vector addition: $\mathbf{u} + (\mathbf{v} + \mathbf{w}) = (\mathbf{u} + \mathbf{v}) + \mathbf{w}$;
# - A2: Commutativity of vector addition: $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$;
# - A3: Identity element of vector addition: there exists an element $\mathbf{0} \in V$ such that $\mathbf{u} + \mathbf{0} = \mathbf{u}$ for all $\mathbf{v} \in V$;
# - A4: Additive inverse: For every $\mathbf{u} \in V$ there exists an element $- \mathbf{v} \in V$, called the **additive inverse**, such that $\mathbf{u} + (- \mathbf{u}) = \mathbf{0}$;
# - M1: Associativity of scalar multiplication: $\alpha(\beta \mathbf{u}) = (\alpha \beta) \mathbf{u}$;
# - M2: Identity element of scalar multiplication: there exists an element $1$ called the **multiplicative identity** such that $1 \mathbf{u} = \mathbf{u}$;
# - M3: Distributivity of scalar multiplication with respect to vector addition: $\alpha(\mathbf{u} + \mathbf{v}) = \alpha \mathbf{u} + \alpha \mathbf{v}$;
# - M4: Distributivity of scalar multiplication with respect to addition: $(\alpha + \beta)\mathbf{u} = \alpha \mathbf{u} + \beta \mathbf{u}$.
# :::
# 
# The first four axioms are concerned with addition and the latter four axioms are concerned with scalar multiplication. When the scalars are real numbers, i.e. $F = \mathbb{R}$, we call $V$ a **'real vector space'** which is short for a *'vector space over the field of real numbers'}*. When the scalars are complex numbers, i.e., $F=\mathbb{C}$, we talk of a **'complex vector space'**. More generally, the scalars can be elements of any field (denoted $F$). 
# 
# We now list some basic properties for multiplication by scalars in a vector space.
# 
# :::{admonition} Theorem: Properties of vector spaces
# :class: important
# :name: properties-of-vector-spaces-theorem
# 
# Let $V$ be a vector space over $F$ and $\mathbf{u} \in V,\alpha\in F$. Then the following hold:
# 
# - $\alpha \cdot \mathbf{0} = \mathbf{0}$;
# - $0 \cdot \mathbf{u} = \mathbf{0}$;
# - if $\alpha \cdot \mathbf{u} = \mathbf{0}$ then either $\alpha = 0$ or $\mathbf{u} = \mathbf{0}$;
# - $-(\alpha \cdot \mathbf{u}) = (-\alpha)\cdot \mathbf{u} = \alpha\cdot(-\mathbf{u})$.
# :::
# 
# The name *'vector space'* indicates a connection with the study of vectors. Indeed our Euclidean spaces $\mathbb{R}^n$, as introduced in [Vectors](vectors-chapter), are vector spaces over $F=\mathbb{R}^n$. Addition and scalar multiplication, in the sense of a vector space, for $\mathbb{R}^n$ are as given in [vector addition](vector-addition-definition) and [scalar multiplication](scalar-multiplication-of-a-vector-definition) respectively. Euclidean vector spaces are often the first examples of vector spaces that a student meets. However, maybe they do not quite demonstrate the power behind this construction. The real motivation of the study of the vector spaces comes from the fact that a lot of more abstract sets, such as differentiable functions or matrices, can be viewed as vector spaces. Everything that we learn about vector spaces can be then applied to any set which satisfies the definition of a vector space. This means that the set of $m\times n$ matrices with matrix addition and scalar multiplication or the set of all polynomials of degree at most $n$, in some sense, behave in a very similar fashion to Euclidean space.
# 
# ::::{admonition} Example 5.1
# :class: seealso
# :name: real-numbers-vector-space-example
# 
# Show that the following are vector spaces:
# 
# (i) &emsp; The set of real numbers over itself;
# 
# :::{dropdown} Solution
# 
# We need to check that all of the axioms of vector spaces are satisfied. Here $V \in \mathbb{R}$ and let $u, v, w \in V$ and $\alpha, \beta \in \mathbb{R}$
# 
# - A1: $u + (v + w) = (u + v) + w \quad \checkmark$
# - A2: $u + v = v + u \quad \checkmark$
# - A3: $u + 0 = u \quad \checkmark$ (i.e., 0 is the identity element of addition)
# - A4: $u + (-u) = 0 \quad \checkmark$ (i.e., the negative of any number is the additive inverse)
# - M1: $\alpha(\beta u) = (\alpha \beta) u \quad \checkmark$
# - M2: $1 u = u \quad \checkmark$ (i.e., 1 is the multiplicative identity of all numbers)
# - M3: $\alpha(u + v) = \alpha u + \alpha v \quad \checkmark$
# - M4: $(\alpha + \beta) u = \alpha u + \beta u \quad \checkmark$
# :::
# 
# (ii) &emsp; The set of all polynomials of degree at most $n$ with real coefficients $P(\mathbb{R}_n)$
# 
# \begin{align*}
#     p = p(x) := a_0x^0 + a_1x^1 + a_2x^2 + \cdots + a_nx^n = \sum_{i=0}^n a_ix^i,
# \end{align*}
# 
# where $a_i \in \mathbb{R}$ and $x$ is some variable. Show that $P(\mathbb{R}_n)$ is a vector space.
# 
# :::{dropdown} Solution
# 
# Let $p, r, q \in P(\mathbb{R}_{n})$ where $a_i, b_i, c_i \in \mathbb{R}$ are the coefficients for $p$, $q$ and $r$ respectively and $k\in \mathbb{R}$ is some scalar then we define
# 
# - Vector addition:
# 
# \begin{align*}
#     p + r &= (a_0 + b_0)x^0 + (a_1 + b_1)x^1 + \cdots + (a_n + b_n)x^n \\
#     &= \sum_{i=0}^n (a_i + b_i)x^i.
# \end{align*}
# 
# - Scalar multiplication:
# 
# \begin{align*}
#     k \cdot p &= ka_0x^0 + ka_1x^1 + \cdots + ka_nx^n \\
#     &= \sum_{i=0}^n ka_ix^i.
# \end{align*}
# 
#  - Additive identity element is the zero polynomial
#  
# \begin{align*}
#     \mathbf{0} = 0x^0 + 0x^1 + \cdots + 0x^n.
# \end{align*}
# 
# - The additive inverse to the polynomial $p$ is
# 
# \begin{align*}
#     -p &= (-a_0)x^0 + (-a_1)x^2 + \cdots + (-a_n)x^n \\
#     &= \sum_{i=0}^n (-a_i)x^i \\
#     &= -\sum_{i=0}^n a_ix^i.
# \end{align*}
# 
# Checking the that axioms of vector spaces are satisfied
# 
# - A1: 
# \begin{align*}
#     p + (q + r) &= \displaystyle \sum_{i=0}^n (a_i + (b_i + c_i))x^i \\
#     &= \displaystyle \sum_{i=0}^n ((a_i + b_i) + c_i)x^i \\
#     &= (p + q) + r \quad \checkmark
# \end{align*}
# 
# - A2: 
# \begin{align*}
#     p + q &= \displaystyle \sum_{i=0}^n (a_i + b_i)x^i \\
#     &= \displaystyle \sum_{i=0}^n (b_i + a_i)x^i \\
#     &= q + p \quad \checkmark
# \end{align*}
# 
# - A3: 
# \begin{align*}
#     p + 0 &= \displaystyle \sum_{i=0}^n (a_i + 0)x^i \\
#     &= \displaystyle \sum_{i=0}^n a_ix^i \\
#     &= p \quad \checkmark
# \end{align*}
# 
# - A4: 
# \begin{align*}
#     p + (-p) &= \displaystyle \sum_{i=0}^n(a_i + (-a_i)) x^i \\
#     &= 0 \quad \checkmark
# \end{align*}
# 
# - M1: 
# \begin{align*}
#     \alpha(\beta p) &= \alpha \displaystyle \sum_{i=0}^n \beta a_i x^i \\
#     &= \alpha \beta \displaystyle \sum_{i=0}^n a_i x^i \\
#     &= (\alpha \beta) p \quad \checkmark
# \end{align*}
# 
# - M2: 
# \begin{align*}
#     1p &= \displaystyle \sum_{i=0}^n 1 a_i x^i \\
#     &= \displaystyle \sum_{i=0}^n a_i x^i \\
#     &= p \quad \checkmark
# \end{align*}
# 
# - M3: 
# \begin{align*}
#     \alpha (p + q) &= \alpha \sum (a_i + b_i) x^i \\
#     &= \alpha \sum a_i x^i + \alpha b_i x^i \\
#     &= \alpha p + \alpha q \quad \checkmark
# \end{align*}
# 
# - M4: 
# \begin{align*}
#     (\alpha + \beta) p &= (\alpha + \beta) \displaystyle \sum_{i=0}^n a_i x^i \\
#     &= \alpha \displaystyle \sum_{i=0}^n a_i x^i + \beta \displaystyle \sum_{i=0}^n a_i x^i \\
#     &= \alpha p + \beta p \quad \checkmark
# \end{align*}
# :::
# ::::
# 
# ## Examples of non-vector spaces
# 
# Of course not all sets are vector spaces. For example, consider the set of integers $\mathbb{Z}$ over $\mathbb{R}$. It is easy to show that the axioms A1 to A4 are satisfied for the set of integers. The problem comes when one tries to define scalar multiplication. From the [definition of scalar multiplication](vector-space-definition), $\mathbb{R} \times \mathbb{Z} \to \mathbb{Z}$ so for $u \in \mathbb{Z}$ and $\alpha \in \mathbb{R}$, $\alpha x$ must be in $\mathbb{Z}$. However, this is not always the case, for example, when $u=1$ and $\alpha = \frac{1}{2}$ we have $\frac{1}{2} \cdot 1 = \frac{1}{2} \notin \mathbb{Z}$. This was an example of a proof by counterexample where we just need to show 1 instance where the axioms are not satisfied to prove that we do not have a vector space.
# 
# ::::{admonition} Example 5.2
# :class: seealso
# :name: non-vector-space-example
# 
# Show that the following a not vector spaces:
# 
# (i) &emsp; The set of all positive real numbers, $\mathbb{R}_+$ over itself
# 
# (ii) &emsp; $V$ is defined to be a parabola $y=x^2$ in $\mathbb{R}^2$, i.e., all the points in $\mathbb{R}^2$ defined by $V = {(x, x^2)}$
# 
# :::{dropdown} Solution
# (i) &emsp; We do not have an identity element for addition since $0 \notin \mathbb{R}_+$ so axiom A3 is not satisfied. Also, by axiom A4, if $u, v \in \mathbb{R}_+$ are two positive real numbers then $x + y > 0$ so no additive inverse exists.
# 
# (ii) If we take the example $\mathbf{u} \in V$ such that $\mathbf{u} = (1, 1)$ then the additive inverse $-\mathbf{u} = (-1, -1) \notin V$ so $V$ is not a vector space.
# :::
# ::::
