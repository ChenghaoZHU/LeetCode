#
# @lc app=leetcode.cn id=445 lang=python
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def get_num(l):
            n = 0
            while l:
                n *= 10
                n += l.val
                l = l.next
            return n
        
        n1 = get_num(l1)
        n2 = get_num(l2)
        res = str(n1 + n2)
        head = ListNode(res[0])
        p = head
        for i in res[1:]:
            p.next = ListNode(i)
            p = p.next
        return head
        
# @lc code=end

