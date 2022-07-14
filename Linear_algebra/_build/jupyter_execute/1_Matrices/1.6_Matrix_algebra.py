#!/usr/bin/env python
# coding: utf-8

# (matrix-algebra-section)=
# # Matrix algebra
# 
# Having defined the rules for addition, scalar multiplication and matrix multiplication, we can now consider solving equations involving matrices. Let $X$ be an $m \times n$ matrix, whose value we want to find.
# 
# Since matrix multiplication is not commutative then we say that in the expression $AB$, $B$ is *"**left multiplied** by $A$"* or $A$ is *"**right multiplied** by $B$"*. You cannot divide by a matrix but you can multiply by an inverse matrix, if one exists. For example, let $A$ and $B$ be invertible matrices (i.e. matrices which have inverses), then
# 
# \begin{align*}
#     AX &= B \\
#     A^{-1}AX &= A^{-1}B & &\textsf{left-multiply both sides by }A^{-1} \\
#     IX &= A^{-1}B & & \textsf{since $A^{-1}A = I$}\\
#     X &= A^{-1}B & & \textsf{since $IX = X$}. 
# \end{align*}
# 
# :::::{admonition} Example 1.17
# :class: seealso
# :name: matrix-algebra-example
# 
# Solve the following matrix equations for $X$:
#     
# ::::{grid}
# :gutter: 2
# 
# :::{grid-item}
# :columns: 4
# (i) &emsp; $2X = A$
# :::
# 
# :::{grid-item}
# :columns: 4
# (ii) &emsp; $kX + A = I$
# :::
# 
# :::{grid-item}
# :columns: 4
# (iii) &emsp; $A(X + B) = C$
# :::
# 
# ::::
# 
# ::::{dropdown} Solution
# (i)
# \begin{align*}
# 2X &= A  \\
# X &= \frac{1}{2}A.
# \end{align*}
# 
# (ii)
# \begin{align*}
# kX + A &= I \\
# kX &= I - A \\
# X &= \frac{1}{k}(I- A).
# \end{align*}
# 
# (iii)
# \begin{align*}
# A(X+B) &= C \\
# AX + AB &= C \\
# AX &= C - AB \\
# A^{-1}AX &= A^{-1}(C - AB) \\
# X &= A^{-1}(C - AB).
# \end{align*}
# ::::
# :::::
