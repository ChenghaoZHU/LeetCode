#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = ['']
        mapping = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            elif mapping[ch] == stack.pop():
                continue
            else:
                return False
        return False if stack[-1] else True
   
# @lc code=end

