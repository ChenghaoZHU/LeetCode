#
# @lc app=leetcode.cn id=500 lang=python
#
# [500] 键盘行
#

# @lc code=start
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = [
            set('qwertyuiop'),
            set('asdfghjkl'),
            set('zxcvbnm')
        ]

        res = []
        for i in words:
            for l in keyboard:
                if set(i.lower()) - l:
                    continue
                res.append(i)
                break
        return res
        
# @lc code=end

