a = [10, 20, 30, 40, 50]
n = len(a)

print(a)

data = int(input("Search Value:"))

def binarySearch(a, n, data):
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if data == a[mid]:
            return mid
        elif data > a[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1

result = binarySearch(a, n, data)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found in the list.")