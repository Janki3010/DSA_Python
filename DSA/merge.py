a = [7, 15, 2, 8, 10, 20, 5]
low = 0
high = len(a) - 1
print("Original:", a)


def merge(a, mid, low, high):
    b = [0] * len(a)
    i = low
    j = mid + 1
    k = low
    while i <= mid and j <= high:
        if a[i] < a[j]:
            b[k] = a[i]
            i += 1
            k += 1
        else:
            b[k] = a[j]
            j += 1
            k += 1

    while i <= mid:
        b[k] = a[i]
        k += 1
        i += 1

    while j <= high:
        b[k] = a[j]
        k += 1
        j += 1

    for i in range(low, high+1):
        a[i] = b[i]


def MS(a, low, high):
    if low < high:
        mid = (low + high) // 2
        MS(a, low, mid)
        MS(a, mid + 1, high)
        merge(a, mid, low, high)


MS(a, low, high)
print("Sorted:", a)
