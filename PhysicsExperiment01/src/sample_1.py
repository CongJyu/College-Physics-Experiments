import math
import numpy as npy


# 光斑移动距离平均值 delta_x
def sample_1_x():
    delta_x = (1 / 9) * (
            (21.5 - 0.0) +
            (41.0 - 21.5) +
            (61.0 - 41.0) +
            (79.0 - 61.0) +
            (99.1 - 79.0) +
            (118.5 - 99.1) +
            (135.0 - 118.5) +
            (153.2 - 135.0) +
            (169.0 - 153.2)
    )
    print("样品1 光斑移动距离：", delta_x)


# 悬臂梁平均厚度
def sample_1_d():
    ave_d = (1 / 5) * (0.925 + 0.922 + 0.926 + 0.922 + 0.924)
    print("样品1 悬臂梁平均厚度：", ave_d)


def sample_1_x_std():
    data = npy.array([21.5, 19.5, 20.0, 18.0, 20.1, 19.4, 16.5, 18.2, 15.8])
    std_output = npy.std(data, ddof=1)
    print("样品1 光斑移动距离标准差：", std_output)


def sample_1_d_std():
    data = npy.array([0.925, 0.922, 0.926, 0.922, 0.924])
    std_output = npy.std(data, ddof=1)
    print("样品1 悬臂梁厚度标准差：", std_output)


def sample_1_e():
    m = 9.28 * (10 ** (-3))
    g = 9.79
    l1 = 220.0 * (10 ** (-3))
    l2 = 235.0 * (10 ** (-3))
    delta_l = 191.1 * (10 ** (-3))
    h1 = 120.0 * (10 ** (-3))
    h2 = 525.0 * (10 ** (-3))
    delta_h = 204.0 * (10 ** (-3))
    a = 22.00 * (10 ** (-3))
    b = 22.00 * (10 ** (-3))
    d = 0.924 * (10 ** (-3))
    delta_x = 18.82 * (10 ** (-3))
    part_1 = (12 * m * g) * ((l1 - (a / 2)) ** 2) / (b * d ** 3 * delta_x)
    part_2 = (2 * h2 - h1) * (1 + (delta_l / delta_h) ** 2) - (l2 - (1 / 3) * (l1 - (a / 2))) * (delta_l / delta_h)
    result_e = part_1 * part_2
    print("样品1 E =", result_e)


def sample_1_sigma_e():
    sigma_m = 0.02 * (10 ** (-3))
    sigma_l1 = 0.3 * (10 ** (-3))
    sigma_b = 0.02 * (10 ** (-3))
    sigma_h2 = 0.3 * (10 ** (-3))
    sigma_delta_l = 0.3 * (10 ** (-3))
    sigma_d = 0.002 * (10 ** (-3))
    sigma_delta_x = 3.03 * (10 ** (-3))
    m = 9.28 * (10 ** (-3))
    l1 = 220.0 * (10 ** (-3))
    delta_l = 191.1 * (10 ** (-3))
    h1 = 120.0 * (10 ** (-3))
    h2 = 525.0 * (10 ** (-3))
    b = 22.00 * (10 ** (-3))
    d = 0.924 * (10 ** (-3))
    delta_x = 18.82 * (10 ** (-3))
    sigma_e_output = math.sqrt(
        (sigma_m / m) ** 2 +
        (sigma_b / b) ** 2 +
        (3 * sigma_d / d) ** 2 +
        (sigma_delta_x / delta_x) ** 2 +
        (2 * sigma_l1 / l1) ** 2 +
        5 * (sigma_h2 / (2 * h2 - h1)) ** 2 +
        2 * (sigma_delta_l / delta_l) ** 2
    )
    print("样品1 sigma_e / E =", sigma_e_output)
