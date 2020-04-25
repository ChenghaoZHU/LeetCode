#
# @lc app=leetcode.cn id=415 lang=python
#
# [415] 字符串相加
#

# @lc code=start
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        trans = {str(i): i for i in xrange(10)}

        res = []
        carry = 0
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        for _ in xrange(len(num1) - len(num2)):
            num2 = '0' + num2
        
        for i in xrange(len(num1)):
            i = len(num1) - i - 1
            a, b = num1[i], num2[i]
            c = trans[a] + trans[b] + carry
            carry = c / 10
            res.append(c % 10)

        if carry: res.append(1)

        return ''.join(map(str, res[::-1]))
        

        
# @lc code=end

