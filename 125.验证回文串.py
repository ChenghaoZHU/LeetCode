#
# @lc app=leetcode.cn id=125 lang=python
#
# [125] 验证回文串
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l < r:
            ch1 = s[l]
            ch2 = s[r]
            if not ch1.isalnum():
                l += 1
            elif not ch2.isalnum():
                r -= 1
            elif ch1.lower() == ch2.lower():
                l += 1
                r -= 1
            else:
                return False
        return True
        
# @lc code=end

