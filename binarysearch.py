# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.
from typing import List


def test_equal(f, result, *args, **kwargs):
    if 'verbose' in kwargs:
        if kwargs['verbose'] == 0:
            pass
        elif kwargs['verbose'] == 1:
            print(*args)
            print(f(*args))
        elif kwargs['verbose'] == 2:
            print(f'''
                    Test for function "{f.__name__}".
                    Arguments = {args},
                    expected result = {result}
                    real result = {f(*args)}
                ''')

    assert f(*args) == result


def guess(num: int) -> int:
    value = 40
    if num > value:
        return -1
    if num < value:
        return 1
    if num == value:
        return 0


bad_version_value = 1


def isBadVersion(version_number: int) -> bool:
    return version_number >= bad_version_value


class Solution:
    def search_basic(self, nums: List[int], target: int) -> int:
        if nums is None:
            raise Exception("nums is None")
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        left = 0
        right = len(nums) - 1
        mid = (right - left) // 2
        while left <= right:
            if target == nums[mid]:
                return mid
            if target == nums[left]:
                return left
            if target == nums[right]:
                return right
            elif target < nums[mid]:
                right = mid - 1
                mid = (right - left) // 2
            elif target > nums[mid]:
                left = mid + 1
                mid = (right + left) // 2
        return -1

    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        mid = 0
        while right >= left:
            mid = (right + left) // 2
            midsqr = mid * mid
            if midsqr == x:
                return mid
            elif midsqr > x:
                right = mid - 1
            elif midsqr < x:
                left = mid + 1
        return right

    def guessNumber(self, n: int) -> int:
        left = 0
        right = n

        while left <= right:
            mid = (left + right) // 2
            print(left, mid, right)
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid - 1
            elif guess(mid) == 1:
                left = mid + 1

    def search(self, nums: List[int], target: int) -> int:
        if nums is None:
            raise Exception("nums is None")
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if left == right:
                break
            if target == nums[mid]:
                return mid
            elif target == nums[left]:
                return left
            elif target == nums[right]:
                return right

            if nums[left] < nums[mid]:
                # Если отсортирована левая часть
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                    continue
                elif target < nums[left] or target > nums[mid]:
                    left = mid + 1
            elif nums[mid] < nums[right]:
                # Если отсортирована правая часть
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                elif target < nums[mid] or target > nums[right]:
                    right = mid - 1
                continue
            else:
                return -1
        return -1

    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            current = isBadVersion(mid)
            prev = isBadVersion(mid - 1)
            if current and not prev:
                return mid
            elif current and prev:
                right = mid - 1

            elif not current and not prev:
                left = mid + 1
        return left

    def findPeakElement(self, nums: List[int]) -> int:
        # TODO: Разобраться, почему же все-таки это работает
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


def peak_element_test():
    a = Solution()
    test_equal(a.findPeakElement, 2, [1, 2, 3, 1])
    test_equal(a.findPeakElement, 3, [1, 2, 3, 4])
    test_equal(a.findPeakElement, 5, [1, 2, 1, 3, 5, 6, 4])
    test_equal(a.findPeakElement, 2, [0, 1, 10, 1, 0])

    # test_equal(a.findPeakElement, 2, [1, 2, 3, 1])
    # test_equal(a.findPeakElement, 2, [1, 2, 3, 1])


def first_bad_version_test():
    a = Solution()
    for i in range(1, 100):
        test_equal(a.firstBadVersion, bad_version_value, i, verbose=0)
    # test_equal(a.firstBadVersion, 10, 15, verbose=2)


def test_search():
    a = Solution()
    # Default
    assert a.search([1, 2, 3, 4, 5], 1) == 0
    assert a.search([1, 2, 3, 4, 5], 5) == 4
    assert a.search([0, 1, 2, 3, 4, 5, 6, 7], 7) == 7
    assert a.search([1, 2, 3, 4, 5], 1) == 0
    assert a.search([1, 2, 3, 4, 5], 1) == 0
    assert a.search([-10, 2], 2) == 1
    assert a.search([-10, 2, 3], 3) == 2
    assert a.search([1, 2, 3], 4) == -1

    # Pivoted
    test_equal(a.search, 4, [4, 5, 6, 7, 0, 1, 2], 0)
    test_equal(a.search, 5, [4, 5, 6, 7, 0, 1, 2], 1)
    test_equal(a.search, 1, [4, 5, 6, 7, 0, 1, 2], 5)
    test_equal(a.search, 2, [4, 5, 6, 7, 0, 1, 2], 6)
    test_equal(a.search, 4, [5, 6, 1, 2, 3], 3)
    test_equal(a.search, -1, [5, 6, 1, 2, 3], 8)
    test_equal(a.search, -1, [5, 6, 1, 2, 3], 0)

    # test(a.search, -1, [3, 1], 0, verbose=2)
    test_equal(a.search, -1, [9, 1, 2, 3, 4], 5, verbose=0)
    test_equal(a.search, -1, [9, 1, 2, 3, 4], 6, verbose=0)
    test_equal(a.search, 3, [9, 1, 2, 3, 4, 5], 3, verbose=0)


def test_sqrt():
    a = Solution()
    assert a.mySqrt(9) == 3
    assert a.mySqrt(0) == 0
    assert a.mySqrt(1) == 1
    assert a.mySqrt(4) == 2
    assert a.mySqrt(8) == 2

    for i in range(0, 100000):
        assert a.mySqrt(i) == int(i ** 0.5)

    # assert a.mySqrt(101) == 10

    # print(a.mySqrt(101))


def test_guess():
    a = Solution()
    print(a.guessNumber(60))


if __name__ == "__main__":
    peak_element_test()
    # first_bad_version_test()
    # test_search()
    # test_sqrt()
    # test_guess()
