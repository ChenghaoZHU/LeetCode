#
# @lc app=leetcode.cn id=263 lang=python
#
# [263] 丑数
#

# @lc code=start
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        if num == 1: return True
        for i in (2, 3, 5):
            while num % i == 0:
                num /= i
        if num == 1: return True
        return False

# @lc code=end

