#
# @lc app=leetcode.cn id=133 lang=python
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return node
        duplica = Node(node.val)
        cur = duplica  # 移动指针
        vst_node = {cur.val: cur}  # 复制过的节点
        vst_edge = set([(cur.val, n.val) for n in node.neighbors])  # 复制过的边
        stack = [(cur, n) for n in node.neighbors]  # n复制后加入cur.neighbors
        while stack:
            cur, n = stack.pop()
            val = n.val
            if val in vst_node:
                d = vst_node[val]
            else:
                d = Node(val)
                vst_node[val] = d
            cur.neighbors.append(d)
            for n in n.neighbors:
                if (val, n.val) not in vst_edge:
                    stack.append((d, n))
                    vst_edge.add((val, n.val))

        return duplica

# @lc code=end

