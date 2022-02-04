from typing import Optional
from collections import deque


class StackNode:
    def __init__(self, a: object):
        self.value: object = a
        self.next = None


class Stack:
    def __init__(self):
        self.head: Optional[StackNode] = None
        self.__min: Optional[int] = None
        self.count: int = 0

    def __bool__(self) -> bool:
        return self.head is not None

    def peek(self):
        if self.head is not None:
            return self.head.value
        return None

    def push(self, a: object):
        temp = self.head
        new = StackNode(a)
        new.next = self.head
        if self.__min is None or self.__min > a:
            self.__min = a
        self.head: StackNode = new
        self.count += 1

    def min(self) -> object:
        return self.__min

    def find_min(self) -> Optional[int]:
        if not self:
            return None
        m = self.head.value
        temp = self.head
        while temp is not None:
            if m < temp.value:
                m = temp.value
            temp = temp.next
        return m

    def pop(self) -> Optional[int]:
        if self.head is None:
            raise IndexError("Stack is shorter than you expect")
        temp = self.head
        self.head = self.head.next
        self.count -= 1
        return temp.value

    def __len__(self):
        return self.count

    def __str__(self) -> str:
        temp: StackNode = self.head
        res = ""
        while temp is not None:
            res += f"{temp.value}"
            if temp.next is not None:
                res += " -> "
            temp = temp.next
        return res

    def remove_by_value(self, value: int) -> None:
        temp = self.head
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        while temp.next is not None:
            if temp.next.value == value:
                temp.next = temp.next.next
                return
            temp = temp.next

    def copy(self):
        if self.head is None:
            return None
        temp = self.head
        result = Stack()
        while temp is not None:
            result.push(temp.value)
            temp = temp.next
        return result

    def is_palindrome(self) -> bool:
        if self.head is None:
            return True
        new_s = Stack()
        temp = self.head
        while temp is not None:
            new_s.push(temp.value)
            temp = temp.next
        temp = self.head
        temp2 = new_s.head
        while temp is not None:
            if temp.value != temp2.value:
                return False
            temp = temp.next
            temp2 = temp2.next
        return True


class Queue:
    def __init__(self):
        self.head: Optional[StackNode] = None
        self.count: int = 0

    def push(self, a: object) -> None:
        if self.head is None:
            self.head = StackNode(a)
            return None
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = StackNode(a)
        self.count += 1

    def pop(self) -> Optional[object]:
        if self.head is None:
            return None
        temp = self.head.value
        self.head = self.head.next
        self.count -= 1
        return temp

    def __str__(self):
        temp: StackNode = self.head
        s: str = ''
        while temp is not None:
            s += f"{temp.value} => "
            temp = temp.next
        s += 'null'
        return s


class NumberQueue(Queue):
    def mean(self) -> float:
        temp = self.head
        res = 0
        while temp is not None:
            res += temp.value
            temp = temp.next
        return res / self.count

    def __init__(self):
        super(NumberQueue, self).__init__()
        self.max = None
        self.min = None

    def push(self, a: float) -> None:
        if not self.max:
            self.max = a
            self.min = a
        if a > self.max:
            self.max = a
        if a < self.min:
            self.min = a
        super(NumberQueue, self).push(a)

    # def max(self):
    #
    # def min(self):


class MyQueue(Stack):
    # def push(self, a: object) -> None:
    #     s = Stack()
    #     temp = self.head
    #     while temp is not None:
    #         s.push(temp.value)
    #         temp = temp.next
    #     s.push(a)
    #     self.head = s.head

    def __str__(self):
        temp = self.head
        s = Stack()
        while temp is not None:
            s.push(temp.value)
            temp = temp.next

        return str(s)


def test_stack_queue():
    a = MyQueue()
    a.push(1)
    a.push(2)
    # a.push(3)
    # a.push(4)
    a.push(5)
    a.pop()
    print(a)


def test_palindrome():
    a = Stack()
    a.push(1);
    a.push(2);
    a.push(2);
    a.push(2)
    assert not a.is_palindrome()
    a.push(1)
    assert a.is_palindrome()


def test_queue():
    q = NumberQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)
    # q.pop()
    # q.pop()
    # q.pop()

    print(q)
    print(q.mean())


def sort_stack(s: Stack):
    if s.head is None:
        return None
    new_s = s.copy()
    result = Stack()
    while new_s:
        m = new_s.find_min()
        new_s.remove_by_value(m)
        result.push(m)
    return result


class SetOfStacks:
    """
        Implement a set of stacks with maximum number of elements in each stack.
        Notice, that methods SetOfStacks.push() and SetOfStacks.pop() must behave
        identically to a single stack.
    """

    def __init__(self, max_elem: int):
        self.max_elem = max_elem
        self.set: list[Stack] = [Stack()]
        self.current_set = 0

    def __bool__(self):
        return bool(self.set[0])

    def push(self, a: int) -> None:
        self.set[self.current_set].push(a)
        if len(self.set[self.current_set]) == self.max_elem:
            self.set.append(Stack())
            self.current_set += 1

    def pop(self) -> int:
        if not self:
            raise IndexError

        if len(self.set[self.current_set]) == 0:
            self.current_set -= 1
        temp: int = self.set[self.current_set].pop()
        return temp


def set_of_stacks_test():
    a = SetOfStacks(max_elem=6)
    print(bool(a))
    for i in range(100):
        a.push(i)

    print(a.pop())
    print(a.pop())
    print(a.pop())


class Solution:
    def valid_parentheses(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return False
        par = {'{': '}', '[': ']', '(': ')'}
        opening = '{[('
        closing = '}])'
        st = Stack()

        for c in s:
            # First, handle the case when string starts with opening bracket
            if st.head is None and c in closing:
                return False
            if st.peek() and st.peek() in opening and c == par[st.peek()]:
                st.pop()
            else:
                st.push(c)
        return len(st) == 0


def test_valid_parentheses():
    a = Solution()
    assert not a.valid_parentheses('}{{}}')
    assert a.valid_parentheses('{{[]}}')
    assert not a.valid_parentheses('{{[(]}}')
    assert a.valid_parentheses('{{}}')


def main():
    test_stack_queue()


if __name__ == "__main__":
    main()
