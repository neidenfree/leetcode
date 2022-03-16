from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, elem):
        if type(elem) == ListNode:
            elem.next = self.head
            self.head = elem
        else:
            temp = ListNode(elem, None)
            temp.next = self.head
            self.head = temp

    def __str__(self):
        s = "["
        head = self.head
        while head is not None:
            s += str(head.val) + ', '
            head = head.next
        s = s[:len(s) - 2]
        s += ']'
        return s


def add_to_list(head: ListNode, elem):
    temp = ListNode(val=elem)
    temp.next = head
    head = temp
    return head


def print_list(head: ListNode):
    new_head = head
    while new_head:
        print(new_head)
        new_head = new_head.next


def create_linked_list_from_array(nums: List[int]) -> Optional[ListNode]:
    if nums is None or len(nums) == 0:
        return None
    first = ListNode(nums[0])
    head = first

    zz = True
    for elem in nums:
        if zz:
            zz = False
            continue
        t = ListNode(elem)
        first.next = t
        first = t

    return head


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._add(val, self.root)

    def _add(self, val: int, node: TreeNode):
        if val < node.val:
            if node.left:
                self._add(val, node.left)
            else:
                node.left = TreeNode(val)
        if val > node.val:
            if node.right:
                self._add(val, node.right)
            else:
                node.right = TreeNode(val)

    def print_tree_l(self):
        if self.root is not None:
            self._print_tree_l(self.root, 0)

    def _print_tree_l(self, node: TreeNode, k: int):
        if node is not None:
            self._print_tree_l(node.right, k + 1)
            print(' ' * k * 3 + str(node.val))
            self._print_tree_l(node.left, k + 1)

    def print_tree_up(self):
        if self.root is not None:
            self._print_tree_up(self.root, 0)

    def _print_tree_up(self, node: TreeNode, k: int):
        if node is None:
            return
        queue = [node]
        while len(queue) > 0:
            cur_node = queue.pop(0)
            print(cur_node.val)
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        p_cur = head
        p_prev = head
        p_n = head
        while n > 0:
            p_n = p_n.next
            n -= 1
        if p_n is None:
            head = head.next
            return head

        flag = False
        while p_n:
            p_cur = p_cur.next
            p_n = p_n.next
            if flag:
                p_prev = p_prev.next
            else:
                flag = True
        if p_cur is None:
            p_prev.next = None
        else:
            p_prev.next = p_cur.next
        del p_cur
        return head

    # @staticmethod
    def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = head
        while p1:
            if p1.next is None:
                return p2
            elif p1.next.next is None:
                return p2.next
            else:
                p1 = p1.next.next
            p2 = p2.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        if temp1 is None and temp2 is None:
            return None

        if temp1 is None:
            return temp2
        if temp2 is None:
            return temp1

        if temp1.val <= temp2.val:
            res = ListNode(temp1.val)
            temp1 = temp1.next
        else:
            res = ListNode(temp2.val)
            temp2 = temp2.next

        prev = res

        while temp1 is not None or temp2 is not None:
            if temp1 is None:
                t = ListNode(temp2.val)
                temp2 = temp2.next
            elif temp2 is None:
                t = ListNode(temp1.val)
                temp1 = temp1.next
            elif temp1.val <= temp2.val:
                t = ListNode(temp1.val)
                temp1 = temp1.next
            elif temp1.val > temp2.val:
                t = ListNode(temp2.val)
                temp2 = temp2.next
            res.next = t
            res = t
        return prev


def test_merge_lists():
    l1 = create_linked_list_from_array([])
    l2 = create_linked_list_from_array([])

    a = Solution()
    res = a.mergeTwoLists(l1, l2)
    print('Debug')


def test_create_list():
    t1 = create_linked_list_from_array([1, 2, 3, 4, 5])
    t2 = create_linked_list_from_array([1])
    t3 = create_linked_list_from_array([1, 2])
    t4 = create_linked_list_from_array([])
    print('Debug')



if __name__ == "__main__":
    test_merge_lists()
    # test_create_list()
    # head = ListNode(5)
    # head = add_to_list(head, 4)
    # head = add_to_list(head, 3)
    # head = add_to_list(head, 2)
    # head = add_to_list(head, 1)
    # head = add_to_list(head, 5)
    #
    # a = Solution()
    # # print_list(Solution.middleNode(head=head))
    # n = 2
    # print_list(a.removeNthFromEnd(head=head, n=n))
