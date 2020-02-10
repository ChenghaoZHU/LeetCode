#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        p1, p2 = 0, 1
        while p2 < len(prices):
            if prices[p2] - prices[p1] < 0:
                p1 = p2
            else:
                profit = max(prices[p2] - prices[p1], profit)
            p2 += 1
        return profit

# @lc code=end

