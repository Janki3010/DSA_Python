a = [432, 8, 530, 90, 88, 231, 11, 45, 677, 199]
count = [0] * 9
n = len(a)


def redixSort(a, n):
    pos = 1
    for pos in ((max(a) / pos) > 0):
        pos *= 10
        print(pos)

redixSort(a, n)
# # a = []
# # for i in range(11):
# #     a.append(int(input()))
# # print(a)
#
#
# def counting_sort(a1, exp):
#     """
#     A function to perform counting sort based on a specific digit (exp - exponent).
#     """
#     n = len(a1)
#     output = [0] * n  # Output array
#     count = [0] * 10  # Count array for digits 0 to 9
#
#     # Store count of occurrences of each digit in the count array
#     for i in range(n):
#         index = a1[i] // exp
#         count[index % 10] += 1
#
#     # Change count[i] so that it contains the actual position of this digit in output[]
#     for i in range(1, 10):
#         count[i] += count[i - 1]
#
#     # Build the output array using the count array
#     i = n - 1
#     while i >= 0:
#         index = a1[i] // exp
#         output[count[index % 10] - 1] = a1[i]
#         count[index % 10] -= 1
#         i -= 1
#
#     # Copy the sorted numbers into the original array
#     for i in range(n):
#         a1[i] = output[i]
#
#
# def radix_sort(a1):
#     """
#     Main function to perform radix sort.
#     """
#     # Find the maximum number to determine the number of digits
#     max_num = max(a1)
#
#     # Perform counting sort for each digit
#     exp = 1
#     while max_num // exp > 0:
#         counting_sort(a1, exp)
#         exp *= 10
#
#
# # Example usage
# a1 = [170, 45, 75, 90, 802, 24, 2, 66]
# print("Original array:", a1)
# radix_sort(a1)
# print("Sorted array:", a1)
