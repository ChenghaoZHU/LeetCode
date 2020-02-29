#
# @lc app=leetcode.cn id=547 lang=python
#
# [547] 朋友圈
#

# @lc code=start
class UnionFind(object):
    def __init__(self, n):
        self.roots = [i for i in xrange(n)]
    
    def find(self, node):
        while self.roots[node] != node:
            self.roots[node] = self.roots[self.roots[node]]  # 路径压缩
            node = self.roots[node]
        return node
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.roots[root2] = root1
    
    def isConnected(self, node1, node2):
        return self.roots[node1] == self.roots[node2]

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(len(M))
        for i in xrange(len(M) - 1):
            for j in xrange(i + 1, len(M)):
                if M[i][j] == 1: uf.union(i, j)
        
        return len([i for i in xrange(len(M)) if uf.roots[i] == i])


# @lc code=end

