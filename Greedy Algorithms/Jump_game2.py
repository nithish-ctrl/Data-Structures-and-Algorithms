
def Jump_game2(arr):
    target_index = len(arr)-1
    count = 0
    for i, idx in enumerate(arr):
        if i + idx == target_index:
            count+=1
            return count
        elif i+idx > target_index : 
            count=0
            return False
        else : 
            count+=1
    return False

'''
nums = [2, 3, 1, 0, 4]
print(Jump_game2(nums))

nums = [3, 2, 1, 0, 4]
print(Jump_game2(nums))

nums = [2, 3, 0, 1, 4]
print(Jump_game2(nums))

nums = [3,2]
print(Jump_game2(nums))

nums = [2, 3, 1, 1, 4]
print(Jump_game2(nums))
'''
