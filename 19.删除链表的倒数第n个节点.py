#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        sentinel = ListNode(0)
        sentinel.next = head

        to_del = cur = sentinel
        move = False
        i = 0
        while cur:
            cur = cur.next
            if not move:
                i += 1
                if i == n + 1:
                    move = True
            else:
                to_del = to_del.next
        if to_del != sentinel:
            to_del.next = to_del.next.next
        else:
            return head.next
        return head

# @lc code=end

