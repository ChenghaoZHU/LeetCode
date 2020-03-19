#
# @lc app=leetcode.cn id=205 lang=python
#
# [205] 同构字符串
#

# @lc code=start
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        mapping = {}
        seen = set()
        i = 0
        while i < len(s):
            if s[i] not in mapping:
                if t[i] in seen:
                    return False
                mapping[s[i]] = t[i]
                seen.add(t[i])
            elif mapping[s[i]] != t[i]:
                return False
            i += 1
        return True

# @lc code=end

