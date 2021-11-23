import numpy as np
from time import time


class ArrayList:
    """
    An attempt to implement Java-like structure ArrayList,
    which doubles its size when one's trying to add element to
    full array.
    This trick is useful, because it brings O(1) amortized time complexity to
    appending elements while saving O(1) lookup time.
    """

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
            self._ar = np.array([element], dtype=self._type)
            self._count = 1
            return
        if self._count < len(self._ar):
            self._ar[self._count] = element
            self._count += 1
            return
        if self._count >= len(self._ar):
            temp = np.zeros((self._count * self._scaling_factor,), dtype=self._type)
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


def test_arraylist_vs_array(n=10000):
    """
    Tests default Python  list vs my ArrayList.
    Looks like default Python list works much faster, though.
    I found an article, which describes the way Python lists implemented:
    https://www.laurentluce.com/posts/python-list-implementation/
    Looks like it's implemented
    :param n:
    :return:
    """
    start = time()
    ar = []
    for i in range(n):
        ar.append(i)
    print(f'For array it is {time() - start} seconds')

    al = ArrayList(t=int, scaling_factor=2)
    start = time()
    for i in range(n):
        al.add(i)
    print(f'For ArrayList it is {time() - start} seconds')
