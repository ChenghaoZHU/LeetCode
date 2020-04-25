#
# @lc app=leetcode.cn id=383 lang=python
#
# [383] 赎金信
#

# @lc code=start
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counter = collections.Counter(ransomNote)
        counter.subtract(magazine)
        return all(v <= 0 for k, v in counter.iteritems())
        
# @lc code=end

