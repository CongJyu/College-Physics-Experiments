# 虚拟仿真实验 GM 计数管

# from math import *
# import numpy


def main():
    # cal_slope()
    # count()


# 坪坡度
def cal_slope():
    n1 = float(input("n1 = "))
    n2 = float(input("n2 = "))
    v1 = float(input("v1 = "))
    v2 = float(input("v2 = "))
    slope = (n2 - n1) / ((n2 + n1 * (v2 - v1)) / 2) * 100
    print("坪坡度 =", slope, "%/伏")


# 本底计数
def count():
    cnt = [21, 18, 19, 21, 26]
    sum_up = 21 + 18 + 19 + 21 + 26
    ave = sum_up / 5
    print("平均计数率 =", ave / 1)
    # 标准误差
    standard_d = [cnt[0] - ave, cnt[1] - ave, cnt[2] - ave, cnt[3] - ave, cnt[4] - ave]
    print(standard_d)


# 主程序
if __name__ == "__main__":
    main()
