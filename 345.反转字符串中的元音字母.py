#
# @lc app=leetcode.cn id=345 lang=python
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = set('aeiouAEIOU')
        l, r = 0, len(s) - 1
        while l < r:
            while l < len(s) - 1 and s[l] not in vowels:
                l += 1
            if l >= r: break
            while r >= 0 and s[r] not in vowels:
                r -= 1
            if r < 0: break
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)
        
# @lc code=end

