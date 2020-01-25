#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            node = stack.pop()
            if isinstance(node, int):
                result.append(node)
                continue
            if node.right: stack.append(node.right)
            stack.append(node.val)
            if node.left: stack.append(node.left)
            
        return result

# @lc code=end

