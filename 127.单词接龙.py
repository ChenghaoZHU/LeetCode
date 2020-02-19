#
# @lc app=leetcode.cn id=127 lang=python
#
# [127] 单词接龙
#

# @lc code=start
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        queue = [(beginWord, 1)]
        visited = set()
        L = len(beginWord)
        all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
                
        while queue:
            word, depth = queue.pop(0)
            if word == endWord: return depth
            for i in range(L):
                key = word[:i] + "*" + word[i+1:]
                for w in all_combo_dict[key]:
                    if w not in visited:
                        queue.append((w, depth + 1))
                        visited.add(w)
                all_combo_dict[key] = []  # 之后的访问路径长度肯定大于之前的访问，所以置空，避免不必要的计算
        return 0
# @lc code=end

