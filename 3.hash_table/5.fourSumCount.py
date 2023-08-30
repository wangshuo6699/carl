from collections import defaultdict

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        res = 0
        count_dict = defaultdict(lambda: 0)
        for i in nums1:
            for j in nums2:
                count_dict[i+j] += 1
        for i in nums3:
            for j in nums4:
                if -(i+j) in count_dict:
                    res += count_dict[-(i+j)]
        return res
                

solution = Solution()
res = solution.fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2])
print(res)
