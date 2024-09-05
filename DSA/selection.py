a = [4, 2, 10, 5, 7, 6]
n = len(a)
print("Original:", a)
for i in range(0, n - 1):
    min = i

    for j in range(i + 1, n):
        if a[j] < a[min]:
            min = j

    if min != i:
        a[i], a[min] = a[min], a[i]

print("Sorted:", a)

