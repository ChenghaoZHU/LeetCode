#
# @lc app=leetcode.cn id=310 lang=python
#
# [310] 最小高度树
#

# @lc code=start
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        E = collections.defaultdict(list)
        matrix = [[n] * n for _ in xrange(n)]
        for i, j in edges:
            E[i].append(j)
            E[j].append(i)

        def bfs(src, best):
            que = collections.deque()
            que.append(([src], set([src])))
            while que:
                path, visited = que.popleft()
                if len(path) > best: return
                src = path[-1]
                for i in E[src]:
                    if i not in visited:
                        for dis, j in enumerate(path[::-1], 1):
                            matrix[j][i] = matrix[i][j] = dis
                        new_path = path + [i]
                        que.append((new_path, set(new_path)))

        best = n
        res = []
        for i in xrange(n):
            matrix[i][i] = 0
            if max(matrix[i]) == n:
                bfs(i, best)
            tmp = max(matrix[i])
            if tmp < best:
                best = tmp
                res = [i]
            elif tmp == best:
                res.append(i)

        return res

# @lc code=end

