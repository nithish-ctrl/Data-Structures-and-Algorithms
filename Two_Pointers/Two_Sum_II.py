"""
Question : 
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.
"""

# Topic - Two Pointers, Array

def TwoSum_II(numbers : list[int], target : int) -> list[int]:
    left, right = 0, len(numbers)-1

    while left<right:
        if target == numbers[left] + numbers[right]:
            return [left+1, right+1]
        elif target < numbers[left] + numbers[right]:
            right -= 1
        else : 
            left += 1
    return []

num = [2,3,4,5,7,8,9]
target = 9
result = TwoSum_II(numbers = num, target= target)
print(f'The input list is : {num} and the target is {target}')
print(f'The indices of the two numbers such that they add up to the target are : {result} acc to 1 based indexing')
