s = 'Hello'
stack = []
for i in s:
    stack.append(i)
print(stack)
l2 = []
for i in range(len(stack)):
    l2.append(stack.pop())
print(l2)
