from typing import Optional, List
# from stacksandqueries import Queue
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self._preorderTraversal(root, res)
        return res

    def _preorderTraversal(self, root: Optional[TreeNode], res: List[str]) -> None:
        if root is not None:
            res.append(root.val)
            self._preorderTraversal(root.left, res)
            self._preorderTraversal(root.right, res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self._inorderTraversal(root, res)
        return res

    def _inorderTraversal(self, root: Optional[TreeNode], res: List[str]) -> None:
        if root is not None:
            self._inorderTraversal(root.left, res)
            res.append(root.val)
            self._inorderTraversal(root.right, res)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self._postorderTraversal(root, res)
        return res

    def _postorderTraversal(self, root: Optional[TreeNode], res: List[str]) -> None:
        if root is not None:
            self._postorderTraversal(root.left, res)
            self._postorderTraversal(root.right, res)
            res.append(root.val)

    def levelorderTraversal(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        res = []
        q = deque()
        if root.left is not None:
            q.append(root.left)
        if root.right is not None:
            q.append(root.right)
        res.append(root.val)
        while len(q) != 0:
            elem = q.popleft()
            res.append(elem.val)
            if elem.left is not None:
                q.append(elem.left)
            if elem.right is not None:
                q.append(elem.right)
        return res

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[str]]:
        if root is None:
            return [[]]
        res = []
        q = deque()
        res.append([root.val])
        child_count = 0
        if root.left is not None:
            q.append(root.left)
            child_count += 1
        if root.right is not None:
            q.append(root.right)
            child_count += 1
        child_count_2 = 0
        r = []

        for _ in range(child_count):
            elem = q.popleft()
            r.append(elem.val)
            if elem.left is not None:
                child_count_2 += 1
                q.append(elem.left)
            if elem.right is not None:
                child_count_2 += 1
                q.append(elem.right)
        res.append(r)
        child_count = 0
        r = []
        if len(q) == 0:
            return res
        for _ in range(child_count_2):
            elem = q.popleft()
            r.append(elem.val)
            if elem.left is not None:
                child_count += 1
                q.append(elem.left)
            if elem.right is not None:
                child_count += 1
                q.append(elem.right)
        res.append(r)

        return res

    def levelOrderList(self, root: Optional[TreeNode]) -> List[List[str]]:
        if root is None:
            return [[]]
        res = [[root]]
        for i in range(tree_height(root) - 1):
            r = []
            for elem in res[-1]:
                if elem.left:
                    r.append(elem.left)
                if elem.right:
                    r.append(elem.right)
            res.append(r)
        result = []
        for level in res:
            r = []
            for elem in level:
                r.append(elem.val)
            result.append(r)
        return result


def tree_height(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return max(tree_height(root.left) + 1, tree_height(root.right) + 1)


def get_nodes_on_level(root: Optional[TreeNode], level: int) -> List[str]:
    if tree_height(root) < level or level < 1:
        return []


if __name__ == '__main__':
    s = Solution()
    a = TreeNode('A', None, None)
    c = TreeNode('C', None, None)
    e = TreeNode('E', None, None)
    d = TreeNode('D', c, e)
    b = TreeNode('B', a, d)
    h = TreeNode('H', None, None)
    i = TreeNode('I', h, None)
    g = TreeNode('G', None, i)
    f = TreeNode('F', b, g)
    # z = s.levelorderTraversal(f)
    z = s.levelOrderList(f)
    print(z)
    # print(tree_height(f))

    # print(s.preorderTraversal(f))
