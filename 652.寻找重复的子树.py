#
# @lc app=leetcode.cn id=652 lang=python
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        node_id_dict = collections.defaultdict()
        node_id_dict.default_factory = node_id_dict.__len__
        visited = collections.defaultdict(int)
        def dfs(node):
            if not node: return
            node_id = node_id_dict[node.val, dfs(node.left), dfs(node.right)]
            visited[node_id] += 1
            if visited[node_id] == 2:
                res.append(node)
            return node_id
        dfs(root)
        return res
        
# @lc code=end

