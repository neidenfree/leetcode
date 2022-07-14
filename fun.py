from typing import List

from utils import test_equal


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


def length_of_last_word_test():
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
    test_single_number()
    # test_valid_palindrome()
    # test_plus_one()
    # str_str_test()
    # length_of_last_word_test()
