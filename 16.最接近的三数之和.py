#
# @lc app=leetcode.cn id=16 lang=python
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_diff = float('inf')
        res = target
        nums.sort()
        for i, n in enumerate(nums):
            s, e = i + 1, len(nums) - 1
            while s < e:
                sm = n + nums[s] + nums[e]
                tmp = target - sm
                if not tmp: return target
                if abs(tmp) < min_diff: 
                    res = sm
                    min_diff = abs(tmp)
                if tmp > 0: s += 1
                else: e -= 1
        return res

# @lc code=end

