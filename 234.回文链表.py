#
# @lc app=leetcode.cn id=234 lang=python
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return True
        p1 = p2 = head
        p2 = p2.next
        count = 0
        while p2:
            p2.prev = p1
            p1 = p1.next
            p2 = p2.next
            count += 1
        p2 = p1
        p1 = head
        while p1 != p2 and count > -1:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.prev
            count -= 2
        return True

# @lc code=end

