#
# @lc app=leetcode.cn id=394 lang=python
#
# [394] 字符串解码
#

# @lc code=start
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        temp = ''
        for ch in s:
            if ch.isdigit():
                if temp and not temp.isdigit():
                    stack.append(temp)
                    temp = ''
                temp += ch
            elif ch == '[':
                stack.append(temp)
                temp = ''
            elif ch == ']':
                if temp: 
                    stack.append(temp)
                    temp = ''
                self.expand(stack)
            else:
                if temp and temp.isdigit():
                    temp = ''
                temp += ch
        if temp: stack.append(temp)
        self.expand(stack)
        return stack[0]
    
    def expand(self, stack):
        repeat = 1
        strs = ''
        while stack:
            i = stack.pop()
            if i.isdigit():
                repeat = int(i)
                break
            else:
                strs = i + strs
        stack.append(repeat * strs)
        
# @lc code=end

