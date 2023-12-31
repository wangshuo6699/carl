class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = 0
        cur_sum, total_sum = 0, 0
        for i in range(len(gas)):
            cur_sum += gas[i] - cost[i]
            total_sum += gas[i] - cost[i]
            if cur_sum<0:
                start = i+1
                cur_sum = 0
        if total_sum<0:
            return -1
        return start
