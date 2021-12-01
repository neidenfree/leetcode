from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self, head: ListNode = None):
        self.head = head

    def add(self, elem):
        if type(elem) == ListNode:
            elem.next = self.head
            self.head = elem
        else:
            temp = ListNode(elem, None)
            temp.next = self.head
            self.head = temp

    def print_reverse(self):
        def reverse_rec(head: ListNode) -> None:
            if head is None:
                return
            reverse_rec(head.next)
            print(head)

        def reverse_iter(head: ListNode) -> None:
            a = []
            while head is not None:
                a.append(head.val)
                head = head.next
            print(a[::-1])

        head_temp = self.head
        reverse_rec(head_temp)
        return None

    def copy(self) -> Optional[LinkedList]:
        def rec_copy(head: ListNode, new_head: LinkedList) -> None:
            if head is None:
                return None
            rec_copy(head.next, new_head)
            new_head.add(head.val)

        h = self.head
        nh = LinkedList()
        rec_copy(h, nh)
        return nh

    # def copy(self) -> Optional[LinkedList]:
    #     if self.head is None:
    #         return None
    #     head = self.head
    #     new_head = LinkedList()
    #     while head is not None:
    #         new_head.add(head.val)
    #         head = head.next
    #     return new_head

    def delete_node(self, val) -> None:
        head = self.head
        if head is None:
            return None
        if head.val == val:
            self.head = head.next
        while head.next is not None:
            if head.next.val == val:
                head.next = head.next.next
            head = head.next

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


if __name__ == "__main__":
    l = LinkedList()
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(4)
    l.add(5)
    # l.delete_node(1)
    l.delete_node(4)
    print(l)

