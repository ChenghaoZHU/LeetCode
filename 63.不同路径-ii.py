#
# @lc app=leetcode.cn id=63 lang=python
#
# [63] 不同路径 II
#

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in xrange(m)]
        if obstacleGrid[0][0] == 1: return 0
        dp[0][0] = 1
        reach = 1
        for i in xrange(1, m):
            if obstacleGrid[i][0] == 1 and reach == 1:
                reach = 0
            dp[i][0] = reach

        reach = 1
        for j in xrange(1, n):
            if obstacleGrid[0][j] == 1 and reach == 1:
                reach = 0
            dp[0][j] = reach
        
        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[-1][-1]
                
# @lc code=end

