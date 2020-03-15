#
# @lc app=leetcode.cn id=705 lang=python
#
# [705] 设计哈希集合
#

# @lc code=start
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_len = 769
        self.data = [[] for _ in xrange(self.hash_len)]
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key): return
        self.data[key % self.hash_len].append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            self.data[key % self.hash_len].remove(key)
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.data[key % self.hash_len]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

