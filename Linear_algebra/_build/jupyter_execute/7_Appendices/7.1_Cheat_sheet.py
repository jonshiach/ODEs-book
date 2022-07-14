#!/usr/bin/env python
# coding: utf-8

# # Linear Algebra Cheat Sheet
# 
# ## Matrices
# 
# 
# ```{glossary}
# Matrix
#     A [matrix](definition-of-a-matrix-section) is a rectangular array of elements. 
# 
# Matrix indexing
#     If a matrix $A$ has $m$ rows and $n$ columns then the elements of $A$ are [indexed](indexing-a-matrix-section) by $a_{ij}$ where $i$ denotes the row and $j$ denotes the column. For example
# 
#     \begin{align*} 
#         \begin{pmatrix} 
#             a_{11} & a_{12} & \cdots & a_{1m} \\  
#             a_{21} & a_{22} & \cdots & a_{2m} \\ 
#             \vdots & \vdots & \ddots & \vdots \\ 
#             a_{m1} & a_{m2} & \cdots & a_{mn} 
#         \end{pmatrix}.
#     \end{align*}
# 
# Matrix equality
#     Two $m \times n$ matrices are [equal](matrix-equality-definition) if their corresponding elements have the same value.
# 
# Addition/subtraction
#     The [addition or subtraction](matrix-addition-definition) of two $n \times m$ matrices is calculated by adding and subtracting corresponding elements. For example
#     
#     \begin{align*} 
#         A + B = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + 
#         \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}
#         = \begin{pmatrix} 6 & 8 \\ 10 & 12 \end{pmatrix}.
#     \end{align*}
#     
# Multiplication by a scalar
#     The [scalar multiplication](scalar-multiplication-of-a-matrix-definition) of a matrix by a scalar is calculated by multiplying each element in the matrix by the scalar. 
#     
#     \begin{align*} 
#         3 A = 3 \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} 
#         = \begin{pmatrix} 3 & 6 \\ 9 & 12 \end{pmatrix}.
#     \end{align*}
#     
# Matrix multiplication
#     The [multiplication](matrix-multiplication-definition) of an $m \times n$ matrix $A$ and an $p \times q$ matrix $B$ where $n = p$ results in an $m \times q$ matrix calculated using $[AB]_{ij} = \displaystyle\sum_{k=1}^n a_{ik}b_{kj}$ for $i = 1, \ldots, m$ and $j = 1, \ldots, q$. For example
#     
#     \begin{align*}
#         AB &= \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} 
#         \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}
#         = \begin{pmatrix} 5 + 14 & 6 + 16 \\ 15 + 28 & 18 + 32 \end{pmatrix} \\
#         &= \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}.
#     \end{align*}
#     
# Matrix exponent
#     The [exponent](matrix-exponents-definition) of the matrix $A$ is calculated using $A^k = \underbrace{AA \cdots A}_{k}$. For example
#     
#     \begin{align*}
#         A^2 = AA = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}
#         = \begin{pmatrix} 7 & 10 \\ 15 & 22 \end{pmatrix}
#     \end{align*}
# 
# Matrix transpose
#     The [transpose](matrix-transpose-definition) of an $m \times n$ matrix $A$ is an $n \times m$ matrix $A^\mathrm{T}$ defined by $[A^\mathrm{T}]_{ij} = a_{ji}$. For example
#     
#     \begin{align*}
#         A^\mathrm{T} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}^\mathrm{T} = 
#         \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}.
#     \end{align*}
#     
# Diagonal matrix
#     An $n \times n$ matrix $A$ is said to be a [diagonal matrix](diagonal-matrix-definition) if all of the elements have a value of zero except the elements on the main diagonal $a_{ii}$ for $i = 1, \ldots, n$. For example
# 
#     \begin{align*} 
#         \begin{pmatrix} 
#           a & 0 & 0 \\ 
#           0 & b & 0 \\ 
#           0 & 0 & c
#         \end{pmatrix}
#     \end{align*}
# 
# Zero matrix
#     A [zero matrix](zero-matrix-definition) is a matrix where all of the elements have a value of zero. For example
# 
#     \begin{align*} 
#         \mathbf{0}_{2\times 3} = \begin{pmatrix} 
#           0 & 0 & 0 \\ 
#           0 & 0  & 0 
#         \end{pmatrix}
#     \end{align*}
#     
# Identity matrix
#     The [identity matrix](identity-matrix-definition) is a diagonal matrix $I$ such that $AI = IA = A$ where the elements on the main diagonal all have a value of 1. 
#     \begin{align*}
#         I_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
#     \end{align*}
#     
# Symmetric matrix
#     An $n \times n$ matrix $A$ is said to be a [symmetric matrix](symmetric-matrix-definition) if $[A]_{ij} = [A]_{ji}$
# 
#     \begin{align*}
#         \begin{pmatrix} a & b & c \\ b & d & e \\ c & e & f \end{pmatrix}
#     \end{align*}
# 
# Determinant of an $2\times 2$ matrix
#     The [determinant of an $2 \times 2$ matrix](2x2-determinant-definition) $A$ is calculated using $\det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$. For example
# 
#     \begin{align*}
#         \det(A) = \begin{vmatrix} 1 & 2 \\ 3 & 4 \end{vmatrix} = 1(4) - 2(3) = -2
#     \end{align*}
#     
# Minor
#     For an $n\times n$ matrix $A$, the value of the [minor](minor-definition) for the element in row $i$ and column $j$, $M_{ij}$, is the determinant of the matrix formed by omitting row $i$ and column $j$ from $A$. For example, for the matrix $A = \begin{pmatrix} 1 & 0 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$
#     
#     \begin{align*}
#         M_{21} = \begin{vmatrix} \square & 0 & 3 \\ \square & \square & \square \\ \square & 8 & 9 \end{vmatrix} = \begin{vmatrix} 0 & 3 \\ 8 & 9 \end{vmatrix} = -24.
#     \end{align*}
#     
# Co-factor
#     For an $n\times n$ matrix $A$, the value of the [cofactor](cofactor-definition) is $C_{ij} = (-1)^{i+j} M_{ij}$. For example, for the matrix $A$ defined above 
#     
#     $$ C_{21} = (-1)^{2+1} M_{21} = (-1)^3 (-24) = 24. $$
# 
# Determinant of an $n \times n$ matrix
#     The [determinant of an $n \times n$ matrix]((nxn-determinant-example)) $A$ is calculated using $\det(A) = \displaystyle\sum_{i = 1}^n a_{ij} C_{ij}$ for $j \in \{1, \ldots, n\}$ for $C_{ij}$ is the co-factor for the element $a_{ij}$. For example, for the matrix $A$ defined above
# 
#     \begin{align*}
#         \begin{vmatrix} 1 & 0 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{vmatrix} 
#         &= 1 \begin{vmatrix} 5 & 6 \\ 8 & 9 \end{vmatrix} - 0 
#         \begin{vmatrix} 4 & 6 \\ 7 & 9 \end{vmatrix} + 3 
#         \begin{vmatrix} 4 & 5 \\ 7 & 8 \end{vmatrix} \\
#         &= 1(45 - 48) + 0(36 - 42) + 3(32 - 35) \\
#         &= -12
#     \end{align*}
#     
# Inverse matrix
#     For an $n \times n$ matrix $A$ such that $\det(A) \neq 0$ then the [inverse matrix](inverse-matrix-definition) is an $n \times n$ matrix $A^{-1}$ such that $AA^{-1} = A^{-1}A = I$.
# 
# Adjoint matrix
#     For an $n \times n$ matrix $A$ the [adjoint matrix](adjoint-definition) is calculated using $\operatorname{adj}(A) = C^T$. For example for the matrix $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$
# 
#     \begin{align*}
#         \operatorname{adj}(A) = \begin{pmatrix} 4 & -3 \\ -2 & 1 \end{pmatrix}^\mathrm{T} =
#         \begin{pmatrix} 4 & -3 \\ -2 & 1 \end{pmatrix}.
#     \end{align*}
#    
# The adjoint-determinant formula
#     The inverse of a non-singular square matrix $A$ can be calculated using the [adjoint-determinant formula](adjoint-determinant-formula-definition) $A^{-1} = \dfrac{\operatorname{adj}(A)}{\det(A)}$. For example, for the matrix $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$
# 
#     \begin{align*}
#         A^{-1} = \dfrac{1}{-2} \begin{pmatrix} 4 & -3 \\ -2 & 1 \end{pmatrix}
#         = \begin{pmatrix} -2 & \frac{3}{2} \\ 1 & -\frac{1}{2} \end{pmatrix}
#     \end{align*}
# ```

# ---
# 
# ## Systems of linear equations
# 
# ```{glossary}
# System of linear equations
#     A [system of linear equations](system-of-linear-equation-definition) can be expressed as the matrix equation $A \mathbf{x} = \mathbf{b}$ such that
# 
#     \begin{align*}
#         \begin{pmatrix}
#             a_{11} & a_{12} & \cdots & a_{1m} \\
#             a_{21} & a_{22} & \cdots & a_{2m} \\
#             \vdots & \vdots & \ddots & \vdots \\
#             a_{m1} & a_{m2} & \cdots & a_{mn}
#         \end{pmatrix}
#         \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} =
#         \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{pmatrix}.
#     \end{align*} 
#     
# Elementary Row Operations (EROs)
#     The following [**elementary row operations**](ero-definition) can be applied to a system without changing the solution
#     - **Swap rows $i$ and $j$**: &emsp;  $R_i \leftrightarrow R_j$
#     - **Multiply row $i$ by $k$**:  &emsp; $kR_i$
#     - **Add row $j$ multiplied by $k$ to row $i$**:  &emsp; $R_i + kR_j$
# 
# Pivot element
#     The [pivot element](ref-definition) is the first non-zero element in the row.
# 
# Row Echelon Form (REF)
#     A matrix is in [row echelon form](ref-definition) if in each non-zero row the pivot element is to the right of the pivot element of the row above.
#     
# Row reduction to row echelon form
#     To [row reduce](ge-definition) an $m \times n$ matrix $A$ to reduced row echelon form we do the following:
# 
#     1. Initialise the pivot row to $i=1$ and pivot column to $k=1$ 
#     2. If $a_{ik} = 0$ perform a row swap with a row beneath the pivot row $i$ with a non-zero element in the pivot column $k$. If no such rows exist set $k = k + 1$ and repeat step 2.
#     3. For each row $j = i+1 \ldots m$ beneath the pivot row subtract the pivot row $i$ multiplied by $\dfrac{a_{jk}}{a_{ik}}$ from row $j$. 
#     4. Set $i = 1 + 1$ and $k = k + 1$ and repeat steps 2 and 3 until $i > m$ or $k > n$. 
# 
# Partial pivoting
#    A row swap is performed so that the pivot element has a larger absolute value than the elements in the column below it. 
#    
# Row reduction using partial pivoting
#     To row reduce an $m \times n$ matrix $A$ to row echelon form using [partial pivoting](ge-pp-definition) we do the following:
# 
#     1. Initialise the pivot row to $i=1$ and pivot column to $k=1$
#     2. Swap the pivot row $i$ with the row below which has the largest absolute value element in the pivot column $k$ which is greater than the absolute value of the pivot element $|a_{ik}|$. 
#     3. If $a_{ik} = 0$ then set $k = k + 1$ and repeat step 2.
#     4. For each row $j = i+1 \ldots m$ beneath the pivot row subtract the pivot row $i$ multiplied by $\dfrac{a_{jk}}{a_{ik}}$ from row $j$. 
#     5. Set $i = 1 + 1$ and $k = k + 1$ and repeat steps 2 to 4 until $i > m$ or $k > n$.
#    
# Reduced Row Echelon Form (RREF)
#     The matrix is in [reduced row echelon form](rref-definition) if the pivot element in each row has a value of 1 and it is the only non-zero element in its column.
# 
# 
# Row reduction to reduced row echelon form
#     To row reduce an $m \times n$ matrix $A$ to [reduced row echelon form](rref-definition) we do the following
# 
#     1. Initalise the pivot row to $i=1$ and pivot column to $k=1$ 
#     2. If $a_{ik} = 0$ perform a row swap with a row beneath the pivot row $i$ with a non-zero element in the pivot column $k$. If no such rows exist set $k = k + 1$ and repeat step 2.
#     3. Divide the pivot row $i$ by the value of the pivot element $a_{ik}$.
#     4. For each row $j = i \ldots m$ where $i \neq j$ subtract the pivot row $i$ multiplied by $a_{ik}$ from row $j$. 
#     5. Set $i = 1 + 1$ and $k = k + 1$ and repeat steps 2 to 4 until $i > m$ or $k > n$.
#     
# Solution of a linear system of equations used inverse matrix
#     The solution to a linear system of equations $A \mathbf{x} = \mathbf{b}$ can be calculated using the [inverse matrix](solution-using-inverse-matrix-theorem) by $\mathbf{x} = A^{-1} \mathbf{b}$ 
#     
# Cramer's rule
#     [Cramer's rule](cramers-rule-theorem) for calculating the solution to a system of linear equations $A \mathbf{x} = \mathbf{b}$ is $x_i = \dfrac{\det(A_i)}{\det(A)}$ where $A_i$ is a matrix formed by replacing column $i$ of $A$ with $\mathbf{b}$.
#     
# Gaussian Elimination (GE)
#     To calculate the solution to a system of linear equations using [**Gaussian elimination**](ge-definition) form an augmented matrix $(A \mid \mathbf{b})$ and use elementary row operations to row reduce to row echelon form. The solution is then calculated using back substitution.
#     
# Gauss-Jordan Elimination (GJE)
#     To calculate the solution to a system of linear equations using [**Gauss-Jordan elimination**](gje-definition) form an augmented matrix $(A \mid \mathbf{b})$ and use elementary row operations to row reduce to reduced row echelon form. The solution vector $\mathbf{x}$ is contained to the right of the partition.
#     
# Calculating an inverse matrix using Gauss-Jordan elimination
#     To calculate the inverse of a non-singular matrix $A$ form an augmented matrix $(A \mid I)$ and row reduce to reduced row echelon form. The inverse of $A$ is the matrix to the right-hand side of the partition. 
#     
# Rank of a matrix
#     The [rank](rank-definition) of a matrix $\operatorname{rank}(A)$ is the number of non-zero rows of the row echelon form of $A$.
#     
# Consistent system 
#     A system of linear equations is [consistent](consistent-system-theorem) and has a solution if $\operatorname{rank}(A \mid \mathbf{b}) = \operatorname{rank}(A)$.
#     
# Inconsistent system     
#     A system of linear equations is [inconsistent](inconsistent-system-theorem) and does not have a solution if $\operatorname{rank}(A \mid \mathbf{b}) > \operatorname{rank}(A)$.
#     
# Indeterminate system
#     A system of $n$ linear equations is [indeterminate](indeterminate-system-theorem) and has an infinite number of solutions if it is consistent and $\operatorname{rank}(A \mid \mathbf{b}) < n$.
# 
# Solution of an indeterminate system
#     A general [solution to an indeterminate system](indeterminate-system-theorem) can be found by assigning parameters to the free variables and solving for the rest. 
# 
# ```

# ---
# 
# ## Vectors
# 
# ```{glossary}
# Vector
#     A [vector](vectors-section) is an object which has direction and magnitude (length).
# 
# Position vector
#     A [position vector](position-vector-section) is a vector which has a tail positioned at the origin.
#     
# Magnitude of a vector
#     The magnitude of a vector $\mathbf{a}$ is the length of the vector which is calculated using $|\mathbf{a}| = \sqrt{\displaystyle\sum_{i=1}^n a_i^2}$. For example, for the vector $\mathbf{a} = (1, 2, 3)$
#     
#     \begin{align*}
#         |\mathbf{a}| &= \sqrt{1^2 + 2^2 + 3^2} = \sqrt{14}.
#     \end{align*}
#     
# Unit vector
#     A [unit vector](unit-vector-definition) is a vector with a magnitude of 1.
#     
# Normalising a vector
#     A unit vector pointing in the same direction as $\mathbf{a}$ can be determined by [normalising](normalising-a-vector-proposition) the vector by calculating $\hat{\mathbf{a}} = \dfrac{\mathbf{a}}{|\mathbf{a}|}$. For example, for the vector $\mathbf{a} = (1, 2, 3)$
#     
#     \begin{align*}
#         \hat{\mathbf{a}} = \frac{1}{\sqrt{14}} \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = 
#         \begin{pmatrix} \frac{1}{\sqrt{14}} \\ \frac{2}{\sqrt{14}} \\ \frac{3}{\sqrt{14}} \end{pmatrix}.
#     \end{align*}
# 
# The dot product
#     The [dot product](dot-product-definition) between the two vectors $\mathbf{a} = (a_1, a_2, \ldots, a_n)$ and $\mathbf{b} = (b_1, b_2, \ldots, b_n)$ is a scalar value calculated using $\mathbf{a} \cdot \mathbf{b} = \displaystyle\sum_{i=1}^n a_i b_i$. For example, for the vectors $\mathbf{a} = (1, 2, 3)$ and $\mathbf{b} = (4, 5, 6)$
# 
#     \begin{align*}
#         \mathbf{a} \cdot \mathbf{b} = 1(4) + 2(5) + 3(6) = 32.
#     \end{align*}
#     
# Geometric definition of the dot product
#     The [dot product](dot-product-definition) between the two vectors $\mathbf{a} \cdot \mathbf{b}$ is related to $\theta$ the angle between $\mathbf{a}$ and $\mathbf{b}$ by $\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \cos(\theta)$.
#     
# Basis vectors in $\mathbb{R}^3$
#     The standard basis vectors in $\mathbf{R}^3$ are $\mathbf{i} = (1, 0, 0)$, $\mathbf{j} = (0, 1, 0)$ and $\mathbf{k} = (0, 0, 1)$. 
#     
# 
# The cross product
#     The [cross product](cross-product-definition) between the two vectors in $\mathbb{R}^3$, $\mathbf{a} = (a_1, a_2, a_3)$ and $\mathbf{b} = (b_1, b_2, b_3)$ is a vector calculated using $\mathbf{a} \times \mathbf{b} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix}$. For example, for the vectors $\mathbf{a} = (1, 2, 3)$ and $\mathbf{b} = (4, 5, 6)$
# 
#     \begin{align*}
#         \mathbf{a} \times \mathbf{b} = 
#         \begin{vmatrix} 
#             \mathbf{i} & \mathbf{j} & \mathbf{k} \\
#             1 & 2 & 3 \\
#             4 & 5 & 6
#         \end{vmatrix} =
#         -3\mathbf{i} + 6\mathbf{j} - 3\mathbf{k} = \begin{pmatrix} -3 \\ 6 \\ -3 \end{pmatrix}.
#     \end{align*}
# 
# Geometric definition of the cross product
#     The [cross product](dot-product-definition) between the two vectors $\mathbf{a}$ and $\mathbf{b}$ in $\mathbb{R}^3$ is perpendicular to the plane that both $\mathbf{a}$ and $\mathbf{b}$ lie on. 
# ```

# ---
# 
# ## Co-ordinate geometry
# 
# ```{glossary}
# Euclidean space
#     The position of an object in $n$-dimensional space, $\mathbb{R}^n$, is defined as the signed distance along $n$ orthogonal (perpendicular) axis from the origin. These distances are expressed in an $n$-tuple, e.g., $(x, y, z)$ for $\mathbb{R}^3$.
#     
# Points
#     A [point](points-section) is an object that has no dimension.
#     
# Lines
#     A [line](lines-section) is a one dimensional object which has length but no breath.
# 
# Planes
#     A [plane](planes-section) is a two dimensional object with length and breadth.
#     
# Vector equation of a line
#     A point on the line $\ell$ can be calculated using the [vector equation of a line]((vector-equation-of-a-line-definition) $Q = P + t\mathbf{d}$ where $P$ is a point on the line, $t\in \mathbb{R}$ and $\mathbf{d}$ is a vector indicating the direction of the line.
#     
# Intersecting lines
#     The two lines $\ell_1$ and $\ell_2$ [intersect](line-line-intersection-definition) if there exists a value of $t$ such that $P_1 + t\mathbf{d}_1 = P_2 + t\mathbf{d}_2$.
#     
# Parallel lines
#     The two lines $\ell_1: P_1 + t\mathbf{d}_1$ and $\ell_2: P_2 + t\mathbf{d}_2$ are [parallel](parallel-lines-definition) if there exists a value $k$ such that $\mathbf{d}_1 = k\mathbf{d}_2$.
#     
# Skew lines
#     The two lines $\ell_1$ and $\ell_2$ are [skew](skew-lines-definition) if they do not intersect and are not parallel.
#     
# Perpendicular lines
#     The two lines $\ell_1: P_1 + t\mathbf{d}_1$ and $\ell_2: P_2 + t\mathbf{d}_2$ are [perpendicular](perpendicular-lines-definition) if $\mathbf{d}_1$ and $\mathbf{d}_2$ are at right angles, i.e., $\mathbf{d}_1 \cdot \mathbf{d}_2 = 0$.
#     
# Normal vector
#     The [normal vector](normal-vector-definition) to a plane is a vector which is perpendicular to every vector that lies on the plane, and is calculated using $\mathbf{n} = \mathbf{d}_1 \times \mathbf{d}_2$.
#     
# Point-normal equation of a plane
#     The [point-normal equation](point-normal-definition) plane which passes through the point with co-ordinates $(x_0, y_0, z_0)$ and has a normal vector $\mathbf{n}$ is $\mathbf{n} \cdot (x - x_0, y - y_0, z - z_0) = 0$.
#     
# Intersection between three planes
#     Three planes in $\mathbb{R}^n$ can intersect at a single point, on a single line or not intersect at all.
#     
# Shortest distance between two points
#     The [shortest distance between the two points](shortest-distance-between-two-points) $P = (p_1, p_2, \ldots, p_n)$ and $Q = (q_1, q_2, \ldots, q_n)$ is $d = |Q - P|$.
#     
# Shortest distance between a point and a line
#     The [shortest distance between the point $Q$ and the line](point-line-distance-theorem) $\ell:P + t\mathbf{d}$ is $d = |Q - R|$ where $R = P + t\mathbf{d}$ and $t = \dfrac{(Q - P)\cdot \mathbf{d}}{\mathbf{d} \cdot \mathbf{d}}$.
# 
# Shortest distance between two skew lines
#     The [shortest distances between the two skew lines](line-line-distance-theorem) $\ell_1:P_1 + t\mathbf{d}_1$ and $\ell_2:P_2 + t\mathbf{d}_2$ is $d = (P_2 - P_1) \cdot \hat{\mathbf{n}}$ where $\mathbf{n} = \mathbf{d}_1 \cdot \mathbf{d}_2$.
#     
# Shortest distance between a point and a plane
#     The [shortest distance between the point $Q$ and the plane](ex4.7) which passes through the point $P$ and has normal vector $\mathbf{n}$ is $d = (Q - P)\cdot \hat{\mathbf{n}}$.
# 
# ```

# ---
# 
# ## Vector spaces
# 
# ```{glossary}
# Vector space
#     A [vector space](vector-space-definition) over a field $F$ is a non-empty set $V$ of which the following operations are defined:
#     - addition: If $\mathbf{u}, \mathbf{v} \in V$ then $\mathbf{u} + \mathbf{v} \in V$.
#     - scalar multiplication: If $\mathbf{u} \in V$ and $\alpha \in F$ then $\alpha \mathbf{u} \in V$.
#     
# Vector space axioms
#     For $V$ to be a vector space over $F$ and $\alpha, \beta \in F$ eight [axioms](vector-space-axioms-theorem) must hold.
#     
# Subspace
#     If $V$ is a vector space and $W \subset V$ then $W$ is a [subspace](subspace-definition) if $\mathbf{u} + \alpha \mathbf{w} \in W$ where $\mathbf{u}, \mathbf{w} \in W$ and $\alpha \in F$. 
#     
# Linear combination
#     For $\mathbf{u} \in V$ there exists a [linear combination](linear-combination-definition) of vectors  $\mathbf{v}_i \in W$ and $\alpha_i \in F$ such that $\mathbf{u} = \alpha_1 \mathbf{v}_1 + \alpha_2 \mathbf{v}_2 + \cdots + \alpha_n \mathbf{v}_n$.
#     
# Linear independence
#     Let $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \in V$ then if the only solution to $\alpha_1 \mathbf{v}_1 + \alpha_2 \mathbf{v}_2 + \cdots + \alpha_n \mathbf{v}_n = \mathbf{0}$ is $\alpha_i = 0$ then $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \in V$ are [linearly independent](linear-dependence-definition) over $F$.
#     
# Linear dependence
#     If the linear combination of vectors above is satisfied for at least one non-zero $\alpha_i$ then $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \in V$ are [linearly dependent](linear-dependence-definition) over $F$.
#     
# Spanning set
#     Let $V$ be a vector space over $F$ and $W$ is a subspace of $V$ such that $\mathbf{u} \in W$ are expressible as a linear combination of $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \in V$ then $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ is a [spanning set](spanning-set-definition) for $W$.
#     
# Basis
#     A [basis](basis-definition) of a vector space $V$ over $F$ is a linearly independent spanning subset of $V$.
#     
# Orthogonal basis
#     An [orthogonal basis](orthogonal-basis-definition) where each of the basis vector is orthogonal (perpendicular) to each other basis vector.
#     
# Orthonormal basis
#     An [orthonormal basis](orthonormal-basis-definition) is an orthogonal basis where each of the basis vector is a unit vector.
#     
# Vector space dimension
#     The [dimension](vector-space-dimension-definition) of a vector space is the number of elements in the basis for the vector space.
#     
# Standard basis
#     The [standard basis](change-of-basis-section) for $\mathbb{R}^n$ is $E = \{ \mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_n \}$ where $\mathbf{e}_i$ is column $i$ of the identity matrix.
#     
# Change of basis
#     The [change of basis](change-of-basis-section) for the vector $[\mathbf{u}]_E$ represented with respect to another basis $W= \{ \mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \}$ is $[\mathbf{u}]_W = (\alpha_1, \alpha_2, \ldots, \alpha_n)$ such that $\alpha_1 \mathbf{v}_1 + \alpha_2 \mathbf{v}_2 + \cdots + \alpha_n \mathbf{v}_n = \mathbf{u}$.
#     
# Change of basis matrix
#     The [change of basis matrix](change-of-basis-matrix-definition) is a matrix $A_{E \to W}$ such that $[\mathbf{u}]_W = A_{E\to W} \mathbf{u}$. 
# ```

# ## Linear transformations
# 
# ```{glossary}
# Linear transformation 
#     If $V$ and $W$ are two vectors spaces over $F$ then a [linear transformation](linear-transformation-definition) is a mapping $T: V \to W$ such that for $x,y \in V$ and $\alpha \in F$ the following hold
# 
#     - **Addition**: $T(x + y) = T(x) + T(y)$.
#     - **Scalar multiplication**: $T(\alpha x) = \alpha T(x)$.
# 
# 
#     We can combine these two conditions to give $T(x + \alpha y) = T(x) + \alpha T(y)$.
# 
# Image
#     The result of apply a transformation to an object is known as the [image](linear-transformation-definition).
#     
# Transformation matrix
#     Let $T:V \to W$ be a linear transformation and $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$ is a basis of $V$ then the [transformation matrix](transformation-matrix-definition) is the matrix $A$ such that $T(\mathbf{u}) = A \mathbf{u}$ where $A = (T(\mathbf{v}_1), T(\mathbf{v}_2), \ldots, T(\mathbf{v}_n))$.
#  
# Finding the transformation matrix from the images
#     Given a set of [images of a linear transformation](finding-transformation-matrix-theorem) $T$ then the transformation matrix for $T$ is $A = (T(\mathbf{u}_1), T(\mathbf{u}_2), \ldots, T(\mathbf{u}_n)) \cdot (\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_n)^{-1}$.
# 
# Inverse transformation 
#     Let $T:V \to W$ be a linear transformation then its [inverse](inverse-transformation-definition) is $T^{-1}: W \to V$.
# 
# Composite transformation
#     Let $S:V \to W$ and $T:W \to X$ be two linear transformations then the [composite transformation](composite-transformation-definition) $S \circ T$ is $S\circ T: V \to X$ defined by $S(T(\mathbf{u}))$ for $\mathbf{u} \in V.$
#     
#     
# Composite transformation matrices
#     If $A$ and $B$ are the transformation matrices for $T$ and $S$ respectively then the [composite transformation matrix](composite-transformation-matrices-theorem) for $S \circ T$ is  $S(T(\mathbf{u})) = BA \mathbf{u}.$
#     
# Homogeneous co-ordinates
#     The homogeneous co-ordinates of a point $\mathbf{u}$ in $\mathbf{R}^n$ expressed using [homogeneous co-ordinates](homogeneous-coordinates-definition) is $\mathbf{u} = (\lambda u_1, \lambda u_2, \ldots, \lambda u_n, \lambda)$. Note that $(x, y, z)$ in Cartesian co-ordinates is the same as $(x, y, z, 1)$ in homogeneous co-ordinates.
# 
# Translation
#     The transformation matrix to [translate](translation-definition) a vector in $\mathbb{R}^n$ expressed in homogeneous co-ordinates by a translation vector $\mathbf{t}$ is 
#     
#     $$T(\mathbf{t}) = \begin{pmatrix} & & & t_1 \\  & I & & \vdots \\ & & & t_n \\ 0 & \cdots & 0 & 1 \end{pmatrix}.$$
# 
# Reflection
#     The transformation matrix to [reflect](reflection-theorem) a vector  in $\mathbb{R}^2$ expressed in homogeneous co-ordinates about a line that passes through the origin and makes an angle $\theta$ with the $x$-axis is 
# 
#     $${Rot}(\theta) = \begin{pmatrix} \cos(\theta) & -\sin(\theta) & 0 \\ \sin(\theta) & \cos(\theta) & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$
#     
# Scaling
#     The transformation matrix to [scale](scaling-definition) a vector in $\mathbb{R}^n$ expressed in homogeneous co-ordinates by the scaling vector $\mathbf{s}$ is
# 
#     $${S}(\mathbf{s}) = \begin{pmatrix} s_1 & 0 & \cdots & 0 \\ 0 & s_2 & \ddots & \vdots \\ \vdots & \ddots & \ddots & 0 \\ 0 & \cdots & 0 & 1 \end{pmatrix}.$$
# ```
