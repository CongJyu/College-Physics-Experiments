# encoding utf-8
# physics experiment 19

x1 = [6.350, 6.350, 6.300, 6.550, 6.545]
xn = [2.745, 2.790, 2.750, 2.960, 2.950]
x1_prime = [2.650, 2.710, 2.700, 2.990, 2.980]
xn_prime = [6.340, 6.365, 6.390, 6.590, 6.575]
delta_x = [0.0, 0.0, 0.0, 0.0, 0.0]
n = 5


def main():
    for i in range(5):
        delta_x[i - 1] = (abs(xn[i - 1] - x1[i - 1]) + abs(xn_prime[i - 1] - x1_prime[i - 1])) / (2 * (n - 1))
    print(delta_x)


def average():
    sum_up_x = 0
    for i in range(5):
        sum_up_x += delta_x[i - 1]
    print(sum_up_x / 5)


if __name__ == "__main__":
    main()
    average()
