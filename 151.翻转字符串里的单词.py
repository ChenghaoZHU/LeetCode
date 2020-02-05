#
# @lc app=leetcode.cn id=151 lang=python
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # strip spaces
        if not s: return s
        s = list(s)
        sp, fp = 0, 0
        in_word = False
        while fp < len(s):
            if s[fp] != ' ':
                if not in_word: in_word = True
                s[sp], s[fp] = s[fp], s[sp]
                sp += 1
            else:
                if in_word: 
                    in_word = False
                    sp += 1
            fp += 1
        # cut the tail of spaces
        fp = len(s) - 1
        while fp >= 0 and s[fp] == ' ':
            fp -= 1
        s = s[:fp + 1]
        # reverse the char array
        self.reverse_str(0, len(s) - 1, s)
        
        # reverse the words
        sp, fp = 0, 0
        while fp < len(s):
            while fp < len(s) and s[fp] != ' ':
                fp += 1
            self.reverse_str(sp, fp - 1, s)
            fp += 1
            sp = fp

        return ''.join(s)
    
    def reverse_str(self, sp, fp, s):
        while sp < fp:
            s[sp], s[fp] = s[fp], s[sp]
            sp += 1
            fp -= 1

                
# @lc code=end

