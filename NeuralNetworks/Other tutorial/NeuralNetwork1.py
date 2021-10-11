import numpy


def sig(x):
    return 1 / (1 + numpy.exp(-x))


def cost(pred, target):
    return (pred - target) ** 2


def slope(pred, target):
    return 2 * (pred - target)


def NN(m1, m2, w1, w2, b):
    z = m1 * w1 + m2 * w2 + b
    return sig(z)


w1 = 1.9992966235891343
w2 = -0.45172038438005807
b = -1.3093042647461088
print(b)

for i in range(10):
    b = b - 0.45 * slope(b, 10)
    print(b)
