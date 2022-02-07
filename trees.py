from typing import Optional, List
# from stacksandqueries import Queue
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

    def levelorderTraversal(self, root: Optional[TreeNode]) -> None:
        """
        :param root:
        :return:
        """

        if root is None:
            return None
        q = deque()
        if root.left is not None:
            q.append(root.left)
        if root.right is not None:
            q.append(root.right)
        print(root.val)
        while len(q) != 0:
            elem = q.popleft()
            print(elem.val)
            if elem.left is not None:
                q.append(elem.left)
            if elem.right is not None:
                q.append(elem.right)

        # if root is not None:
        #     q = deque()
        #     print(root.val)
        #     q.append(root.left)
        #     q.append(root.right)
        #     q2 = deque()
        #     for elem in q:
        #         if elem is not None:
        #             print(elem.val)
        #             q2.append(elem.left)
        #             q2.append(elem.right)
        #     q = deque()
        #     for elem in q2:
        #         if elem is not None:
        #             print(elem.val)
        #             q.append(elem.left)
        #             q.append(elem.right)
        #     q2 = deque()
        #     for elem in q:
        #         if elem is not None:
        #             print(elem.val)
        #             q2.append(elem.left)
        #             q2.append(elem.right)
        #     for elem in q2:
        #         if elem is not None:
        #             print(elem.val)
        #             q.append(elem.left)
        #             q.append(elem.right)


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
    s.levelorderTraversal(f)

    # print(s.preorderTraversal(f))
