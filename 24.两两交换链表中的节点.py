#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sentinel = ListNode(None)
        sentinel.next = head
        p = sentinel
        while p and p.next and p.next.next:
            tail = p.next.next.next
            a = p.next
            b = p.next.next
            p.next = b
            b.next = a
            a.next = tail
            p = p.next.next
        return sentinel.next

# @lc code=end

