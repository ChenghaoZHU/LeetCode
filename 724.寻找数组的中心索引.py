#
# @lc app=leetcode.cn id=724 lang=python
#
# [724] 寻找数组的中心索引
#

# @lc code=start
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1
        if len(nums) == 1: return 0
        left = 0
        right = sum(nums)
        for i, n in enumerate(nums):
            right -= nums[i]
            if left == right: return i
            left += nums[i]
        return -1

# @lc code=end

