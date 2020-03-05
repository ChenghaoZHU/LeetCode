#
# @lc app=leetcode.cn id=203 lang=python
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        sentinel = ListNode(0)
        sentinel.next = head
        p = sentinel
        c = head
        while c:
            if c.val == val:
                p.next = c.next
                c = p.next
            else:
                p = c
                c = c.next
        return sentinel.next

# @lc code=end

