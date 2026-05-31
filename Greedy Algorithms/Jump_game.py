
def jump_game(arr):
    target_index = len(arr)-1
    for i,idx in enumerate(arr):
        if i + idx > target_index and i == len(arr)-1:
            return False
        elif i+idx == target_index:
            return True
    return False

'''
nums = [2, 3, 1, 0, 4]
print(jump_game(nums))

nums = [3, 2, 1, 0, 4]
print(jump_game(nums))

nums = [1,2]
print(jump_game(nums))

nums = [3,2]
print(jump_game(nums))

nums = [1,3,2,4,5]
print(jump_game(nums))
'''