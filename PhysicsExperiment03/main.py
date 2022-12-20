# 实验三 薄透镜焦距的测量

from math import *


def sum_up(x1, x2, x3, x4, x5):
    return x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2 + x5 ** 2


def sum_up2(x1, x2, x3):
    return x1 ** 2 + x2 ** 2 + x3 ** 2


if __name__ == "__main__":
    a1 = float(input("数据1#："))
    a2 = float(input("数据2#："))
    a3 = float(input("数据3#："))
    a4 = float(input("数据4#："))
    a5 = float(input("数据5#："))
    sigma = sqrt(sum_up(a1, a2, a3, a4, a5) / (5 * 4))
    sigma2 = sqrt(sum_up2(a1, a2, a3) / (3 * 2))
    print("Sigma =", sigma)
