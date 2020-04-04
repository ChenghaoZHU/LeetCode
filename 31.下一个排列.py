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
        def helper(p):
            while p > 1:
                if nums[p] > nums[p - 1]:
                    nums[p], nums[p - 1] = nums[p - 1], nums[p]
                    while p < len(nums) - 1:
                        if nums[p] < nums[p + 1]:
                            nums[p], nums[p + 1] = nums[p + 1], nums[p]
                        p += 1
                    return True
                p -= 1
            return False
        
        p = len(nums) - 1
        while p > 1:
            if helper(p): return
            p -= 1
        l, r = 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        for i in xrange(1, len(nums)):
            if nums[i] > nums[0]:
                nums[0], nums[i] = nums[i], nums[0]
                return
        nums.append(nums.pop(0))


# @lc code=end

