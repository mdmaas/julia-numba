using LoopVectorization

""" Trapezoidal rule for numerical quadrature"""
function quad_trap(f,a,b,N) 
    h = (b-a)/N
    int = h * ( f(a) + f(b) ) / 2
    @turbo for k=1:N-1
        xk = (b-a) * k/N + a
        int = int + h*f(xk)
    end
    return int
end

g(p) = quad_trap( x -> exp(p*x) - 10, -1, 1, 10000) 
g(1)
@time g(1)