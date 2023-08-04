# computer range and precesion

import math
from tkinter import E
# 1
def questionSet1():
    N = 200
    under = 1
    over = 1
    for i in range(N):
        # if under == 0.0:
        #     break
        try:
            print(float(over*(i+1)))
        except:
            break
        under /= (i+11)
        over *= (i+1)
    print("loop num = ", i, "\nunder = ", under, "\nover = ", float(over))
# 2
def questionSet2():
    e = 1
    e_complex = 1 + 1j
    N = 58
    for i in range(N):
        e /= 2
        e_complex /= 2

        one = 1.0 + e
        one_complex = (1.0 + 1.0j) + e_complex

        if(one_complex == (1.0 + 1.0j)):
            break
        if(one == 1.0):
            break
    print("loop number = ", i, "\none = ", one, "\ne = ", e)
    print("loop number = ", i, "\none complex = ", one_complex, "\ne complex = ", e_complex)
def main():
    # questionSet1()
    questionSet2()
if __name__ == "__main__":
    main()


