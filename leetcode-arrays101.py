from typing import List
from collections import deque

# There are link where I get all tasks from
# https://leetcode.com/explore/learn/card/fun-with-arrays/


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

    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        p2 = len(nums) - 1
        while p1 <= p2:  # Reconsider this!
            if nums[p2] == val:
                p2 -= 1
                continue
            if nums[p1] == val:
                nums[p1] = nums[p2]
                nums[p2] = val
            else:
                p1 += 1

        val_count = 0
        for i in reversed(range(0, len(nums))):
            if nums[i] == val:
                val_count += 1
            else:
                break

        return len(nums) - val_count

    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if i >= len(nums) - 1:
                break
            while nums[i] == nums[i + 1]:
                del nums[i + 1]
                if i >= len(nums) - 1:
                    break
        return len(nums)

    def checkIfExist(self, arr: List[int]) -> bool:
        d = {}
        zeros = 0
        for elem in arr:
            if elem == 0:
                zeros += 1
            else:
                d[elem * 2] = 1
        print(d)
        if zeros > 1:
            return True
        for elem in arr:
            if elem in d:
                return True
        return False

    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 2:
            return False
        changes = 0
        up = arr[0] < arr[1]
        if not up:
            return False
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                return False
            if up:
                if arr[i] > arr[i + 1]:
                    up = False
                    changes += 1
            else:
                if arr[i] < arr[i + 1]:
                    changes += 1
        print('c = ', changes)
        return changes == 1

    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) < 2:
            return [-1]
        local_max = arr[len(arr) - 1]
        current_max = arr[len(arr) - 1]
        for i in range(len(arr) - 1, -1, -1):
            current_max = max(arr[i], current_max)
            arr[i] = local_max
            local_max = max(current_max, local_max)
        arr[len(arr) - 1] = -1
        return arr

    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        fast = 0
        while fast != len(nums):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            fast += 1
            if nums[slow] != 0:
                slow += 1

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        fast = 0
        slow = 0

        while fast != len(nums):
            if nums[slow] % 2 != 0 and nums[fast] % 2 == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            fast += 1
            if nums[slow] % 2 == 0:
                slow += 1
        return nums

    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        res = 0
        for i in range(len(sorted_heights)):
            if heights[i] != sorted_heights[i]:
                res += 1
        return res

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        max_n = len(nums)
        present = {}
        for elem in nums:
            if elem not in present:
                present[elem] = 1
        res = []
        for i in range(1, max_n + 1):
            if i not in present:
                res.append(i)
        return res


if __name__ == '__main__':
    sol = Solution()

    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(nums)
    print(sol.findDisappearedNumbers(nums))
