class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None

    def create(self, data):
        newnode = Node(data)

        if self.head == None:
            self.head = self.temp = newnode
        else:
            self.temp.next = newnode
            self.temp = newnode

    def insertAtFirst(self, data):
        newnode = Node(data)

        newnode.next = self.head
        self.head = newnode

    def insertAtLast(self, data):
        newnode = Node(data)

        self.temp.next = newnode
        self.temp = newnode

    def insertAtPos(self, pos, data):
        newnode = Node(data)
        if pos == 0:
            newnode.next = self.head
            self.head = newnode
            return

        temp = self.head
        count = 1
        while count < pos - 1:
            temp = temp.next
            count += 1
        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1

        newnode.next = temp.next
        temp.next = newnode
        if temp is None:
            print("Position out of bounds.")
            return

    def afterPos(self, pos, data):
        newnode = Node(data)
        temp = self.head
        count = 0
        while count < pos - 1:
            temp = temp.next
            count += 1
        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1

        newnode.next = temp.next
        temp.next = newnode

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next
        print()


n1 = LinkedList()
n1.create(10)
n1.create(11)
n1.create(20)
n1.insertAtFirst(5)
n1.insertAtFirst(3)
n1.insertAtLast(25)
n1.insertAtLast(33)
n1.insertAtPos(2, 4)
n1.insertAtPos(5, 15)
n1.afterPos(6, 12)
n1.display()
print(n1.temp.value)
