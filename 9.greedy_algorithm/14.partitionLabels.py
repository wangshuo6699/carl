class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        from collections import defaultdict
        char_indexs = defaultdict(list)
        for i, c in enumerate(s):
            char_indexs[c].append(i+1)
        indexs = [[v[0], v[-1]] for k, v in char_indexs.items()]
        indexs = sorted(indexs, key=lambda x: x[0])
        i = 1
        result = [0]
        while i<len(indexs):
            if indexs[i][0]<indexs[i-1][1]:
                indexs[i][1] = max(indexs[i-1][1], indexs[i][1])
            else:
                result.append(indexs[i-1][-1]-sum(result))
            i+=1
        result.append(indexs[-1][-1]-sum(result))
        result.pop(0)
        return result


solution = Solution()
res = solution.partitionLabels(s="ababcbacadefegdehijhklij")
print(res)
