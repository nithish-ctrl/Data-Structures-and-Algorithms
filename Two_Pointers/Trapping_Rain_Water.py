"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.
"""

# Topic - Two Pointers, array

def Trapping_Rain_Water(height : list[int]) -> int:
    left, right = 0, len(height) -1
    leftMax, rightMax, totalWater = 0,0,0

    while left < right : 
        leftMax = max(leftMax, height[left])
        rightMax = max(rightMax, height[right])

        if leftMax < rightMax : 
            totalWater += leftMax - height[left]
            left += 1
        else : 
            totalWater += rightMax - height[right]
            right -= 1 
    return totalWater

height = [0,1,0,2,1,0,1,3,2,1,2,1]
result = Trapping_Rain_Water(height = height)
print(f'The input list of heights is : {height}')
print(f'The total amount of water that can be trapped is : {result}')