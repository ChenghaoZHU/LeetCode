#
# @lc app=leetcode.cn id=1025 lang=python
#
# [1025] 除数博弈
#

# @lc code=start
class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        def helper(n):
            tmp = []
            for i in xrange(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    if not dp[n - i]: return True
            return False

        dp = [0] * (N + 1)
        dp[1] = False
        i = 2
        while i <= N:
            dp[i] = helper(i)
            i += 1
        return dp[N]

# @lc code=end

