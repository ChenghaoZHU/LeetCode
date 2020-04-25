#
# @lc app=leetcode.cn id=1304 lang=python
#
# [1304] 和为零的N个唯一整数
#

# @lc code=start
class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        b = 0
        for i in xrange(1, n / 2 + 1):
            res.append(i)
            res.append(-i)
        
        if n % 2:
            res.append(0)
        
        return res


        
# @lc code=end

