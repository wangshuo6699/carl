class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hash_map = {}
        while(1):
            n = self.getSum(n)
            if n==1:
                return True
            else:
                if n not in hash_map:
                    hash_map.add(n)
                else:
                    return False
        
    def getSum(self, n):
        res = 0
        while(n):
            res += (n%10)**2
            n //= 10
        return res

solution = Solution()
res = solution.getSum(19)
print(res)
