#!/usr/bin/env python
# coding: utf-8

# (arithmetic-operations-on-vectors-section)=
# # Arithmetic operations on vectors
# 
# ## Vector equality
# 
# :::::{admonition} Definition: Vector equality
# :class: note
# :name: vector-equality-definition
# 
# Two vectors in $\mathbb{R}^n$ are said to be equal if they are represented by the same $n$-tuple. In other words $\mathbf{a},\mathbf{b}\in \mathbb{R}^n$ represented by $n$-tuples $(a_1, a_2, \ldots, a_n)$ and $(b_1, b_2, \ldots, b_n)$ respectively, are equal if and only if the elements which correspond co-ordinate-wise are equal, i.e.,
# 
# \begin{align*}
#     a_i = b_i, \qquad i = 1, \ldots, n.
# \end{align*}
# 
# Informally this happens if and only if they have the same magnitude and they point in the same direction.
# :::::
# 
# It follows from the [definition of vector equality](vector-equality-definition) that a vector can be moved parallel to itself and still represent the same vector, i.e., the position of the vector does not matter when considering vector equality. Consider {numref}`vector-equality-figure` which shows four vectors in $\mathbb{R}^2$. The vectors $\mathbf{a}$ and $\mathbf{b}$ point in the same direction and have the same magnitude so we can say that $\mathbf{a}=\mathbf{b}$. The vector $\mathbf{c}$ has the same magnitude as $\mathbf{a}$ and $\mathbf{b}$ but points in the opposite direction so $\mathbf{c}\neq \mathbf{a}$. The vector $\mathbf{d}$ points in the same direction as $\mathbf{a}$ but has a larger magnitude so $\mathbf{d} \neq \mathbf{a}$.
# 
# :::{figure} ../Images/vector_equality.png
# :name: vector-equality-figure
# 
# Of these four vectors only $\mathbf{a}$ and $\mathbf{b}$ are equal.
# :::
# 
# ### Python
# 
# To check whether two vectors `u` and `v` are equal we can use the command `u == v`. 

# In[1]:


from sympy import *

u = Matrix([1, 2, 3])
v = Matrix([2 ** 0, 4 / 2, sqrt(9)])

print(u == v)


# ## Vector addition
# 
# Given three points $A$, $B$ and $C$ in $\mathbb{R}^n$ it is natural to ask how we might express the vector $\overrightarrow{AC}$ in terms of $\overrightarrow{AB}$ and $\overrightarrow{BC}.$ The answer is given by vector addition. In other words $\overrightarrow{AC} = \overrightarrow{AB} + \overrightarrow{BC}$ where addition of two vectors is defined below.
# 
# ::::{admonition} Definition: Addition of two vectors
# :class: note
# :name: vector-addition-definition
# 
# The addition of two vectors $\mathbf{a},\mathbf{b}\in\mathbb{R}^n$ is calculated using
# \begin{align*}
#     \mathbf{a} + \mathbf{b} = 
#     \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix} + 
#     \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{pmatrix} =
#     \begin{pmatrix} a_1 + b_1 \\ a_2 + b_2 \\ \vdots \\ a_n + b_n \end{pmatrix}.
# \end{align*}
# ::::
# 
# Intuitively this makes sense, the displacement from $A$ to $C$ in any coordinate direction is just the displacement from $A$ to $B$ plus the displacement from $B$ to $C$ in the relevant coordinate direction.
# 
# The geometric representation of $\mathbf{a}+\mathbf{b}$ is represented in {numref}`vector-addition-figure`. Note that $\mathbf{a}+\mathbf{b}$ is the same as placing the tail of $\mathbf{b}$ at the head of $\mathbf{a}$. Note also, as the figure demonstrates, that the order in which one adds the two vectors is unimportant. This is known as the **parallelogram law of addition**.
# 
# :::{figure} ../Images/vector_addition.png
# :name: vector-addition-figure
# 
# The addition of two vectors.
# :::

# ## Scalar multiplication
# 
# 
# ::::{admonition} Definition: Scalar multiplication of a vector
# :class: note
# :name: scalar-multiplication-of-a-vector-definition
# 
# The multiplication of a vector $\mathbf{a}\in \mathbb{R}^n$ by a scalar $k \in \mathbb{R}$ is defined by
# 
# \begin{align*}
#     k\mathbf{a} = k\begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix} = 
#     \begin{pmatrix} k a_1 \\ k a_2 \\ \vdots \\ k a_n \end{pmatrix}.
# \end{align*}
# ::::
# 
# Multiplying a vector by a scalar has the effect of **scaling** the vector $\mathbf{a}$ to produce a vector **parallel** to $\mathbf{a}$ with a magnitude of $k|\mathbf{a}|$. In general if two vectors $\mathbf{u}$ and $\mathbf{v}$ are parallel then we write $\mathbf{u} \parallel \mathbf{v}$.
# 
# ::::{admonition} Theorem: Properties of scalar multiplication of vectors
# :class: important
# :name: properties-of-scalar-multiplication-of-vectors
# 
# The scalar multiplication of a vector $\mathbf{a}$ by a scalar $k$ has the following properties:
# 
# - $k\mathbf{a}$ = $\mathbf{a}k$  is a vector parallel to $\mathbf{a}$;
# - $0\mathbf{a} = (0, 0, \ldots, 0) = \mathbf{0}$;
# - $1\mathbf{a} = \mathbf{a}$;
# - $|k\mathbf{a}| = |k||\mathbf{a}|$;
# - if $k>0$ then $\mathbf{a}$ and $k\mathbf{a}$ point in the same direction, whereas if $k<0$ then $\mathbf{a}$ and $k\mathbf{a}$ point in opposite directions.
# ::::
# 
# :::{figure} ../Images/scalar_multiplication_of_a_vector.png
# :name: scalar-multiplication-of-a-vector-figure
# 
# Scaled variations of the vector $\mathbf{a}$.
# :::
