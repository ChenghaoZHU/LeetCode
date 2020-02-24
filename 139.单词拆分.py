#
# @lc app=leetcode.cn id=139 lang=python
#
# [139] 单词拆分
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in xrange(1, len(s) + 1):
            for j in xrange(0, i):
                dp[i] = dp[j] and s[j: i] in wordDict
                if dp[i]: break
                
        return dp[-1]

# @lc code=end

