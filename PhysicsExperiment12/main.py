# encoding utf-8
# physics experiment 12

import statistics
import math

# 平均值 s - s0
s_ave = (1.20 + 0.45 + 0.91 + 1.00 + 0.90) / 5
print("平均值 s - s0 係：", s_ave)

# alpha = m0g(s - s0) / (sl delta_l)
m0 = 0.5
g = 9.8
ll = 5.20
slope = 0.64

alpha = (m0 * g * s_ave) / (2 * ll * slope)
print("alpha 嘅值係：", alpha)

# 求標準差 sigma
delta_l_dataset = [
    0.79 - 0,
    1.23 - 0.79,
    1.90 - 1.23,
    2.55 - 1.90,
    3.28 - 2.55,
    4.00 - 3.28,
    4.62 - 4.00,
    5.11 - 4.62,
    5.68 - 5.11
]
sigma_delta_l = statistics.stdev(delta_l_dataset)
print("delta l 嘅標準差係：", sigma_delta_l)

s_s0_dataset = [1.20, 0.45, 0.91, 1.00, 0.90]
sigma_s_s0 = statistics.stdev(s_s0_dataset)
print("s - s0 嘅標準差係：", sigma_s_s0)

# 求 E alpha
e_alpha = math.sqrt((0.27 / 0.892) ** 2 + 0 + (0.11 / 0.64) ** 2)
print("E_alpha 係：", e_alpha / 100, "%")

sigma_alpha = 0.66 * e_alpha
print("sigma_alpha =", 0.66 * e_alpha / 100)

print("====結果====")
print("alpha =", 0.66 + 0.66 * e_alpha / 100, 0.66 - 0.66 * e_alpha / 100)
print("E_alpha =", e_alpha)
