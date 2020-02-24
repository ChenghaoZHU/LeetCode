#
# @lc app=leetcode.cn id=138 lang=python
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return head
        built = {}
        
        def copy(node):
            if not node: return node
            if node in built: return built[node]
            new_node = Node(node.val)
            built[node] = new_node
            new_node.next = copy(node.next)
            new_node.random = copy(node.random)
            return new_node
        
        new_head = copy(head)
        return new_head

# @lc code=end

