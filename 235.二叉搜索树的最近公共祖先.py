#
# @lc app=leetcode.cn id=235 lang=python
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def get_path(root, node):
            path = []
            while root:
                path.append(root)
                if root.val == node.val:
                    break
                elif root.val > node.val:
                    root = root.left
                else:
                    root = root.right
            return path
        
        p1 = get_path(root, p)
        p2 = get_path(root, q)

        for i in xrange(min(len(p1), len(p2)) - 1, -1, -1):
            if p1[i] == p2[i]:
                return p1[i]
        
# @lc code=end

