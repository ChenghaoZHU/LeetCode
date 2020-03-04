#
# @lc app=leetcode.cn id=707 lang=python
#
# [707] 设计链表
#

# @lc code=start
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def get_node(self, index):
        if index >= self.size:
            return None
        if index <= self.size / 2:
            p = self.head
            while index >= 0:
                p = p.next
                index -= 1
        else:
            p = self.tail
            index = self.size - index - 1
            while index >= 0:
                p = p.prev
                index -= 1
        return p

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        node = self.get_node(index)
        return node.val if node else -1
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(val)
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.size += 1
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(val)
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        node.next = self.tail
        self.size += 1
        
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
        else:
            node = Node(val)
            target = self.get_node(index)
            node.prev = target.prev
            target.prev.next = node
            target.prev = node
            node.next = target
            self.size += 1
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        node = self.get_node(index)
        if node:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

