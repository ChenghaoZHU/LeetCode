#
# @lc app=leetcode.cn id=146 lang=python
#
# [146] LRU缓存机制
#

# @lc code=start
class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.data = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.data:
            return -1
        node = self.data[key]
        if node.prev != self.head:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.head.next.prev = node
            node.next = self.head.next
            self.head.next = node
            node.prev = self.head
            
        return node.val


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.data:
            self.data[key].val = value
            self.get(key)
            return
        if self.size == self.capacity:
            node = self.tail.prev
            self.tail.prev = node.prev
            node.prev.next = self.tail
            del self.data[node.key]
            self.size -= 1
        self.size += 1
        self.data[key] = Node(key, value)
        node = self.data[key]
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

