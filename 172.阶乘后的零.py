#
# @lc app=leetcode.cn id=172 lang=python
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 5
        res = 0
        while n / k:
            res += n / k
            k *= 5
        return res
# @lc code=end

