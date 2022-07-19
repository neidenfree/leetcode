from typing import List

from utils import test_equal

import unittest


def spiral_matrix(n: int):
    def print_mat(mat) -> None:
        for i in range(len(mat)):
            for j in range(len(mat)):
                print(mat[i][j], end=' ')
            print()

    if n < 1:
        return None
    if n == 1:
        return [1]
    if n % 2 == 0:
        return None

    mat = [[0 for x in range(n)] for x in range(n)]
    i = n // 2
    j = n // 2
    direction = ['right', 'down', 'left', 'up']
    d = 0

    move_max = 1
    move_count = 0
    move_two = 0

    for s in range(1, n ** 2 + 1):
        print(f'{s} iteration, [{i},{j}], direction={direction[d]}')
        mat[i][j] = s
        print_mat(mat)
        move_count += 1
        if direction[d] == 'right':
            j += 1
        if direction[d] == 'down':
            i += 1
        if direction[d] == 'left':
            j -= 1
        if direction[d] == 'up':
            i -= 1

        if move_count == move_max:
            d += 1
            if d > 3:
                d = 0
            move_count = 0
            move_two += 1

        if move_two == 2:
            move_max += 1
            move_two = 0

    print_mat(mat)
    return mat


class Solution:
    def strStr(self, haysack: str, needle: str) -> int:
        if len(needle) > len(haysack):
            return -1
        if len(needle) == len(haysack):
            if needle == haysack:
                return 0
            else:
                return -1
        if len(needle) == 0:
            return 0

        for i in range(len(haysack) - len(needle) + 1):  # maybe even -1
            if haysack[i:i + len(needle)] == needle:
                return i
        return -1

    def lengthOfLastWord(self, s: str) -> int:
        last = ''
        for x in s.split(' '):
            if x != '':
                last = x
        return len(last)

    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        rem = 0
        for i in reversed(range(0, len(digits))):
            if digits[i] == 9:
                digits[i] = 0
                rem = 1
            else:
                digits[i] += rem
                rem = 0
                break
        if rem != 0:
            digits.insert(0, rem)
        return digits

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned = ''.join([x for x in s if x.isalnum()])
        return cleaned == cleaned[::-1]

    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dic = {}
        for el in nums:
            if el in dic:
                dic[el] += 1
            else:
                dic[el] = 1

        for el in dic:
            if dic[el] == 1:
                return el

    def addBinary(self, a: str, b: str) -> str:
        a1 = int(a, 2)
        b1 = int(b, 2)
        c = a1 + b1
        return str(bin(c))[2:]

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        row = [1, 1]

        for i in range(2, rowIndex + 1):
            new_row = [1 for _ in range(i + 1)]
            for j in range(len(row) - 1):
                new_row[j + 1] = row[j] + row[j + 1]
            row = new_row

        return row

    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        m = -1
        elem = 0
        for n in dic:
            if dic[n] > m:
                m = dic[n]
                elem = n
        return elem

    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        temp = columnNumber
        while temp != 0:
            if temp % 26 == 0:
                res.append(26)
                temp -= 1
            else:
                res.append(temp % 26)
            temp = temp // 26
        res.reverse()
        return ''.join([chr(x + 64) for x in res])

    def titleToNumber(self, columnTitle: str) -> int:
        res = []
        for i, c in enumerate(columnTitle):
            res.append(ord(c) - 64)
        res.reverse()
        r = 0
        for i, n in enumerate(res):
            r += n * (26 ** i)
        return r

    def hammingWeight(self, n: int) -> int:
        s = str(bin(n)[2:])
        res = 0
        for c in s:
            if c == '1':
                res += 1
        return res

    def isIsomorphic(self, s: str, t: str) -> bool:
        n = m = 0
        dif_s = {}
        order_s = []
        dif_t = {}
        order_t = []
        for i in range(len(s)):
            if s[i] not in dif_s:
                dif_s[s[i]] = n
                n += 1
            order_s.append(dif_s[s[i]])

            if t[i] not in dif_t:
                dif_t[t[i]] = m
                m += 1
            order_t.append(dif_t[t[i]])

        return order_t == order_s


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_get_row(self):
        self.assertEqual(self.solution.getRow(0), [1])
        self.assertEqual(self.solution.getRow(1), [1, 1])
        self.assertEqual(self.solution.getRow(2), [1, 2, 1])
        self.assertEqual(self.solution.getRow(3), [1, 3, 3, 1])
        self.assertEqual(self.solution.getRow(4), [1, 4, 6, 4, 1])

    def test_majority_element(self):
        self.assertEqual(self.solution.majorityElement([3, 2, 3]), 3)
        self.assertEqual(self.solution.majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)

    def test_convert_to_title(self):
        self.assertEqual(self.solution.convertToTitle(1), 'A')
        self.assertEqual(self.solution.convertToTitle(28), 'AB')
        self.assertEqual(self.solution.convertToTitle(26), 'Z')
        self.assertEqual(self.solution.convertToTitle(701), 'ZY')
        self.assertEqual(self.solution.convertToTitle(133), 'EC')
        self.assertEqual(self.solution.convertToTitle(286), 'JZ')
        self.assertEqual(self.solution.convertToTitle(754), 'ABZ')
        self.assertEqual(self.solution.convertToTitle(753), 'ABY')

    def test_title_to_number(self):
        self.assertEqual(self.solution.titleToNumber('A'), 1)
        self.assertEqual(self.solution.titleToNumber('AB'), 28)
        self.assertEqual(self.solution.titleToNumber('ZY'), 701)
        self.assertEqual(self.solution.titleToNumber('EC'), 133)
        self.assertEqual(self.solution.titleToNumber('JZ'), 286)
        self.assertEqual(self.solution.titleToNumber('ABZ'), 754)
        self.assertEqual(self.solution.titleToNumber('ABY'), 753)

    def test_hammingWeight(self):
        self.assertEqual(self.solution.hammingWeight(0), 0)
        self.assertEqual(self.solution.hammingWeight(7), 3)
        self.assertEqual(self.solution.hammingWeight(8), 1)
        self.assertEqual(self.solution.hammingWeight(9), 2)
        self.assertEqual(self.solution.hammingWeight(8123), 11)

    def test_is_isomorphic(self):
        self.assertTrue(self.solution.isIsomorphic("egg", "add"))
        self.assertFalse(self.solution.isIsomorphic("foo", "bar"))
        self.assertTrue(self.solution.isIsomorphic("paper", "title"))
        self.assertTrue(self.solution.isIsomorphic("asdfgh", "qwerty"))
        self.assertFalse(self.solution.isIsomorphic("asdfga", "qwqrtq"))


def test_add_binary():
    a = Solution()
    assert a.addBinary("11", "1") == "100"
    assert a.addBinary("1010", "1011") == "10101"
    assert a.addBinary("10", "0") == "10"
    assert a.addBinary("111", "11") == "1010"


def test_length_of_last_word():
    a = Solution()
    test_equal(a.lengthOfLastWord, 5, "Hello World")
    test_equal(a.lengthOfLastWord, 4, "   fly me   to   the moon  ")
    test_equal(a.lengthOfLastWord, 6, "luffy is still joyboy")
    test_equal(a.lengthOfLastWord, 1, "luffy is still joyboay z")
    test_equal(a.lengthOfLastWord, 1, "luffy is still joyboay z")


def test_plus_one():
    a = Solution()
    test_equal(a.plusOne, [9, 9], [9, 8], list_check=True, verbose=0)
    test_equal(a.plusOne, [3], [2], list_check=True, verbose=0)
    test_equal(a.plusOne, [1, 1, 0], [1, 0, 9], verbose=0, list_check=True)
    test_equal(a.plusOne, [1, 9, 1], [1, 9, 0], verbose=0, list_check=True)
    test_equal(a.plusOne, [1, 0], [9], verbose=0, list_check=True)


def str_str_test():
    a = Solution()
    test_equal(a.strStr, 2, 'hell', 'll', verbose=0)
    test_equal(a.strStr, 0, 'llhell', 'll', verbose=0)
    test_equal(a.strStr, 0, 'aaaksjdhsakj', 'aa')
    test_equal(a.strStr, 0, 'aaaksjdhsakj', 'aa')
    test_equal(a.strStr, 6, 'aaaksjzbzdhsakj', 'zbz')
    test_equal(a.strStr, -1, '2', 'zbz')
    test_equal(a.strStr, 4, "mississippi", "issip")

    # test_equal(a.strStr, 2, 'hello', 'll')
    # test_equal(a.strStr, 2, 'hello', 'll')
    # test_equal(a.strStr, 2, 'hello', 'll')


def test_single_number():
    a = Solution()
    assert a.singleNumber([2, 2, 1]) == 1
    assert a.singleNumber([4, 1, 2, 1, 2]) == 4
    assert a.singleNumber([1]) == 1


def test_valid_palindrome():
    a = Solution()
    assert a.isPalindrome("A man, a plan, a canal: Panama")
    assert not a.isPalindrome("race a car")
    assert not a.isPalindrome("asdfghjl")
    assert a.isPalindrome(" ")
    assert not a.isPalindrome("0P")


if __name__ == "__main__":
    unittest.main()
