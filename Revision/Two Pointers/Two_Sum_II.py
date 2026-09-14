

def TwoSumII(nums, target):
    left, right = 0, len(nums)-1
    while left < right :
        summ = nums[left] + nums[right]
        if summ == target : 
            return [left + 1, right + 1]
        elif summ < target : 
            left += 1
        else : 
            right -= 1
    return -1

numbers = [2,7,11,15]
target = 9
print(TwoSumII(numbers, target))