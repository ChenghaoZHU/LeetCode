#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1: return 0
        profit = 0
        temp = 0
        f = prices[0]
        for p in prices:
            if p - f >= temp:
                temp = p - f
            else:
                f = p
                profit += temp
                temp = 0
        profit += temp if temp else 0
        return profit

# @lc code=end

