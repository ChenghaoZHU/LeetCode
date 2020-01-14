#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if not n:
            return []
        elif n == 1:
            return [[nums[0]]]
        result = []
        for temp in self.permute(nums[:n - 1]):
            for i in xrange(n):
                l = temp[:]
                l.insert(i, nums[n-1])
                result.append(l)
        return result

# @lc code=end

