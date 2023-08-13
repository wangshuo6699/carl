
def square(nums):
    result = []
    i, j, k = 0, len(nums)-1, len(nums)-1
    while i <= j:
        if nums[i]*nums[i] < nums[j]*nums[j]:
            result.insert(0, nums[j]*nums[j])
            j -= 1
        else:
            result.insert(0,nums[i]*nums[i])
            i += 1
    return result


res = square([-7,-3,2,3,11])
print(res)