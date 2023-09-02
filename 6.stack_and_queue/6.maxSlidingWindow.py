from collections import deque

class myDeque:
    def __init__(self):
        self.deque = deque([])
    
    def push(self, value):
        while self.deque and self.deque[-1]<value:
            self.deque.pop()
        self.deque.append(value)

    def pop(self, value):
        if self.deque and self.front()==value:
            self.deque.popleft()

    def front(self):
        return self.deque[0]

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        mydeque = myDeque()
        for num in nums[:k]:
            mydeque.push(num)
        res.append(mydeque.front())
        for i in range(k, len(nums)):
            mydeque.pop(nums[i-k])
            mydeque.push(nums[i])
            res.append(mydeque.front())
        return res

solution = Solution()
res = solution.maxSlidingWindow(nums=[1,3,-1,-3,5,3,6,7], k=3)
print(res)
