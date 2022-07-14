#!/usr/bin/env python
# coding: utf-8

# (subspaces-section)=
# # Subspaces
# 
# We have seen that a [vector space](vector-space-definition) is a set, and hence we can consider studying its [subsets](https://en.wikipedia.org/wiki/Subset). Think of the Euclidean space $\mathbb{R}^3$ (which we think of with the usual $x,y,z$-coordinates). This is a vector space, and consider the plane $p = \{(x,y,z) : x + y + z = 0\} \subseteq \mathbb{R}^3$. In fact, we can view $p$ itself as a vector space, meaning it satisfies the [vector space axioms](vector-space-axioms-theorem) A1 -- A4 and M1 -- M4, where we define addition and scalar multiplication as coming from $\mathbb{R}^3$. We saw in [Co-ordinate geometry](coordinate-geometry-chapter) that this vector space $p$ actually closely resembles $\mathbb{R}^2$.
# 
# :::{admonition} Definition: Subspace
# :class: note
# :name: subspace-definition
# 
# A non-empty subset $W$ of a vector space $V$ is called a **subspace** (or a vector subspace) if it satisfies all the vector space properties A1 -- A4 and M1 -- M4.
# :::
# 
# Actually most of the [axioms](vector-space-axioms-theorem) A1 -- A4 and M1 -- M4 are automatically satisfied, simply because they're satisfied in $V$. The only things we really need to check are that addition and scalar multiplication are well-defined. In other words we need to check that when we 'add' or 'multiply' in $W$ we are not taken outside of $W$ ({numref}`vector-space-figure`). This idea is formalised in [the subspace condition](subspace-condition-theorem).
# 
# :::{figure} ../Images/vector_space.png
# :name: vector-space-figure
# 
# Illustration of a subspace $W$ of a vector space $V$.
# :::
# 
# ::::{admonition} Theorem: Subspace condition
# :class: important
# :name: subspace-condition-theorem
# 
# Let $V$ be a vector space over $F$ and $W$ be a non-empty subset of $V$ then $W$ is a subspace if and only if the following condition is satisfied
# 
# :::{math}
# :label: subspace-condition-equation
# 
# \mathbf{u} + \alpha\mathbf{w} \in W,
# :::
# 
# where $\mathbf{u}, \mathbf{w} \in W$ and $\alpha \in F$.
# ::::
# 
# To demonstrate the use of [the subspace condition](subspace-condition-theorem) let's check whether $W = \{(x, y, z) : x + 2y - 3z = 0\}$ is a subspace of $\mathbb{R}^3$. First we need to verify that $W$ is non-empty. To do this we simply need to find an element of $W$, e.g., $(0, 0, 0) \in W$ so $W$ is non-empty.
# 
# Next we need to take two arbitrary vectors in $W$, $\mathbf{u} = (x_1, y_1, z_1), \mathbf{v} = (x_2, y_2, z_2) \in W$ and $\alpha \in \mathbb{R}$ then 
# 
# \begin{align*}
#     \mathbf{u} + \alpha \mathbf{v} = 
#     \begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} + \alpha 
#     \begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix} 
#     = \begin{pmatrix} x_1 + \alpha x_2 \\ y_1 + \alpha y_2 \\ z_1 + \alpha z_2 \end{pmatrix}.
# \end{align*}
# 
# We now need to show that $(x_1 + \alpha x_2, y_1 + \alpha y_2, z_1 + \alpha z_2) = 0$ (i.e., it is in $W$)
# 
# \begin{align*}
#     (x_1 + \alpha x_2) + 2(y_1 + \alpha y_2) - 3(z_1 + \alpha z_2) &= (x_1 + 2y_1 - 3z_1) \\
#     & \qquad + \alpha (x_2 + 2y_2 - 3z_2) \\
#     &= 0 + \alpha \cdot 0 = 0,
# \end{align*}
# 
# therefore $\mathbf{u} + \alpha \mathbf{v} \in W$ and $W$ is a subspace of $\mathbb{R}^3$
# 
# By a proof similar to the above, you can show that any plane of the form $\{(x, y, z) : ax + by + cz = d\}$ is a subspace of $\mathbb{R}^3$ when $d=0$ and not a subspace otherwise.
# 
# ::::{admonition} Example 5.3
# :class: seealso
# :name: subspace-example
# 
# (i) &emsp; Let $W$ be the subset $M_{2\times 2}$ given by
# 
# \begin{align*}
#     W = \left\{ \begin{pmatrix} a & b \\ c & d \end{pmatrix} : a + b + c + d = 0 \right\}.
# \end{align*}
# 
# Show that $W$ is a subspace of $M_{2\times 2}$.
# 
# :::{dropdown} Solution
# 
# Clearly $\mathbf{0}_{2\times 2} \in W$ so $W$ is non-empty. Let $U = \begin{pmatrix} x_1 & y_1 \\ z_1 & w_1 \end{pmatrix}, V = \begin{pmatrix} x_2 & y_2 \\ z_2 & w_2 \end{pmatrix} \in W$ and $\alpha \in \mathbb{R}$. Then 
# 
# \begin{align*}
#     U + \alpha V = 
#     \begin{pmatrix} 
#         x_1 + \alpha x_2 & y_1 + \alpha y_2 \\ 
#         z_1 + \alpha z_2 & w_1 + \alpha w_2 \end{pmatrix}.
# \end{align*}
# 
# Checking that $U + \alpha V \in W$
# 
# \begin{align*}
#     & x_1 + \alpha x_2 + y_1 + \alpha y_2 + z_1 + \alpha z_2 + w_1 + \alpha w_2 \\ 
#     & \qquad = (x_1 + y_1 + z_1 + w_1) + \alpha (x_2 + y_2 + z_2 + w_2) \\
#     & \qquad = 0 + \alpha \cdot 0 = 0,
# \end{align*}
# 
# so $U + \alpha V \in W$ therefore $W$ is a subspace of $M_{2\times 2}$.
# :::
# 
# (ii) &emsp; Let $W = \{ p(x) \in P(\mathbb{R}_n) : p(x) = p(-x)\} \subseteq P(\mathbb{R}_n)$ be the set of all even functions. Show that $W$ is a subspace of $P(\mathbb{R}_n)$.
# 
# :::{dropdown} Solution
# The zero polynomial $0 \in W$ so $W$ is non-empty. Let $p, r \in W$ and $\alpha \in \mathbb{R}$, we need to show that $p + \alpha r \in W$. Now we know that $p(-x) = p(x)$ and $r(-x) = r(x)$
# 
# \begin{align*}
#     (p + \alpha r)(-x) = p(-x) + \alpha r(-x) = p(x) + \alpha r(x) = (p + \alpha r)(x),
# \end{align*}
# 
# so $(p + \alpha r)(x) \in W$ is an even function therefore $W$ is a subspace.
# :::
# ::::
# 
# ## Non-examples of Subspaces
# 
# Not all subsets of a vector space will be a subspace. For example, define $p$ as the polynomial 
# 
# \begin{align*}
#     p(x)=a_0 + a_1 x + a_2 x^2 + \cdots + a_n x^n = \sum_{i = 0}^n a_ix^i \in P(\mathbb{R}),
# \end{align*}
# 
# with $a_n\neq 0$, we say $p$ has degree $n$ and write $\operatorname{deg}(p)=n$. The zero polynomial will say has degree $-\infty$. Let 
# 
# \begin{align*}
#     W = \{p \in P(\mathbb{R}_5) : \operatorname{deg}(p) \in \{-\infty,0,2,4\}\}
# \end{align*}
# 
# i.e, those polynomials of even degree at most five together with the zero polynomial. Is $W$ a subspace of $P(\mathbb{R}_5)$?
# 
# Let $p = x^2$ and $r = -x ^ 2 + x$ then $p, r \in W$ but $p + r = x^2 - x^2 + x = x \notin W$ since $\operatorname{deg}(x) = 1$ is odd. Therefore $W$ is not a subspace of $P(\mathbb{R}_5)$. Here we came up with a single counter example to show that the linear combination $p + r \notin W$. 
# 
# This counterexample is great but how does one come up with such a counterexample if you can't immediately think of one? If you do not see an obvious counterexample, try and construct one: we are looking for two even-degree polynomials, whose sum is not an even polynomial. Let's start at the lowest degree: $0$. The sum of two polynomials of degree $0$ is always $0$ or $\infty$, so there is no counterexample here. Let's try degree $2$. Now we need to find: $p(x) = ax^2 + bx + c$ and $r(x) = dx^2 + ex + f$, such that $p+r$ has degree one. Now 
# 
# \begin{align*}
#     p+r = (a + d)x^2 + (b + e)x + (c + f)
# \end{align*}
# 
# has degree one when $(a + d) = 0$ and $(b + e) \neq 0$. So let's take $a = 1$, $d = -1$ and $b = 0$, $e = 1$ (we don't care about $c$ or $f$, so let's just set both to be 0). This yields $p = x^2$ and $r = -x^2 + x$, which was our counterexample.
# 
# If we try constructing a counterexample and but fail, then it might mean that (a) a counterexample is not easy to find or (b) the statement is actually true. With a lot of pure maths research, mathematicians are often in this situation, trying to find a counterexample or a proof, not knowing which one it should be.
# 
# ::::{admonition} Example 5.4
# :class: seealso
# :name: non-subspace-example
# 
# Show that the following are not subspaces:
# 
# (i) &emsp; $W = \{z = (a+bi) : a + b = 5\} \subseteq \mathbb{C}$;
# 
# (i) &emsp; $W = \{z = (a + bi) : a^2 + b^2 < 0\} \subseteq \mathbb{C}$;
# 
# (i) &emsp; $W = \{(x,y,z) : x + y + z = 5\} \subseteq{\mathbb{R}^3}$.
# 
# :::{dropdown} Solution
# (i) &emsp;  Let $z = 1 + 4i \in W$ but $-1 \cdot z = -1 - 4i \notin W$. This shows that $W$ is not closed under taking scalar multiples, and hence not a subspace of $\mathbb{C}$ over $\mathbb{R}$. We could have also noted simply that $0\notin W$. 
# 
# The condition that there is a neutral element with respect to addition is one of the properties of a vector space (A3). So a subspace must also contain it.
# 
# (ii) &emsp; $W$ is the empty since $a^2 + b^2 \geq 0$ for all $a, b \in \mathbb{R}$. Hence $W$ is not a subspace.
# 
# (iii) &emsp;  Let $\mathbf{u} = (1, 2, 2) \in W$ and $\mathbf{v} = (2, 1, 2) \in W$, then $\mathbf{u} + \mathbf{v} = (3, 3, 4) \notin W$. We could've also just noted that $0 \notin W$. 
# :::
# ::::
