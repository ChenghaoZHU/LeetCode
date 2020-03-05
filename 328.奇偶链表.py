#
# @lc app=leetcode.cn id=328 lang=python
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 用一个指针把偶数串起来
        # 最后续在奇数串后面
        if not head: return head
        odd = head
        sentinel = ListNode(0)
        even = sentinel
        while odd.next:
            even.next = odd.next
            even = even.next
            odd.next = even.next
            even.next = None
            if odd.next:
                odd = odd.next
            else:
                break
            
        odd.next = sentinel.next
        return head

# @lc code=end

