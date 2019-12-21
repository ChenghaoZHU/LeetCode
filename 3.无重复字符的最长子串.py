#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        head = 0
        seen = {}
        for tail in xrange(len(s)):
            ch = s[tail]
            if ch in seen:
                head = max(head, seen[ch])
            result = max(result, tail - head + 1)
            seen[ch] = tail + 1

        return result

# @lc code=end

