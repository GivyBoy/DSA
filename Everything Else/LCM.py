def EuclidGCD(a, b):
    if b == 0:
        return a
    a1 = a % b
    return EuclidGCD(b, a1)


def LCM(a, b):
    return int((a * b) / EuclidGCD(a, b))


print(LCM(6, 12))
