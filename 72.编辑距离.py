#
# @lc app=leetcode.cn id=72 lang=python
#
# [72] 编辑距离
#

# @lc code=start
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1), len(word2)
        if not word1 or not word2:
            return max(l1, l2)
        dp = [[0] * (l2 + 1) for _ in xrange(l1 + 1)] 
        for i in xrange(1, l1 + 1):
            dp[i][0] = i
        for i in xrange(1, l2 + 1):
            dp[0][i] = i
        
        for i in xrange(1, l1 + 1):
            for j in xrange(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j])
        return dp[i][j]
        # dp[i][j - 1]表示word2新增
        # dp[i - 1][j]表示word1新增
        # dp[i - 1][j - 1]表示修改word1或word2
# @lc code=end

