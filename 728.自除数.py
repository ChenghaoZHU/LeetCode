#
# @lc app=leetcode.cn id=728 lang=python
#
# [728] 自除数
#

# @lc code=start
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def selfDivided(n):
            t = n
            while t:
                d = t % 10
                if not d: return False
                if n % d != 0: return False
                t /= 10
            return True
        res = []
        for i in xrange(left, right + 1):
            if selfDivided(i):
                res.append(i)
        return res
        
# @lc code=end

