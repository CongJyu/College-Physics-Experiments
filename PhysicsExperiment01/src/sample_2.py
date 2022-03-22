import math
import numpy as npy


def sample_2_d():
    ave_d = (1 / 5) * (1.920 + 1.921 + 1.919 + 1.915 + 1.918)
    print("样品2 悬梁臂平均厚度：", ave_d)


def sample_2_d_std():
    data = npy.array([1.920, 1.921, 1.919, 1.915, 1.918])
    std_output = npy.std(data, ddof=1)
    print("样品2 悬梁臂厚度标准差：", std_output)


def sample_2_e():
    m = 9.28 * (10 ** (-3))
    g = 9.79
    l1 = 215.0 * (10 ** (-3))
    l2 = 235.0 * (10 ** (-3))
    delta_l = 187.5 * (10 ** (-3))
    h1 = 110.0 * (10 ** (-3))
    h2 = 573.0 * (10 ** (-3))
    delta_h = 225.0 * (10 ** (-3))
    a = 22.00 * (10 ** (-3))
    b = 22.00 * (10 ** (-3))
    d = 1.918 * (10 ** (-3))
    delta_x = 6.48 * (10 ** (-3))
    part_1 = (12 * m * g) * ((l1 - (a / 2)) ** 2) / (b * d ** 3 * delta_x)
    part_2 = (2 * h2 - h1) * (1 + (delta_l / delta_h) ** 2) - (l2 - (1 / 3) * (l1 - (a / 2))) * (delta_l / delta_h)
    result_e = part_1 * part_2
    print("样品2 E =", result_e)


def sample_2_sigma_e():
    sigma_m = 0.02 * (10 ** (-3))
    sigma_l1 = 0.3 * (10 ** (-3))
    sigma_b = 0.02 * (10 ** (-3))
    sigma_h2 = 0.3 * (10 ** (-3))
    sigma_delta_l = 0.3 * (10 ** (-3))
    sigma_d = 0.002 * (10 ** (-3))
    sigma_delta_x = 0.74 * (10 ** (-3))
    m = 9.28 * (10 ** (-3))
    l1 = 215.0 * (10 ** (-3))
    delta_l = 187.5 * (10 ** (-3))
    h1 = 110.0 * (10 ** (-3))
    h2 = 573.0 * (10 ** (-3))
    b = 22.00 * (10 ** (-3))
    d = 1.918 * (10 ** (-3))
    delta_x = 6.48 * (10 ** (-3))
    sigma_e_output = math.sqrt(
        (sigma_m / m) ** 2 +
        (sigma_b / b) ** 2 +
        (3 * sigma_d / d) ** 2 +
        (sigma_delta_x / delta_x) ** 2 +
        (2 * sigma_l1 / l1) ** 2 +
        5 * (sigma_h2 / (2 * h2 - h1)) ** 2 +
        2 * (sigma_delta_l / delta_l) ** 2
    )
    print("样品2 sigma_e / E =", sigma_e_output)
