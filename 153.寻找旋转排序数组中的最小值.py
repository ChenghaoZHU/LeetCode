#
# @lc app=leetcode.cn id=153 lang=python
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] >= nums[0]:
                left = mid + 1
            elif mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            else:
                right = mid - 1
        return nums[0]  # 数组没有pivotal
# @lc code=end

