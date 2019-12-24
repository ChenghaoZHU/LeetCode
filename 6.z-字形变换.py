#
# @lc app=leetcode.cn id=6 lang=python
#
# [6] Z 字形变换
#

# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        data = ['' for i in xrange(numRows)]
        i = 0
        d = 1
        for c in s:
            data[i] += c
            i += d
            if i == numRows:
                i -= 1
            elif i == -1:
                i = 0
            if i == numRows - 1:
                d = -1
            elif i == 0:
                d = 1
            
        return ''.join(data)
        
# @lc code=end

