# encoding utf-8
# physics experiment 19

import numpy as np

x1 = [6.350, 6.350, 6.300, 6.550, 6.545]
xn = [2.745, 2.790, 2.750, 2.960, 2.950]
x1_prime = [2.650, 2.710, 2.700, 2.990, 2.980]
xn_prime = [6.340, 6.365, 6.390, 6.590, 6.575]
delta_x = [0.0, 0.0, 0.0, 0.0, 0.0]
n = 5
lbd = 627.0 * 10 ** (-6)
foc = 100


def average():
    sum_up_x = 0
    for i in range(5):
        sum_up_x += delta_x[i - 1]
    return sum_up_x / 5


def get_a():
    sum_up_x = 0
    for i in range(5):
        sum_up_x += delta_x[i - 1]
    a = lbd * foc / (sum_up_x / 5)
    return a


def get_sigma_delta_x():
    sigma_delta_x = np.std(delta_x)
    return sigma_delta_x


def get_ave_sigma_delta_x():
    ave_sigma_delta_x = get_sigma_delta_x() / np.sqrt(5)
    return ave_sigma_delta_x


def get_e_a():
    ea = np.sqrt((get_ave_sigma_delta_x() / average()) ** 2)
    return ea


def get_sigma_ave_a():
    sigma_ave_a = get_a() * get_e_a()
    return sigma_ave_a


def main():
    for i in range(5):
        delta_x[i - 1] = (abs(xn[i - 1] - x1[i - 1]) + abs(xn_prime[i - 1] - x1_prime[i - 1])) / (2 * (n - 1))
    print(delta_x)

    print("平均 Delta x：", average())
    print("狭缝宽度：", get_a())
    print("Delta x 的标准差：", get_sigma_delta_x())
    print("Delta x 的平均的标准差：", get_ave_sigma_delta_x())
    print("Ea 等于：", get_e_a())
    print("a 的平均的标准差：", get_sigma_ave_a())


if __name__ == "__main__":
    main()
