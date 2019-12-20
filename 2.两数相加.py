#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
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
        result = ListNode(0)  # initialize
        current = result
        add_one = 0
        for i, j in self.next_move(l1, l2):
            new_node = ListNode((i + j + add_one) % 10)
            current.next = new_node
            current = new_node
            add_one = (i + j + add_one) / 10
        if add_one:  # more than 10
            current.next = ListNode(1)
        
        return result.next  # cut off the head, which is just a placeholder

    @staticmethod
    def next_move(l1, l2):
        """
        move to next node simultaneously
        """
        p1 = l1
        p2 = l2
        while p1 or p2:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            yield v1, v2
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            
        
# @lc code=end

