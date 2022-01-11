from typing import Optional
from collections import deque


class StackNode:
    def __init__(self, a: int):
        self.value = a
        self.next = None


class Stack:
    def __init__(self):
        self.head: Optional[StackNode] = None
        self.__min: Optional[int] = None
        self.count: int = 0

    def __bool__(self) -> bool:
        return self.head is not None

    def push(self, a: int):
        temp = self.head
        new = StackNode(a)
        new.next = self.head
        if self.__min is None or self.__min > a:
            self.__min = a
        self.head: StackNode = new
        self.count += 1

    def min(self) -> int:
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


def main():
    a = Stack()
    a.push(23)
    a.push(22)
    a.push(51)
    a.push(11)
    a.push(21)
    b = sort_stack(a)

    print(a)
    print(b)


if __name__ == "__main__":
    main()
