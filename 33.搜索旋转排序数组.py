#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if target == nums[mid]:
                return mid
            if (nums[0] > target) ^ (nums[mid] < nums[0]) ^ (nums[mid] < target):
                left = mid + 1
            else:
                right = mid
        
        return left if nums[left] == target else -1

# @lc code=end

