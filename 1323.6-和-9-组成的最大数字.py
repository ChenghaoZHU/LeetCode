#
# @lc app=leetcode.cn id=1323 lang=python
#
# [1323] 6 和 9 组成的最大数字
#

# @lc code=start
class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        for i, ch in enumerate(s):
            if ch == '6':
                break
        
        return int(s[:i] + '9' + s[i + 1:])

        
# @lc code=end

