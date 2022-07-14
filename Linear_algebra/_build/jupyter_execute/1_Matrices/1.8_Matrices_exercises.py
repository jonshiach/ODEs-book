#!/usr/bin/env python
# coding: utf-8

# # Matrices exercises

# :::::{admonition} Exercise 1.1
# :class: note
# :name: ex1.1
# 
# Write down the $3 \times 3$ matrix $A$ whose entries are given by $a_{ij} = i+j.$
# 
# ::::{dropdown} Solution
# \begin{align*}
#     A = \begin{pmatrix} 2 & 3 & 4 \\
#         3 & 4 & 5 \\
#         4 & 5 & 6 \end{pmatrix}
# \end{align*}
# ::::
# :::::

# :::::{admonition} Exercise 1.2
# :class: note
# :name: ex1.2
# 
# Write down the $4 \times 4$ matrix $B$ whose entries are given by $b_{ij} = (-1)^{i+j}.$
# 
# ::::{dropdown} Solution
# \begin{align*}
#     B = \begin{pmatrix}
#         1 & -1 & 1 & -1 \\
#         -1 & 1 & -1 & 1 \\
#         1 & -1 & 1 & -1 \\
#         -1 & 1 & -1 & 1
#         \end{pmatrix}
# \end{align*}
# ::::
# :::::

# :::::{admonition} Exercise 1.3
# :class: note
# :name: ex1.3
# 
# Write down the $4 \times 4$ matrix $C$ whose entries are given by 
# \begin{align*}
#     c_{ij} = 
#     \begin{cases}
#     -1, & i>j, \\
#     0, & i=j, \\
#     1, & i<j. \\
#     \end{cases}
# \end{align*}
# 
# ::::{dropdown} Solution
# \begin{align*}
#     C = \begin{pmatrix}
#         0 & 1 & 1 & 1 \\
#         -1 & 0 & 1 & 1 \\
#         -1 & -1 & 0 & 1 \\
#         -1 & -1 & -1 & 0
#     \end{pmatrix}
# \end{align*}
# ::::
# :::::

# :::::{admonition} Exercise 1.4
# :class: note
# :name: ex1.4
# 
# Given the matrices
# \begin{align*}
#     A &= \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix}, &
#     B &= \begin{pmatrix} 3 & 0 \\ -1 & 5 \end{pmatrix}, \\
#     C &= \begin{pmatrix} 5 \\ 9 \end{pmatrix}, &
#     D &= \begin{pmatrix} 1 & 1 & 3 \\ 4 & -2 & 3 \end{pmatrix}, \\
#     E &= \begin{pmatrix} 1 & 2 \\ 0 & 6 \\ -2 & 3 \end{pmatrix} &
#     F &= \begin{pmatrix} 1 & -2 & 4 \end{pmatrix}, \\
#     G &= \begin{pmatrix} 4 & 2 & 3 \\ -2 & 6 & 0 \\ 0 & 7 & 1 \end{pmatrix}, &
#     H &= \begin{pmatrix} 1 & 0 & 1 \\ 5 & 2 & -2 \\ 2 & -3 & 4 \end{pmatrix}.
# \end{align*}
# 
# Calculate the following where possible:
# 
# ::::{grid}
# 
# :::{grid-item}
# :columns: 4
# (a) &emsp; $A + B$
# :::
# 
# :::{grid-item}
# :columns: 4
# (b) &emsp; $B + C$
# :::
# 
# :::{grid-item}
# :columns: 4
# (c) &emsp; $A^\mathrm{T}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (d) &emsp; $C^\mathrm{T}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (e) &emsp; $D + E^\mathrm{T}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (f) &emsp; $3B - A$
# :::
# 
# :::{grid-item}
# :columns: 4
# (g) &emsp; $E + F^\mathrm{T}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (h) &emsp; $(F^\mathrm{T})^\mathrm{T}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (i) &emsp; $2(G + H)$
# :::
# 
# :::{grid-item}
# :columns: 4
# (j) &emsp; $A^\mathrm{T} + B^\mathrm{T}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (k) &emsp; $(A + B)^\mathrm{T}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (l) &emsp; $-G$
# :::
# 
# ::::
# 
# ::::{dropdown} Solutions
# (a) &emsp; $A + B = \begin{pmatrix} 1 + 3 & -3 + 0 \\ 4 + (-1) & 2 + 5 \end{pmatrix} = \begin{pmatrix} 4 & -3 \\ 3 & 7 \end{pmatrix}$
# 
# (b) &emsp; $B + C$ is undefined since $B$ is $2\times 2$ and $C$ is $2\times 1$
# 
# (c) &emsp; $A^\mathrm{T} = \begin{pmatrix} 1 & 4 \\ -3 & 2 \end{pmatrix}$
# 
# (d) &emsp; $C^\mathrm{T} = \begin{pmatrix} 5 & 9 \end{pmatrix}$
# 
# (e) &emsp; $D + E^\mathrm{T} = \begin{pmatrix} 1 & 1 & 3 \\ 4 & -2 & 3 \end{pmatrix} + \begin{pmatrix} 1 & 0 & -2 \\ 2 & 6 & 3 \end{pmatrix} = \begin{pmatrix} 2 & 1 & 1 \\ 6 & 4 & 6 \end{pmatrix}$
# 
# (f) &emsp; $3 B - A = \begin{pmatrix} 9 & 0 \\ -3 & 15 \end{pmatrix} - \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix} = \begin{pmatrix} 8 & 3 \\ -7 & 13 \end{pmatrix}$
# 
# (g) &emsp; $E + F^\mathrm{T}$ is undefined since $E$ is $3\times 2$ and $F^\mathrm{T}$ is $3\times 1$
# 
# (h) &emsp;  $(F^\mathrm{T})^\mathrm{T} = \begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}^\mathrm{T} = \begin{pmatrix} 1 & -2 & 4 \end{pmatrix} = F$
# 
# (i) &emsp; $2(G+H) = 2 \begin{pmatrix} 5 & 2 & 4 \\ 3 & 8 & -2 \\ 2 & 4 & 5 \end{pmatrix} = \begin{pmatrix} 10 & 4 & 8 \\ 6 & 16 & -4 \\ 4 & 8 & 10 \end{pmatrix}$
# 
# (j) &emsp; $A^\mathrm{T} + B^\mathrm{T} = \begin{pmatrix} 1 & 4 \\ -3 & 2 \end{pmatrix} + \begin{pmatrix} 3 & -1 \\ 0 & 5 \end{pmatrix} = \begin{pmatrix} 4 & 3 \\ -3 & 7 \end{pmatrix}$
# 
# (k) &emsp; $(A + B)^\mathrm{T} = \begin{pmatrix} 4 & -3 \\ 3 & 7 \end{pmatrix}^\mathrm{T} = \begin{pmatrix} 4 & 3 \\ -3 & 7 \end{pmatrix}$
# 
# (l) &emsp; $-G = \begin{pmatrix} -1 & 0 & -1 \\ -5 & -2 & 2 \\ -2 & 3 & -4 \end{pmatrix}$
# 
# ::::
# 
# :::::

# :::::{admonition} Exercise 1.5
# :class: note
# :name: ex1.5
# 
# Using the matrices from [exercise 1.4](ex1.4) calculate the following where possible:
# 
# ::::{grid}
# 
# :::{grid-item}
# :columns: 4
# (a) &emsp;  $AB$
# :::
# 
# :::{grid-item}
# :columns: 4
# (b) &emsp;  $BA$
# :::
# 
# :::{grid-item}
# :columns: 4
# (c) &emsp;  $AC$
# :::
# 
# :::{grid-item}
# :columns: 4
# (d) &emsp;  $CA$
# :::
# 
# :::{grid-item}
# :columns: 4
# (e) &emsp;  $C^\mathrm{T}C$
# :::
# 
# :::{grid-item}
# :columns: 4
# (f) &emsp;  $CC^\mathrm{T}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (g) &emsp;  $DE$
# :::
# 
# :::{grid-item}
# :columns: 4
# (h) &emsp;  $GH$
# :::
# 
# :::{grid-item}
# :columns: 4
# (i) &emsp;  $A(DE)$
# :::
# 
# :::{grid-item}
# :columns: 4
# (j) &emsp;  $(AD)E$
# :::
# 
# :::{grid-item}
# :columns: 4
# (k) &emsp;  $A^3$
# :::
# 
# :::{grid-item}
# :columns: 4
# (l) &emsp;  $G^4$
# :::
# 
# ::::
# 
# ::::{dropdown} Solutions
# (a) &emsp; $AB = \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix} \begin{pmatrix} 3 & 0 \\ -1 & 5 \end{pmatrix} = \begin{pmatrix} 3 + 3 & 0 - 15 \\ 7 - 2 & 0 + 10 \end{pmatrix} = \begin{pmatrix}6 & -15 \\ 10 & 10 \end{pmatrix}$
# 
# (b) &emsp; $BA = \begin{pmatrix} 3 & 0 \\ -1 & 5 \end{pmatrix}\begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix} = \begin{pmatrix} 3 + 0 & -9 + 0 \\ -1 + 20 & 3 + 10 \end{pmatrix} = \begin{pmatrix} 3 & -9 \\ 19 & 13 \end{pmatrix}$
# 
# (c) &emsp; $AC = \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix}\begin{pmatrix} 5 \\ 9 \end{pmatrix} = \begin{pmatrix} 15 - 27 \\ 20 + 18 \end{pmatrix} = \begin{pmatrix} -22 \\ 38 \end{pmatrix}$
# 
# (d) &emsp; $CA$ is undefined since $C$ has 1 column and $A$ has 2 rows
# 
# (e) &emsp; $C^TC = \begin{pmatrix} 5 & 9 \end{pmatrix} \begin{pmatrix} 5 \\ 9 \end{pmatrix} = 25 + 81 = 106$
# 
# (f) &emsp; $CC^T = \begin{pmatrix} 5 \\ 9 \end{pmatrix}\begin{pmatrix} 5 & 9 \end{pmatrix} = \begin{pmatrix} 25 & 45 \\ 45 & 81 \end{pmatrix}$
# 
# (g) &emsp; 
# \begin{align*}
#     DE &= \begin{pmatrix} 1 & 1 & 3 \\ 4 & -2 & 3 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 6 \\ -2 & 3 \end{pmatrix} = \begin{pmatrix} 1 + 0 - 6 & 2 + 6 + 9 \\ 4 + 0 - 6 & 8 - 12 + 9 \end{pmatrix} \\
#     &= \begin{pmatrix} -5 & 17 \\ -2 & 5 \end{pmatrix}
# \end{align*}
# 
# (h) &emsp; 
# \begin{align*}
#     GH &= \begin{pmatrix} 4 & 2 & 3 \\ -2 & 6 & 0 \\ 0 & 7 & 1 \end{pmatrix}
#     \begin{pmatrix} 1 & 0 & 1 \\ 5 & 2 & -2 \\ 2 & -3 & 4 \end{pmatrix} \\
#     &= \begin{pmatrix} 
#         4 + 10 + 6 & 0 + 4 - 9 & 4 - 4 + 12 \\
#         -2 + 30 + 0 & 0 + 12 + 0 & -2 - 12 + 0 \\
#         0 + 35 + 2 & 0 + 14 - 3 & 0 - 14 + 4
#     \end{pmatrix} \\
#     &= \begin{pmatrix} 20 & -5 & 12 \\ 28 & 12 & -14 \\ 37 & 11 & -10 \end{pmatrix}
# \end{align*}
# 
# (i) &emsp; 
# \begin{align*}
#     A(DE) &= \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix} \left(
#     \begin{pmatrix} 1 & 1 & 3 \\ 4 & -2 & 3 \end{pmatrix} 
#     \begin{pmatrix} 1 & 2 \\ 0 & 6 \\ -2 & 3 \end{pmatrix} \right) \\
#     &= \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix}
#     \begin{pmatrix} -5 & 17 \\ -2 & 5 \end{pmatrix} \\
#     &= \begin{pmatrix} 1 & 2 \\ -24 & 78 \end{pmatrix}
# \end{align*}
# 
# (j) &emsp; 
# \begin{align*}
#     (AD)E &= \left(
#     \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix}
#     \begin{pmatrix} 1 & 1 & 3 \\ 4 & -2 & 3 \end{pmatrix}
#     \right)
#     \begin{pmatrix} 1 & 2 \\ 0 & 6 \\ -2 & 3 \end{pmatrix} \\
#     &= \begin{pmatrix} -11 & 7 & -6 \\ 12 & 0 & 18 \end{pmatrix}
#     \begin{pmatrix} 1 & 2 \\ 0 & 6 \\ -2 & 3 \end{pmatrix} \\
#     &= \begin{pmatrix} 1 & 2 \\ -24 & 78 \end{pmatrix}
# \end{align*}
# 
# (k) &emsp; 
# \begin{align*}
#     A^3 &= \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix}
#     \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix}
#     \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix} \\
#     &= \begin{pmatrix} -11 & -9 \\ 12 & -8 \end{pmatrix}
#     \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix} \\
#     &= \begin{pmatrix} -47 & 15 \\ -20 & -52 \end{pmatrix}
# \end{align*}
# 
# (l) &emsp; 
# \begin{align*}
#     G^2 &= \begin{pmatrix} 4 & 2 & 3 \\ -2 & 6 & 0 \\ 0 & 7 & 1 \end{pmatrix}
#     \begin{pmatrix} 4 & 2 & 3 \\ -2 & 6 & 0 \\ 0 & 7 & 1 \end{pmatrix} \\
#     &= \begin{pmatrix} 12 & 41 & 15 \\ -20 & 32 & -6 \\ -14 & 49 & 1 \end{pmatrix} \\
#     \therefore G^4 &= G^2G^2 = 
#     \begin{pmatrix} 12 & 41 & 15 \\ -20 & 32 & -6 \\ -14 & 49 & 1 \end{pmatrix}
#     \begin{pmatrix} 12 & 41 & 15 \\ -20 & 32 & -6 \\ -14 & 49 & 1 \end{pmatrix} \\
#     &=
#     \begin{pmatrix} -886 & 2539 & -51 \\ -796 & -90 & -498 \\ -1162 & 1043 & -503 \end{pmatrix}
# \end{align*}
# ::::
# :::::

# :::::{admonition} Exercise 1.6
# :class: note
# :name: ex1.6
# 
# Using the matrices from [exercise 1.4](ex1.4) calculate the following:
# 
# ::::{grid}
# 
# :::{grid-item}
# :columns: 4
# (a) &emsp;  $\det(A)$
# :::
# 
# :::{grid-item}
# :columns: 4
# (b) &emsp;  $|B|$
# :::
# 
# :::{grid-item}
# :columns: 4
# (c) &emsp;  $\det(3A)$
# :::
# 
# :::{grid-item}
# :columns: 4
# (d) &emsp;  $\det(G)$
# :::
# 
# :::{grid-item}
# :columns: 4
# (e) &emsp;  $\operatorname{adj}(B)$
# :::
# 
# :::{grid-item}
# :columns: 4
# (f) &emsp;  $\operatorname{adj}(H)$
# :::
# 
# :::{grid-item}
# :columns: 4
# (g) &emsp;  $A^{-1}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (h) &emsp;  $B^{-1}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (i) &emsp;  $G^{-1}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (j) &emsp;  $(AB)^{-1}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (k) &emsp;  $B^{-1}A^{-1}$
# :::
# 
# :::{grid-item}
# :columns: 4
# (l) &emsp;  $(DE)^{-1}$
# :::
# ::::
# 
# ::::{dropdown} Solutions
# 
# (a) &emsp;  $\det(A) = 1(2) - (-3)4 = 2 + 12 = 14$
# 
# (b) &emsp;  $|B| = 3(5) - 0(-1) = 15$
# 
# (c) &emsp;  $\det(3A) = 3\begin{vmatrix} 3 & -9 \\ 12 & 6 \end{vmatrix} = 3(6) - (-9)(12) = 126$.
# 
# Alternatively since each row of $A$ is multiplied by 3 then by the [properties of determinants](properties-of-determinants-theorem) we could simply multiply $\det(A)=14$ by $3 \times 3 = 9$ to give $\det(3A) = 126$.
# 
# (d) &emsp; 
# \begin{align*}
#     \det(G) &= \begin{vmatrix} 4 & 2 & 3 \\ -2 & 6 & 0 \\ 0 & 7 & 1 \end{vmatrix} \\
#     &= 4 \begin{vmatrix} 6 & 0 \\ 7 & 1 \end{vmatrix} - (-2)
#     \begin{vmatrix} 2 & 3 \\ 7 & 1 \end{vmatrix} \\
#     &= 4(6) + 2(2 - 21) = -14
# \end{align*}
# 
# (e) &emsp;  $\operatorname{adj}(B) = \begin{pmatrix} 5 & -(-1) \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 5 & 0 \\ 1 & 3 \end{pmatrix}$
# 
# (f) &emsp; 
# 
# \begin{align*}
#     \operatorname{adj}(H) &= 
#     \begin{pmatrix}
#         \begin{vmatrix} 2 & -2 \\ -3 & 4 \end{vmatrix} &
#         - \begin{vmatrix} 5 & -2 \\ 2 & 4 \end{vmatrix} &
#         \begin{vmatrix} 5 & 2 \\ 2 & -3 \end{vmatrix} \\
#         - \begin{vmatrix} 0 & 1 \\ -3 & 4 \end{vmatrix} &
#         \begin{vmatrix} 1 & 1 \\ 2 & 4 \end{vmatrix} &
#         - \begin{vmatrix} 1 & 0 \\ 2 & -3 \end{vmatrix} \\
#         \begin{vmatrix} 0 & 1 \\ 2 & -2 \end{vmatrix} &
#         - \begin{vmatrix} 1 & 1 \\ 5 & -2 \end{vmatrix} &
#         \begin{vmatrix} 1 & 0 \\ 5 & 2 \end{vmatrix}
#     \end{pmatrix}^T \\
#     &= \begin{pmatrix} 2 & -24 & -19 \\ -3 & 2 & 3 \\ -2 & 7 & 2 \end{pmatrix}^T \\
#     &= \begin{pmatrix} 2 & -3 & -2 \\ -24 & 2 & 7 \\ -19 & 3 & 2 \end{pmatrix}
# \end{align*}
# 
# (g) &emsp; 
# \begin{align*}
#     \operatorname{adj}(A) &= \begin{pmatrix} 2 & 3 \\ -4 & 1 \end{pmatrix}, \qquad
#     \det(A) = 14, \\
#     \therefore A^{-1} &= \frac{\operatorname{adj}(A)}{\det(A)} 
#     = \frac{1}{14}\begin{pmatrix} 2 & -4 \\ 3 & 1 \end{pmatrix}
#     = \begin{pmatrix} \frac{1}{7} & \frac{3}{14} \\ -\frac{2}{7} & \frac{1}{14} \end{pmatrix} 
# \end{align*}
# 
# Check: $\begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix}\begin{pmatrix} \frac{1}{7} & \frac{3}{14} \\ -\frac{2}{7} & \frac{1}{14} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \quad \checkmark$
# 
# (h) &emsp;
# \begin{align*}
#     \operatorname{adj}(B) &= \begin{pmatrix} 5 & 0 \\ 1 & 3 \end{pmatrix}, \qquad
#     \det(B) = 15, \\
#     \therefore B^{-1} &= \frac{\operatorname{adj}(B)}{\det(A)} 
#     = \frac{1}{15} \begin{pmatrix} 5 & 0 \\ 1 & 3 \end{pmatrix} 
#     = \begin{pmatrix} \frac{1}{3} & 0 \\ \frac{1}{15} & \frac{1}{5} \end{pmatrix}
# \end{align*}
# 
# Check: $BB^{-1} = \begin{pmatrix} 3 & 0 \\ -1 & 5 \end{pmatrix}\begin{pmatrix} \frac{1}{3} & 0 \\ \frac{1}{15} & \frac{1}{5} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \quad \checkmark$
# 
# (i) &emsp;  $G^{-1}$
# 
# \begin{align*}
#     \operatorname{adj}(G) &= 
#     \begin{pmatrix}  6 & 2 & -14 \\ 19 & 4 & -28 \\ -18 & -6 & 28 \end{pmatrix}^T
#     = \begin{pmatrix} 6 & 19 & -18 \\ 2 & 4 & -6 \\ -14 & -28 & 28 \end{pmatrix}, \\
#     \det(G) &= -14, \\
#     \therefore G^{-1} &= \frac{\operatorname{adj}(G)}{\det(G)} = -\frac{1}{14}
#     \begin{pmatrix} 6 & 19 & -18 \\ 2 & 4 & -6 \\ -14 & -28 & 28 \end{pmatrix} \\
#     &= \begin{pmatrix} 
#         -\frac{3}{7} & -\frac{19}{14} & \frac{9}{7} \\
#         -\frac{1}{7} & -\frac{2}{7} & \frac{3}{7} \\
#         1 & 2 & -2
#     \end{pmatrix}
# \end{align*}
# 
# Check: $GG^{-1} = \begin{pmatrix} 4 & 2 & 3 \\ -2 & 6 & 0 \\ 0 & 7 & 1 \end{pmatrix} 
#     \begin{pmatrix} 
#         -\frac{3}{7} & -\frac{19}{14} & \frac{9}{7} \\
#         -\frac{1}{7} & -\frac{2}{7} & \frac{3}{7} \\
#         1 & 2 & -2
#     \end{pmatrix} =
#     \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \quad  \checkmark$
# 
# (j) &emsp;  $(AB)^{-1}$
# 
# \begin{align*}
#     \operatorname{adj}(AB) &= \begin{pmatrix} 10 & -15 \\ 10 & 6 \end{pmatrix}, \qquad
#     \det(AB) = 60 + 150 = 210, \\
#     \therefore (AB)^{-1} &= \frac{\operatorname{adj}(AB)}{\det(AB)} = \frac{1}{210}
#     \begin{pmatrix} 10 & -15 \\ 10 & 6 \end{pmatrix} =
#     \begin{pmatrix} \frac{1}{21} & \frac{1}{14} \\ -\frac{1}{21} & \frac{1}{35} \end{pmatrix}
# \end{align*}
# 
# Check $(AB)(AB)^{-1} = \begin{pmatrix} 6 & -15 \\ 10 & 10 \end{pmatrix} \begin{pmatrix} \frac{1}{21} & \frac{1}{14} \\ -\frac{1}{21} & \frac{1}{35} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \quad \checkmark$
# 
# (k) &emsp; Using the [properties of inverse matrices](properties-of-inverse-matrices-theorem) we know that $(AB)^{-1} = B^{-1}A^{-1}$ so
# 
# \begin{align*}
#     B^{-1}A^{-1} = \begin{pmatrix} \frac{1}{21} & \frac{1}{14} \\ -\frac{1}{21} & \frac{1}{35} \end{pmatrix}
# \end{align*}
# 
# (l) &emsp; 
# 
# \begin{align*}
#     \operatorname{adj}(DE) &= \begin{pmatrix} 5 & -17 \\ 2 & -5 \end{pmatrix}, \qquad
#     \det(DE) = -25 + 34 = 9, \\
#     \therefore (DE)^{-1} &= \frac{\operatorname{adj}(DE)}{\det(DE)} 
#     = \frac{1}{9} \begin{pmatrix} 5 & -17 \\ 2 & -5 \end{pmatrix}
#     = \begin{pmatrix} \frac{5}{9} & -\frac{17}{9} \\ \frac{2}{9} & -\frac{5}{9} \end{pmatrix}
# \end{align*}
# 
# Check: $(DE)(DE)^{-1} = \begin{pmatrix} -5 & 17 \\ -2 & 5 \end{pmatrix} \begin{pmatrix} \frac{5}{9} & -\frac{17}{9} \\ \frac{2}{9} & -\frac{5}{9} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \quad \checkmark$
# 
# ::::
#     
# :::::

# :::::{admonition} Exercise 1.7
# :class: note
# :name: ex1.7
# 
# Using [the properties of determinants](properties-of-determinants-theorem) and solutions from [exercise 1.6](ex1.6) where necessary, find the determinants for the following matrices.
# 
# 
# ::::{grid}
# :gutter: 2
# 
# :::{grid-item}
# :columns: 6
# (a) &emsp;  $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 6
# (b) &emsp;  $\begin{pmatrix} 4 & 2 \\ 1 & -3 \end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 6
# (c) &emsp;  $\begin{pmatrix} 1 & 0 \\ -1 & 0 \end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 6
# (d) &emsp;  $\begin{pmatrix} 4 & 2 & 3 \\ -4 & 12 & 0 \\ 0 & 7 & 1 \end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 6
# (e) &emsp;  $\begin{pmatrix} 1 & 2 & 3 \\ -1 & -2 & -3 \\ 2 & 4 & 4 \end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 6
# (f) &emsp;  $\begin{pmatrix} 1 & 2 & 1 \\ -3 & -6 & 1 \\ 2 & 4 & 4 \end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 6
# (g) &emsp;  $\begin{pmatrix} 1 & 2 & 3 \\ -1 & -2 & 0 \\ 0 & 0 & 0 \end{pmatrix}$
# :::
# 
# :::{grid-item}
# :columns: 6
# (h) &emsp;  $\begin{pmatrix} 3 & 6 \\ -1 & 3 \end{pmatrix}$
# :::
# 
# ::::
# 
# 
# ::::{dropdown} Solutions
# 
# (a) &emsp; Row 2 is 2 times row 1 so the determinant is 0.
# 
# (b) &emsp; This is the same as the matrix $A$ above but with rows 1 and 2 swapped. Therefore the determinant of this matrix is $-\det(A) = -14$.
# 
# (c) &emsp; Column 2 is all zeros so the determinant is 0.
# 
# (d) &emsp; This it the same as the matrix $G$ from above with row 2 multiplied by 2. Therefore the determinant of this matrix is $2\det(G) = 2(-14) = -28$.
# 
# (e) &emsp; Row 2 is -1 times row 1 so the determinant is 0.
# 
# (f) &emsp; Column 2 is 2 times column 1 so the determinant is 0.
# 
# (g) &emsp; Row 3 is all zeros so the determinant is 0.
# 
# (h) &emsp; This is the same as the matrix $B$ from above with 2 times column 1 added to column 2. Therefore the determinant of this matrix is $\det(B) = 15$.
#         
# :::::
# 
# :::::{admonition} Exercise 1.8
# :class: note
# :name: ex1.8
# 
# Prove that adding a multiple of a row or column to another row or column does not change the value of the determinant for a $2\times 2$ matrix.
# 
# ::::{dropdown} Solution
# Let $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ and $k$ be a scalar then
# 
# \begin{align*}
#     \begin{vmatrix} a & b \\ c + ka & d + kb \end{vmatrix} &= ad + abk - bc - abk = ad - bc = \det(A), \\
#     \begin{vmatrix} a & b + ak \\ c & d + ck \end{vmatrix} &= ad + ack - bc - ack = ad - bc = \det(A)
# \end{align*}
# 
# <div style="text-align: right"> &#9633; </div>
# 
# ::::
# 
# :::::

# :::::{admonition} Exercise 1.9
# Given the matrices
# 
# \begin{align*}
#     A &= \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix}, &
#     B &= \begin{pmatrix} 3 & 0 \\ -1 & 5 \end{pmatrix},
# \end{align*}
# 
# solve the following equations for $X$.
# 
# ::::{grid}
# 
# :::{grid-item}
# :columns: 6
# (a) &emsp; $5X = A$
# :::
# 
# :::{grid-item}
# :columns: 6
# (b) &emsp; $X + A = I$
# :::
# 
# :::{grid-item}
# :columns: 6
# (c) &emsp; $2X - B = A$
# :::
# 
# :::{grid-item}
# :columns: 6
# (d) &emsp; $XA = I$
# :::
# 
# :::{grid-item}
# :columns: 6
# (e) &emsp; $BX = A$
# :::
# 
# :::{grid-item}
# :columns: 6
# (f) &emsp; $A^2 = X$
# :::
# 
# :::{grid-item}
# :columns: 6
# (g) &emsp; $X^2 = B$
# :::
# 
# :::{grid-item}
# :columns: 6
# (h) &emsp; $(X + A)B = I$
# :::
# 
# ::::
# 
# 
# ::::{dropdown} Solutions
# (a) &emsp; 
# \begin{align*}
#     5X &= A \\
#     X &= \frac{1}{5} A \\
#     &= \dfrac{1}{5}\begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix} 
#     = \begin{pmatrix} \frac{1}{5} & -\frac{3}{5} \\ \frac{4}{5} & \frac{2}{5} \end{pmatrix}
# \end{align*}
# 
# (b) &emsp; 
# \begin{align*}
#     X + A &= I \\
#     X &= I - A \\
#     &= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix} = \begin{pmatrix} 0 & 3 \\ -4 & -1 \end{pmatrix}
# \end{align*}
# 
# (c) &emsp; 
# 
# \begin{align*}
#     2X - B &= A \\
#     2X &= A + B \\
#     X &= \dfrac{1}{2}(A + B) = \dfrac{1}{2}\left( \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix} + \begin{pmatrix} 3 & 0 \\ -1 & 5 \end{pmatrix} \right) \\
#     &= \dfrac{1}{2} \begin{pmatrix} 4 & -3 \\ 3 & 7 \end{pmatrix} = \begin{pmatrix} 2 & -\frac{3}{2} \\ \frac{3}{2} & \frac{7}{2} \end{pmatrix}
# \end{align*}
# 
# (d) &emsp; 
# 
# \begin{align*}
#     XA &= I \\
#     X &= IA^{-1} = A^{-1}I \\
#     &= \dfrac{1}{14} \begin{pmatrix} 2 & 3 \\ -4 & 1 \end{pmatrix} = \begin{pmatrix} \frac{1}{7} & \frac{3}{14} \\ -\frac{2}{7} & \frac{1}{14} \end{pmatrix}
# \end{align*}
# 
# (e) &emsp; 
# 
# \begin{align*}
#     BX &= A \\
#     X &= B^{-1}A \\
#     &= \dfrac{1}{15}\begin{pmatrix} 5 & -1 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix} \\
#     &= \dfrac{1}{15} \begin{pmatrix} 5 & -15 \\ 13 & 3\end{pmatrix} = \begin{pmatrix} \frac{1}{3} & -1 \\ \frac{13}{15} & \frac{1}{5} \end{pmatrix}
# \end{align*}
# 
# (f) &emsp; 
# \begin{align*}
#     A^2 &= X \\
#     X &= \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix}\begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix} = \begin{pmatrix} -11 & -9 \\ 12 & -8 \end{pmatrix}
# \end{align*}
# 
# (g) &emsp; We begin by setting $X = \begin{pmatrix}a & b \\ c & d\end{pmatrix}$, and then $X^2 = B$ gives
# 
# \begin{align*}
#     \begin{pmatrix}a^2 + bc & ab + bd \\ ca+dc & cb+d^2\end{pmatrix} =
#     \begin{pmatrix} a^2 + bc & b(a + d) \\ c(a + d) & cb + d^2 \end{pmatrix} =
#     \begin{pmatrix} 3 & 0 \\ -1 & 5 \end{pmatrix}.
# \end{align*}
# 
# Now we can solve the quadratic equations over $\mathbb{R}$, since $[X^2]_{12} = 0$ then
# \begin{align*}
#     b(a + d) &= 0 \\
#     \therefore b &= 0 \text{ or } a = -d.
# \end{align*}
# 
# For the case when $b = 0$
# 
# \begin{align*}
#     a^2 + bc &= 3 \implies a = \pm \sqrt{3}, \\
#     cb + d^2 &= 5 \implies d = \pm \sqrt{5}.
# \end{align*}
# 
# So we have four possible solutions
# 
# \begin{align*}
#     X &= \begin{pmatrix} \pm \sqrt{3} & 0 \\ - 1 / (\pm \sqrt{3} \pm \sqrt{5}) & \pm\sqrt{5} \end{pmatrix}, &
#     X &\begin{pmatrix} \pm \sqrt{3} & 0 \\ - 1 / (\pm \sqrt{3} \mp \sqrt{5}) & \mp\sqrt{5} \end{pmatrix}.
# \end{align*}
# 
# For the case when $a = -d$
# \begin{align*}
#     c(a + d) = 0c = -1,
# \end{align*}
# which is a contradiction so $a = -d$ yields no solutions.
# 
# (h) &emsp; 
# 
# \begin{align*}
#     (X + A)B &= I \\
#     XB + AB &= I \\
#     XB &= I - AB \\
#     X &= B^{-1}(I - AB) \\
#     &= \begin{pmatrix} \frac{1}{3} & 0 \\ \frac{1}{15} & \frac{1}{5} \end{pmatrix}\left(
#     \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - 
#     \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix}
#     \begin{pmatrix} 3 & 0 \\ -1 & 5 \end{pmatrix} \right) \\
#     &= \begin{pmatrix} \frac{1}{3} & 0 \\ \frac{1}{15} & \frac{1}{5} \end{pmatrix}\left(
#     \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - 
#     \begin{pmatrix} 6 & -15 \\ 10 & 10 \end{pmatrix} \right) \\
#     &= \begin{pmatrix} \frac{1}{3} & 0 \\ \frac{1}{15} & \frac{1}{5} \end{pmatrix}
#     \begin{pmatrix} -5 & 15 \\ -10 & -9 \end{pmatrix} \\
#     &= \begin{pmatrix} -\frac{5}{3} & 5 \\ -\frac{7}{3} & -\frac{4}{5} \end{pmatrix}
# \end{align*}
# ::::
# 
# :::::

# :::::{admonition} Exercise 1.10
# :class: note
# :name: ex1.10
# 
# Use Python and SymPy to calculate the solutions to exercises [1.4](ex1.4) to [1.6](ex1.6).
# 
# [Exercise 1.4](ex1.4)
# ::::{dropdown} Solution
# :::python
# from sympy import *
# 
# A = Matrix([[1, -3], [4, 2]])
# B = Matrix([[3, 0], [-1, 5]])
# C = Matrix([[5], [9]])
# D = Matrix([[1, 1, 3], [4, -2, 3]])
# E = Matrix([[1, 2], [0, 6], [-2, 3]])
# F = Matrix([[1, -2, 4]])
# G = Matrix([[4, 2, 3], [-2, 6, 0], [0, 7, 1]])
# H = Matrix([[1, 0, 1], [5, 2, -2], [2, -3, 4]])
# 
# # Exercise 1.4
# # (a)
# AplusB = A + B
# print("(a)")
# display(AplusB)
# 
# # (b) B + C is undefined
# 
# # (c)
# AT = A.T
# print("(c)")
# display(AT)
# 
# # (d)
# CT = C.T
# print("(d)")
# display(CT)
# 
# # (e)
# DplusET = D + E.T
# print("(e)")
# display(DplusET)
# 
# # (d)
# threeBminusA = 3 * B - A
# print("(f)")
# display(threeBminusA)
# 
# # (g) E + F^T is undefined
# 
# # (h)
# FTT = F.T.T
# print("(h)")
# display(FTT)
# 
# # (i)
# twoGplusH = 2 * (G + H)
# print("(i)")
# display(twoGplusH)
# 
# # (j)
# ATplusBT = A.T + B.T
# print("(j)")
# display(ATplusBT)
# 
# # (k)
# AplusBT = (A + B).T
# print("(k)")
# display(AplusBT)
# 
# # (l)
# minusG = -G
# print("(l)")
# display(minusG)
# :::
# 
# ::::
# 
# [Exercise 1.5](ex1.5)
# ::::{dropdown} Solution
# :::python
# # Exercise 1.5
# # (a)
# AB = A * B
# print("(a)")
# display(AB)
#  
# # (b)
# BA = B * A
# print("(b)")
# display(BA)
# 
# # (c)
# AC = A * C
# print("(c)")
# display(AC)
# 
# # (d) CA is undefined"
# 
# # (e)
# CTC = C.T * C
# print("(e)")
# display(CTC)
# 
# # (f)
# CCT = C * C.T
# print("(f)")
# display(CCT)
# 
# # (g)
# DE = D * E
# print("(g)")
# display(DE)
# 
# # (h)
# GH = G * H
# print("(h)")
# display(GH)
# 
# # (i)
# ADE = A * (D * E)
# print("(i)")
# display(ADE)
# 
# # (j)
# ADE = (A * D) * E
# print("(j)")
# display(ADE)
# 
# # (k)
# A3 = A ** 3
# print("(k)")
# display(A3)
# 
# # (g)
# G4 = G ** 4
# print("(l)")
# display(G4)
# :::
# 
# ::::
# 
# [Exercise 1.6](ex1.6)
# ::::{dropdown} Solution
# :::python
# # Exercise 1.6
# # (a)
# detA = A.det()
# print(f"(a) det(A) = {detA}")
# 
# # (b)
# detB = B.det()
# print(f"(b) |B| = {detB}")
# 
# # (c)
# det3A = (3 * A).det()
# print(f"(c) det(3A) = {det3A}")
# 
# # (d)
# detG = G.det()
# print(f"(d) det(G) = {detG}")
# 
# # (e)
# adjB = B.adjugate()
# print("(e)")
# display(adjB)
# 
# # (f)
# adjH = H.adjugate()
# print("(f)")
# display(adjH)
# 
# # (g)
# invA = A.inv()
# print("(g) ")
# display(invA)
# 
# # (h)
# invB = B.inv()
# print("(h)")
# display(invB)
# 
# # (i)
# invG = G.inv()
# print("(i)")
# display(invG)
# 
# # (j)
# invAB = (A * B).inv()
# print("(j)")
# display(invAB)
# 
# # (k)
# invBinvA = B.inv() * A.inv()
# print("(k)")
# display(invBinvA)
# 
# # (l)
# invDE = (D * E).inv()
# print("(l)")
# display(invDE)
# :::
# 
# ::::
# 
# :::::

# In[1]:


from sympy import *

A = Matrix([[1, -3], [4, 2]])
B = Matrix([[3, 0], [-1, 5]])
C = Matrix([[5], [9]])
D = Matrix([[1, 1, 3], [4, -2, 3]])
E = Matrix([[1, 2], [0, 6], [-2, 3]])
F = Matrix([[1, -2, 4]])
G = Matrix([[4, 2, 3], [-2, 6, 0], [0, 7, 1]])
H = Matrix([[1, 0, 1], [5, 2, -2], [2, -3, 4]])

# Exercise 1.4
# (a)
AplusB = A + B
print("(a)")
display(AplusB)

# (b) B + C is undefined

# (c)
AT = A.T
print("(c)")
display(AT)

# (d)
CT = C.T
print("(d)")
display(CT)

# (e)
DplusET = D + E.T
print("(e)")
display(DplusET)

# (d)
threeBminusA = 3 * B - A
print("(f)")
display(threeBminusA)

# (g) E + F^T is undefined

# (h)
FTT = F.T.T
print("(h)")
display(FTT)

# (i)
twoGplusH = 2 * (G + H)
print("(i)")
display(twoGplusH)

# (j)
ATplusBT = A.T + B.T
print("(j)")
display(ATplusBT)

# (k)
AplusBT = (A + B).T
print("(k)")
display(AplusBT)

# (l)
minusG = -G
print("(l)")
display(minusG)


# In[2]:


# Exercise 1.5
# (a)
AB = A * B
print("(a)")
display(AB)
 
# (b)
BA = B * A
print("(b)")
display(BA)

# (c)
AC = A * C
print("(c)")
display(AC)

# (d) CA is undefined"

# (e)
CTC = C.T * C
print("(e)")
display(CTC)

# (f)
CCT = C * C.T
print("(f)")
display(CCT)

# (g)
DE = D * E
print("(g)")
display(DE)

# (h)
GH = G * H
print("(h)")
display(GH)

# (i)
ADE = A * (D * E)
print("(i)")
display(ADE)

# (j)
ADE = (A * D) * E
print("(j)")
display(ADE)

# (k)
A3 = A ** 3
print("(k)")
display(A3)

# (g)
G4 = G ** 4
print("(l)")
display(G4)


# In[3]:


# Exercise 1.6
# (a)
detA = A.det()
print(f"(a) det(A) = {detA}")

# (b)
detB = B.det()
print(f"(b) |B| = {detB}")

# (c)
det3A = (3 * A).det()
print(f"(c) det(3A) = {det3A}")

# (d)
detG = G.det()
print(f"(d) det(G) = {detG}")

# (e)
adjB = B.adjugate()
print("(e)")
display(adjB)

# (f)
adjH = H.adjugate()
print("(f)")
display(adjH)

# (g)
invA = A.inv()
print("(g) ")
display(invA)

# (h)
invB = B.inv()
print("(h)")
display(invB)

# (i)
invG = G.inv()
print("(i)")
display(invG)

# (j)
invAB = (A * B).inv()
print("(j)")
display(invAB)

# (k)
invBinvA = B.inv() * A.inv()
print("(k)")
display(invBinvA)

# (l)
invDE = (D * E).inv()
print("(l)")
display(invDE)

