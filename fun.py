from typing import List

from collections import Counter

from utils import test_equal

import unittest

from collections import deque


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

    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                res += prices[i + 1] - prices[i]
        return res

    def rotate_deque(self, nums: List[int], k: int) -> None:
        from collections import deque
        k = k % len(nums)
        temp = deque(nums)
        for _ in range(k):
            item = temp.pop()
            temp.appendleft(item)
        for i, x in enumerate(temp):
            nums[i] = x

    def rotate_list(self, nums: List[int], k: int):
        k = k % len(nums)
        new_nums = []
        for i in range(k + 1, len(nums)):
            new_nums.append(nums[i])
        for i in range(0, k + 1):
            new_nums.append(nums[i])
        for i in range(len(nums)):
            nums[i] = new_nums[i]

    def rotate_inplace(self, nums: List[int], k: int):
        k = k % len(nums)
        for _ in range(k):
            item = nums.pop()
            nums.insert(0, item)

    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for elem in nums:
            if elem in dic:
                return True
            else:
                dic[elem] = True
        return False

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            return self.intersect(nums2, nums1)

        res = []
        for el in nums1:
            if el in nums2:
                del nums2[nums2.index(el)]
                res.append(el)

        return res

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #             return [i, j]
        d = {target - value: i for i, value in enumerate(nums)}
        for i, el in enumerate(nums):
            if el in d:
                if i != d[el]:
                    return [i, d[el]]

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # each row
        d = {}
        for row in board:
            for el in row:
                if el != '.':
                    if el in d:
                        return False
                    else:
                        d[el] = True
            d.clear()
        # each column
        for i in range(len(board)):
            for j in range(len(board)):
                if board[j][i] != '.':
                    if board[j][i] in d:
                        return False
                    else:
                        d[board[j][i]] = True
            d.clear()

        # each nine sub-boxes
        for topleft, bottomright in zip([(0, 0), (0, 3), (0, 6),
                                         (3, 0), (3, 3), (3, 6),
                                         (6, 0), (6, 3), (6, 6)],
                                        [(2, 2), (2, 5), (2, 8),
                                         (5, 2), (5, 5), (5, 8),
                                         (8, 2), (8, 5), (8, 8)]):
            d.clear()
            for i in range(topleft[0], bottomright[0] + 1):
                for j in range(topleft[1], bottomright[1] + 1):
                    if board[i][j] != '.':
                        if board[i][j] in d:
                            return False
                        else:
                            d[board[i][j]] = True
        return True

    def rotate_other_matrix(self, matrix: List[List[int]]) -> None:
        n = len(matrix) - 1
        m = [[None for x in range(len(matrix))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                m[j][n - i] = matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = m[i][j]
        s = ''

    @staticmethod
    def print_matrix(matrix: List[List[int]]):
        for row in matrix:
            for el in row:
                print(str(el).ljust(3, ' '), end='')
            print()

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) - 1
        # first, we interchange rows
        for i in range(len(matrix) // 2):
            matrix[i], matrix[n - i] = matrix[n - i], matrix[i]

        # second, we transpose matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        for _ in range(len(s) // 2):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverse(self, x: int) -> int:
        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0
        s = str(x)
        if s[0] == '-':
            res = int('-' + s[1:][::-1])
        else:
            res = int(str(x)[::-1])

        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        return res

    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i, elem in enumerate(s):
            if c[elem] == 1:
                return i
        return -1

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c1, c2 = Counter(s), Counter(t)
        return c1 == c2

    def myAtoi(self, s: str) -> int:
        sign_occurred = False
        digit_occurred = False
        sign = True
        res: List[str] = []
        s = s.lstrip()
        for elem in s:
            if elem == "-" and not sign_occurred and not digit_occurred:
                sign = False
                sign_occurred = True
            elif elem == "+" and not sign_occurred and not digit_occurred:
                sign = True
                sign_occurred = True
            elif elem.isnumeric():
                res.append(elem)
                digit_occurred = True
            else:
                break

        if len(res) == 0:
            return 0

        res_int = int("".join(res))
        if not sign:
            res_int = -res_int
        if res_int > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if res_int < -2 ** 31:
            return -2 ** 31
        return res_int

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        res = []
        word_with_min_length = min(strs, key=lambda x: len(x))
        for i, letter in enumerate(word_with_min_length):
            letter_acceptable = True
            for elem in strs:
                if elem[i] != letter:
                    letter_acceptable = False
                    break
            if letter_acceptable:
                res.append(letter)
            else:
                break
        return "".join(res)





class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_longestCommonPrefix(self):
        f = self.solution.longestCommonPrefix
        self.assertEqual(f(["flower", "flow", "flight"]), "fl")
        self.assertEqual(f(["dog", "racecar", "car"]), "")
        self.assertEqual(f(["dog", "dogfuck", "dogsomething"]), "dog")

    def test_myAtoi(self):
        f = self.solution.myAtoi
        self.assertEqual(f("+1"), 1)
        self.assertEqual(f("00000-42a1234"), 0)
        self.assertEqual(f("42"), 42)
        self.assertEqual(f("      -42"), -42)
        self.assertEqual(f("      --42"), 0)
        self.assertEqual(f("   23  "), 23)
        self.assertEqual(f("  -23asshole"), -23)
        self.assertEqual(f("4193 with words"), 4193)
        self.assertEqual(f("23     asshole"), 23)
        self.assertEqual(f("words and 987"), 0)
        self.assertEqual(f("21474836460"), 2147483647)

    def test_isAnagram(self):
        f = self.solution.isAnagram
        self.assertTrue(f("boob", "bobo"))
        self.assertTrue(f("zyzz", "yzzz"))
        self.assertTrue(f("anagram", "naaramg"))
        self.assertFalse(f("rat", "carr"))
        self.assertFalse(f("rat", "car"))

    def test_firstUniqChar(self):
        f = self.solution.firstUniqChar
        self.assertEqual(f('leetcode'), 0)
        self.assertEqual(f('loveleetcode'), 2)
        self.assertEqual(f('aabb'), -1)
        self.assertEqual(f('aabbcc'), -1)
        self.assertEqual(f('aabbc'), 4)

    def test_reverse(self):
        f = self.solution.reverse
        self.assertEqual(123, f(321))
        self.assertEqual(-123, f(-321))
        self.assertEqual(0, f(1534236469))
        self.assertEqual(12, f(21))
        self.assertEqual(2, f(2))

    def test_reverseString(self):
        f = self.solution.reverseString

        orig = [*"some"]
        f(orig)
        self.assertListEqual(orig, [*"emos"])

        orig = [*"s"]
        f(orig)
        self.assertListEqual(orig, [*"s"])

        orig = [*"somee"]
        f(orig)
        self.assertListEqual(orig, [*"eemos"])

        orig = [*"abc"]
        f(orig)
        self.assertListEqual(orig, [*"cba"])

    def test_rotate(self):
        matrix = [[1, 2], [3, 4]]
        right_res = [[3, 1], [4, 2]]
        self.solution.rotate(matrix)
        self.assertListEqual(matrix, right_res)

        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        right_res = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.solution.rotate(matrix)
        self.assertListEqual(matrix, right_res)
        #
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        right_res = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        self.solution.rotate(matrix)
        self.assertListEqual(matrix, right_res)

    def test_isValidSudoku(self):
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        self.assertTrue(self.solution.isValidSudoku(board))

        board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

        self.assertFalse(self.solution.isValidSudoku(board))

        board = [["5", "3", ".", "7", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        self.assertFalse(self.solution.isValidSudoku(board))

    def test_twoSum(self):
        s = self.solution
        nums = [2, 7, 11, 15]
        target = 9
        self.assertListEqual(s.twoSum(nums, target), [0, 1])

        nums = [3, 2, 4]
        target = 6
        self.assertListEqual(s.twoSum(nums, target), [1, 2])

        nums = [3, 3]
        target = 6
        self.assertListEqual(s.twoSum(nums, target), [0, 1])

    def test_intersection(self):
        s = self.solution
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        self.assertListEqual([2, 2], s.intersect(nums1, nums2))

        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        self.assertListEqual([9, 4], s.intersect(nums1, nums2))

        nums1 = [1, 2, 3]
        nums2 = [4, 5]
        self.assertListEqual([], s.intersect(nums1, nums2))

    def test_duplicate(self):
        nums = [1, 2, 3, 4, 5]
        self.assertFalse(self.solution.containsDuplicate(nums))
        nums = [1, 2, 3, 4, 5, 1]
        self.assertTrue(self.solution.containsDuplicate(nums))
        nums = [1, 1]
        self.assertTrue(self.solution.containsDuplicate(nums))

    def test_max_profit(self):
        f = self.solution.maxProfit
        self.assertEqual(f([7, 1, 5, 3, 6, 4]), 7)
        self.assertEqual(f([1, 2, 3, 4, 5]), 4)
        self.assertEqual(f([7, 6, 4, 3, 1]), 0)
        self.assertEqual(f([]), 0)

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
