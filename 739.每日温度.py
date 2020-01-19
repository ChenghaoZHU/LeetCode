#
# @lc app=leetcode.cn id=739 lang=python
#
# [739] 每日温度
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        size = len(T)
        result = [0] * size
        stack = []
        for i in xrange(size - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack: result[i] = stack[-1] - i
            stack.append(i)

        return result

# @lc code=end

