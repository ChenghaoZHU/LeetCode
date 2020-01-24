#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mp = {}
        for s in strs:
            k = ''.join(sorted([i for i in s]))
            if k in mp:
                mp[k].append(s)
            else:
                mp[k] = [s]
        return [mp[k] for k in mp]
        
# @lc code=end

