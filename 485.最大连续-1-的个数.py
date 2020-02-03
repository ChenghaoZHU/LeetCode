#
# @lc app=leetcode.cn id=485 lang=python
#
# [485] 最大连续1的个数
#

# @lc code=start
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sp, fp = 0, 0
        result = -1
        while fp < len(nums):
            if nums[fp]:
                fp += 1
            else:
                result = max(result, fp - sp)
                sp = fp = fp + 1
        return max(result, fp - sp)     
            
        
# @lc code=end

