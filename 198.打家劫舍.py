#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) < 3: return max(nums)
        dp = [0 for _ in xrange(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for i in xrange(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
        
# @lc code=end

