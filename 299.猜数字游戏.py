#
# @lc app=leetcode.cn id=299 lang=python
#
# [299] 猜数字游戏
#

# @lc code=start
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        from itertools import izip
        all_nums = set()
        sec_nums = collections.defaultdict(int)
        gue_nums = collections.defaultdict(int)
        an = 0
        bn = 0
        for i, j in izip(secret, guess):
            if i == j: an += 1
            else:
                all_nums.add(i)
                sec_nums[i] += 1
                all_nums.add(j)
                gue_nums[j] += 1

        for n in all_nums:
            bn += min(sec_nums[n], gue_nums[n])
        
        return '%sA%sB' % (an, bn)
        
# @lc code=end

