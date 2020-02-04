#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 旋转数组
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        i, count = 0, 0
        while count < n and i < k:
            r = (i + k) % n
            temp = nums[i]
            while r != i:
                nums[r], temp = temp, nums[r]
                count += 1
                r = (r + k) % n
            nums[i] = temp
            count += 1
            i += 1

# @lc code=end

