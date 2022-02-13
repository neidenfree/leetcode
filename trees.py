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


class Node(TreeNode):
    def __init__(self, val, left=None, right=None, next=None):
        super().__init__(val, left, right)
        self.next = next


def _mirror(root: Optional[TreeNode]) -> None:
    if root is None:
        return None
    temp = root.left
    root.left = root.right
    root.right = temp
    _mirror(root.left)
    _mirror(root.right)


def _comparison(root1: Optional[TreeNode], root2: Optional[TreeNode]):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.val != root2.val:
        return False
    if not _comparison(root1.left, root2.left):
        return False
    if not _comparison(root1.right, root2.right):
        return False
    return True


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

    def levelOrderList(self, root: Optional[TreeNode]) -> List[List[str]]:
        if root is None:
            return []
        res = [[root]]
        for i in range(tree_height(root) - 1):
            r = []
            for elem in res[-1]:
                if elem.left:
                    r.append(elem.left)
                if elem.right:
                    r.append(elem.right)
            res.append(r)
        return res

    def levelOrderListValues(self, root: Optional[TreeNode]) -> List[List[str]]:
        res = self.levelOrderList(root)
        result = []
        for level in res:
            r = []
            for elem in level:
                r.append(elem.val)
            result.append(r)
        return result

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def _maxDepth(root: Optional[TreeNode], ans) -> int:
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return ans
            return max(_maxDepth(root.left, ans + 1), _maxDepth(root.right, ans + 1))

        a = _maxDepth(root, 1)
        return a

    def print_tree(self, root: Optional[TreeNode]) -> None:
        def _print_tree(root: Optional[TreeNode], level: int):
            # print(f'print_tree({root} {level})')
            if root is None:
                return None
            _print_tree(root.right, level + 1)
            print(level * 10 * ' ', root.val)
            _print_tree(root.left, level + 1)

        _print_tree(root, 0)

    def isSymmetric_first(self, root: Optional[TreeNode]) -> bool:
        """
        This is my first attempt to solve the symmetric problem
        It turned out that it don't work if we have same values in left and right subtree
        for example,
                2
            2
        1
                2
            2
        this particular case must be non-symmetric, but my solution claims that it is
            symmetric.
        """

        def _left_traversal(root: Optional[TreeNode], res: List[object]):
            if root is None:
                return None
            _left_traversal(root.left, res)
            res.append(root.val)
            _left_traversal(root.right, res)

        def _right_traversal(root: Optional[TreeNode], res: List[object]):
            if root is None:
                return None
            _right_traversal(root.right, res)
            res.append(root.val)
            _right_traversal(root.left, res)

        left_res = []
        right_res = []
        _left_traversal(root.right, left_res)
        _right_traversal(root.left, right_res)
        print(left_res, right_res)
        if len(left_res) != len(right_res):
            return False
        return left_res == right_res

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        This is my second attempt. I think, that the best idea to solve this problem
        would be the following. At first, we must mirror the right subtree
        and then compare two tree. So we need two additional functions: mirroring the tree
        and tree comparison.
        """
        _mirror(root.right)
        print('Left tree:')
        self.print_tree(root.left)
        print('Right tree')
        self.print_tree(root.right)
        print('-----------')
        res = _comparison(root.left, root.right)
        # _mirror(root.right)
        return res

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def _path_sum(root: Optional[TreeNode], target: int, current: int) -> bool:
            if root is None:
                return False
            if root.left is None and root.right is None:
                print(current + root.val)
                return target == current + root.val
            if _path_sum(root.left, target, current + root.val):
                return True
            if _path_sum(root.right, target, current + root.val):
                return True
            return False

        return _path_sum(root, targetSum, 0)

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) != len(postorder):
            return None
        if len(inorder) == 0:
            return None
        # Let's assume, that in other ways our input is correct. Maybe it'll be
        # different elements in two arrays, maybe some elements will happen to be
        # in different amounts and so on. I can write code to check this,
        # but it will make the function too complex.
        # I found a solution, but it seems to be so hard for me
        # https://www.geeksforgeeks.org/construct-a-binary-tree-from-postorder-and-inorder/

    def _connect(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return None
        if root.left is not None and root.right is not None:
            root.left.next = root.right
        if root.left is not None and root.left.right is not None:
            root.left.right.next = root.right.left
        self._connect(root.left)
        self._connect(root.right)

    def connect(self, root: Optional[Node]) -> Optional[Node]:
        self._connect(root)
        return root

    def connect_all(self, root: Optional[Node]) -> Optional[Node]:
        """
        Actually, task said that you must provide a solution with constant extra space,
            which I don't get how to achieve this.
        But, the task said that you must provide this solution for PERFECT binary tree,
            which seems to be possible with constant extra space.
        Solution below works for all kinds of binary trees, not only perfect.
        But does it in O(N) space, where N is the count of nodes.
        """
        # self._connect(root)
        r = self.levelOrderList(root)
        for level in r:
            for i in range(len(level) - 1):
                level[i].next = level[i + 1]
        return root

    def lowestCommonAncestor_slow(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        At first, I need to write a function, which checks if there are element in the tree.
        Then I'll apply this function to left and right subtrees of root, trying to find
            p and q. If p and q are in the same branch, recur into that branch. Otherwise, return
                root of the branch.
            This straightforward approach worked quite well, but it turned out, that
                it is too slow for big trees. Let's try to optimize it!!!
        This is too slow solution, so I came with a better one
        """

        def is_value(root: Optional[TreeNode], value: int) -> bool:
            if root is None:
                return False
            if root.val == value:
                return True
            if root.left and is_value(root.left, value):
                return True
            if root.right and is_value(root.right, value):
                return True
            return False

        def lca(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            if root.val == p.val:
                return root
            if root.val == q.val:
                return root

            p_left = is_value(root.left, p.val)
            q_left = is_value(root.left, q.val)

            if not p_left and q_left:
                return root
            if p_left and not q_left:
                return root
            if not p_left and not q_left:
                return lca(root.right, p, q)
            if p_left and q_left:
                return lca(root.left, p, q)

        return lca(root, p, q)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Okay, here are better solution. So, you need to find path from the root to p and to q.
        Then, you compare this two paths and return the first different node.
        """

        def get_path(root: TreeNode, node: TreeNode, path: List[TreeNode]) -> List[TreeNode]:
            if root is None:
                return None
            if root.val == node.val:
                path += [root]
                return path
            return get_path(root.left, node, path + [root]) or get_path(root.right, node, path + [root])

        path_p = get_path(root, p, [])
        path_q = get_path(root, q, [])
        print('path_p = ', path_p)
        print('path_q = ', path_q)
        min_len = min(len(path_q), len(path_p))
        res = path_p[0]
        for i in range(0, min_len):
            if path_p[i] == path_q[i]:
                if path_p[i] == q or path_p[i] == p:
                    return path_p[i]
                res = path_p[i]
            else:
                return res



def lsa_test():
    sol = Solution()


    # f = TreeNode(0)
    # g = TreeNode(8)
    # h = TreeNode(7)
    # i = TreeNode(4)
    # d = TreeNode(6)
    # c = TreeNode(1, f, g)
    # e = TreeNode(2, h, i)
    # b = TreeNode(5, d, e)
    # a = TreeNode(3, b, c)
    #
    # # print(sol.preorderTraversal(a))
    # p = f
    # q = g
    # print(f'lca for {p} and {q} = ', sol.lowestCommonAncestor(c, p, q))
    # sol.print_tree(c)

    b = TreeNode(2)
    a = TreeNode(1, b, None)

    p = a
    q = b
    print(f'lca for {p} and {q} = ', sol.lowestCommonAncestor(a, p, q))
    sol.print_tree(a)



def test_connect():
    sol = Solution()
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)
    b = Node(2, d, e)
    c = Node(3, f, g)
    a = Node(1, b, c, None)
    sol.connect(a)
    sol.print_tree(a)


def test_has_sum():
    g = TreeNode(7, None, None)
    h = TreeNode(2, None, None)
    e = TreeNode(5, None, None)
    f = TreeNode(4, None, None)
    c = TreeNode(8, e, f)
    d = TreeNode(11, g, h)
    b = TreeNode(4, d, None)
    a = TreeNode(5, b, c)

    sol = Solution()
    sol.print_tree(a)
    # 27    22    18    17
    print(sol.hasPathSum(a, 1))
    print(sol.hasPathSum(None, 1))
    print(sol.hasPathSum(d, 20))


def test_symmetry():
    sol = Solution()
    # a31 = TreeNode(3, None, None)
    # a41 = TreeNode(4, None, None)
    # a21 = TreeNode(2, a31, a41)
    # a42 = TreeNode(4, None, None)
    # a32 = TreeNode(3, None, None)
    # a22 = TreeNode(2, a42, a32)
    # a1 = TreeNode(1, a21, a22)
    # sol.print_tree(a1)
    # assert sol.isSymmetric(a1)
    # print('--------------')
    #
    # a32 = TreeNode(3, None, None)
    # a22 = TreeNode(2, a32, None)
    # a31 = TreeNode(3, None, None)
    # a21 = TreeNode(2, a31, None)
    # a1 = TreeNode(1, a21, a22)
    #
    # # a.isSymmetric(a1)
    # sol.print_tree(a1)
    # assert not sol.isSymmetric(a1)

    f = TreeNode(5, None, None)
    c = TreeNode(3, f, None)
    e = TreeNode(5, None, None)
    d = TreeNode(4, None, None)
    b = TreeNode(3, d, e)
    a = TreeNode(2, b, c)
    sol.print_tree(a)
    print(sol.isSymmetric(a))

    # assert not sol.isSymmetric(a)


def tree_height(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return max(tree_height(root.left) + 1, tree_height(root.right) + 1)


def get_nodes_on_level(root: Optional[TreeNode], level: int) -> List[str]:
    if tree_height(root) < level or level < 1:
        return []


def test_traversal() -> None:
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
    s.print_tree(a)


def test_depth() -> None:
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
    s.print_tree(f)
    print('depth = ', s.maxDepth(f))


def test_comparsion() -> None:
    a2 = TreeNode(2, None, None)
    a1 = TreeNode(1, a2, None)
    b2 = TreeNode(2, None, None)
    b1 = TreeNode(1, None, b2)
    a = Solution()
    a.print_tree(a1)
    print('------------------------')
    a.print_tree(b1)
    print('-------Mirroring the second tree------')
    _mirror(b1)
    a.print_tree(b1)
    print(_comparison(a1, b1))


def test_traversals():
    n6 = TreeNode('6', None, None)
    n5 = TreeNode('5', None, n6)
    n7 = TreeNode('7', None, None)
    n8 = TreeNode('8', None, None)
    n2 = TreeNode('2', n7, n8)
    n3 = TreeNode('3', n5, n2)

    a = Solution()
    print(a.preorderTraversal(n3))
    print(a.inorderTraversal(n3))
    print(a.postorderTraversal(n3))


if __name__ == '__main__':
    lsa_test()
    # test_comparsion()
    # test_symmetry()

    # print(tree_height(f))

    # print(s.preorderTraversal(f))
