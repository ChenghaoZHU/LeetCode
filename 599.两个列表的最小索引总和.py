#
# @lc app=leetcode.cn id=599 lang=python
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = []
        mapping = {s: i  for i, s in enumerate(list1)}
        min_val = 2000
        for i, s in enumerate(list2):
            if s in mapping:
                t = i + mapping[s]
                if t < min_val:
                    min_val = t
                    res = [s]
                elif t == min_val:
                    res.append(s)
        return res
        
# @lc code=end

