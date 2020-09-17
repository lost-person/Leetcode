#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        p, q = dummy, head
        while q:
            if q.val == val:
                p.next = q.next
            else:
                p = q
            q = q.next
        return dummy.next


# @lc code=end
