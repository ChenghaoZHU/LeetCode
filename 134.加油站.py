#
# @lc app=leetcode.cn id=134 lang=python
#
# [134] 加油站
#

# @lc code=start
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        def valid(src):
            g = gas[src]
            c = cost[src]
            if g < c:
                return False
            i = (src + 1) % len(gas)
            while i != src:
                g += gas[i]
                c += cost[i]
                if g < c: return False
                i = (i + 1) % len(gas)
            return True

        for i in xrange(len(gas)):
            if valid(i):
                return i
        return -1

# @lc code=end

