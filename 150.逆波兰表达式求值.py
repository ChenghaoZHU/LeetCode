#
# @lc app=leetcode.cn id=150 lang=python
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                stack.append(-stack.pop() + stack.pop())
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                stack.append(int(operator.truediv(stack.pop(-2), stack.pop())))
            else:
                stack.append(int(t))
        return stack.pop()

# @lc code=end

