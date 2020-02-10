#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i]表示第i阶楼梯有多少种方法
        dp = [0 for _ in xrange(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in xrange(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
        
# @lc code=end

