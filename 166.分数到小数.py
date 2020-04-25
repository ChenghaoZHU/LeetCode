#
# @lc app=leetcode.cn id=166 lang=python
#
# [166] 分数到小数
#

# @lc code=start
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator % denominator == 0:
            return str(numerator / denominator)
        res_f = float(numerator) / denominator
        res_s = str(res_f)
        res = list(res_s)
        if res_f != float(res_s):
            res[-1] = res[-2]
        if res[res.index('.') + 1:].count(res[-1]) > 2 and float(''.join(res)) * denominator != numerator:
            i = res[-1]
            while res[-1] == i:
                res.pop()
            res.append('(%s)' % i)
            return ''.join(res)
        return ''.join(res)

# @lc code=end

