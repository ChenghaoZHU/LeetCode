#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        cp = ''  # common prefix
        i = 0
        stop = False
        while 1:
            p = ''
            for s in strs:
                if i == len(s):
                    stop = True
                    break
                elif not p:
                    p = s[i]
                elif p != s[i]:
                    stop = True
                    break
            if stop: break
            cp += p
            i += 1
        return cp
        
# @lc code=end

