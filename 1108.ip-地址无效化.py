#
# @lc app=leetcode.cn id=1108 lang=python
#
# [1108] IP 地址无效化
#

# @lc code=start
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        res = []
        for i in address:
            if i == '.':
                res.append('[.]')
            else:
                res.append(i)
        return ''.join(res)
        
# @lc code=end

