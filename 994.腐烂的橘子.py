#
# @lc app=leetcode.cn id=994 lang=python
#
# [994] 腐烂的橘子
#

# @lc code=start
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        queue = []

        def bfs(r, c):
            if r - 1 >= 0 and grid[r - 1][c] not in visited:
                if grid[r - 1][c] == 1:
                    queue.append((r - 1, c))
                elif grid[r - 1][c] == 0:
                    visited.add((r - 1, c))
            if c + 1 < len(grid[0]) and grid[r][c + 1] not in visited:
                if grid[r][c + 1] == 1:
                    queue.append((r, c + 1))
                elif grid[r][c + 1] == 0:
                    visited.add((r, c + 1))
            if r + 1 < len(grid) and grid[r + 1][c] not in visited:
                if grid[r + 1][c] == 1:
                    queue.append((r + 1, c))
                elif grid[r + 1][c] == 0:
                    visited.add((r + 1, c))
            if c - 1 >= 0 and grid[r][c - 1] not in visited:
                if grid[r][c - 1] == 1:
                    queue.append((r, c - 1))
                elif grid[r][c - 1] == 0:
                    visited.add((r, c - 1))

        t = 0
        while 1:
            queue = []
            for r in xrange(rows):
                for c in xrange(cols):
                    if grid[r][c] in visited: continue
                    if grid[r][c] == 0:
                        visited.add((r, c))
                    elif grid[r][c] == 2:
                        visited.add((r, c))
                        bfs(r, c)
            if not queue: break
            else: 
                t += 1
                while queue:
                    r, c = queue.pop()
                    grid[r][c] = 2

        return -1 if any([j == 1 for i in grid for j in i]) else t
            

# @lc code=end

