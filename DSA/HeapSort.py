

A = [15, 5, 20, 1, 17, 10, 30]


def MaxHeapify(A, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and A[l] > A[largest]:
        largest = l

    if r < n and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        MaxHeapify(A, n, largest)

    return A


def HeapSort(A):
    n = len(A)

    for i in range(n // 2 - 1, -1, -1):
        MaxHeapify(A, n, i)

    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        MaxHeapify(A, i, 0)

    return A

