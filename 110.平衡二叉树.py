#
# @lc app=leetcode.cn id=110 lang=python
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node):
            if not node: return True, 0
            lb, lh = dfs(node.left)
            if not lb: return False, 0
            rb, rh = dfs(node.right)
            if not rb: return False, 0
            return abs(lh - rh) <= 1, max(lh, rh) + 1
        
        return dfs(root)[0]

# @lc code=end

