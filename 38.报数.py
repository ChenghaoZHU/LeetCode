#
# @lc app=leetcode.cn id=38 lang=python
#
# [38] 报数
#

# @lc code=start
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        
        pre = self.countAndSay(n - 1)
        result = ''
        p = pre[0]
        c = 0
        for i in pre:
            if i != p:
                result += '%d%s' % (c, p)
                c = 1
                p = i
            else:
                c += 1
        result += '%d%s' % (c, p)
        return result

# @lc code=end

