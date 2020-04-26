#
# @lc app=leetcode.cn id=997 lang=python
#
# [997] 找到小镇的法官
#

# @lc code=start
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        counter = collections.defaultdict(int)  # 记录入度
        for a, b in trust:
            counter[a] = N  # a有出度，将其入度设为N，之后a就相当于被排除
            counter[b] += 1  # b入度加1
        
        for i in xrange(1, N + 1):
            if counter[i] == N - 1:  # 找到法官
                return i
        return -1
        
# @lc code=end

