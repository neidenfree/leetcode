class Node:
    def __init__(self, val: int, next=None, prev=None):
        self.val: int = val
        self.next: Node = next
        self.prev: Node = prev

    def __str__(self):
        return str(self.val)


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count: int = 0

    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        if index < self.count:
            # Here are the moment, where we can optimize.
            # We can check if index is closer to head or tail. And then go from head or tail.
            # This simple trick can save some time for performance.
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.count += 1
        if self.head is None:
            node = Node(val, None, None)
            self.head = node
            self.tail = node
        else:
            node = Node(val, self.head, None)
            self.head.prev = node
            self.head = node

    def addAtTail(self, val: int) -> None:
        self.count += 1
        if self.tail is None:
            node = Node(val, None, None)
            self.head = node
            self.tail = node
        else:
            node = Node(val, None, self.tail)
            self.tail.next = node
            self.tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return None
        if index == 0:
            self.addAtHead(val)
            return None
        if index == self.count:
            self.addAtTail(val)
            return None

        self.count += 1
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
        node = Node(val, temp.next, temp)
        temp.next.prev = node
        temp.next = node

    def popHead(self):
        if self.head is None:
            return None
        self.count -= 1
        value = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return value

    def popTail(self):
        if self.tail is None:
            return None
        self.count -= 1
        value = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return value

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.count:
            return None
        if index == 0:
            self.popHead()
            return None
        if index + 1 == self.count:
            self.popTail()
            return None
        self.count -= 1
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
        temp.next = temp.next.next
        temp.next.prev = temp

    def __str__(self):
        r = '['
        temp = self.head
        while temp is not None:
            r += str(temp.val)
            if temp.next:
                r += ', '

            temp = temp.next
        r += ']'
        return r


if __name__ == "__main__":
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(2)
    obj.addAtTail(3)
    # obj.deleteAtIndex(1)
    obj.addAtIndex(3, 10)

    # print(obj.get(3))
    # obj.deleteAtIndex(4)
    # print(obj.get(1))
    print(obj)

    a = 200
