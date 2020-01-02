#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        cur = 0
        for i, n in enumerate(nums[1:], 1):
            if nums[cur] != n:
                cur += 1
                nums[cur] = n
        return cur + 1

# @lc code=end

