#
# @lc app=leetcode.cn id=1038 lang=python
#
# [1038] 从二叉搜索树到更大和树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        def helper(root):
            if not root: return None
            helper(root.right)
            root.val += self.sum
            self.sum = root.val
            helper(root.left)
            return root
        helper(root)
        return root
# @lc code=end

