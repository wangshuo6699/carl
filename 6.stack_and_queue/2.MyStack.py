from collections import deque

class MyStack(object):

    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue_in.append(x)


    def pop(self):
        """
        :rtype: int
        """


    def top(self):
        """
        :rtype: int
        """


    def empty(self):
        """
        :rtype: bool
        """



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()