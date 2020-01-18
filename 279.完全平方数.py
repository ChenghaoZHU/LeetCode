#
# @lc app=leetcode.cn id=279 lang=python
#
# [279] 完全平方数
#

# @lc code=start
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue = collections.deque([(n, 0)])
        visited = {n}
        while queue:
            n, depth = queue.popleft()
            for v in (n - i ** 2 for i in xrange(1, int(n ** 0.5) + 1)):
                if v == 0: return depth + 1
                if v not in visited:
                    queue.append((v, depth + 1))
                    visited.add(v)

# @lc code=end

