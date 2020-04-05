#
# @lc app=leetcode.cn id=460 lang=python
#
# [460] LFU缓存
#

# @lc code=start
class ListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.freq = 1
        self.prev = None
        self.next = None

def init_linked_list():
    head = ListNode(None, None)
    tail = ListNode(None, None)
    head.next = tail
    tail.prev = head
    return head, tail

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.keys = {}
        self.freqs = collections.defaultdict(init_linked_list)
        self.capacity = capacity
        self.size = 0
        self.min_freq = 1

    def _evict(self):
        _, tail = self.freqs[self.min_freq]
        node = tail.prev
        self.keys.pop(node.key)
        tail.prev = node.prev
        tail.prev.next = tail
        self.size -= 1

    def _insert(self, node):
        head, _ = self.freqs[node.freq]
        node.prev = head
        node.next = head.next
        head.next = node
        node.next.prev = node
    
    def _increase(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        if node.prev.key is None and node.next.key is None:
            if self.min_freq == node.freq:
                self.min_freq = node.freq + 1
        node.freq += 1
        self._insert(node)

    def get(self, key):
        node = self._get(key) 
        if node is not None:
            return node.val
        return -1

    def _get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.keys:
            node = self.keys[key]
            self._increase(node)
            return node
        return None
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return  # 不能装任何元素

        node = self._get(key)
        if not node:
            node = ListNode(key, value)
            self.keys[key] = node
            if self.size == self.capacity:
                self._evict()
            self.min_freq = 1
            self._insert(node)
            self.size += 1
        else:
            node.val = value

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

