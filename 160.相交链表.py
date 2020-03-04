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
    def getIntersectionNode_prev(self, headA, headB):
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
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return
        p1, p2 = headA, headB
        while p1.next:
            p1 = p1.next
        while p2.next:
            p2 = p2.next
        if p1 is not p2:
            return
        tail = p1
        p1, p2 = headA, headB
        while p1 is not p2:
            if p1 is tail:
                p1 = headB
            else:
                p1 = p1.next
            if p2 is tail:
                p2 = headA
            else:
                p2 = p2.next
        return p1
# @lc code=end

