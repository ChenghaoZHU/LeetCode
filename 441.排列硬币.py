#
# @lc app=leetcode.cn id=441 lang=python
#
# [441] 排列硬币
#

# @lc code=start
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        def judge(k, n):
            t = (k ** 2 + k) >> 1
            if t == n:
                return n
            elif t < n:
                return True
            else:
                return False
        
        l, r = 1, n
        while l <= r:
            mid = (l + r) >> 1
            t = judge(mid, n)
            if t is True:
                l = mid + 1
            elif t is False:
                r = mid - 1
            else:
                return mid
        return l - 1
        
# @lc code=end

