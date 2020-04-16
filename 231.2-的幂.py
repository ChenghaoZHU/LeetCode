#
# @lc app=leetcode.cn id=231 lang=python
#
# [231] 2的幂
#

# @lc code=start
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        while n != 1:
            if n & 1 == 1: return False
            n = n >> 1
        return True
# @lc code=end

