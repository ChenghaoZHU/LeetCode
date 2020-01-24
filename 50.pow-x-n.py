#
# @lc app=leetcode.cn id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0: return 0
        if n == 0: return 1
        if x == 1: return 1
        if x == -1:
            if n % 2 == 1:
                return -1
            else:
                return 1
        MIN_INT = - 1 << 31
        MAX_INT = - MIN_INT - 1
        sign = 1 if n >= 0 else -1
        n = abs(n)

        low = 1
        cache = x
        while low < n and cache:
            if 2 * low <= n:
                cache = cache * cache
                low *= 2
            else:
                cache = cache * x
                low += 1
        
        if sign == 1:
            return min(cache, MAX_INT)
        else:
            return max(1 / cache, MIN_INT)

# @lc code=end

