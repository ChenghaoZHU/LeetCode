#
# @lc app=leetcode.cn id=430 lang=python
#
# [430] 扁平化多级双向链表
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return head
        p = head
        while p:
            child = self.flatten(p.child)
            if child:
                p.child = None
                tail = p.next
                p.next = child
                child.prev = p
                while p and p.next:
                    p = p.next
                p.next = tail
                if tail: tail.prev = p

            p = p.next
        
        return head

# @lc code=end

