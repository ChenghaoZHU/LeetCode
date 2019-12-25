#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        temp = x
        rvs_x = 0
        while temp:
            rvs_x = 10 * rvs_x + temp % 10
            temp /= 10
        return rvs_x  == x

# @lc code=end

