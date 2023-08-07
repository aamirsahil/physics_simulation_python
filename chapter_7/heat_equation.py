# Solve 1D heat eqation numerically
# define temperature field
# define forward and central differentials
# find temperature with time
import numpy as np
import matplotlib.pyplot as plt

def main():
    total_time = 100
    # t step
    dt = 0.01
    total_t_num = int(total_time // dt)
    time = np.linspace(0, total_time, total_t_num)
    
    x_min, x_max = 0, 1
    # x step
    dx = 0.01
    total_x_num = int((x_max - x_min) // dx)
    # x coordiante
    x = np.linspace(x_min, x_max, total_x_num)
    
    # temperature field
    T = np.zeros(total_x_num)
    # boundary condition
    T[0], T[-1] = (0, 0)
    T[1:-1] = np.sin(np.pi*x[1: -1])
    
    plt.plot(x, T)
    plt.show()

    K = 0.01
    C_rho = 100
    eta = K*dt/C_rho/(dx)**2

    for t_idx, t_value in enumerate(time):
        for x_idx, x_value in enumerate(x[1:-1]):
            T[x_idx+1] = T[x_idx+1] + eta*(T[(x_idx+1)+1] + T[(x_idx+1)-1] - 2*T[x_idx+1])            
        # progress time
        time += dt

    plt.plot(x, T)
    plt.show()

if __name__ == "__main__":
    main()