def search_value(nums, val):
    i, j = 0, len(nums)
    while i<j:
        mid = (i+j)//2
        if nums[mid]<val:
            i = mid+1
        elif nums[mid]>val:
            j = mid
        else:
            return mid
    return -1

res = search_value([-1,0,3,5,9,12], 2)
print(res)
