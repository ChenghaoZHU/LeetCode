#
# @lc app=leetcode.cn id=34 lang=python
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        found = -1
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            found = left
        if found == -1:
            return [-1, -1]
        
        found2 = found
        left = found
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left + 1) / 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        if nums[right] == target:
            found2 = right
        return [found, found2]
        
# @lc code=end

