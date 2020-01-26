#
# @lc app=leetcode.cn id=733 lang=python
#
# [733] 图像渲染
#

# @lc code=start
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols = len(image[0])
        visited = set()
        stack = [(sr, sc)]
        originColor = image[sr][sc]
        while stack:
            r, c = stack.pop()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            image[r][c] = newColor
            if r - 1 >= 0 and image[r - 1][c] == originColor:
                stack.append((r - 1, c))
            if c + 1 < cols and image[r][c + 1] == originColor:
                stack.append((r, c + 1))
            if r + 1 < rows and image[r + 1][c] == originColor:
                stack.append((r + 1, c))
            if c - 1 >= 0 and image[r][c - 1] == originColor:
                stack.append((r, c - 1))
        return image
        
# @lc code=end

