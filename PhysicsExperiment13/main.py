# encoding utf-8
# physics experiment 13

velocity = [
    0.0053,
    0.0062,
    0.0064,
    0.0085,
    0.0187,
    0.0279,
    0.0335
]

ita = [
    0, 0, 0, 0, 0, 0, 0
]

ita1 = [
    0, 0, 0, 0, 0, 0, 0
]

row = 7800
row0 = 950
D = 0.02
g = 9.8
d = 0.993

print("====ita====")
for i in range(7):
    ita[i - 1] = ((row - row0) * g * (d * 10 ** (-3)) ** 2) / (18 * velocity[i - 1])
    print(ita[i - 1])

print("====ita1====")
for i in range(7):
    ita1[i - 1] = ((row - row0) * g * (d * 10 ** (-3)) ** 2) / (18 * velocity[i - 1] * (1 + 2.4 * d / D))
    print(ita1[i - 1])
