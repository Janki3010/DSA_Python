# a = [2, 1, 1, 0, 2, 5, 4, 0, 2, 8, 7, 7, 9, 2, 0, 1, 9]
# b = [0] * len(a)
# count = [0] * (max(a) + 1)
#
# for num in a:
#     count[num] += 1
# print("Count occurrences:", count)
#
# for i in range(1, len(count)):
#     count[i] += count[i - 1]
# print("Cumulative counts:", count)
#
# for i in range(len(a) - 1, -1, -1):
#     b[count[a[i]] - 1] = a[i]
#     count[a[i]] -= 1
# print("Sorted array:", b)


a = [2, 1, 1, 0, 2, 5, 4, 0, 2, 8, 7, 7, 9, 2, 0, 1, 9]
b = [0] * len(a)
count = []

for i in range(max(a) + 1):
    count.append(0)

for i in range(len(a)):
    count[a[i]] += 1
print(count)

for i in range(1, len(count)):
    count[i] = count[i] + count[i - 1]
print(count)

for i in range(len(a)-1, -1, -1):
    b[count[a[i]] - 1] = a[i]
    count[a[i]] -= 1

a = b
print(a)

