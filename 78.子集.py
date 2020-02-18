#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]

        _map = {n: i for i, n in enumerate(nums)}
        _map[None] = -1
        level = [[]]
        for i in xrange(len(nums)):
            temp = []
            for l in level:
                j = _map[l[-1] if l else None]
                for n in nums[j + 1:]:
                    k = l[:]
                    k.append(n)
                    temp.append(k)
            level = temp
            result.extend(level)

        return result

# @lc code=end

