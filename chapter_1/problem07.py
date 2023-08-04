# central limit theorem
import numpy as np
import matplotlib.pyplot as plt

def question1():
    iter_count = 10000
    sum_list = []
    for i in range(iter_count):
        N = 1000
        r = np.random.uniform(0,1,N)
        sum_list.append(sum(r)/len(r))
    avg = sum(sum_list)/len(sum_list)
    sigma = sum((sum_list - avg)**2)/len(sum_list)
    x = np.linspace(min(sum_list), max(sum_list), 100)
    guass_dist = 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-(x-avg)**2/(2*sigma**2))
    plt.hist(sum_list, bins=100, density=True)
    plt.plot(x, guass_dist)
    plt.show()

    pass
def main():
    question1()

if __name__ == "__main__":
    main()