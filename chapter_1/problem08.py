# rk4 method
import matplotlib.pyplot as plt
import numpy as np

def func1(x,y):
    f = np.sin(x)
    return f

def rk4(h, y0, x0, func):
    k1 = h*func(x0, y0)
    k2 = h*func(x0+h/2, y0+k1/2)
    k3 = h*func(x0+h/2, y0+k2/2)
    k4 = h*func(x0+h, y0+k3)
    y1 = y0 + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    return y1
def ODESolver(func, x0, y0, a, b, N):
    x = [x0]
    y = [y0]
    h = (b - a)/N
    for i in range(N):
        y1 = rk4(h=h, y0=y0, x0=x0, func=func)
        x0 = x0 + h
        y0 = y1
        x.append(x0)
        y.append(y0)
    return x,y

def main():
    x0, y0 = 0, 0
    a, b = x0, 10
    N = 100
    func = func1
    x,y = ODESolver(func, x0=x0, y0=y0, a=a, b=b, N=N)
    plt.plot(x,y)
    plt.show()

if __name__ == "__main__":
    main()