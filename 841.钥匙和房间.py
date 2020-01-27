#
# @lc app=leetcode.cn id=841 lang=python
#
# [841] 钥匙和房间
#

# @lc code=start
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        keys = set([0])
        stack = [rooms[0]]
        while stack:
            rks = stack.pop()
            for k in (set(rks) - keys):
                stack.append(rooms[k])
            keys.update(rks)
            if len(keys) == len(rooms): return True

        return False

# @lc code=end

