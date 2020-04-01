#
# @lc app=leetcode.cn id=1111 lang=python
#
# [1111] 有效括号的嵌套深度
#

# @lc code=start
class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        return [(i & 1) ^ (s == ')') for i, s in enumerate(seq)]
        
# @lc code=end

