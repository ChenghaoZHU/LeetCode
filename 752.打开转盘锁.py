#
# @lc app=leetcode.cn id=752 lang=python
#
# [752] 打开转盘锁
#

# @lc code=start
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        dead = set(deadends)
        seen = {'0000'}
        queue = collections.deque([('0000', 0)])
        while queue:
            node, step = queue.popleft()
            if node == target: return step
            if node in dead: continue
            for n in self.expand(node):
                if n not in seen:
                    seen.add(n)
                    queue.append((n, step + 1))
        return -1

    def expand(self, node):
        for i in xrange(4):
            bit = int(node[i])
            for d in (1, -1):
                new_bit = (bit + d) % 10
                yield node[:i] + str(new_bit) + node[i + 1:]

# @lc code=end

