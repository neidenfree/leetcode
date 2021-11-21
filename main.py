from typing import List, Optional
from collections import deque

from utils import right_result, binary_search
from linkedlist import TreeNode


class Solution(object):
    def rob_simple(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        prev1 = 0
        prev2 = 0
        for num in nums:
            tmp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = tmp
        return prev1

    def rob(self, nums) -> int:
        def rob_simple(nums: List[int]) -> int:
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums[0], nums[1])

            prev1 = 0
            prev2 = 0
            for num in nums:
                tmp = prev1
                prev1 = max(prev2 + num, prev1)
                prev2 = tmp
            return prev1

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(rob_simple(nums[1:]), rob_simple(nums[:-1]))

    def intersect(self, nums1, nums2):
        if len(nums1) < len(nums2):
            return self.intersect(nums2, nums1)
        counts = {}
        res = []
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1
        for num in nums2:
            if num in counts and counts[num] > 0:
                counts[num] -= 1
                res.append(num)
        return res

    def maxProfit(self, prices: List[int]) -> int:
        flag = True
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                flag = False
        if flag:
            return 0

        max_profit = prices[len(prices) - 1] - prices[len(prices) - 1]
        max_value = prices[len(prices) - 1]
        for i in range(len(prices) - 2, -1, -1):
            max_value = max(max_value, prices[i + 1])
            max_profit = max(max_profit, max_value - prices[i])
        return max_profit

    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = [0] * (10 ** 4 + 1)
        maximum = minimum = nums[0]
        for num in nums:
            counts[num] += 1
            maximum = max(maximum, num)
            minimum = min(minimum, num)
        prev = curr = 0
        for i in range(minimum, maximum + 1):
            prev, curr = curr, max(prev + counts[i] * i, curr)
        return curr

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        result = []
        row = []
        steps = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                row.append(mat[i][j])
                steps += 1
                if steps == c:
                    steps = 0
                    result.append(row)
                    row = []
        return result

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]
        if numRows == 2:
            return res
        for i in range(3, numRows + 1):
            row = [0] * i
            for j in range(0, i):
                if j > 0 and j < i - 1:
                    row[j] = res[i - 2][j - 1] + res[i - 2][j]
                else:
                    row[j] = 1
            res.append(row)
        return res

    def lengthOfLongestSubstringVerbose(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        p1 = 0
        p2 = 0
        counts = {}
        max_len = 0
        max_substring = ""
        while p1 < len(s) - 1:
            if s[p2] not in counts and p2 < len(s) - 1:
                counts[s[p2]] = True
                p2 += 1
            else:
                if s[p2] not in counts and p2 == len(s) - 1:
                    counts[s[p2]] = True
                if max_len < len(counts):
                    max_len = len(counts)
                    max_substring = ''.join(counts.keys())
                counts = {}
                p1 += 1
                p2 = p1
        return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        p1 = 0
        p2 = 0
        counts = {}
        max_len = 0
        while p1 < len(s) - 1:
            if s[p2] not in counts and p2 < len(s) - 1:
                counts[s[p2]] = True
                p2 += 1
            else:
                if s[p2] not in counts and p2 == len(s) - 1:
                    counts[s[p2]] = True
                if max_len < len(counts):
                    max_len = len(counts)
                counts = {}
                p1 += 1
                p2 = p1
        return max_len

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        res = False
        hash_s1 = {}
        for c in s1:
            hash_s1[c] = hash_s1.get(c, 0) + 1
        p1 = 0
        p2 = len(s1)
        while p2 <= len(s2):
            hash_w = {}
            for c in s2[p1:p2]:
                if c not in hash_s1:
                    break
                else:
                    hash_w[c] = hash_w.get(c, 0) + 1
            if hash_s1 == hash_w:
                return True
            p1 += 1
            p2 += 1
        return res

    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        trail = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] != 0:
                if nums[i] > trail:
                    trail = 0
                else:
                    trail += 1
            else:
                trail += 1
        return trail == 0

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def fill(image: List[List[int]], sr, sc, newColor, color):
            if sc < 0 or sc >= len(image[0]) or sr < 0 or sr >= len(image) or image[sr][sc] != color:
                return None
            image[sr][sc] = newColor
            fill(image, sr - 1, sc, newColor=newColor, color=color)
            fill(image, sr + 1, sc, newColor=newColor, color=color)
            fill(image, sr, sc - 1, newColor=newColor, color=color)
            fill(image, sr, sc + 1, newColor=newColor, color=color)

        if image[sr][sc] == newColor:
            return image

        fill(image, sr, sc, newColor=newColor, color=image[sr][sc])
        return image

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def island_area(grid: List[List[int]], i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] <= 0:
                return 0
            else:
                grid[i][j] = -1
                return 1 + island_area(grid, i + 1, j) + \
                       island_area(grid, i - 1, j) + \
                       island_area(grid, i, j - 1) + \
                       island_area(grid, i, j + 1)

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(max_area, island_area(grid, i, j))
        return max_area

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            ar = [0] * 10
            for c in row:
                if c == '.':
                    pass
                else:
                    if ar[int(c)] != 0:
                        return False
                    else:
                        ar[int(c)] = 1
        for i in range(9):
            ar = [0] * 10
            for j in range(9):
                c = board[j][i]
                if c == '.':
                    pass
                else:
                    if ar[int(c)] != 0:
                        return False
                    else:
                        ar[int(c)] = 1

        for col in range(3):
            for row in range(3):
                ar = [0] * 10
                for i in range(col * 3, (col + 1) * 3):
                    for j in range(row * 3, (row + 1) * 3):
                        c = board[j][i]
                        if c == '.':
                            pass
                        else:
                            if ar[int(c)] != 0:
                                return False
                            else:
                                ar[int(c)] = 1
        return True

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # nums = [x[0] for x in matrix]
        if len(matrix) == 1:
            return binary_search(matrix[0], target)
        l = 0
        r = len(matrix) - 1
        while l <= r:
            m = l + (r - l) // 2
            if target == matrix[m][0]:
                return True
            elif target > matrix[m][0]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
        if l > len(matrix) - 1:
            l = len(matrix) - 1
        if target < matrix[l][0]:
            l -= 1
        return binary_search(matrix[l], target)

    @staticmethod
    def jump(nums):
        if len(nums) <= 1:
            return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        return times

    @staticmethod
    def maxSubArray(nums: List[int]) -> int:
        max_ending = max_current = nums[0]

        for i in nums[1:]:
            max_ending = max(i, max_ending + i)
            max_current = max(max_current, max_ending)

        return max_current

    @staticmethod
    def inorder_traversal(root: TreeNode) -> List[int]:
        def helper(root: TreeNode, res: List[int]):
            if root:
                helper(root.left, res)
                res.append(root.val)
                helper(root.right, res)

        res = []
        helper(root, res)
        return res

    @staticmethod
    def preorder_traversal(root: TreeNode) -> List[int]:
        def helper(root: TreeNode, res: List[int]):
            if root:
                res.append(root.val)
                helper(root.left, res)
                helper(root.right, res)

        res = []
        helper(root, res)
        return res

    @staticmethod
    def postorder_traversal(root: TreeNode) -> List[int]:
        def helper(root: TreeNode, res: List[int]):
            if root:
                helper(root.left, res)
                helper(root.right, res)
                res.append(root.val)

        res = []
        helper(root, res)
        return res

    @staticmethod
    def preorder_traversal_iterative(root: TreeNode) -> List[int]:
        if root is None:
            return None
        res = []
        # s = [root]
        s = deque([root])
        # print(stack[0])
        while len(s) > 0:
            root = s.pop()
            if root.right:
                s.append(root.right)
            if root.left:
                s.append(root.left)
            res.append(root.val)

        return res

    @staticmethod
    def inorder_traversal_iterative(root: TreeNode) -> List[int]:
        res = []
        s = []
        node = root

        while True:
            if node is not None:
                s.append(node)
                node = node.left
            else:
                if not s:
                    break
                node = s.pop()
                res.append(node.val)
                node = node.right
        return res

    @staticmethod
    def postorder_traversal_iterative(root: TreeNode) -> List[int]:
        if not root:
            return None
        res = []
        # s = [root]
        s = deque([root])
        # print(stack[0])
        while len(s) > 0:
            root = s.pop()
            if root.left:
                s.append(root.left)
            if root.right:
                s.append(root.right)
            res.append(root.val)
        return res[::-1]

    # @staticmethod

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        ans = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
        ans.left = self.mergeTrees(root1 and root1.left, root2 and root2.left)
        ans.right = self.mergeTrees(root1 and root1.right, root2 and root2.right)
        return ans


def print_tree(node: TreeNode, k: int) -> None:
    if node is not None:
        print_tree(node.right, k + 1)
        print(' ' * k * 3 + str(node.val))
        print_tree(node.left, k + 1)
