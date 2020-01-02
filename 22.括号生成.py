#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 0: return ['']
        results = [[''], ['()']]
        for i in xrange(2, n + 1):
            temp = []
            for j in xrange(i):
                inner = results[j]
                outer = results[i - 1 - j]
                for ic in inner:
                    for oc in outer:
                        temp.append('(' + ic + ')' + oc)
            results.append(temp)
        return results[n]

# @lc code=end

