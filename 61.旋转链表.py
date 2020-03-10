#
# @lc app=leetcode.cn id=61 lang=python
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        size = 1
        p = head
        while p and p.next:
            p = p.next
            size += 1
        p.next = head
        
        p = head
        m = size - k % size
        while m > 1:
            p = p.next
            m -= 1
        head = p.next
        p.next = None
        return head

# @lc code=end

