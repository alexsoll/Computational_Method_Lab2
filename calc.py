import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np

import math

Fi_a = 3.5
Fi_b = 1
Fi_c = 1

def FuncFi(x, l):
    return Fi_a * 1 + Fi_b * math.cos(math.pi * x / l) + Fi_c * math.cos(2 * math.pi * x / l)


B_a = 0
B_b = 0.25
B_c = -0.25
B_d = -0.5
B_e = -0.5

def FuncB(x, l):
    return B_a * 1 + B_b * math.cos(math.pi * x / l) + B_c * math.sin(math.pi * x / l) + \
        B_d * math.cos(2 * math.pi * x / l) + B_e * math.sin(2 * math.pi * x / l)


def RightConst(y, l, tau):
    x = np.zeros(len(y))
    c = l / 2

    simpson = (l / 6) * (FuncB(0, l) + 4 * FuncB(c, l) + FuncB(l, l))

    for i in range(1, len(x)):
        x[i] = y[i] * ((1 / tau) + FuncB(i, l) - simpson)

    return x

def main(args):
    T = args[0] ; l = args[1] ; a = args[2] ; h = args[3] ; tau = args[4]
    Fi_a = args[5] ; Fi_b = args[6] ; Fi_c = args[7]
    B_a = args[8] ; B_b = args[9] ; B_c = args[10] ; B_d = args[11] ; B_e = args[12]

    y = np.zeros(l - 1)
    b = np.zeros(l + 1)
    y0 = np.zeros(l + 1)
    A = np.zeros((l - 1, l - 1))
    B = np.zeros((l + 1, l + 1))
    yb = np.zeros(l + 1)

    for i in range(len(y)):
        y[i] = FuncFi(i + 1, l)

    for i in range(len(y0)):
        y0[i] = FuncFi(i, l)
        b[i] = FuncB(i, l)

    coef1 = (-1) * (a * a) / (h * h)
    coef2 = ((2 * a * a) / (h * h)) + (1 / tau)

    for i in range(1, l - 2):
        A[i][i - 1] = coef1
        A[i][i] = coef2
        A[i][i + 1] = coef1

    A[0][0] = coef2
    A[0][1] = coef1
    A[l - 2][l - 3] = coef1
    A[l - 2][l - 2] = coef2

    for i in range(1, l):
        B[i][i - 1] = coef1
        B[i][i] = coef2
        B[i][i + 1] = coef1

    B[0][0] = 1
    B[0][1] = -1
    B[1][0] = 0
    B[l - 1][l] = 0
    B[l][l - 1] = -1
    B[l][l] = 1

    for i in range(len(y)):
        yb[i + 1] = y[i]

    yb[0] = 0
    yb[l] = 0


    for i in range(1, T + 1):
        tmp_y = RightConst(yb, l, tau)
        yb = np.linalg.solve(B, tmp_y)


    print(y)
    print(y0)
    print(yb)

    x = [i for i in range(0, l + 1)]
    plt.plot(x, yb, color='black')
    plt.plot(x, y0, color='blue')
    plt.plot(x, b, color='red')
    plt.show()

 
