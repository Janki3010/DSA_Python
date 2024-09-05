a = [1, 4, 7, 2, 5, 9, 2, 4, 1, 3, 7, 5]
n = len(a)
f = 0
print("Original:", a)
for i in range(n):
    f = 0
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            f = 1
    if f == 0:
        break

print("Sorted:", a)
