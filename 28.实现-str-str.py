#
# @lc app=leetcode.cn id=28 lang=python
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        n = len(haystack)
        for i in xrange(n):
            found = i
            for j, ch in enumerate(needle):
                if i + j == n: return -1
                if ch != haystack[i + j]:
                    found = -1
                    break
            if found >= 0: return found

        return -1
        
# @lc code=end

