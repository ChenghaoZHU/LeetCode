#
# @lc app=leetcode.cn id=268 lang=python
#
# [268] 缺失数字
#

# @lc code=start
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (1 + n) / 2 - sum(nums)

        
# @lc code=end

