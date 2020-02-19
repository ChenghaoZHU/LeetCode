#
# @lc app=leetcode.cn id=124 lang=python
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ms = float('-inf')
        def maxSum(root):
            if not root: return 0
            left = maxSum(root.left)
            right = maxSum(root.right)
            self.ms = max(self.ms, root.val + left + right)
            return max(0, max(left, right) + root.val)
        maxSum(root)
        return self.ms
        
# @lc code=end

