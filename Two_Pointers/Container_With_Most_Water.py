"""
### Question : 
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
"""

# Topic - Two strings 

def Container_with_Most_water(height : list[int]) -> int : 
    max_area = 0
    right = len(height) - 1
    left = 0 

    while left < right : 
        curr_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, curr_area)
        if height[left] < height[right]:
            left += 1
        else : 
            right -=1 
    return max_area


height = [1,8,6,2,5,4,8,3,7]
result = Container_with_Most_water(height=height)
print(f'The input list is : {height}')
print(f'The maximum amount of water a container can store is {result}')