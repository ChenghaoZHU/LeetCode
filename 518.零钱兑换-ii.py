#
# @lc app=leetcode.cn id=518 lang=python
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        nums = [0] * len(coins)
        nums[-1] = amount / coins[-1]
        

# @lc code=end

