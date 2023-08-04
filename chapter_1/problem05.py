# integration

import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

def multy(f,w):
    return f*w
def sumProd(f,w):
    vmulty = np.vectorize(multy)
    sum_prod = sum(vmulty(f,w))
    return sum_prod
def integrate(func, a, b, N, method):
    x = np.linspace(a, b, N)
    h = (b - a)/(N - 1)
    f = func(x)
    w = np.ones(N)*h
    if method == "trepezoidal":
        w[0], w[-1] = h/2, h/2
    elif method == "simpsons":
        w[0], w[-1] = h/3, h/3
        w[1:-1:2] = 4*h/3
        w[2:-1:2] = 2*h/3
    integral = sumProd(f=f, w=w)
    return integral
def monteIntegrate(func, a, b, N):
    x = np.random.uniform(a,b,N)
    f = func(x)
    h = (b-a)
    avg_f = sum(f)/N
    integral = avg_f*h
    return integral
def gaussIntegrate(func, a, b, N):
    x,w = sp.roots_legendre(N)
    x = (b+a)/2 + ((b-a)/2)*x
    w = ((b-a)/2)*w
    f = func(x)
    integral = sumProd(f=f, w=w)
    return integral
def plotError(trep, simp, monte, gauss, N, true_integral):
    plt.title("Error Plot")
    plt.xlabel("N")
    plt.ylabel("Error")
    trep_error = np.absolute(true_integral - trep)/true_integral
    simp_error = np.absolute(true_integral - simp)/true_integral
    monte_error = np.absolute(true_integral - monte)/true_integral
    gauss_error = np.absolute(true_integral - gauss)/true_integral
    plt.plot(np.log10(N), np.log10(trep_error), 'r')
    plt.plot(np.log10(N[1:-1:2]), np.log10(simp_error), 'g')
    plt.plot(np.log10(N), np.log10(monte_error), 'b')
    plt.plot(np.log10(N), np.log10(gauss_error), 'c')
    legend = ['trep-error', 'simp-error', 'monte_e', 'gauss_error']
    plt.legend(legend)
    plt.show()
def f(x):
    return x**9 + x**3
def question1():
    # integrate func(x) from a to b
    func = np.vectorize(f)
    a, b = 0, 1
    true_integral = 0.35

    n1, n2 = 6, 100
    N = np.linspace(n1, n2, n2-n1+1, dtype=int)
    vIntegral = np.vectorize(integrate)
    # trepezoidal method
    trep_integral = vIntegral(func=func, a=a, b=b, N=N, method="trepezoidal")
    # simpsons method
    simp_integral = vIntegral(func=func, a=a, b=b, N=N[1:-1:2], method="simpsons")
    # gaussian quadrature
    vIntegral_gauss = np.vectorize(gaussIntegrate)
    gauss_integral = vIntegral_gauss(func=func, a=a, b=b, N=N)
    # monte carlo
    vIntegral_monte = np.vectorize(monteIntegrate)
    monte_integral = vIntegral_monte(func=func, a=a, b=b, N=N)
    plotError(trep=trep_integral, simp=simp_integral, gauss=gauss_integral, monte=monte_integral, N=N, true_integral=true_integral)
def g(x):
    x = -x**2
    return np.exp(x)
def question2():
    # integrate func(x) from a to b
    func = np.vectorize(g)
    a, b = 0, 10000
    N = 10001
    vIntegral = np.vectorize(integrate)
    # trepezoidal method
    trep_integral = vIntegral(func=func, a=a, b=b, N=N, method="trepezoidal")
    # simpsons method
    simp_integral = vIntegral(func=func, a=a, b=b, N=N, method="simpsons")
    # gaussian quadrature
    vIntegral_gauss = np.vectorize(gaussIntegrate)
    gauss_integral = vIntegral_gauss(func=func, a=a, b=b, N=N)
    # monte carlo
    vIntegral_monte = np.vectorize(monteIntegrate)
    monte_integral = vIntegral_monte(func=func, a=a, b=b, N=N)
    print("Integral:")
    print(f"Trepezoidal Method : {trep_integral}")
    print(f"Simpson's Method : {simp_integral}")
    print(f"Guassian Quadrature : {gauss_integral}")
    print(f"Monte Carlo : {monte_integral}")
def getBelow(dist, r):
    if dist < r:
        return 1
    return 0
def question3():
    r = 1
    N = 1000
    x = np.random.uniform(-r, r, N)
    y = np.random.uniform(-r, r, N)
    dist = np.sqrt(x**2 + y**2)
    vGetBelow = np.vectorize(getBelow)
    dist_below = vGetBelow(dist=dist, r=r)
    num = sum(dist_below)
    pi = 4*(num/N)
    print(pi)
    plt.scatter(x, y)
    a = np.linspace(-r, r, 100)
    b = np.sqrt(r**2 - a**2)
    plt.plot(a, b, 'g')
    plt.plot(a, -b, 'g')
    plt.show()
def main():
    # question1()
    # question2()
    question3()

if __name__ == "__main__":
    main()