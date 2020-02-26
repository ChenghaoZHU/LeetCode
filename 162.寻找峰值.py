#
# @lc app=leetcode.cn id=162 lang=python
#
# [162] 寻找峰值
#

# @lc code=start
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) / 2
            if mid == 0:
                if mid + 1 < len(nums) and nums[mid] > nums[mid + 1] or mid + 1 == len(nums):
                    return mid
                else:
                    l = mid + 1
            elif mid == len(nums) - 1:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    r = mid + 1
            else:
                if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                    return mid
                elif nums[mid + 1] > nums[mid - 1]:
                    l = mid + 1
                else:
                    r = mid - 1

# @lc code=end

