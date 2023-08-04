import numpy as np
import matplotlib.pyplot as plt

def f1(x,y):
    f = x**2 - 4*y**2 - 1
    return f

def f2(x,y):
    f = x - 8*y**3 - 3
    return f
def main():
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-1, 0, 100)
    X,Y = np.meshgrid(x,y)
    Z1 = f1(X,Y)
    Z2 = f2(X,Y)
    Z3 = np.zeros([100,100])
    ax = plt.axes(projection='3d')
    ax.contour3D(X,Y,Z1, 50)
    ax.contour3D(X,Y,Z2, 50)
    # ax.contour3D(X,Y,Z3, 50, cmap='binary')
    plt.show()

if __name__=="__main__":
    main()