#
# @lc app=leetcode.cn id=342 lang=python
#
# [342] 4的幂
#

# @lc code=start
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s = bin(num)[2:]
        return s[0] == '1' and not int(s[1:] or 0) and len(s) % 2
# @lc code=end

