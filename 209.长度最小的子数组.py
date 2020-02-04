#
# @lc app=leetcode.cn id=209 lang=python
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        res = len(nums) + 1
        sm = 0
        while right < len(nums):
            sm += nums[right]
            right += 1
            while sm >= s:
                res = min(res, right - left)
                sm -= nums[left]
                left += 1

        return res if res != len(nums) + 1 else 0
  
# @lc code=end

