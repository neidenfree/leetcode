from __future__ import annotations
from typing import Optional, Union


class ListNode:
    def __init__(self, val=None, next: ListNode = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class LinkedList:
    """
    All tasks from CTCI:
    1+. Demove duplicates 2+. Return Kth to last element
    3+. Delete middle node  4. Partition (?)
    5. Sum two lists (big numbers sum) 6. Palindrome
    7. Intersection (?) 8. Lood detection (?)
    """

    # Overrides

    def __init__(self, head: Union[ListNode, list] = None):
        self.head: ListNode = None
        if type(head) == ListNode:
            self.head = head
        if type(head) == list:
            for el in reversed(head):
                self.add(el)

    def __str__(self):
        s = ""
        head = self.head
        while head is not None:
            s += str(head.val) + ' -> '
            head = head.next
        s += 'null'
        return s

    # Vital methods
    def add(self, elem):
        if type(elem) == ListNode:
            elem.next = self.head
            self.head = elem
        else:
            temp = ListNode(elem, None)
            temp.next = self.head
            self.head = temp

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

    # Tasks
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

    def remove_duplicates(self) -> None:
        """
        Modified version, seems to be working well.
        :return:
        """
        if self.head is None:
            return None
        head = self.head
        temp_head = self.head
        values = {head.val: 1}
        while head is not None and head.next is not None:
            if head.next.val in values:
                temp = head.next
                while temp is not None and temp.val in values:
                    temp = temp.next
                head.next = temp
            else:
                values[head.next.val] = 1
            head = head.next
        self.head = temp_head

    def remove_duplicates_addition(self) -> None:
        """
        Simplified version with other linked list
        :return:
        """
        if self.head is None:
            return None
        head = self.head
        values = {}
        while head is not None:
            values[head.val] = 1
            head = head.next
        new_list = LinkedList()
        for val in reversed(list(values.keys())):
            new_list.add(val)
        self.head = l.head

    def get_kth_from_to_last(self, k: int) -> Optional[ListNode]:
        if self.head is None:
            return None
        head = self.head
        head2 = self.head
        for i in range(k):
            if head2 is not None:
                head2 = head2.next
            else:
                return None
        while head2 is not None:
            head2 = head2.next
            head = head.next
        return head

    def bubble_sort(self) -> None:
        """
        This method has function id in it. As I understand, it is some kind
        of analogue of & operator in C.
        Quote: "CPython implementation detail: This is the address of the object in memory."
                https://docs.python.org/3/library/functions.html#id
        :return:
        """
        head = self.head
        while head is not None:
            head2 = head
            while head2 is not None:
                if head2.val < head.val:
                    head.val, head2.val = head2.val, head.val
                print(id(head), id(head2))
                head2 = head2.next
            head = head.next

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

    def middle_node(self) -> Optional[ListNode]:
        if self.head is None:
            return None
        if self.head.next is None:
            return self.head
        head = self.head
        temp = self.head
        while temp is not None:
            temp = temp.next
            if temp is not None:
                temp = temp.next
            else:
                return head
            if temp is None:
                return head
            head = head.next
        return head

    def delete_middle_node(self) -> None:
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
        head = self.head
        temp = self.head
        temp_head = head
        while temp.next is not None:
            temp = temp.next
            if temp.next is not None:
                temp = temp.next
            else:
                break
            if temp.next is None:
                break
            head = head.next
        print("ЗАЛУУПА")
        head.next = head.next.next
        self.head = temp_head
        # return head

    def partition(self, k: int) -> None:
        if self.head is None:
            return
        if self.head.next is None:
            return
        head_less = LinkedList()
        head_greater = LinkedList()
        head = self.head
        while head is not None:
            if head.val < k:
                head_less.add(head.val)
            else:
                head_greater.add(head.val)
            head = head.next
        head = head_less.head
        while head.next is not None:
            head = head.next
        head.next = head_greater.head
        self.head = head_less.head



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
    l = LinkedList([8, 5, 20, 5, 10, 2, 8])
    # l.add(2)
    # l.add(4)
    # l.add(3)
    # l.add(1)
    # l.add(6)
    # l.add(6)
    # l.add(2)
    print(l)
    l.partition(8)
    print(l)

    # print(l.middle_node())
    # l.delete_middle_node()
    # print(l)

    # print(l.middle_node())
    # l.print_reverse()
    # print(l.get_kth_from_to_last(1))
    # l.remove_duplicates()
    # print(l)
