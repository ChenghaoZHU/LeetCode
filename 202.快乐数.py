#
# @lc app=leetcode.cn id=202 lang=python
#
# [202] 快乐数
#

# @lc code=start
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set([n])
        while n != 1:
            temp = 0
            while n:
                i = n % 10
                temp += i ** 2
                n = n / 10
            n = temp
            if n in visited: return False
            visited.add(n)
        return True

# @lc code=end

