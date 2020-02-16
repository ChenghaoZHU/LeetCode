#
# @lc app=leetcode.cn id=75 lang=python
#
# [75] 颜色分类
#

# @lc code=start
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        s = 0  # 暂存点
        while l < r:
            if not nums[l]:
                if s != l:
                    nums[s], nums[l] = nums[l], nums[s]
                l += 1
                s += 1
            elif nums[l] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        if not nums[l]: nums[s], nums[l] = nums[l], nums[s]

# @lc code=end

