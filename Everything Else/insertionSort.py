a = [int(x) for x in input().split()]
n = len(a)


def insertionSort(a, n):
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return print(a)


insertionSort(a, n)
