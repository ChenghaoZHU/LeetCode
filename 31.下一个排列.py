#
# @lc app=leetcode.cn id=31 lang=python
#
# [31] 下一个排列
#

# @lc code=start
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 寻找最后的升序
        def helper(idx):
            i = idx - 1
            for i in xrange(idx - 1, -1, -1):
                if nums[idx] > nums[i]:
                    return i
            return -1

        l, r = 0, len(nums) - 1
        best_l = -1
        best_r = len(nums)
        while l < r:
            found = helper(r)
            if found != -1:
                if found > best_l and r < best_r:
                    best_l = found
                    best_r = r
                    l = best_l
            r -= 1
        if best_l != -1:
            nums[best_l], nums[best_r] = nums[best_r], nums[best_l]
            nums[best_l + 1:] = sorted(nums[best_l + 1:])
        else:
            nums.sort()

# @lc code=end

