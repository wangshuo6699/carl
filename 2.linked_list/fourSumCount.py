class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        from collections import defaultdict
        res_dict = defaultdict(int)
        for a in nums1:
            for b in nums2:
                res_dict[0-(a+b)] += 1
        count = 0
        for c in nums3:
            for d in nums4:
                count += res_dict.get(c+d, 0)
        return count


solution = Solution()
solution.fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2])
