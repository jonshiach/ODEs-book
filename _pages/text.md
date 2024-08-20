(a) Calculate LU decomposition of the coefficient matrix $A = \left(\begin{matrix}2 & 3 & -1\\4 & 9 & -1\\0 & 3 & 2\end{matrix}\right)$

$$ \begin{align*} 
    j &= 1: &     u_{11} &= a_{11} = 2 , \\ 
            && \ell_{21} &= \frac{1}{u_{11}} \left( a_{21} \right) = \frac{1}{2} \left( 4 \right) = 2, \\ 
            && \ell_{31} &= \frac{1}{u_{11}} \left( a_{31} \right) = \frac{1}{2} \left( 0 \right) = 0, \\ 
    j &= 2: &     u_{12} &= a_{12} = 3 , \\ 
               && u_{22} &= a_{22} - \ell_{21} u_{12} = 9 - 2 \cdot 3 = 3, \\ 
            && \ell_{32} &= \frac{1}{u_{22}} \left( a_{32} - \ell_{31} u_{12} \right) = \frac{1}{3} \left( 3 - 0 \cdot 3 \right) = 1, \\ 
    j &= 3: &     u_{13} &= a_{13} = -1 , \\ 
               && u_{23} &= a_{23} - \ell_{21} u_{13} = -1 - 2 \cdot -1 = 0, \\ 
               && u_{33} &= a_{33} - \ell_{31} u_{13} - \ell_{32} u_{23} = 2 - 0 \cdot -1 - 1 \cdot 1 = 1, \\ 
\end{align*} $$ 

So $L = \left(\begin{matrix}1 & 0 & 0\\2 & 1 & 0\\0 & 1 & 1\end{matrix}\right)$ and $U = \left(\begin{matrix}2 & 3 & -1\\0 & 3 & 1\\0 & 0 & 1\end{matrix}\right)$. 

Solving $L \vec{y} = \vec{b}$ gives $\vec{y} = \mathtt{\text{[ 4. 10.  1.]}}$ and solving $U \vec{x} = \vec{y}$ gives $\vec{x} = \mathtt{\text{[-2.  3.  1.]}}$.

(b) Calculate LU decomposition of the coefficient matrix $A = \left(\begin{matrix}3 & 9 & 5\\1 & 2 & 2\\2 & 4 & 5\end{matrix}\right)$

$$ \begin{align*} 
    j &= 1: &     u_{11} &= a_{11} = 3 , \\ 
            && \ell_{21} &= \frac{1}{u_{11}} \left( a_{21} \right) = \frac{1}{3} \left( 1 \right) = 1/3, \\ 
            && \ell_{31} &= \frac{1}{u_{11}} \left( a_{31} \right) = \frac{1}{3} \left( 2 \right) = 2/3, \\ 
    j &= 2: &     u_{12} &= a_{12} = 9 , \\ 
               && u_{22} &= a_{22} - \ell_{21} u_{12} = 2 - 1/3 \cdot 9 = -1, \\ 
            && \ell_{32} &= \frac{1}{u_{22}} \left( a_{32} - \ell_{31} u_{12} \right) = \frac{1}{-1} \left( 4 - 2/3 \cdot 9 \right) = 2, \\ 
    j &= 3: &     u_{13} &= a_{13} = 5 , \\ 
               && u_{23} &= a_{23} - \ell_{21} u_{13} = 2 - 1/3 \cdot 5 = 0, \\ 
               && u_{33} &= a_{33} - \ell_{31} u_{13} - \ell_{32} u_{23} = 5 - 2/3 \cdot 5 - 2 \cdot 1/3 = 1, \\ 
\end{align*} $$ 

So $L = \left(\begin{matrix}1 & 0 & 0\\\frac{1}{3} & 1 & 0\\\frac{2}{3} & 2 & 1\end{matrix}\right)$ and $U = \left(\begin{matrix}3 & 9 & 5\\0 & -1 & \frac{1}{3}\\0 & 0 & 1\end{matrix}\right)$. 

Solving $L \vec{y} = \vec{b}$ gives $\vec{y} = \mathtt{\text{[20.         -3.66666667 -2.        ]}}$ and solving $U \vec{x} = \vec{y}$ gives $\vec{x} = \mathtt{\text{[ 1.  3. -2.]}}$.

(c) Calculate LU decomposition of the coefficient matrix $A = \left(\begin{matrix}1 & 0 & 3 & 2\\3 & -2 & 5 & 1\\4 & -1 & -2 & -3\\0 & 2 & 0 & 3\end{matrix}\right)$

$$ \begin{align*} 
    j &= 1: &     u_{11} &= a_{11} = 1 , \\ 
            && \ell_{21} &= \frac{1}{u_{11}} \left( a_{21} \right) = \frac{1}{1} \left( 3 \right) = 3, \\ 
            && \ell_{31} &= \frac{1}{u_{11}} \left( a_{31} \right) = \frac{1}{1} \left( 4 \right) = 4, \\ 
            && \ell_{41} &= \frac{1}{u_{11}} \left( a_{41} \right) = \frac{1}{1} \left( 0 \right) = 0, \\ 
    j &= 2: &     u_{12} &= a_{12} = 0 , \\ 
               && u_{22} &= a_{22} - \ell_{21} u_{12} = -2 - 3 \cdot 0 = -2, \\ 
            && \ell_{32} &= \frac{1}{u_{22}} \left( a_{32} - \ell_{31} u_{12} \right) = \frac{1}{-2} \left( -1 - 4 \cdot 0 \right) = 1/2, \\ 
            && \ell_{42} &= \frac{1}{u_{22}} \left( a_{42} - \ell_{41} u_{12} \right) = \frac{1}{-2} \left( 2 - 0 \cdot 0 \right) = -1, \\ 
    j &= 3: &     u_{13} &= a_{13} = 3 , \\ 
               && u_{23} &= a_{23} - \ell_{21} u_{13} = 5 - 3 \cdot 3 = 0, \\ 
               && u_{33} &= a_{33} - \ell_{31} u_{13} - \ell_{32} u_{23} = -2 - 4 \cdot 3 - 1/2 \cdot -4 = -12, \\ 
            && \ell_{43} &= \frac{1}{u_{33}} \left( a_{43} - \ell_{41} u_{13} - \ell_{42} u_{23} \right) = \frac{1}{-12} \left( 0 - 0 \cdot 3 - -1 \cdot -4 \right) = 1/3, \\ 
    j &= 4: &     u_{14} &= a_{14} = 2 , \\ 
               && u_{24} &= a_{24} - \ell_{21} u_{14} = 1 - 3 \cdot 2 = 0, \\ 
               && u_{34} &= a_{34} - \ell_{31} u_{14} - \ell_{32} u_{24} = -3 - 4 \cdot 2 - 1/2 \cdot -5 = 0, \\ 
               && u_{44} &= a_{44} - \ell_{41} u_{14} - \ell_{42} u_{24} - \ell_{43} u_{34} = 3 - 0 \cdot 2 - -1 \cdot -5 - 1/3 \cdot -17/2 = 5/6, \\ 
\end{align*} $$ 

So $L = \left(\begin{matrix}1 & 0 & 0 & 0\\3 & 1 & 0 & 0\\4 & \frac{1}{2} & 1 & 0\\0 & -1 & \frac{1}{3} & 1\end{matrix}\right)$ and $U = \left(\begin{matrix}1 & 0 & 3 & 2\\0 & -2 & -4 & -5\\0 & 0 & -12 & - \frac{17}{2}\\0 & 0 & 0 & \frac{5}{6}\end{matrix}\right)$. 

Solving $L \vec{y} = \vec{b}$ gives $\vec{y} = \mathtt{\text{[ 21.         -35.         -78.5          4.16666667]}}$ and solving $U \vec{x} = \vec{y}$ gives $\vec{x} = \mathtt{\text{[ 2. -1.  3.  5.]}}$.

(d) Calculate LU decomposition of the coefficient matrix $A = \left(\begin{matrix}1 & 5 & 2 & 2\\-2 & -4 & 2 & 0\\3 & 1 & -2 & -1\\-3 & -3 & 4 & -1\end{matrix}\right)$

$$ \begin{align*} 
    j &= 1: &     u_{11} &= a_{11} = 1 , \\ 
            && \ell_{21} &= \frac{1}{u_{11}} \left( a_{21} \right) = \frac{1}{1} \left( -2 \right) = -2, \\ 
            && \ell_{31} &= \frac{1}{u_{11}} \left( a_{31} \right) = \frac{1}{1} \left( 3 \right) = 3, \\ 
            && \ell_{41} &= \frac{1}{u_{11}} \left( a_{41} \right) = \frac{1}{1} \left( -3 \right) = -3, \\ 
    j &= 2: &     u_{12} &= a_{12} = 5 , \\ 
               && u_{22} &= a_{22} - \ell_{21} u_{12} = -4 - -2 \cdot 5 = 6, \\ 
            && \ell_{32} &= \frac{1}{u_{22}} \left( a_{32} - \ell_{31} u_{12} \right) = \frac{1}{6} \left( 1 - 3 \cdot 5 \right) = -7/3, \\ 
            && \ell_{42} &= \frac{1}{u_{22}} \left( a_{42} - \ell_{41} u_{12} \right) = \frac{1}{6} \left( -3 - -3 \cdot 5 \right) = 2, \\ 
    j &= 3: &     u_{13} &= a_{13} = 2 , \\ 
               && u_{23} &= a_{23} - \ell_{21} u_{13} = 2 - -2 \cdot 2 = 0, \\ 
               && u_{33} &= a_{33} - \ell_{31} u_{13} - \ell_{32} u_{23} = -2 - 3 \cdot 2 - -7/3 \cdot 6 = 6, \\ 
            && \ell_{43} &= \frac{1}{u_{33}} \left( a_{43} - \ell_{41} u_{13} - \ell_{42} u_{23} \right) = \frac{1}{6} \left( 4 - -3 \cdot 2 - 2 \cdot 6 \right) = -1/3, \\ 
    j &= 4: &     u_{14} &= a_{14} = 2 , \\ 
               && u_{24} &= a_{24} - \ell_{21} u_{14} = 0 - -2 \cdot 2 = 0, \\ 
               && u_{34} &= a_{34} - \ell_{31} u_{14} - \ell_{32} u_{24} = -1 - 3 \cdot 2 - -7/3 \cdot 4 = 0, \\ 
               && u_{44} &= a_{44} - \ell_{41} u_{14} - \ell_{42} u_{24} - \ell_{43} u_{34} = -1 - -3 \cdot 2 - 2 \cdot 4 - -1/3 \cdot 7/3 = -20/9, \\ 
\end{align*} $$ 

So $L = \left(\begin{matrix}1 & 0 & 0 & 0\\-2 & 1 & 0 & 0\\3 & - \frac{7}{3} & 1 & 0\\-3 & 2 & - \frac{1}{3} & 1\end{matrix}\right)$ and $U = \left(\begin{matrix}1 & 5 & 2 & 2\\0 & 6 & 6 & 4\\0 & 0 & 6 & \frac{7}{3}\\0 & 0 & 0 & - \frac{20}{9}\end{matrix}\right)$. 

Solving $L \vec{y} = \vec{b}$ gives $\vec{y} = \mathtt{\text{[-10.         -10.           4.66666667  -4.44444444]}}$ and solving $U \vec{x} = \vec{y}$ gives $\vec{x} = \mathtt{\text{[ 1.00000000e+00 -3.00000000e+00 -5.92118946e-16  2.00000000e+00]}}$.

