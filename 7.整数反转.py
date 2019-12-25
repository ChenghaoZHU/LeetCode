#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        while x:
            n = x % 10
            x /= 10
            result = 10 * result + n
        result = sign * result
        if result >= 2**31 or result < -2**31:
            return 0 
        return result
        
# @lc code=end

