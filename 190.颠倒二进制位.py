#
# @lc app=leetcode.cn id=190 lang=python
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        stack = []
        while n:
            stack.append(n % 2)
            n = n >> 1
        length = len(stack)
        stack[length: 32] = [0 for i in xrange(32 - length)]
        i = 0
        while stack:
            n += (stack.pop() << i)
            i += 1
        return n

# @lc code=end

