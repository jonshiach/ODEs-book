import numpy as np

def ivp_solver(f, tspan, y0, h, solver):

    # Initialise t and y arrays
    nsteps = int((tspan[1] - tspan[0]) / h)
    t = h * np.arange(nsteps + 1)
    y = np.zeros((nsteps + 1,len(y0)))
    t[0] = tspan[0]
    y[0,:] = y0

    # Loop through steps and calculate single step solver solution
    for n in range(nsteps):
        y[n+1] = solver(f, t[n], y[n,:], h)
        
    return t, y


def euler(f, t, y, h): 
    return y + h * f(t, y)


def heun(f, t, y, h): 
    k1 = f(t, y)
    k2 = f(t + h, y + h * k1)
    return y + h/2 * (k1 + k2)


def rk4(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + 0.5 * h, y + 0.5 * h * k1)
    k3 = f(t + 0.5 * h, y + 0.5 * h * k2)
    k4 = f(t + h, y + h * k3)
    return y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


def asc_ivp_solver(f, tspan, y0, h, tol, solver):

    # Initialise t and y arrays
    t = np.zeros(100000)
    y = np.zeros((100000, len(y0)))
    t[0] = tspan[0]
    y[0,:] = y0

    # Loop through steps
    n, nfail = 0, 0
    while t[n] < tspan[1]:

        # Calculate order p and p+1 solutions
        yp1, yp, p, s = solver(f, t[n], y[n,:], h)

        # Estimate error
        delta = max(abs(yp1 - yp))

        # Check whether the step was successful or not
        if delta < tol:
            y[n+1,:] = yp1
            t[n+1] = t[n] + h
            n += 1
        else:
            nfail = nfail + 1

        # Calculate new value of h for the next step
        h *= max(0.5, min(2, 0.9 * (tol / delta) ** (1 / (1 + p))))

        # Limit h so we don't overrun tmax
        h = min(h, tspan[1] - t[n])

    # Print solver stats
    print("\nSolver stats")
    print("----------------------")
    print(f"{n} successful steps")
    print(f"{nfail} failed steps")
    print(f"{s * (n - 1 + nfail)} function evaluations")
        
    return t[:n+1], y[:n+1,:]


def rkf45(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + 1/4 * h, y + 1/4 * h * k1)
    k3 = f(t + 3/8 * h, y + h * (3/32 * k1 + 9/32 * k2))
    k4 = f(t + 12/13 * h, y + h * (1932/2197 * k1 - 7200/2197 * k2 + 7296/2197 * k3))
    k5 = f(t + h, y + h * (439/216 * k1 - 8 * k2 + 3680/513 * k3 - 845/4104 * k4))
    k6 = f(t + 1/2 * h, y + h * (-8/27 * k1 + 2 * k2 - 3544/2565 * k3 + 1859/4104 * k4 - 11/40 * k5))
    y5 = y + h * (16/135 * k1 + 6656/12825 * k3 + 28561/56430 * k4 - 9/50 * k5 + 2/55 * k6)
    y4 = y + h * (25/216 * k1 + 1408/2565 * k3 + 2197/4104 * k4 - 1/5 * k5)
    p, s = 4, 6
    return y5, y4, p, s


def rkbs23(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + 1/2 * h, y + 1/2 * h * k1)
    k3 = f(t + 3/4 * h, y + 3/4 * h * k2)
    k4 = f(t + h, y + h * (2/9 * k1 + 1/3 * k2 + 4/9 * k3))
    y3 = y + h * (2/9 * k1 + 1/3 * k2 + 4/9 * k3)
    y2 = y + h * (7/24 * k1 + 1/4 * k2 + 1/3 * k3 + 1/8 * k4)
    p, s = 2, 4
    return y3, y2, p, s


def radauIA(f, t, y, h): 
    neq = len(y)
    Y1, Y2, Y1prev, Y2prev = np.ones(neq), np.ones(neq), np.ones(neq), np.ones(neq)
    for k in range(10):
        Y1 = y + h * (1/4 * f(t, Y1) - 1/4 * f(t + 2/3 * h, Y2))
        Y2 = y + h * (1/4 * f(t, Y1) + 5/12 * f(t + 2/3 * h, Y2))
        if max(np.amax(abs(Y1 - Y1prev)), np.amax(abs(Y2 - Y2prev))) < tol:
            break
        Y1prev, Y2prev = Y1, Y2

    ynew = y + h / 4 * (f(t, Y1) + 3 * f(t + 2/3 * h,Y2))
    return ynew


def lu(A):
    n = A.shape[0]
    L, U = np.eye(n), np.zeros((n, n))
    for j in range(n):
        for i in range(n):
            sum_ = 0
            if i <= j:
                for k in range(i):
                    sum_ += L[i,k] * U[k,j]
        
                U[i,j] = A[i,j] - sum_   
            
            else:         
                for k in range(j):
                    sum_ += L[i,k] * U[k,j]
                    
                L[i,j] = (A[i,j] - sum_) / U[j,j]
    
    return L, U


def forward_substitution(L, b):
    n = L.shape[0]
    x = np.zeros(n)
    for i in range(n):
        sum_ = 0
        for j in range(i):
            sum_ += L[i,j] * x[j]
            
        x[i] = (b[i] - sum_) / L[i,i]
    
    return x


def back_substitution(U, b):
    n = U.shape[0]
    x = np.zeros(n)
    x[-1] = b[-1] / U[-1,-1]
    for i in range(n - 2, -1, -1):
        sum_ = 0
        for j in range(i + 1, n):
            sum_ += U[i,j] * x[j]
            
        x[i] = (b[i] - sum_) / U[i,i]
        
    return x


def partial_pivot(A):
    n = A.shape[0]
    P = np.eye(n)
    for j in range(n):
        maxpivot, maxpivotrow = A[j,j], j
        for i in range(j + 1, n):
            if A[i,j] > maxpivot:
                maxpivot, maxpivotrow = A[i,j], i

        A[[j,maxpivotrow]] = A[[maxpivotrow,j]] 
        P[[j,maxpivotrow]] = P[[maxpivotrow,j]]

    return P


def cholesky(A):
    n = A.shape[0]
    L = np.zeros((n, n))   
    for j in range(n):
        for i in range(j, n):
            for k in range(j):
                L[i,j] += L[i,k] * L[j,k]
                
            if i == j:
                L[i,j] = np.sqrt(A[i,j] - L[i,j])
            else:
                L[i,j] = (A[i,j] - L[i,j]) / L[j,j]
    
    return L


def qr_gramschmidt(A):
    n = A.shape[1]
    Q, R = np.zeros(A.shape), np.zeros((n,n))
    for j in range(n):
        sum_ = 0
        for i in range(j):
            R[i,j] = np.dot(Q[:,i], A[:,j])
            sum_ += R[i,j] * Q[:,i]

        u = A[:,j] - sum_
        R[j,j] = np.linalg.norm(u)
        Q[:,j] = u / R[j,j]
    
    return Q, R


def qr_householder(A):
    m, n = A.shape
    I = np.eye(m)
    Q, R = np.eye(m), np.copy(A)
    for j in range(n):
        u = R[:,[j]]
        u[:j] = 0
        u = u + np.sign(R[j,j]) * np.linalg.norm(u) * I[:,[j]]
        v = u / np.linalg.norm(u)
        H = I - 2 * np.dot(v, v.T)
        R = np.dot(H, R)
        Q = np.dot(Q, H)
    
    return Q, R


def jacobi(A, b, tol=1e-6):
    n = len(b)
    x, xnew = np.zeros(n), np.zeros(n)
    for k in range(100):
        for i in range(n):
            sum_ = 0
            for j in range(n):
                if i != j:
                    sum_ += A[i,j] * x[j]
        
            xnew[i] = (b[i] - sum_) / A[i,i]
        
        x = np.copy(xnew)
        r = b - np.dot(A, x)
        if max(abs(r)) < tol:
            break
    
    return x


def gauss_seidel(A, b, tol=1e-6):
    n = len(b)
    x = np.zeros(n)
    for k in range(100):
        for i in range(n):
            sum_ = 0
            for j in range(n):
                if i != j:
                    sum_ += A[i,j] * x[j]
        
            x[i] = (b[i] - sum_) / A[i,i]
            
        r = b - np.dot(A, x)

        if max(abs(r)) < tol:
            break
    
    return x


def sor(A, b, omega, tol=1e-6):
    n = len(b)
    x = np.zeros(n)
    for k in range(100):
        for i in range(n):
            sum_ = 0
            for j in range(n):
                if i != j:
                    sum_ += A[i,j] * x[j]
        
            x[i] = (1 - omega) * x[i] + omega * (b[i] - sum_) / A[i,i]
            
        r = b - np.dot(A, x)
        if max(abs(r)) < tol:
            break
    
    return x