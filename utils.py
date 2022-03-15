import collections
from typing import List


def compare_lists(a: List, b: List):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def test_equal(f, result, *args, **kwargs):
    real_result = f(*args)
    if 'verbose' in kwargs:
        if kwargs['verbose'] == 0:
            pass
        elif kwargs['verbose'] == 1:
            print(*args)
            print(real_result)
        elif kwargs['verbose'] == 2:
            print(f'''
                    Test for function "{f.__name__}".
                    Arguments = {args},
                    expected result = {result}
                    real result = {real_result}
                ''')
    if "list_check" in kwargs:
        assert compare_lists(real_result, result)
    else:
        assert f(*args) == result


def right_result(right, result, **nums):
    # if nums:
    assert right == result, f'''Wrong! It must be "{right}" but it is "{result}" instead!'''
    # else:
    #     assert right == result, f'''Wrong! For {nums} it must be "{right}" but it is "{result}" instead!'''


def binary_search(nums: List[object], target) -> bool:
    """

    :param target: object
    :param nums: List[object]
    :rtype: bool


    Function that returns True if element is in nums, otherwise returns False.
    """

    if not nums:
        return False
    if len(nums) == 1:
        return True if nums[0] == target else False
    left = 0
    right = len(nums) - 1
    while left <= right:
        m = left + (right - left) // 2
        if nums[m] == target:
            return True
        if target < nums[m]:
            right = m - 1
        if target > nums[m]:
            left = m + 1

    return False


def binary_search_index(nums: List[object], target) -> int:
    """

    :param target: object
    :param nums: List[object]
    :rtype: int


    Function that finds index of element target in array nums.
    If there is no target in nums, returns -1.
    """

    if not nums:
        return -1
    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    left = 0
    right = len(nums) - 1
    while left < right:
        m = left + (right - left) // 2
        if nums[m] == target:
            return m
        if target < nums[m]:
            right = m - 1
        if target > nums[m]:
            left = m + 1

    return -1


a = 500
