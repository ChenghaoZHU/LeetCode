#
# @lc app=leetcode.cn id=378 lang=python
#
# [378] 有序矩阵中第K小的元素
#

# @lc code=start
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # 多路归并
        # O(k * n) 最差 O(n^2)
        n = len(matrix)
        pointers = [0] * n
        while k:
            temp = [(matrix[pointers[i]][i], i) for i in xrange(n) if pointers[i] < n]
            min_val, min_col = min(temp, key=lambda x: x[0])  # 线性扫描可以改成使用优先队列，变成logn
            pointers[min_col] += 1
            k -= 1
        return min_val


    def kthSmallest_priority_queue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        from Queue import PriorityQueue
        visited = set()
        queue = PriorityQueue()
        queue.put((matrix[0][0], (0, 0)))
        visited.add((0, 0))
        while k and queue:
            res, d = queue.get()
            r, c = d
            k -= 1
            if r + 1 < n and (r + 1, c) not in visited:
                visited.add((r + 1, c))
                queue.put((matrix[r + 1][c], (r + 1, c)))
            if c + 1 < n and (r, c + 1) not in visited:
                visited.add((r, c + 1))
                queue.put((matrix[r][c + 1], (r, c + 1)))
        return res

# @lc code=end

