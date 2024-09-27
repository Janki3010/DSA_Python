"""
Question 1: Removing Duplicate Values from a List
Remove duplicate values from the list [1, 2, 3, 3, 4, 5, 6, 4] without using any built-in functions like set().
"""

l1 = [1, 2, 3, 3, 4, 5, 6, 4]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
l1 = l2
print(l1)

"""
Question 2: Recursive Sum of List Elements
Compute the sum of all elements in the list [15, 19, 39, 61, 2, 74] using recursion, without using any built-in functions or constructs other than recursion.
"""

list1 = [15, 19, 39, 61, 2, 74]


def sum(list1):
    if not list1:
        return 0
    return list1[0] + sum(list1[1:])


print(sum(list1))

# def sum(list1):
#     s = 0
#     for i in list1:
#         s += i
#     return s
#
#
# print(sum(list1))

"""
Question 3: Calculating the Average
Calculate the average of the numbers in the list [50, 25, 46, 78, 64, 22] without using the len() function.
"""
list1 = [50, 25, 46, 78, 64, 22]


def findAvg(list1):
    count = 0
    s = 0
    for i in list1:
        count += 1
        s += i
    return s / count


print(findAvg(list1))

"""Question 4: Palindrome Checking Without Slicing or Built-in Reverse
Check if a given string is a palindrome without using slicing or the built-in reverse() function.
"""
str1 = "aabbaa"


def palindrome(str1):
    l1 = list(str1)
    l2 = []
    for s in range(len(l1) - 1, -1, -1):
        l2.append(l1[s])
    if l1 == l2:
        print('Yes')
    else:
        print('No')


palindrome(str1)

