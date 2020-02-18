#
# @lc app=leetcode.cn id=103 lang=python
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue = [root]
        res = []
        i = 0
        while queue:
            i += 1
            level = []
            temp = []
            while queue:
                node = queue.pop(0)
                temp.append(node.val)
                if node.left: level.append(node.left)
                if node.right: level.append(node.right)
            queue = level
            res.append(temp if i % 2 else temp[::-1])
        return res
        
# @lc code=end

