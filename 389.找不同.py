#
# @lc app=leetcode.cn id=389 lang=python
#
# [389] 找不同
#

# @lc code=start
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        c = Counter()
        c.update(t)
        c.subtract(s)
        for i, j in c.iteritems():
            if j == 1: return i
        
# @lc code=end

