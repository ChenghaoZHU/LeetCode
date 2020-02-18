#
# @lc app=leetcode.cn id=91 lang=python
#
# [91] 解码方法
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        dp = [0 for i in xrange(len(s))]
        dp[0] = 1 if s[0] != '0' else 0
        if not dp[0]: return 0
        for i in xrange(1, len(s)):
            if s[i] != '0':
                dp[i] = dp[i - 1]
                if s[i - 1] != '0' and int(s[i -1 ] + s[i]) <= 26:
                    dp[i] += dp[i - 2] if i >= 2 else 1
            else:  # s[i]为0，s[i]只能和s[i - 1]结合
                if s[i - 1] == '0' or int(s[i - 1] + s[i]) > 26: return 0
                dp[i] = dp[i - 2] if i >= 2 else 1

        return dp[-1]
        
# @lc code=end

