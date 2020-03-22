#
# @lc app=leetcode.cn id=771 lang=python
#
# [771] 宝石与石头
#

# @lc code=start
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        res = 0
        J = set(J)
        for i in S:
            if i in J:
                res += 1
        return res
        
# @lc code=end

