class Stack:
    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        self.item.pop()

    def peek(self):
        print(self.item[-1])

    def display(self):
        for i in self.item:
            print(i)

    def stackLen(self):
        print(len(self.item))

s1 = Stack()
s1.push(10)
s1.push(7)
s1.push(5)
s1.push(3)
print("Peek element is")
s1.peek()
print("Display:")
s1.display()
print("len of stack is")
s1.stackLen()
s1.pop()
print("After performing pop operation, display:")
s1.display()

# s = 'Hello'
# stack = []
# for i in s:
#     stack.append(i)
# print(stack)
# l2 = []
# for i in range(len(stack)):
#     l2.append(stack.pop())
# print(l2)
