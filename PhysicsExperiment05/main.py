# 实验五 非线性元件伏安特性的测定

from math import *

h = 6.6260
e = 1.6021
c = 2.9979


def main():
    u_red = float(input())
    u_blue = float(input())
    u_yellow = float(input())
    get_lambda(u_red, "red")
    get_lambda(u_blue, "blue")
    get_lambda(u_yellow, "yellow")


def get_lambda(u, s):
    result = (h * c) / (e * u)
    print(s, result)


if __name__ == "__main__":
    main()
