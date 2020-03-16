#
# @lc app=leetcode.cn id=706 lang=python
#
# [706] 设计哈希映射
#

# @lc code=start
class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None  

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = 10000
        self.m = 2069
        self.data = [Node(None, None) for _ in xrange(self.bucket)]
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        idx = key % self.m
        p = self.data[idx]
        while p.next:
            if p.next.key == key:
                p.next.val = value
                return 
            p = p.next
        p.next = Node(key, value)

        
    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        idx = key % self.m
        p = self.data[idx].next
        while p:
            if p.key == key:
                return p.val
            p = p.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        idx = key % self.m
        p = self.data[idx]
        while p and p.next:
            if p.next.key == key:
                p.next = p.next.next
            p = p.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

