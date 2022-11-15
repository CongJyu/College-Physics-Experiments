# Physics Experiment 08

import numpy as np


def main():
    # ln 的平均值
    LN = [0.4157, 0.4110, 0.4176, 0.4231, 0.4246]
    ln_sum = 0
    for i in range(5):
        ln_sum += LN[i - 1]
    ave_ln = ln_sum / 5
    print("ln 的平均值：", ave_ln)

    # 平均周期
    T = [1.5638, 1.5641, 1.5643, 1.5646, 1.5648, 1.5650, 1.5652, 1.5654, 1.5655, 1.5657]
    t_sum = 0
    for i in range(10):
        t_sum += T[i - 1]
    ave_t = t_sum / 10
    print("平均周期：", ave_ln)

    # 求阻尼系数 beta
    beta = ave_ln / (5 * ave_t)
    print("阻尼系数 beta：", beta)

    # 受迫振动的幅度特性和相频特性曲线
    t = [1.530, 1.540, 1.550, 1.560, 1.570, 1.580, 1.590, 1.600, 1.610, 1.620, 1.630, 1.640, 1.650, 1.660]
    theta = [67.0, 85.5, 112.4, 137.0, 136.1, 111.8, 86.1, 69.6, 59.0, 50.0, 43.0, 38.5, 34.5, 31.0]
    t0 = [1.5645, 1.5643, 1.5639, 1.5635, 1.5638, 1.5643, 1.5644, 1.5644, 1.5644, 1.5643, 1.5643, 1.5641, 1.5639]
    phi = [-163.85, -154.85, -136.40, -113.00, -85.75, -61.50, -50.15, -42.00, -35.05, -30.90, -28.15, -25.80, -24.00,
           -22.55]
    phi_result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pi = 3.14159
    for i in range(14):
        phi_result[i - 1] = (np.tan((- beta * t0[i - 1] ** 2 * t[i - 1]) / (pi * (t[i - 1] ** 2 - t0[i - 1] ** 2)))) ** (-1)
    print("Phi: ", phi_result)
    omega_omega0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(14):
        omega_omega0[i - 1] = t0[i - 1] / t[i - 1]
    print("omega/omega0：", omega_omega0)


if __name__ == "__main__":
    main()
