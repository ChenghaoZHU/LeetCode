#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        # 层序遍历时验证每层是否对称
        queue = [root]
        while queue:
            nums = []
            level = []
            while queue:
                node = queue.pop(0)
                nums.append(node.val if node else None)
                if node:
                    level.append(node.left or None)
                    level.append(node.right or None)
            queue = level
            if not self.is_symmetric(nums): return False
        return True
    
    def is_symmetric(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] != nums[r]: return False
            l += 1
            r -= 1
        return True

# @lc code=end

