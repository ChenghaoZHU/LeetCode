#
# @lc app=leetcode.cn id=27 lang=python
#
# [27] 移除元素
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        sp = 0
        for n in nums:
            if n != val:
                nums[sp] = n
                sp += 1
        return sp

# @lc code=end

