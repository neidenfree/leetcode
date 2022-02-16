from typing import Optional


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


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast = head
        slow = head
        while fast is not None:
            if fast.next is None:
                break
            fast = fast.next.next
            if fast == slow:
                return True
            slow = slow.next

        return False

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        vals = {}
        temp = head
        while temp is not None:
            if temp in vals:
                return temp
            else:
                vals[temp] = 1
                temp = temp.next
        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        vals = {}
        temp = headA
        while temp is not None:
            vals[temp] = 1
            temp = temp.next
        temp = headB
        while temp is not None:
            if temp in vals:
                return temp
            temp = temp.next
        return None

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        temp = head
        for i in range(n):
            if not temp:
                return head
            temp = temp.next
        fast = temp
        slow = head
        if temp is None:
            head = head.next
            return head
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        if slow.next:
            slow.next = slow.next.next
        else:
            slow.next = None
        return head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        dummy = None
        while temp is not None:
            one = temp.next
            temp.next = dummy
            dummy = temp
            temp = one
        return dummy

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        temp = head
        while temp and temp.val == val:
            temp = temp.next
        head = temp
        if temp is None:
            return None
        while temp.next is not None:
            if temp.next and temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:





def test_remove():
    h1 = ListNode(3)
    h2 = ListNode(1)
    h3 = ListNode(1)
    h4 = ListNode(1)
    h5 = ListNode(3)
    h1.next = h2
    h2.next = h3
    h3.next = h4
    h4.next = h5
    sol = Solution()
    res = sol.removeElements(h1, 3)
    print('thats is')


def test_reverse():
    h1 = ListNode(1)
    h2 = ListNode(2)
    # h3 = ListNode(3)
    # h4 = ListNode(4)
    # h5 = ListNode(5)
    h1.next = h2
    # h2.next = h3
    # h3.next = h4
    # h4.next = h5
    sol = Solution()
    res = sol.reverseList(h1)
    print('thats it')


def test_cycle():
    h1 = ListNode(1)
    h2 = ListNode(2)
    h3 = ListNode(3)
    h4 = ListNode(4)
    h5 = ListNode(5)
    h1.next = h2
    h2.next = h3
    h3.next = h4
    h4.next = h5
    sol = Solution()
    res = sol.reverseList(h1)

    print('is done')

    # assert not sol.hasCycle(h3)


if __name__ == "__main__":
    test_remove()

    # a = {}
    # a[1] = 2
    # a[2] = 3
    # a[3] = 4
    # for el in a:
    #     print(a[el])
