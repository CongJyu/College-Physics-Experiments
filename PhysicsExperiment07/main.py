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

    # 计算 TA 的标准差
    sigma_a = np.std(A)
    print("TA 的标准差是", sigma_a)

    # 计算 T(A+B) 的标准差
    sigma_a_b = np.std(B)
    print("T(A + B) 的标准差是 ", sigma_a_b)

    # 计算 TA 的平均的标准差
    sigma_mean_a = sigma_a / math.sqrt(5)
    print("TA 的平均标准差是 ", sigma_mean_a)

    # 计算 T(A+B) 的平均的标准差
    sigma_mean_a_b = sigma_a_b / math.sqrt(5)
    print("T(A+B) 的平均标准差是 ", sigma_mean_a_b)

    # A 的平均转动惯量
    j_a = ((ma * g * R * r) / (4 * pi ** 2 * L)) * ta ** 2
    print("A 的平均转动惯量：", j_a)

    # A + b 的平均转动惯量
    j_a_b = ((ma + mb) * g * R * r) / (4 * pi ** 2 * L) * tab ** 2
    print("A + b 的平均转动惯量：", j_a_b)

    # E_j_a 百分比
    e_j_a = np.sqrt(
        (2 * sigma_mean_a / ta) ** 2 +
        (sigma_ma / ma) ** 2 +
        (sigma_L / L) ** 2 +
        (sigma_R / R) ** 2 +
        (sigma_r / r) ** 2
    ) * 100
    print("Eja 百分比：", e_j_a, "%")

    # E_j_ab 百分比
    e_j_ab = np.sqrt(
        (2 * sigma_mean_a_b / tab) ** 2 +
        ((sigma_ma ** 2 + sigma_mb ** 2) / (ma + mb) ** 2) +
        (sigma_L / L) ** 2 +
        (sigma_R / R) ** 2 +
        (sigma_r / r) ** 2
    ) * 100
    print("Ejab 百分比：", e_j_ab, "%")

    # B 的转动惯量
    j_b = j_a_b - j_a
    print("B 的转动惯量：", j_b)

    # 理论值
    j_a0 = 0.5 * ma * R_a ** 2
    print("理论值：Ja =", j_a0)
    j_b0 = 0.5 * (mb * R_b ** 2 + mb * r_b ** 2)
    print("理论值：Jb0 =", j_b0)


if __name__ == "__main__":
    main()
