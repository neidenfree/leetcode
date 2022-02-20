class PowTwo:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


class MyList:
    def __init__(self, *args, **kwargs):
        if 'ar' in kwargs:
            self._ar = kwargs['ar']
        else:
            self._ar = []
        self.iter_index = 0

    def add(self, val: object):
        self._ar.append(val)

    def __iter__(self):
        for element in self._ar:
            yield element

    def __len__(self):
        return len(self._ar)

    def __getitem__(self, item: int) -> object:
        try:
            item = int(item)
        except:
            raise TypeError("Index is not int!")

        if item < len(self):
            return self._ar[item]
        raise IndexError


class ListIterator:
    def __init__(self, my_list):
        self.list = my_list
        self._index = 0

    def __next__(self):
        if self._index < len(self.list):
            result = self.list[self._index]
            self._index += 1
            return result
        raise StopIteration


class ListNode:
    def __init__(self, val: object, link=None):
        self.val = val
        self.link = link


class LinkedList:

    def __init__(self, **kwargs):
        self.head = None
        self.count = 0

        if 'list' in kwargs:
            for el in reversed(kwargs['list']):
                self.push(el)

    def push(self, obj: object):
        new = ListNode(obj)
        new.link = self.head
        self.head = new
        self.count += 1

    def __str__(self) -> str:
        temp: ListNode = self.head
        res = ""
        while temp is not None:
            res += f"{temp.val}"
            if temp.link is not None:
                res += " -> "
            temp = temp.link
        return res

    def __iter__(self):
        temp = self.head
        while temp is not None:
            res = temp.val
            temp = temp.link
            yield res

        # return LinkedListIterator(self.head)


class LinkedListIterator:
    def __init__(self, head: ListNode):
        self.head = head

    def __next__(self):
        if self.head is not None:
            val = self.head.val
            self.head = self.head.link
            return val
        raise StopIteration


def some(n: int):
    print(f'{n} in some func')
    yield n + 1


def rev_str(string: str) -> str:
    for c in reversed(string):
        yield c


class Range:
    def __init__(self, start: int, end: int, step: int = 1):
        self.start = start
        self.end = end
        self.step = step
        self.index = start

    def __iter__(self):
        return RangeIterator(self.start, self.end, self.step)


class RangeIterator:
    def __init__(self, start: int, end: int, step: int = 1):
        self.start = start
        self.end = end
        self.step = step
        self.index = start

    def __next__(self):
        if self.index < self.end:
            res = self.index
            self.index += self.step
            return res
        raise StopIteration


if __name__ == "__main__":

    pass

# for i in range(5):
#     some(i)
# a = some(5)
# for i in some(5):
#     print(i)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
