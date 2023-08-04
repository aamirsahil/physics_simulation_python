# Mathrix inverse, Solution to linear equation, Eigen values

import numpy as np
# 1
def questionSet1(A, inv_A, inv_A_analytic):
    print("Numerical")
    print("---------")
    print("A * inv(A) = \n", np.around(np.matmul(A, inv_A), decimals=16))
    print("inv(A) * A = \n", np.around(np.matmul(inv_A, A), decimals=16))
    print("Analytical")
    print("----------")
    print("A * inv(A) = \n", np.around(np.matmul(A, inv_A_analytic), decimals=16))
    print("inv(A) * A = \n", np.around(np.matmul(inv_A_analytic, A), decimals=16))
    print("difference")
    print("----------")
    print("inv(A)_numeric - inv(A)_analitic = \n", np.around(inv_A - inv_A_analytic, decimals=17))
# 2
def questionSet2(inv_A):
    b = np.array([12, -25, 32])
    print("A * x = b")
    print("---------")
    print("b = ", b)
    print("x = ", np.around(np.matmul(inv_A, b), decimals=3))
    print("*******************")

    b = np.array([4, -10, 22])
    print("b = ", b)
    print("x = ", np.around(np.matmul(inv_A, b), decimals=3))
    print("*******************")

    b = np.array([20, -30, 40])
    print("b = ", b)
    print("x = ", np.around(np.matmul(inv_A, b), decimals=3))
    print("*******************")
# 3
def questionSet3(a, b):
    A = np.array([
        [a, b],
        [-b, a]
    ])
    e_values, e_vectors = np.linalg.eig(A)
    print("eigen value 1 = ", e_values[0])
    print("eigen value 2 = ", e_values[1])
    print("eigen vectors 1 = ", e_vectors[:, 0]/.70710678)
    print("eigen vectors 2 = ", e_vectors[:, 1]/.70710678)

    print("Checking")
    print("A*x1 - lam1*x1 = ", np.matmul(A, e_vectors[:, 0]) - e_values[0]*e_vectors[:, 0])
    print("A*x2 - lam2*x2 = ", np.matmul(A, e_vectors[:, 1]) - e_values[1]*e_vectors[:, 1])

def main():
    A = np.array([
        [4, -2, 1],
        [3, 6, -4],
        [2, 1, 8]
    ])
    inv_A = np.linalg.inv(A)
    inv_A_analytic = np.array([
        [52, 17, 2],
        [-32, 30, 19],
        [-9, -8, 30]
    ])/263
    print("################ Question 1 ######################")
    questionSet1(A, inv_A, inv_A_analytic)
    print("################ Question 2 ######################")
    questionSet2(inv_A)
    print("################ Question 3 ######################")
    questionSet3(50, 25)


if __name__ == '__main__':
    main()