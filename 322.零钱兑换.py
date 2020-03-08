#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins: return -1
        if not amount: return 0
        coins = sorted(coins, reverse=True)
        self.res = float('inf')

        def dfs(i, res, step):
            if not res:
                self.res = min(self.res, step)
                return
            if i == len(coins):
                return  
            coin = coins[i]
            n = res / coin
            while n >= 0:
                if n + step >= self.res:
                    break  # 这个剪枝尤为重要
                dfs(i + 1, res - n * coin, step + n)
                n -= 1
        
        dfs(0, amount, 0)
        return self.res if self.res != float('inf') else -1
        
# @lc code=end

