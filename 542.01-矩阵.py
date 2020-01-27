#
# @lc app=leetcode.cn id=542 lang=python
#
# [542] 01 矩阵
#

# @lc code=start
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(matrix), len(matrix[0])
        self.cache = {}
        self.matrix = matrix
        self.rows, self.cols = rows, cols
        new_values = [self.bfs(r, c) for r in xrange(rows) for c in xrange(cols)]
        for r in xrange(rows):
            for c in xrange(cols):
                matrix[r][c] = new_values.pop(0)
        return matrix

    def get_from_cache(self, r, c):
        temp = []
        if (r - 1, c) in self.cache: temp.append(self.cache[(r - 1, c)]) 
        if (r, c + 1) in self.cache: temp.append(self.cache[(r, c + 1)])
        if (r + 1, c) in self.cache: temp.append(self.cache[(r + 1, c)])
        if (r, c - 1) in self.cache: temp.append(self.cache[(r, c - 1)])
        if temp:
            min_val = min(temp)
            if not min_val or len(temp) == 4:
                self.cache[(r, c)] = min_val + 1
                return self.cache[(r, c)]
        return None

    def bfs(self, r, c):
        # use cache to accelerate
        if self.matrix[r][c]:
            val = self.get_from_cache(r, c)
            if val is not None:
                return val
        else:
            self.cache[(r, c)] = 0
            return 0

        queue = [(r, c, 0)]
        visited = set()
        while queue:
            r, c, step = queue.pop(0)
            if not self.matrix[r][c]:
                self.cache[(r, c)] = step
                return step
            visited.add((r, c))
            if r - 1 >= 0 and (r - 1, c) not in visited:
                queue.append((r - 1, c, step + 1))
            if c + 1 < self.cols and (r, c + 1) not in visited:
                queue.append((r, c + 1, step + 1))
            if r + 1 < self.rows and (r + 1, c) not in visited:
                queue.append((r + 1, c, step + 1))
            if c - 1 >= 0 and (r, c - 1) not in visited:
                queue.append((r, c - 1, step + 1))
        return step + 1

# @lc code=end

