# Physics Experiment 07
import math

import numpy as np

# 圆盘 A
A = [59.02, 58.90, 58.55, 58.62, 58.71]

# 圆盘 A + B
B = [63.60, 62.72, 63.20, 63.01, 62.64]

ma = 316.0 * 10 ** (-3)
mb = 343.3 * 10 ** (-3)
sigma_ma = 0.3 * 10 ** (-3)
sigma_mb = 0.3 * 10 ** (-3)

sigma_L = 0.03 * 10 ** (-2)
sigma_R = 0.002 * 10 ** (-2)
sigma_r = 0.03 * 10 ** (-2)

R_a = 6.420 * 10 ** (-2)
R_b = 6.006 * 10 ** (-2)
r_b = 4.005 * 10 ** (-2)
R = 6.36 * 10 ** (-2)
r = 4.42 * 10 ** (-2)
L = 45.50 * 10 ** (-2)

g = 9.8
pi = 3.1415926


def main():
    # 计算平均 A
    sum_a = 0
    for i in range(5):
        sum_a += A[i - 1]
    ta = sum_a / 5
    print("A 的平均周期是 ", ta)

    # 计算平均 A + B
    sum_a_b = 0
    for i in range(5):
        sum_a_b += B[i - 1]
    tab = sum_a_b / 5
    print("A + B 的平均周期是 ", tab)

    # 计算 TA 的方差
    sigma_a = np.var(A)
    print("TA 的方差是", sigma_a)

    # 计算 T(A+B) 的方差
    sigma_a_b = np.var(B)
    print("T(A + B) 的方差是 ", sigma_a_b)

    # 计算 TA 的平均的方差
    sigma_mean_a = sigma_a / math.sqrt(5)
    print("TA 的平均方差是 ", sigma_mean_a)

    # 计算 T(A+B) 的平均的方差
    sigma_mean_a_b = sigma_a_b / math.sqrt(5)
    print("T(A+B) 的平均方差是 ", sigma_mean_a_b)


if __name__ == "__main__":
    main()
