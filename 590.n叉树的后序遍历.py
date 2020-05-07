#
# @lc app=leetcode.cn id=590 lang=python
#
# [590] N叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if isinstance(node, int):
                res.append(node)
            else:
                stack.append(node.val)
                for i in node.children[::-1]:
                    stack.append(i)
        return res
        
# @lc code=end

