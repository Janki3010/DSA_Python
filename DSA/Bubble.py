a = [16, 14, 6, 8, 5]
n = len(a)
f = 0
print("Original:", a)
for i in range(n):
    f = 0
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            f = 1
    if f == 0:
        break

print("Sorted:", a)
