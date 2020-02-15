#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals: return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        temp = intervals.pop(0)
        while intervals:
            i = intervals.pop(0)
            c = self.combine(temp, i)
            if c:
                temp = c
            else:
                res.append(temp)
                temp = i
        res.append(temp)
        return res
    
    def combine(self, a, b):
        if a[1] < b[0]: return None
        return [a[0], max(a[1], b[1])]

        
# @lc code=end

