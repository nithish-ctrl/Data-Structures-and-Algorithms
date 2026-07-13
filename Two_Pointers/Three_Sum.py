"""
### Question :
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets. 
"""

# Topic - Two Pointers, String 

def threeSum(nums : list[int]) -> list[list[int]] :
    nums.sort()
    result = []

    for i in range(len(nums)): 
        if i>0 and nums[i] ==nums[i-1] : 
            continue 

        j = i + 1 
        k = len(nums) - 1 
        while j < k :
            total = nums[i] + nums[j] + nums[k]
            if total < 0 : 
                j += 1
            elif total > 0 : 
                k -= 1
            else : 
                result.append([nums[i], nums[j], nums[k]])
                j += 1

                while j < k and nums[j] == nums[j-1]:
                    j += 1 
    return result

nums = [-1,0,1,2,-1,-4]
result = threeSum(nums=nums)
print(f'The input list is : {nums}')
print(f'The unique triplets in the list which gives the sum of zero are : {result}') 
