# random numbers
import matplotlib.pyplot as plt
import numpy as np
import time

def randomGen(a, c, M, N=1,seed=time.time()):
    r = [seed]
    for i in range(N):
        r_next = (a*r[-1] + c)%M
        r.append(r_next)
    return r[1:]
def question1():
    N = 100
    x = np.linspace(0,1,N)
    a, c, M = 57, 1, 256
    seed = 10
    r = randomGen(a=a, c=c, M=M, N=N, seed=seed)
    # r = randomGen(a=a, c=c, M=M, N=N)
    plt.plot(x, r)
    plt.show()
    # scatterPlot(r)
def scatterPlot(r):
    x = r[0::2]
    y = r[1::2]
    plt.scatter(x,y)
    plt.show()
def kMoment(N,k):
    r = np.random.uniform(0,1,N)
    k_moment = sum(r**k)/N
    return k_moment
def kCorrelation(N,k):
    r = np.random.uniform(0,1,N)
    k_correlation = 0
    for i in range(N-k):
        k_correlation += (r[i]*r[i+k])
    if (N-k) <= 0:
        k_correlation = 0
    else:
        k_correlation /= (N-k)
    return k_correlation
def question2():
    # N = 1000
    # r = np.random.uniform(0,1,N)
    # scatterPlot(r)
    k = 2
    N = range(3,1001)

    # vkMoment = np.vectorize(kMoment)
    # k_moment = vkMoment(N=N, k=k)
    # deviation = (1/(k+1) - k_moment)
    vkCorrelation = np.vectorize(kCorrelation)
    k_correlation = vkCorrelation(N=N, k=k)
    deviation = (1/4 - k_correlation)
    plt.plot(N, deviation)
    plt.show()
def main():
    # question1()
    question2()
if __name__ == "__main__":
    main()