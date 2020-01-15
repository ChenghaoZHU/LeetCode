#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = grid
        self.rows = len(grid)
        if not self.rows:
            return 0
        self.cols = len(grid[0])
        if not self.cols:
            return 0
        num = 0
        self.visited = set()
        for r in xrange(self.rows):
            for c in xrange(self.cols):
                num += self.expand(r, c)
        
        return num
                
    def expand(self, r, c):
        if (r, c) in self.visited or self.grid[r][c] == '0':
            return 0
        queue = [(r,c)]
        while len(queue):
            size = len(queue)
            for _ in xrange(size):
                r, c = queue[0]
                if r - 1 >= 0 and self.grid[r - 1][c] == '1' and (r - 1, c) not in self.visited:
                    queue.append((r - 1, c))
                    self.visited.add((r - 1, c))
                if c + 1 < self.cols and self.grid[r][c + 1] == '1' and (r, c + 1) not in self.visited:
                    queue.append((r, c + 1))
                    self.visited.add((r, c + 1))
                if r + 1 < self.rows and self.grid[r + 1][c] == '1' and (r + 1, c) not in self.visited:
                    queue.append((r + 1, c))
                    self.visited.add((r + 1, c))
                if c - 1 >= 0 and self.grid[r][c - 1] == '1' and (r, c - 1) not in self.visited:
                    queue.append((r, c - 1))
                    self.visited.add((r, c - 1))
                self.visited.add(queue.pop(0))
        return 1
# @lc code=end

