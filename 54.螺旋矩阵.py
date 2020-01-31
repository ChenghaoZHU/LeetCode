#
# @lc app=leetcode.cn id=54 lang=python
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        rows, cols = len(matrix), len(matrix[0])
        if rows == 1: return matrix[0]
        if cols == 1: return sum(matrix, [])
        rl, rr = 1, rows  # 行左边界，行右边界
        cl, cr = 0, cols  # 列左边界，列右边界
        rd, cd = 1, 1     # 移动方向（行、列）
        flag = True       # True移动列，False移动行
        result = []
        x, y = 0, 0
        while 1:
            if flag:  # 移动列
                if cl == cr: break
                if cd == 1:
                    while y < cr:
                        result.append(matrix[x][y])
                        y += cd
                    y -= cd
                    x += rd
                    cr -= 1
                else:
                    while y >= cl:
                        result.append(matrix[x][y])
                        y += cd
                    y -= cd
                    x += rd
                    cl += 1
                flag, cd = not flag, -cd
            else:  # 移动行
                if rl == rr: break
                if rd == 1:
                    while x < rr:
                        result.append(matrix[x][y])
                        x += rd
                    x -= rd
                    y += cd
                    rr -= 1
                else:
                    while x >= rl:
                        result.append(matrix[x][y])
                        x += rd
                    x -= rd
                    y += cd
                    rl += 1
                flag, rd = not flag, -rd
        return result

# @lc code=end

