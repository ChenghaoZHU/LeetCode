#
# @lc app=leetcode.cn id=242 lang=python
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        seen = {}
        for ch in s:
            if ch in seen:
                seen[ch] += 1
            else:
                seen[ch] = 1
        for ch in t:
            if ch in seen:
                seen[ch] -= 1
                if seen[ch] == 0:
                    seen.pop(ch)
            else:
                return False
        
        return False if len(seen) else True
     
# @lc code=end

