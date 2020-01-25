#
# @lc app=leetcode.cn id=232 lang=python
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        temp = []
        while self.stack:
            temp.append(self.stack.pop())
        self.stack.append(x)
        while temp:
            self.stack.append(temp.pop())
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stack.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return False if len(self.stack) else True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

