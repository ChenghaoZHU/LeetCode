#
# @lc app=leetcode.cn id=62 lang=python
#
# [62] 不同路径
#

# @lc code=start
class Solution(object):
    def uniquePaths_1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 递归超时
        m = m - 1
        n = n - 1
        return self.find_paths(m, n)
    
    def find_paths(self, m, n):
        if m and n:
            return self.find_paths(m - 1, n) + self.find_paths(m, n - 1)
        else:
            return 1
    
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 看答案以后发现空间还可优化
        # 因为dp当前行的计算只和上一行有关，故空间复杂度可以压缩到O(n)
        # 另外，你可以用组合数公式！
        if not n or not m: return 0
        dp = [[0] * n] * m

        for i in xrange(m):
            for j in xrange(n):
                if not (i and j): dp[i][j] = 1
                elif i and j:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                elif i:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]
        
        return dp[m - 1][n - 1]

# @lc code=end

