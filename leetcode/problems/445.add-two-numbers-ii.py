#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        def get_length(ListNode):
            length = 0
            node = ListNode

            while node:
                node = node.next
                length += 1

            return length

        def print_linked_list(l):
            node = l
            while node:
                print(node.val, end=" ")
                node = node.next

        N, M = get_length(l1), get_length(l2)

        # Gurantee l1 is longer or equal than l2
        if N < M:
            N, M = M, N
            l1, l2 = l2, l1

        new_num = ListNode()
        node = new_num
        for _ in range(N - M):
            node.next = ListNode()
            node = node.next
            node.val = l1.val

            l1 = l1.next

        while l1:
            s = l1.val + l2.val
            carry_in, carry_out = s // 10, s - (s // 10 * 10)
            node.val += carry_in

            node.next = ListNode(carry_out)
            node = node.next

            l1, l2 = l1.next, l2.next

        return new_num.next


# @lc code=end
