#
# @lc app=leetcode.cn id=67 lang=python
#
# [67] 二进制求和
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a
        result = []
        carry = 0
        for i in xrange(len(b)):
            i = -i - 1
            x, y = a[i], b[i]
            if x == '1' and y == '1':
                if carry:
                    result.append('1')
                else:
                    result.append('0')
                    carry = 1
            elif x == '0' and y == '0':
                if carry:
                    result.append('1')
                    carry = 0
                else:
                    result.append('0')
            else:
                if carry:
                    result.append('0')
                else:
                    result.append('1')

        for ch in a[:len(a)-len(b)][::-1]:
            if carry:
                if ch == '1': result.append('0')
                else:
                    result.append('1')
                    carry = 0
            else:
                result.append(ch)
        if carry: result.append('1')

        return ''.join(result[::-1])
# @lc code=end

