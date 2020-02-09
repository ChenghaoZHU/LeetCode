#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root: return result
        queue = [root]
        while queue:
            temp = []
            level = []
            while queue:
                node = queue.pop(0)
                temp.append(node.val)
                if node.left: level.append(node.left)
                if node.right: level.append(node.right)
            result.append(temp)
            queue = level
        return result

# @lc code=end

