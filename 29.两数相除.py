#
# @lc app=leetcode.cn id=29 lang=python
#
# [29] 两数相除
#

# @lc code=start
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MIN = - 1 << 31
        INT_MAX = (1 << 31) - 1
        sign = (dividend >= 0) ^ (divisor < 0)
        dvd = abs(dividend)
        dis = abs(divisor)
        if dvd < dis:
            return 0
        carry = 0
        while dis <= dvd:
            dis <<= 1
            carry += 1
        quotient = 0
        while carry:
            carry -= 1
            dis >>= 1
            if dvd >= dis:
                quotient += 1 << carry
                dvd -= dis
        if not sign: quotient = -quotient
        return quotient if INT_MIN <= quotient <= INT_MAX else INT_MAX

# @lc code=end

