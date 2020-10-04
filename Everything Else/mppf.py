a = [int(x) for x in input().split()]
n = len(a)


def MaxPairwiseProductFast(a, n):
    index = 0

    for c in range(n):
        if a[c] > a[index]:
            index = c

    if index == 0:
        index2 = 1
    else:
        index2 = 0

    for c in range(n):
        if a[c] != a[index] and a[c] > a[index2]:
            index2 = c

    return print(a[index] * a[index2])


MaxPairwiseProductFast(a, n)
