# 大学物理实验二 数据处理
# 非良导体热导率的测定

import matplotlib.pyplot as plt
import numpy as npy
from numpy import *
from scipy.optimize import curve_fit

t1 = 90.00
t2 = 47.20
# 温度
ta = npy.array([
    48.21, 47.95, 47.12, 46.26, 45.38, 44.60, 43.75, 43.20,
    42.33, 41.57, 40.93, 40.23, 39.65, 39.09, 38.50, 37.88
])
# 时间
time = npy.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
da = 1 * 10 ** (-2)  # 铝圆柱体 A 高度
lb = 0.316 * 10 ** (-2)  # 待测薄片 B 厚度
ma = 259.3  # 铝圆柱体 A 质量
d = 10.000 * 10 ** (-2)  # 铝圆柱体 A 直径
c = 0.217  # 比热
k = -0.012  # 斜率


def function(x, a, b):
    return a * npy.exp(-b * x)


def get_k():
    plt.figure(figsize=(10, 10), dpi=100)
    plt.scatter(time, ta, label="original")
    # 指数拟合
    popt, pcov = curve_fit(function, time, ta)
    a = popt[0]
    b = popt[1]
    y_vals = function(time, a, b)
    plt.plot(time, y_vals, "r", label="polyfit values")
    plt.xlabel("t(min)")
    plt.ylabel("TA(°C)")
    plt.legend()
    plt.show()


def get_lambda():
    output_lambda_up = (2 * c * ma * lb * (d + 4 * da)) * k
    output_lambda_down = (pi * d ** 2) * (d + 2 * da) * (t2 - t1)
    output_lambda = output_lambda_up / output_lambda_down
    print("λ =", output_lambda)


if __name__ == "__main__":
    get_k()
    get_lambda()
