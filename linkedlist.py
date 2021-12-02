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
        # ВОЗМОЖНО НЕВЕРНО, Я ТУТ НЕЧАЯННО НАТЫКАЛ ЧЕГО_ТО
        self.head = new_list.head

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
        """
        Write code to partition a linked list around a value X, such that all nodes less
            than X come before all nodes greater than or equal to X. If X is contained within
            the list, the values of X only need to be after the elements less than X.
        The partition element X can appear anywhere in the "right partition";
            it does not need to appear between the left and right partitions.

        This is slightly faster solution than partition_old: we have only one iteration
            over all elements from original linked list.
        """
        if self.head is None:
            return
        if self.head.next is None:
            return
        head_less = None
        head_greater = None
        temp_head = None
        head = self.head
        while head is not None:
            if head.val < k:
                if head_less is None:
                    head_less = ListNode(head.val)
                    temp_head = head_less
                else:
                    temp = ListNode(head.val)
                    temp.next = head_less
                    head_less = temp
            else:
                if head_greater is None:
                    head_greater = ListNode(head.val)
                else:
                    temp = ListNode(head.val)
                    temp.next = head_greater
                    head_greater = temp
            head = head.next
        if temp_head is not None:
            temp_head.next = head_greater
            self.head = head_less

    def partition_old(self, k: int) -> None:
        """
        Straightforward solution.
        :param k:
        :return:
        """
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

    def sum_lists(self, other: LinkedList) -> int:
        """
        Well working method. There are tests that cover all possible cases:
                assert LinkedList([9, 9]).sum_lists(LinkedList([9, 9])) == 198
                assert LinkedList([9, 9, 9]).sum_lists(LinkedList([9, 9])) == 1098
                assert LinkedList([9]).sum_lists(LinkedList([9, 9])) == 108
                assert LinkedList([2, 1]).sum_lists(LinkedList([3, 8])) == 95
                assert LinkedList([9, 1]).sum_lists(LinkedList([3, 8])) == 102
                assert LinkedList([9, 1]).sum_lists(LinkedList([3, 8])) == 102
                assert LinkedList([3, 8]).sum_lists(LinkedList()) == 83
                assert LinkedList([1, 1, 1, 1, 1, 1, 1]).sum_lists(LinkedList([3])) == 1111114
        """
        if self.head is None and other.head is None:
            return 0

        result = 0
        rank = 1
        remainder = 0
        head = self.head
        head2 = other.head

        while head is not None and head2 is not None:
            temp = head.val + head2.val + remainder
            remainder = 0
            if temp > 9:
                remainder = 1
                temp = temp % 10
            result += temp * rank
            rank *= 10
            head = head.next
            head2 = head2.next

        if head is None:
            head = head2

        if head is not None:
            while head is not None:
                temp = head.val + remainder
                remainder = 0
                if temp > 9:
                    remainder = 1
                    temp = temp % 10
                result += rank * temp
                rank *= 10
                head = head.next
        if remainder == 1:
            result += rank
        return result

    def is_palindrome(self) -> bool:
        if self.head is None:
            return True
        if self.head.next is None:
            return True
        l2 = LinkedList()
        head = self.head
        while head is not None:
            l2.add(head.val)
            head = head.next
        head = self.head
        head2 = l2.head
        while head is not None:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True


class CircularList:
    """
    Thought it'd be useful for Loop Detection, but it's not, actually.
    """
    def __init__(self, val=None):
        if val is None:
            self.head = None
        else:
            self.head = ListNode(val=val, next=self.head)

    def add(self, val) -> None:
        if self.head is None:
            self.head = ListNode(val=val, next=self.head)
            self.head.next = self.head
            return

        temp = ListNode(val, self.head.next)
        self.head.next = temp
        self.head = temp

        # self.head = temp

    def infinite_loop(self, k: int = 100) -> None:
        if self.head is None:
            return None
        head = self.head
        iters = 0
        while head is not None and iters < k:
            print(head.val)
            iters += 1
            head = head.next


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


def is_intersect(a: ListNode, b: ListNode) -> bool:
    if a is None or b is None:
        return False
    run1 = a
    run2 = b
    while run1.next is not None:
        run1 = run1.next
    while run2.next is not None:
        run2 = run2.next
    return run1 == run2


def get_intersect_node(a: ListNode, b: ListNode) -> Optional[ListNode]:
    import ctypes

    if not is_intersect(a, b):
        return None
    addr_a = LinkedList()
    addr_b = LinkedList()
    run_a = a
    run_b = b
    while run_a is not None:
        addr_a.add(id(run_a))
        run_a = run_a.next
    while run_b is not None:
        addr_b.add(id(run_b))
        run_b = run_b.next
    temp = None
    run_a = addr_a.head
    run_b = addr_b.head
    print(addr_a)
    print(addr_b)
    while run_a is not None and run_b is not None and run_a.val == run_b.val:
        temp = run_a.val
        run_a = run_a.next
        run_b = run_b.next
    if temp is None:
        raise Exception("WHAT??")
    print(temp)
    return ctypes.cast(temp, ctypes.py_object).value
    # return ctypes.cast(temp, ctypes.py_object)

    # return False


def test_intersect_node() -> None:
    a = ListNode(8)
    a.next = ListNode(5)
    a.next.next = ListNode(2)
    a.next.next.next = ListNode(3)
    a.next.next.next.next = ListNode(9)

    b = ListNode(21)
    b.next = a.next.next.next

    print(get_intersect_node(a, b))


def get_loop_start_node(a: ListNode) -> Optional[ListNode]:
    if a is None:
        return None
    addr = {}
    head = a
    while head is not None:
        if id(head) in addr:
            return head
        addr[id(head)] = 1
        head = head.next

def test_get_loop_start_node() -> None:
    a = ListNode(7, None)
    a.next = ListNode(8)
    a.next.next = ListNode(1)
    a.next.next.next = ListNode(2)
    a.next.next.next.next = ListNode(3)
    a.next.next.next.next.next = a.next.next.next
    print(get_loop_start_node(a))






if __name__ == "__main__":

    pass
    # test_intersect_node()


    # assert is_intersect(a, b)
    # run = b
    # while run is not None:
    #     print(run.val)
    #     run = run.next

    # assert is_intersect(a, b)
