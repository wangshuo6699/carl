class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        int_n = []
        while n:
            int_n.insert(0, n%10)
            n = n//10
        if len(int_n)<=1:
            return n
        for i in range(len(int_n)-1, 0, -1):
            if int_n[i-1] > int_n[i]:
                int_n[i-1] -= 1
                int_n[i:] = [9]*len(int_n[i:])
        return int(''.join(map(str,int_n)))


solution = Solution()
res = solution.monotoneIncreasingDigits(n = 101)
print(res)
