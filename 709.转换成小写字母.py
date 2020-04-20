#
# @lc app=leetcode.cn id=709 lang=python
#
# [709] 转换成小写字母
#

# @lc code=start
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        base = ord('a')
        delta = base - ord('A')
        res = []
        for ch in str:
            if ch.isalpha() and ord(ch) < base:
                res.append(chr(ord(ch) + delta))
            else:
                res.append(ch)
        return ''.join(res)
        
# @lc code=end

