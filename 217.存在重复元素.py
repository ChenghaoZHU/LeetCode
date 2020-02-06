#
# @lc app=leetcode.cn id=217 lang=python
#
# [217] 存在重复元素
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        _set = set()
        for i, n in enumerate(nums, 1):
            _set.add(n)
            if len(_set) != i:
                return True
        return False
        
# @lc code=end

