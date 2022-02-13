from typing import List
from collections import deque


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons = 0
        cur_cons = 0
        for n in nums:
            if n == 1:
                cur_cons += 1
            else:
                if cur_cons > max_cons:
                    max_cons = cur_cons
                cur_cons = 0
        return max(cur_cons, max_cons)

    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                c += 1
        return c

    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        p1 = 0
        p2 = len(nums) - 1
        while p1 != p2:
            if abs(nums[p1]) > abs(nums[p2]):
                res.append(nums[p1] ** 2)
                p1 += 1
            else:
                res.append(nums[p2] ** 2)
                p2 -= 1
        res.append(nums[p1] ** 2)
        return list(reversed(res))

        # return sorted([x ** 2 for x in nums])

    def duplicateZeros(self, arr: List[int]) -> None:
        new_arr = []
        n = len(arr)
        for i in range(n):
            if arr[i] == 0:
                new_arr.append(0)
                new_arr.append(0)
                # arr.append(0)
            else:
                new_arr.append(arr[i])
        for i in range(n):
            arr[i] = new_arr[i]

    def merge_n2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        This is merge variant with standard python sorting
        """
        res = []
        for i in range(m):
            res.append(nums1[i])
        res.extend(nums2)
        res = sorted(res)
        for i in range(n + m):
            nums1[i] = res[i]

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = 0
        p2 = 0
        res = []

        while p1 != m and p2 != n:
            if nums1[p1] > nums2[p2]:
                res.append(nums2[p2])
                p2 += 1
            else:
                res.append(nums1[p1])
                p1 += 1
        while p1 != m:
            res.append(nums1[p1])
            p1 += 1
        while p2 != n:
            res.append(nums2[p2])
            p2 += 1

        for i in range(m + n):
            nums1[i] = res[i]





if __name__ == '__main__':
    sol = Solution()
    # arr = [1, 0, 2, 3, 0, 4, 5, 0]
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    sol.merge(nums1, 3, nums2, 3)
    print(nums1)
    # print(arr)
