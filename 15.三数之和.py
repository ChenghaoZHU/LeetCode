#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        l = len(nums)
        if l < 3:
            return results
        else:
            nums.sort()
        i = 0
        while i < l:
            if nums[i] > 0: return results
            while i > 0 and nums[i - 1]  == nums[i]:
                if i >= l - 2: return results
                i += 1  # 去掉重复元素
            left = i + 1
            right = l - 1
            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                if sum3 == 0:
                    results.append([nums[i], nums[left], nums[right]])
                    # 去掉重复元素
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum3 > 0:
                    right -= 1
                else:
                    left += 1
            i += 1

        return results

# @lc code=end

