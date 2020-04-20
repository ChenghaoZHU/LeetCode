#
# @lc app=leetcode.cn id=114 lang=python
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root: return None
        right = self.flatten(root.right)
        left = self.flatten(root.left)

        root.right = left
        root.left = None

        prev = root
        while left:
            prev = left
            left = left.right
        prev.right = right

        return root
# @lc code=end

