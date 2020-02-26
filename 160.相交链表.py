#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p = headA
        while p:
            if p.next: p.next.prev = p
            p = p.next

        common = None
        p = headB
        while p:
            if p is headA:
                common = headA
                break
            if hasattr(p, 'prev'):
                common = p
                break
            p = p.next
        
        p = headA
        while p:
            if hasattr(p, 'prev'): del p.prev
            p = p.next
        
        return common
        
# @lc code=end

