#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = float('-inf')
        total = 0
        for i in nums:
            total += i
            result = max(result, total)
            if total < 0:
                total = 0
        return result

# @lc code=end

