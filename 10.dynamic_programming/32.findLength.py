class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        max_num = 0
        dp = [[0]*(len(nums1)+1) for _ in range(len(nums2)+1)]
        for i in range(1, len(nums2)+1):
            for j in range(1, len(nums1)+1):
                if nums1[j-1]==nums2[i-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    max_num = max(max_num, dp[i][j])
        return max_num

solution = Solution()
res = solution.findLength([1,2,3,2,1], [3,2,1,4,7])
print(res)
