#
# @lc app=leetcode.cn id=213 lang=python
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return max(nums or [0])
        def helper(nums):
            if len(nums) <= 2:
                return max(nums or [0])
            a, b = nums[0], max(nums[0], nums[1])
            for i in xrange(2, len(nums)):
                a, b = b, max(a + nums[i], b)
            return b
        return max(helper(nums[:-1]), helper(nums[1:]))

# @lc code=end

