class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        hash_map = {}
        for num in nums1:
            hash_map[num] = hash_map.get(num, 0) + 1
        for num in nums2:
            if num in hash_map:
                res.append(num)
                del hash_map[num]
        return res

solution = Solution()
res = solution.intersection(nums1=[1,2,2,1], nums2=[2,2])
print(res)
