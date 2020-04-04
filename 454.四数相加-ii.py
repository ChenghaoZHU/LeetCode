#
# @lc app=leetcode.cn id=454 lang=python
#
# [454] 四数相加 II
#

# @lc code=start
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB_sum = {}
        for i in A:
            for j in B:
                if i + j in AB_sum:
                    AB_sum[i + j] += 1
                else:
                    AB_sum[i + j] = 1
        res = 0
        for i in C:
            for j in D:
                if -(i + j) in AB_sum:
                    res += AB_sum[-(i + j)]
        return res

# @lc code=end

