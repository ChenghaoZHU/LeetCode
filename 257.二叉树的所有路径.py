#
# @lc app=leetcode.cn id=257 lang=python
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root: return []
        from itertools import imap
        res = []
        def dfs(path, node):
            if not node.left and not node.right:
                res.append('->'.join(imap(str, path)))
                return
            
            if node.left:
                dfs(path + [node.left.val], node.left)
            if node.right:
                dfs(path + [node.right.val], node.right)

        dfs([root.val], root)
        return res
# @lc code=end

