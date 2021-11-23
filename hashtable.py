from time import time


class HashTable:
    def __init__(self, array_len=1024):
        self.array = [0] * array_len
        self.keys = []

    def __getitem__(self, key):
        idx = hash(key) % len(self.array)
        return self.array[idx]

    def __contains__(self, key) -> bool:
        return self.array[hash(key) % len(self.array)] is not None

    def __setitem__(self, key, value) -> None:
        self.keys.append(key)
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
