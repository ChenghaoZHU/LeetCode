#
# @lc app=leetcode.cn id=561 lang=python
#
# [561] 数组拆分 I
#

# @lc code=start
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])

# @lc code=end

