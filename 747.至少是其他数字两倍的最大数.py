#
# @lc app=leetcode.cn id=747 lang=python
#
# [747] 至少是其他数字两倍的最大数
#

# @lc code=start
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        max_idx = -1
        max_val = float('-inf')
        pre_max = float('-inf')
        for i, n in enumerate(nums):
            if n > max_val:
                pre_max = max_val
                max_val = n
                max_idx = i
            elif n > pre_max:
                pre_max = n
                
        return max_idx if max_val >= 2 * pre_max else -1
        
# @lc code=end

