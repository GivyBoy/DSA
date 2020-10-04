def FibList(n):
    a = [0, 1]
    for i in range(2, n+1):
        a.append(None)
        a[i] = a[i - 1] + a[i - 2]

    return a[n]


print(FibList(3))