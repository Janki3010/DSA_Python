a = [10, 15, 1, 2, 9, 16, 11]
lb = 0
ub = len(a) - 1
print("Original array:", a)


def partition(a, lb, ub):
    pivot = a[lb]
    start = lb + 1
    end = ub

    while start <= end:
        while start <= end and a[start] <= pivot:
            start += 1
        while start <= end and a[end] > pivot:
            end -= 1
        if start < end:
            a[start], a[end] = a[end], a[start]

    a[lb], a[end] = a[end], a[lb]

    return end


def quickSort(a, lb, ub):
    if lb < ub:
        loc = partition(a, lb, ub)
        quickSort(a, lb, loc - 1)
        quickSort(a, loc + 1, ub)


quickSort(a, lb, ub)

print("Sorted array:", a)
