#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        for i in xrange(len(s), 0, -1):
            right = len(s) - 1
            left = right - i + 1
            while left >= 0:
                if self.isPalindrome(s, left, right):
                    return s[left: right + 1]
                right -= 1
                left -= 1

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        
# @lc code=end

