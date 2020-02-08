#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        hight = 0
        if root:
            queue = [(root, 1)]
            while queue:
                node, h = queue.pop()
                hight = max(h, hight)
                if node.left: queue.append((node.left, h + 1))
                if node.right: queue.append((node.right, h + 1))

        return hight
        
# @lc code=end

