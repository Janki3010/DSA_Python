a = [7, 2, 4, 9, 3, 10]
n = len(a)
print("Original", a)
for i in range(1, n):
    temp = a[i]
    j = i - 1
    while j >= 0 and a[j] > temp:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = temp

print("Sorted:", a)
