#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        sp = 0
        for fp in xrange(len(nums)):
            if nums[fp] != 0:
                nums[sp], nums[fp] = nums[fp], nums[sp]
                sp += 1
        
# @lc code=end

