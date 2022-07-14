#!/usr/bin/env python
# coding: utf-8

# # Vector products
# 
# (dot-product-section)=
# ## Dot product
# 
# ::::{admonition} Definition: The dot product
# :class: note
# :name: dot-product-definition
# 
# The **dot product** (also known as the **scalar product**) of two vectors $\mathbf{a}$ and $\mathbf{b}$ in $\mathbb{R}^n$, is defined by
# 
# :::{math}
# :label: arithmetic-dot-product-equation
#   
# \mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^n a_ib_i = a_1b_1 + a_2b_2 + \cdots + a_nb_n.
# :::
# 
# In $\mathbb{R}^2$ and $\mathbb{R}^3$ the **dot product** of two vectors $\mathbf{a}$ and $\mathbf{b}$, can be defined in geometric terms by
# 
# :::{math}
# :label: geometric-dot-product-equation
# 
# \mathbf{a} \cdot \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \cos(\theta),
# :::
# 
# where $\theta$ is the angle between $\mathbf{a}$ and $\mathbf{b}$ ({numref}`dot-product-figure`).
# ::::
# 
# :::{figure} ../Images/dot_product.png
# :name: dot-product-figure
# 
# The dot product $\mathbf{a} \cdot \mathbf{b}$ is a scalar that is related to the angle between $\mathbf{a}$ and $\mathbf{b}$.
# :::
# 
# From the [definition of the dot product](dot-product-definition), we can observe the following:
# 
# - the dot product produces is a scalar quantity (an element of $\mathbb{R}$);
# - the dot product of two perpendicular vectors is zero, we write $\mathbf{a}\perp\mathbf{b}$ if $\mathbf{a}\cdot\mathbf{b}=0$;
# - the dot product of two co-directional (parallel) vectors $\mathbf{a}$ and $\mathbf{b}$ is equal to $|\mathbf{a}| |\mathbf{b}|$.
# 
# ::::{admonition} Theorem: Properties of the dot product
# :class: important
# :name: dot-product-properties-theorem
# 
# For any vectors $\mathbf{u},\mathbf{v},\mathbf{w}$ in $\mathbb{R}^n$ and any scalar $k$ in $\mathbb{R}$:
# 
# - the dot product is associative, i.e., $(\mathbf{u} + \mathbf{v})\cdot \mathbf{w} = \mathbf{u} \cdot \mathbf{w} + \mathbf{v} \cdot \mathbf{w}$;
# - for any scalar $k$, $(k \mathbf{u})\cdot \mathbf{v} = \mathbf{u} \cdot (k \mathbf{v})= k (\mathbf{u} \cdot \mathbf{v})$;
# - the dot product is commutative, i.e., $\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}$;
# - $\mathbf{u} \cdot \mathbf{u} = |\mathbf{u}|^2 \geq 0 \text{ and } \mathbf{u} \cdot \mathbf{u} = 0 \iff \mathbf{u} = \mathbf{0}.$
# ::::
# 
# :::::{admonition} Example 3.4
# :class: seealso
# :name: dot-product-example
# 
# Given the vectors $\mathbf{u} = (1, 2, 3)$ and $\mathbf{v} = (3, -1, 0)$. Calculate:
# 
# (i) &emsp; $\mathbf{u} \cdot \mathbf{v}$;
# 
# (ii) &emsp; the angle between $\mathbf{u}$ and $\mathbf{v}$
# 
# ::::{dropdown} Solution
# 
# (i) &emsp; Using equation {eq}`arithmetic-dot-product-equation`
# 
# \begin{align*}
#     \mathbf{u} \cdot \mathbf{v} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \cdot \begin{pmatrix} 3 \\ -1 \\ 0 \end{pmatrix} = 1(3) + 2(-1) + 3(0) = 3 - 2 + 0 = 1
# \end{align*}
# 
# (ii) &emsp; Using equation {eq}`geometric-dot-product-equation`
# \begin{align*}
#     \mathbf{u} \cdot \mathbf{v} &= |\mathbf{u}| |\mathbf{v}| \cos(\theta) \\
#     \therefore \theta &= \cos^{-1} \left( \frac{\mathbf{u} \cdot \mathbf{v}}{|\mathbf{u}||\mathbf{v}|}\right) \\
#     &= \cos^{-1} \left( \frac{1}{\sqrt{14}\sqrt{10}}\right) = 1.4862.
# \end{align*}
# 
# ::::
# :::::
# 
# Note: angles should be expressed in radians at all times.
# 
# ### Python code
# 
# The SymPy command for calculating the dot product of two vectors `u` and `v` is `u.dot(v)`. The code below calculates the solution to [example 3.4](dot-product-example).

# In[1]:


from sympy import * 

u = Matrix([1, 2, 3])
v = Matrix([3, -1, 0])
udotv = u.dot(v)
theta = acos(udotv / (u.norm() * v.norm()))

print(f"(i) u . v = {udotv}")
print(f"(ii) theta = {theta.evalf():0.4f}")


# (cross-product-section)=
# ## The cross product
# 
# ::::{admonition} Definition: The cross product
# :class: note
# :name: cross-product-definition
# 
# The **cross product** (also known as the **vector product) of two vectors in $\mathbb{R}^3$, $\mathbf{a}=(a_1,a_2,a_3)$ and $\mathbf{b}=(b_1,b_2,b_3)$ can be calculated using the formula
# 
# :::{math}
# :label: cross-product-equation
# 
# \mathbf{a} \times \mathbf{b} = \det 
# \begin{pmatrix}
#     \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 
#     a_1 & a_2 & a_3 \\ 
#     b_1 & b_2 & b_3 
# \end{pmatrix}.
# :::
# ::::
# 
# ::::{admonition} Theorem: Properties of the cross product
# :class: important
# :name: cross-product-properties-theorem
# 
# The cross product has the following properties:
# 
# - $\mathbf{a}\times \mathbf{b}$ produces a vector in the same space as $\mathbf{a}$ and $\mathbf{b}$;
# - $\mathbf{a}\times \mathbf{b}$ produces a vector that is perpendicular to both $\mathbf{a}$ and $\mathbf{b}$;
# - $\mathbf{a} \times \mathbf{b} = -(\mathbf{b} \times \mathbf{a})$ (i.e., there are two vectors perpendicular to $\mathbf{a}$ and $\mathbf{b}$ pointing in opposite directions);
# - if $\mathbf{a}$ and $\mathbf{b}$ are parallel vectors, then $\mathbf{a}\times \mathbf{b} = \mathbf{0}$;
# - the self cross product of a vector is the zero vector, i.e., $\mathbf{a} \times \mathbf{a} = \mathbf{0}$;
# - the cross product is not commutative, i.e., $\mathbf{a} \times \mathbf{b} \neq \mathbf{b} \times \mathbf{a}$;
# - the cross product is distributive over addition, i.e., $\mathbf{a} \times (\mathbf{b} + \mathbf{c}) = (\mathbf{a} \times \mathbf{b}) + (\mathbf{a} \times \mathbf{c})$;
# - the cross product is not associative, i.e., $\mathbf{a} \times (\mathbf{b} \times \mathbf{c}) \neq (\mathbf{a} \times \mathbf{b}) \times \mathbf{c}$.
# ::::
# 
# :::{figure} ../Images/cross_product.png
# :name: cross-product-figure
# 
# The cross product $\mathbf{a} \times \mathbf{b}$ is another vector perpendicular to both $\mathbf{a}$ and $\mathbf{b}$.
# :::
# 
# :::::{admonition} Example 3.5
# :class: seealso
# :name: cross-product-example
# 
# Calculate the cross product between the vectors $\mathbf{u} = (1, 2, 3)$ and $\mathbf{v} = (4, 5, 6)$.
# 
# ::::{dropdown} Solution
# 
# \begin{align*}
#     \mathbf{u} \times \mathbf{v} &= \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & 3 \\ 4 & 5 & 6 \end{vmatrix}
#     = (12 - 15)\mathbf{i} - (6 - 12) \mathbf{j} + (5 - 8) \mathbf{k} \\
#     &= -3\mathbf{i} + 6 \mathbf{j} + 3\mathbf{k}
#     = \begin{pmatrix} -3 \\ 6 \\ -3 \end{pmatrix}.
# \end{align*}
# 
# ::::
# :::::
# 
# ### Python code
# 
# The SymPy command for calculating the cross product of two vectors `u` and `v` is `u.cross(v)`. The following code calculates the solution to [example 3.5](cross-product-example).

# In[2]:


u = Matrix([1, 2, 3])
v = Matrix([4, 5, 6])

ucrossv = u.cross(v)
display(ucrossv)

