
def min_length1(nums, val):
    result = nums
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1, 1):
            if sum(nums[i:j]) >= val:
                if len(nums[i:j]) < len(result):
                    result = nums[i:j]
    return result

def min_length2(nums, val):
    sum = 0
    i, j = 0, 0 
    result = len(nums)
    for j in range(len(nums)):
        sum += nums[j]
        while sum >= val:
            result = min(result, j-i+1)
            sum -= nums[i]
            i += 1
    return result


res = min_length2([2,3,1,2,4,3], 7)
print(res)
