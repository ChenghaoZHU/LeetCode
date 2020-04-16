#
# @lc app=leetcode.cn id=804 lang=python
#
# [804] 唯一摩尔斯密码词
#

# @lc code=start
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        counter = set()
        translations = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            tmp = ''
            for ch in word:
                tmp += translations[ord(ch) - ord('a')]
            counter.add(tmp)
        return len(counter)
        
# @lc code=end

