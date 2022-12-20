# 实验四 用分光计测量三棱镜折射率

from math import *

# 数据
pi = 3.1415
alpha = 60 / 360 * pi
delta_m = 51.2 / 360 * pi

# 计算折射率
if __name__ == "__main__":
    n = sin((alpha + delta_m) / 2) / sin(alpha / 2)
    print("三棱镜的折射率为", n)
