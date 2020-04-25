#
# @lc app=leetcode.cn id=1309 lang=python
#
# [1309] 解码字母到整数映射
#

# @lc code=start
class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        trans = {str(i + 1): chr(ord('a') + i) for i in xrange(26)}

        res = []
        t = ''
        for ch in s:
            if ch == '#':
                res.append(''.join(map(lambda x: trans.get(x, ''), t[:-2])) + trans[t[-2:]])
                t = ''
            else:
                t += ch
        res.append(''.join(map(lambda x: trans.get(x, ''), t)))
        return ''.join(res)

# @lc code=end

