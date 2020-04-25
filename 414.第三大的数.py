#
# @lc app=leetcode.cn id=414 lang=python
#
# [414] 第三大的数
#

# @lc code=start
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq
        heap = []
        in_h = set()
        for n in nums:
            if n in in_h:
                continue
            if len(heap) == 3:
                if n < heap[0]: continue
                in_h.discard(heapq.heappop(heap))
            heapq.heappush(heap, n)
            in_h.add(n)

        return heap[0] if len(heap) != 2 else heap[1]

# @lc code=end

