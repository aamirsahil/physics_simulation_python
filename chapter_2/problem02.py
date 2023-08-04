# root finding 2
import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(1, 'D:\Coding\computational_problems_in_physics\chapter_1')

from problem01 import NewtRaph as NR
from problem01 import bisection as Bs
from chapter_1.problem04 import central_difference_method as cdm

def boundOnF(f, bound=20):
    if type(f) == np.float64:
        return f
    for i in range(len(f)):
        if f[i] > 20:
            f[i] = 20
        if f[i] < -20:
            f[i] = -20
    return f
def func1(x):
    return np.sqrt(x)
def func2(x):
    m = np.sqrt(10 - x)
    f = m*np.tan(m)
    f = boundOnF(f)
    return f
def func3(x):
    m = np.sqrt(10 - x)
    f = m*(1/np.tan(m))
    f = boundOnF(f)
    return f
def func4(x):
    f = func2(x) - func1(x)
    return f
def func4Neg(x):
    f = func2(x) + func1(x)
    return f
def func5(x):
    f = func3(x) - func1(x)
    return f
def func5Neg(x):
    f = func3(x) + func1(x)
    return f

def plotGraph(x,y1,y2,legend):
    # plt.xlim(-1, 11)
    # plt.ylim(-1, 5)
    plt.plot(x,y1, 'r')
    plt.plot(x,-y1, 'r')
    plt.plot(x,y2, '')
    plt.legend(legend)
    plt.show()
def printResults(x,i,func):
    # bisection
    # symmetric
    print(x)
    if i !=None:
        print(f"f({x}) = {func(x)}")
        print(f"Found in {i} iterations")
    # anti symmetric

def main():
    EB = np.linspace(0, 10, 10000)

    RHS = func1(EB)
    LHS1 = func2(EB)
    LHS2 = func3(EB)
    # plotGraph(x=EB, y1=RHS, y2=LHS1, legend=['RHS','LHS'])
    # plotGraph(x=EB, y1=RHS, y2=LHS2, legend=['RHS','LHS'])
    # x,i = Bs(a=2, b=6, func=func5Neg, N=100, error=0.00001)
    x,i = NR(x=2, func=func5Neg, dfunc=cdm, N=100, error=0.00001)
    printResults(x,i,func=func5Neg)
if __name__ == "__main__":
    main()