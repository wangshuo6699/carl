import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_count = Counter(nums)
        pri_que = []
        for num, freq in nums_count.items():
            heapq.heappush(pri_que, (freq, num))
            if len(pri_que)>k:
                heapq.heappop(pri_que)
        
        result = [0]*k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result


solution = Solution()
res = solution.topKFrequent(nums=[1,1,1,2,2,3], k=2)
print(res)
