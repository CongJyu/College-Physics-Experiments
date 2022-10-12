# encoding utf-8
# physics experiment 12

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
