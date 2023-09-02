class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n>=0:
            res = self.powModule(x, n)
        else:
            res = 1/self.powModule(x, -n)
        return res

    
    def powModule(self, x, n):
        if n==0:
            return 1
        if n==1:
            return x
        y = self.powModule(x, n//2)
        if n%2==1:
            return x*y*y
        else:
            return y*y

solution = Solution()
res = solution.myPow(x = 2.00000, n = -2)
print(res)
