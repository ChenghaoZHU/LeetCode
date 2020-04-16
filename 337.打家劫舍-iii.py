#
# @lc app=leetcode.cn id=337 lang=python
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node: return 0, 0
            if not (node.left or node.right):
                return node.val, 0  # 包含顶点最大值，不包最大值
            
            l1, l2 = dfs(node.left)
            r1, r2 = dfs(node.right)
            
            return (node.val + l2 + r2, max(l1, l2) + max(r1, r2))
        
        return max(dfs(root))
        
# @lc code=end

