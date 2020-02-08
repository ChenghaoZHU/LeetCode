#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        # 中序遍历树结构，获得的值应该是排序的数组
        stack = [root]
        min_val = float('-inf')
        while stack:
            node = stack.pop()
            if isinstance(node, TreeNode):
                if node.right: stack.append(node.right)
                stack.append(node.val)
                if node.left: stack.append(node.left)
            else:
                if node <= min_val: return False
                min_val = node
        return True

# @lc code=end

