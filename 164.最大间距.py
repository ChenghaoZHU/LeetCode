#
# @lc app=leetcode.cn id=164 lang=python
#
# [164] 最大间距
#

# @lc code=start
class Solution(object):
    def maximumGap_with_heap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return 0
        from Queue import PriorityQueue
        queue = PriorityQueue()
        for n in nums: queue.put(n)
        res = 0
        n1 = queue.get(block=False)
        while queue.qsize():
            n2 = queue.get(block=False)
            res = max(res, n2 - n1)
            n1 = n2
        return res

    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return 0
        nums = sorted(nums)
        res = 0
        for i in xrange(len(nums) - 1):
            res = max(res, nums[i + 1] - nums[i])
        return res

# @lc code=end

