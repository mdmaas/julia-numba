import math
import numba as nb
import time

@nb.njit   
def quad_trap(f,a,b,N):
    h = (b-a)/N
    integral = h * ( f(a) + f(b) ) / 2
    for k in range(N):
        xk = (b-a) * k/N + a
        integral = integral + h*f(xk)
    return integral

@nb.njit(nb.float64(nb.float64))
def func(x):
    return math.exp(x) - 10

def f(p): 
    @nb.njit(nb.float64(nb.float64))
    def integrand(x):
        return math.exp(p*x) - 10
    return quad_trap(integrand, -1, 1, 10000) 


# warm-up JIT
q1 = quad_trap(func,-1,1,10000)

start_time = time.time()
q1 = quad_trap(func,-1,1,10000)
print("Quadrature--- %s seconds ---" % (time.time() - start_time))

# warm-up JIT
a = f(1)

start_time = time.time()
r = f(1)
print("Eval f(1)--- %s seconds ---" % (time.time() - start_time))


