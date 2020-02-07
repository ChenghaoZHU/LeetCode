#
# @lc app=leetcode.cn id=387 lang=python
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = [0 for _ in xrange(26)]
        for i, ch in enumerate(s):
            seen[ord(ch) - ord('a')] += 1
        for i, ch in enumerate(s):
            if seen[ord(ch) - ord('a')] == 1:
                return i
        return -1

# @lc code=end

