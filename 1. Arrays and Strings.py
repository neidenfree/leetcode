from __future__ import annotations

import random
from time import time
import numpy as np


# Data Structutres implementation

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


class StringBuilder:
    """
        Actually, I wanted to implements two constructors. The first one was planned to be implemented like
        def __init__(self, s: str):
            self._ar = [s]
        But Python doesn't support multiple constructors, it just uses the last implemented one.
        All stuff that supposed to be in multiple constructors needs to be implemented using
        *args, **krargs and that kind of crap.
    """

    def __init__(self):
        self._ar = []

    def add(self, s: str):
        self._ar.append(s)

    def __str__(self):
        return ''.join(self._ar)

    def __len__(self):
        return len(self._ar)

    def last_item(self):
        return self._ar[-1]


# Data Structures test cases

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

    al = ArrayList(t=int, scaling_factor=2)
    start = time()
    for i in range(n):
        al.add(i)
    print(f'For ArrayList it is {time() - start} seconds')


def test_string_concat_vs_stringbuilder(n=100000, concat_string="abcdef") -> None:
    """
    Tests default Python string concatenation vs custom StringBulider implementation.
    It turns out, that for 3000000 iterations of concatenations of "abcdefg" string it takes
        For default str it is 11.217000007629395 seconds
        For StringBuilder str it is 0.612999677658081 seconds
    which gives us 18 times performance improvement!
    But it needs to be said that for approximately n < 50000 default string concatenation beats StringBuilder.


    :param n: int amount of strings to concatenate
    :param concat_string: str string to concatenate for n times
    :return: None
    """

    start = time()
    python_string = ""

    for _ in range(n):
        python_string += concat_string
    print(f'For default str it is {time() - start} seconds')

    start = time()
    sb = StringBuilder()
    for _ in range(n):
        sb.add(concat_string)
    custom_string = str(sb)
    print(f'For StringBuilder str it is {time() - start} seconds')

    assert custom_string == python_string, "Warning! Strings are not equal!!!"


# Interview Questions implementations using above data structures

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

    def urlify(self) -> str:
        sb = StringBuilder()
        for c in self:
            if c != " ":
                sb.add(c)
            else:
                if sb.last_item() != '%20':
                    sb.add('%20')
        return str(sb)

    def urlify_in_place(self) -> None:
        """
        Can't get with a solution immediately, but i'm sure that there is one.
        :return:
        """
        # TODO: implement URLIFY in place

        pass

    def palindrome_permutation(self) -> bool:
        """
        Given a string, write a function to check if it is a permutation of a palindrome.
        A palindrome is a word or phrase that is the same forwards and backwards.
        A permutation is a rearrangement of letters.

        Answer. It's quite a simple problem. At first, palindrome has a property, that is
        a key to this task: if it's length is an odd number, that every letter of a word
        must be an even number, except one letter that can be present only odd number of times.

        :return: bool
        """
        if len(self) < 3:
            return True
        ht = HashTable()
        for elem in self:
            ht[elem] += 1
        if len(self) % 2 == 0:
            for elem in ht.keys:
                if ht[elem] % 2 != 0:
                    return False
        else:
            odd_chars = 0
            for elem in ht.keys:
                if ht[elem] % 2 != 0:
                    if odd_chars == 1:
                        return False
                    else:
                        odd_chars += 1

        return True

    def compress(self) -> str:
        """
        Implement a method to perform basic string compression using the counts of repeated characters.
        For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become
        smaller than the original string, your method should return the original string.

        Straightforward solution. At first, let's see if the length of the given string is less than 3. If it's true,
        return the original string. For example, if given string is aa, method must return a2, which is no shorter
        than original string.

        Optimal solution. We can use stringbuilder for this task. Also, we can check the length of output string
        while iterating over original string to stop algorithm when it'll be over than length of original string.

        :return: str
        """
        # region Straightforward solution with checking the length of result string.
        # if len(self) < 3:
        #     return str(self)
        # current_char = self[0]
        # count = 1
        # result = ""
        # for i in range(1, len(self)):
        #     if self[i] == current_char:
        #         count += 1
        #     else:
        #         result += current_char + str(count)
        #         if len(result) >= len(self):
        #             return str(self)
        #         current_char = self[i]
        #         count = 1
        # result += current_char + str(count)
        # if len(result) >= len(self):
        #     return str(self)
        # return result
        # endregion

        # region Solution with StringBuilder
        if len(self) < 3:
            return str(self)
        result_len = 0
        sb = StringBuilder()
        current_char = self[0]
        count = 1
        for i in range(1, len(self)):
            if self[i] == current_char:
                count += 1
            else:
                s = current_char + str(count)
                result_len += len(s)
                if result_len > len(self):
                    return str(self)
                sb.add(s)
                current_char = self[i]
                count = 1
        s = current_char + str(count)
        result_len += len(s)
        if result_len > len(self):
            return str(self)
        sb.add(s)
        return str(sb)

        # endregion


def is_substring(one: str, other: str) -> bool:
    """
    Given two strings, one and other, write an algorithm to check if one string is a substring for another.
    For example, abc is a substring for abcdef, so is_substring('abc', 'abcdef') == true,
    as well as is_substring('abcdef', 'abc').

    Solution. At first, we must make sure that the "one" string is greater than the "other".
    Then, we check if the lenght of one of strings is equal to zero. If it is, return True.
    We set out pointer on the beginning of the second stirng. Then, we iterate through
    first string and count how many chars from string one are equal to chars from other.
    If we come to state when count of these equal chars is equal to length of second string,
    we return True. Otherwise, we return false.

    :param one: str
    :param other: str
    :return: bool
    """
    # to make sure first string is bigger
    if len(one) < len(other):
        return is_substring(other, one)
    # If empty string is a substring of any string
    if len(one) == 0 or len(other) == 0:
        return True
    cur_ind = 0
    for c in one:
        if c == other[cur_ind]:
            cur_ind += 1
            if cur_ind == len(other):
                return True
        else:
            cur_ind = 0
    return False


def is_rotation(s1: str, s2: str) -> bool:
    """
    Assume you have a method is_substring which checks if one word is a substring of another.
    Given two stirngs, s1 and s2, write code to check if s2 is a rotation of s1
    using only one call to is_substring
    e.g. "waterbottle" is a rotation of "erbottlewat".

    I didn't came to solution myself, I used hints. All of them.
    The solution is so brilliant and simple.
    Of course, at first we check if the length of s1 is equal to s2.
    If s1 is equal to s2, return true.
    Then we append s2 to s2, using concatenation. I don't think SB will be really
        useful there.

    :param s1: str
    :param s2: str
    :return: bool
    """
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    return is_substring(s1, s2 + s2)


def test_is_substring() -> None:
    assert is_substring("abcdef", "abc")
    assert not is_substring("abcdef", "ced")
    assert is_substring("abcdef", "def")
    assert is_substring("abcdef", "abcdef")
    assert is_substring("ab", "abc")
    assert not is_substring("qwert", "bc")


def test_is_rotation() -> None:
    assert is_rotation("", "")
    assert not is_rotation("", "a")
    assert not is_rotation("a", "")
    assert is_rotation("abc", "bca")
    assert is_rotation("waterbottle", "rbottlewate")


def one_away(one: str, two: str) -> bool:
    """
    There are three types of edits that can be perormed on strings: insert a character,
    remove a character or replace a character. Given two strings, write a function to check if
    they are one edit (or zero edits) away.

    Let's see examples.
    pale, ple -> true, pales, pale -> true, pale, bale -> true, pale, bake -> false.
    One thing comes to mind: when we are iterating through strings with two pointers,
    those two pointers must be the same for all the time, except once,
    where one of the pointers can iterate faster or slower.

    Other thing that comes to mind. We can use a hash table for first and second string,
        if their lengths differs not more than 1, otherwise function returns false.
        But! Hash tables don't consider the order of string: permutations of one string
        will be considered as True, while there can be a case like this: "abcd" - "dcba".
    Answer. Let's see. Can we use hash-tables here?

    Right answer. At first, we need to check len(one) - len(two) < 2. If it is greater than 2 return False,
    If len(one) == len(two), then both string must be equal in all places except one, so we are going to
        iterate through every string at the same time and count times when chars are unequal.
        If there are less than two chars, return True, else return False.
    If len(one) is less than len(two), then we call our function with swapped stirngs.
    If len(one) == len(two) + 1, we set then we initialize two pointers as the beginning of each string: id1 and id2,
        respectively. Then we iterate from 0 to len(two). If there are difference between id1-th element of string
        one and id2-th element of string two, than we check if id1 != id2 ('cos if those indices are not equal,
        then we encountered same case earlier, so it leads to at least two insertions). If id1 != id2 than we
        return False. Else we increment id1 by one.



    :param two: str
    :param one: str
    :return:
    """

    if len(one) < len(two):
        return one_away(two, one)

    if len(one) - len(two) > 1:
        return False  # 'cos it must be at least two insertions into the second string

    if len(one) == len(two):
        dif = False
        for i in range(len(one)):
            if one[i] != two[i]:
                if dif:
                    return False
                else:
                    dif = True
        return True
    elif len(one) > len(two):
        in1 = 0
        in2 = 0
        for i in range(len(two)):
            if one[in1] != two[in2]:
                if in1 != in2:
                    return False
                in1 += 1
            in1 += 1
            in2 += 1

        return True


def test_one_away() -> None:
    assert one_away("abcd", "abcde")
    assert one_away("aabcd", "abcd")
    assert one_away("abcd", "abccd")
    assert one_away("pales", "pale")
    assert not one_away("pale", "bake")


def test_compress() -> None:
    assert "string" == MyString("string").compress()
    assert "a4" == MyString("aaaa").compress()
    assert "bb" == MyString("bb").compress()
    assert "a5b2" == MyString("aaaaabb").compress()
    assert "a3" == MyString("aaa").compress()
    assert "a5b1" == MyString("aaaaab").compress()
    assert "qwertyuiop" == MyString("qwertyuiop").compress()


class Matrix:
    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self._mat = [[]]
            self._shape = (0, 0)

        if "shape" in kwargs:
            if type(kwargs['shape']) == tuple and len(kwargs['shape']) == 2:
                self._shape = kwargs['shape']
                self._mat = []
                for _ in range(kwargs['shape'][0]):
                    a = []
                    for _ in range(kwargs['shape'][1]):
                        a.append(random.randint(0, 10))
                    self._mat.append(a)
            else:
                raise TypeError("For shape you must provide a tuple with exactly two positive variables!")

        if "mat" in kwargs:
            # TODO: Check if this kwarg is a two-dimensional array!
            try:
                if kwargs["mat"][0][0] is not None:
                    mat = kwargs["mat"]
                    self._mat = mat
                    self._shape = (len(mat), len(mat[0]))
            except TypeError:
                raise TypeError("You must provide a two-dimensional array!")

    def __str__(self):
        res = ""
        for i in range(self._shape[0]):
            for j in range(self._shape[1]):
                res += "%3d " % self._mat[i][j]
            res += "\n"
        return res

    def rotate(self) -> Matrix:
        if self._shape[0] != self._shape[1]:
            raise IndexError("You can't rotate non-square matrices!")
        if self._shape == (1, 1):
            return self
        mat = self._mat
        res = []
        for i in range(self._shape[0]):
            temp = []
            for j in range(self._shape[1]):
                temp.append(mat[self._shape[0] - 1 - j][i])
            res.append(temp)

        return Matrix(mat=res)

    def zero_matrix(self) -> Matrix:
        """
        Write an algorithm such that if an element in an MxN matrix if 0,
        its entire row and column are set to 0.
        :return: Matrix
        """
        set_columns = set()
        set_rows = set()

        mat = self._mat
        for i in range(self._shape[0]):
            for j in range(self._shape[1]):
                if mat[i][j] == 0:
                    set_columns.add(i)
                    set_rows.add(j)
        for col in set_columns:
            for j in range(self._shape[1]):
                mat[col][j] = 0
        for row in set_rows:
            for i in range(self._shape[0]):
                mat[i][row] = 0
        return Matrix(mat=mat)


if __name__ == "__main__":
    test_is_rotation()
    # test_is_substring()
    # mat = [
    #     [0, 2, 1],
    #     [1, 1, 2],
    #     [1, 2, 2],
    #     [0, 1, 2]
    # ]
    # m = Matrix(mat=mat)
    # print(m)
    # m2 = m.zero_matrix()
    # print(m2)
