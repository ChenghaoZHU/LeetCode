#
# @lc app=leetcode.cn id=225 lang=python
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.count = 0
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        self.count += 1


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        temp = []
        while len(self.queue) > 1:
            temp.append(self.queue.pop(0))
        
        res = self.queue.pop(0)
        while temp:
            self.queue.append(temp.pop(0))
        self.count -= 1
        return res
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        temp = []
        while len(self.queue) > 1:
            temp.append(self.queue.pop(0))
        
        res = self.queue.pop(0)
        while temp:
            self.queue.append(temp.pop(0))
        self.queue.append(res)
        return res


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return False if self.count else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

