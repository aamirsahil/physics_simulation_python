import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from ODEsolver import RK4 as rk

def position(a,x0,w,p0,m,t):
    pos = np.exp(a*t)*(x0*np.cos(w*t) + (p0/m/w)*np.sin(w*t))
    return pos
def momentum(a,x,x0,w,p0,m,t):
    vel = a*x + w*np.exp(a*t)*(-x0*np.sin(w*t) + (p0/m/w)*np.cos(w*t))
    mom = m*vel
    return mom
def plot(x, y, title="", xlabel="", ylabel=""):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(x,y)
def problem1():
    w0 = 0.8
    k = 0.4
    w = np.sqrt(w0**2 - k**2/4)
    a = -k/2
    x0 = 1.0
    p0 = 4.0
    m = 1.0

    t = np.linspace(1,10,100)
    x = position(a=a,x0=x0,w=w,p0=p0,m=m,t=t)
    p = momentum(a=a,x=x,x0=x0,w=w,p0=p0,m=m,t=t)

    gs = gridspec.GridSpec(2,2)
    plt.subplot(gs[0,0])
    plot(t,x,"position plot","time", "position")

    gs = gridspec.GridSpec(2,2)
    plt.subplot(gs[0,1])
    plot(t,p,"momentum plot","time", "momentum")

    gs = gridspec.GridSpec(2,2)
    plt.subplot(gs[1,:])
    p0=0.0
    x = position(a=a,x0=x0,w=w,p0=p0,m=m,t=t)
    p = momentum(a=a,x=x,x0=x0,w=w,p0=p0,m=m,t=t)
    plot(x,p)
    p0=0.2
    x = position(a=a,x0=x0,w=w,p0=p0,m=m,t=t)
    p = momentum(a=a,x=x,x0=x0,w=w,p0=p0,m=m,t=t)
    plot(x,p)
    p0=0.4
    x = position(a=a,x0=x0,w=w,p0=p0,m=m,t=t)
    p = momentum(a=a,x=x,x0=x0,w=w,p0=p0,m=m,t=t)
    plot(x,p)
    p0=0.6
    x = position(a=a,x0=x0,w=w,p0=p0,m=m,t=t)
    p = momentum(a=a,x=x,x0=x0,w=w,p0=p0,m=m,t=t)
    plot(x,p)
    p0=0.8
    x = position(a=a,x0=x0,w=w,p0=p0,m=m,t=t)
    p = momentum(a=a,x=x,x0=x0,w=w,p0=p0,m=m,t=t)
    plot(x,p)
    p0=1.0
    x = position(a=a,x0=x0,w=w,p0=p0,m=m,t=t)
    p = momentum(a=a,x=x,x0=x0,w=w,p0=p0,m=m,t=t)
    plot(x,p,"phase plot","position", "momentum")
    
    plt.show()
def problem2():
    def force(x):
        F = 0.5*w0**2*(2*x-2/3*0.01*x**2)
        return F
    def func2(x,v,t,w0):
        return -w0**2*x - force(x)
    def func1(x,v,t):
        return v
    
    A = 2.0
    k=(2*np.pi)**2
    m=(10)**2
    w0 = np.sqrt(k/m)
    x0 = 0
    v0 = A*w0
    t0 = 0
    T = 2*np.pi/w0
    h = T/100
    t_end=5*T
    N = int(t_end/h)

    system = rk(func1=func1, func2=func2, x0=x0, v0=v0, t0=t0, w0=w0, h=h)
    system.solve(N)
    x,v,t = system.get()

    plot(t,x)
    # x_analytical = A*np.sin([w0*i for i in t])
    # v_analytical = w0*A*np.cos([w0*i for i in t])
    # plot(t,x_analytical)
    
    plt.show()

    # error = x - x_analytical
    # plot(t, error)

    # plt.show()
def main():
    problem2()

if __name__ == "__main__":
    main()