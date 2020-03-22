#
# @lc app=leetcode.cn id=219 lang=python
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        idict = {}
        for i, n in enumerate(nums):
            if n not in idict:
                idict[n] = i
            elif i - idict[n] <= k:
                return True
            else:
                idict[n] = i
        return False
# @lc code=end

