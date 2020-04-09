#
# @lc app=leetcode.cn id=112 lang=python
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        def dfs(node, residue):
            if not (node.left or node.right):
                if not residue: return True
                return False

            return bool(node.left) and dfs(node.left, residue - node.left.val) or \
                bool(node.right) and dfs(node.right, residue - node.right.val)
        
        return dfs(root, sum - root.val)
            

# @lc code=end

