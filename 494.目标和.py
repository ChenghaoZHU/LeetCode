#
# @lc app=leetcode.cn id=494 lang=python
#
# [494] 目标和
#

# @lc code=start
class Solution(object):
    def bfs(self, nums, S):
        total = sum(nums)
        if S > total or S < -total:
            return 0  # 剪枝

        size = len(nums)
        n = nums[0]
        if size == 1:
            return int(n == S) + int(n == -S)

        # 使用缓存
        cache = self.cache
        size -= 1
        if (size, S - n) in cache:
            x = cache[(size, S - n)]
        else:
            x = self.bfs(nums[1:], S - n)
            cache[(size, S - n)] = x
        if (size, S + n) in cache:
            y = cache[(size, S + n)]
        else:
            y = self.bfs(nums[1:], S + n)
            cache[(size, S + n)] = y

        return x + y

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.cache = {}
        return self.bfs(nums, S)

# @lc code=end

