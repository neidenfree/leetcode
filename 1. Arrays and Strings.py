from time import time
import numpy as np


class HashTable:
    def __init__(self, array_len=1024):
        self.array = [0] * array_len

    def __getitem__(self, key):
        idx = hash(key) % len(self.array)
        return self.array[idx]

    def __contains__(self, key) -> bool:
        return self.array[hash(key) % len(self.array)] is not None

    def __setitem__(self, key, value) -> None:
        self.array[hash(key) % len(self.array)] = value

    def __delitem__(self, key):
        self.array[hash(key) % len(self.array)] = 0

    def __str__(self) -> str:
        result = "{"
        for i, el in enumerate(self.array):
            if el != 0:
                result += f"{i}: {el}, "
        result += "}"
        return result

    def __eq__(self, other):
        return self.array == other.array

    def add(self, key, value) -> None:
        idx = hash(key) % len(self.array)
        self.array[idx] = value


class MyString(str):
    def is_unique(self) -> bool:
        if not self:
            return False
        if len(self) == 1:
            return True
        if len(self) == 2:
            return self[0] != self[1]

        values = {}
        for c in self:
            if c in values:
                return False
            values[c] = 1
        return True

    def is_permutation(self, other: str) -> bool:
        if len(self) != len(other):
            return False
        if len(other) == 1:
            return True
        h1 = HashTable(2048)
        h2 = HashTable(2048)
        for i in range(len(self)):
            h1[self[i]] += 1
            h2[self[i]] += 1
        print(h1, h2)
        return h1 == h2


class ArrayList:
    def __init__(self, t: type, scaling_factor=2):
        self._ar: np.array = np.array([], dtype=t)
        self._count: int = 0
        self._type = t
        self._scaling_factor = scaling_factor

    def count(self):
        return self._count

    def add(self, element: object) -> None:
        if type(element) != self._type:
            try:
                element = self._type(element)
            except TypeError:
                raise TypeError(f"Can't add element of type {type(element)} to ArrayList of type {self._type}!")
        if self._count == 0:
            self._count = 1
            self._ar = np.array([element], dtype=self._type)
            return
        if self._count < len(self._ar):
            self._ar[self._count] = element
            self._count += 1
            return
        if self._count >= len(self._ar):
            temp = np.zeros((self._count * self._scaling_factor,), dtype=self._type)
            # temp = np.array([] * self._count * 2, dtype=type(element))
            for i in range(len(self._ar)):
                temp[i] = self._ar[i]
            temp[self._count] = element
            self._ar = temp
            self._count += 1
            return

    def __str__(self) -> str:
        result = "["
        for i in range(self._count - 1):
            result += str(self._ar[i]) + ', '
        result += str(self._ar[self._count - 1]) + ']'
        return result

    def index_exceptions(self, key: int) -> None:
        if key < 0:
            raise IndexError("Index can't be less than zero!")
        if key > self._count:
            raise IndexError(f"Index '{key}' is out of bounds for ArrayList with length '{self._count}'")

    def __setitem__(self, key: int, value) -> None:
        self.index_exceptions(key)
        self._ar[key] = value

    def __getitem__(self, key: int) -> object:
        self.index_exceptions(key)
        return self._ar[key]

    def for_each(self, f) -> None:
        """

        :type f: lambda
        """
        for i in range(self._count):
            f(self._ar[i])

    def modify_each(self, f) -> None:
        """

        :type f: lambda
        """
        for i in range(self._count):
            self._ar[i] = f(self._ar[i])


def test_array_vs_hashtable(n=100000):
    b = list(range(1024))
    a = HashTable(array_len=1024)
    a[1] = "One"
    a[4] = "Two"
    a[1023] = "Three"

    element_to_find = 1023

    start = time()
    for _ in range(n):
        if element_to_find in b:
            pass
    print(f'For array it is {time() - start} seconds')

    start = time()
    for _ in range(n):
        if element_to_find in a:
            pass
    print(f'For HashTable it is {time() - start} seconds')

    c = {1: "One", 4: "Two", 1023: "Three"}

    start = time()
    for _ in range(n):
        if element_to_find in c:
            pass
    print(f'For default python dict it is {time() - start} seconds')


def test_arraylist_vs_array(n=10000):
    """
    Tests default Python  list vs my ArrayList.
    Looks like default Python list works much faster, though.
    I found an article, which describes the way Python lists implemented:
    http://www.laurentluce.com/posts/python-list-implementation/
    Looks like it's implemented
    :param n:
    :return:
    """
    start = time()
    ar = []
    for i in range(n):
        ar.append(i)
    print(f'For array it is {time() - start} seconds')

    start = time()
    al = ArrayList(t=int, scaling_factor=2)
    for i in range(n):
        al.add(i)
    print(f'For ArrayList it is {time() - start} seconds')


if __name__ == "__main__":

    test_arraylist_vs_array(1000000)
    # s = MyString("abcdef")
    # print(s.is_permutation("abcdef"))
    # al = ArrayList(t=int, scaling_factor=3)
    # al.add(1.2)
    # al.add(2.2)
    # # al.add("3.")
    # al.add(4.1)
    # al.add(5)
    #
    # print(al)
    # # al.modify_each(lambda x: x ** 2)
    # print(al)

    # al.add(8)

    # print(s.is_unique())
