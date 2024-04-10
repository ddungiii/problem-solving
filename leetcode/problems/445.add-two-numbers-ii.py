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
        nodes = [new_num]

        node = new_num
        index = 0
        for _ in range(N - M):
            node.next = ListNode()
            node = node.next
            node.val = l1.val

            nodes.append(node)
            index += 1

            l1 = l1.next

        while l1:
            s = l1.val + l2.val
            carry_in, carry_out = s // 10, s - (s // 10 * 10)

            prev_index = index
            while carry_in:
                prev_node = nodes[prev_index]
                prev_node.val += carry_in

                if prev_node.val < 10:
                    break

                prev_node.val -= 10
                prev_index -= 1

            node.next = ListNode(carry_out)
            node = node.next
            nodes.append(node)
            index += 1

            l1, l2 = l1.next, l2.next

        return new_num if new_num.val > 0 else new_num.next


# @lc code=end
