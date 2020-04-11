#
# @lc app=leetcode.cn id=657 lang=python
#
# [657] 机器人能否返回原点
#

# @lc code=start
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        counter = collections.defaultdict(int)
        for i in moves:
            counter[i] += 1
        
        return counter['L'] == counter['R'] and counter['U'] == counter['D']
        
# @lc code=end

