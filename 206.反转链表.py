#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 循环
        # if not head or not head.next: return head

        # h, r = head, None
        # while h:
        #     tmp = h.next
        #     h.next = r
        #     r = h
        #     h = tmp
        # return r

        # 递归
        if not head or not head.next: return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return p


# @lc code=end
