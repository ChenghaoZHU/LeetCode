#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x: return x
        low, hig = 1, x
        while low <= hig:
            mid = low + (hig - low) / 2
            r = mid * mid
            if r == x:
                return mid
            if r > x:
                hig = mid - 1
            else:
                low = mid + 1
        return low - 1
                  
# @lc code=end

