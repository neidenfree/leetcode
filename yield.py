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
        return ListIterator(self)

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
                # print(el)
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
        return LinkedListIterator(self.head)


class LinkedListIterator:
    def __init__(self, head: ListNode):
        self.head = head

    def __next__(self):
        if self.head is not None:
            val = self.head.val
            self.head = self.head.link
            return val
        raise StopIteration


ll = LinkedList(list=[1, 2, 3, 4, 5])

for el in ll:
    print(el)
# print(ll)

# a = MyList(ar=[1, 2, 3, 4, 5])
# it = iter(a)
# for el in a:
#     print(el)
