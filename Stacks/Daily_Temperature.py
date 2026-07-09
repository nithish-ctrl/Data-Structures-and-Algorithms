"""
## Question :
Given an array of integers temperatures represents the daily temperatures, return an array answer such 
that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

# topics - monotonic stack

def daily_temperature(temp_list) : 
    temp_stack = []
    results = [0] * len(temp_list)

    for idx, temp in enumerate(temp_list) : 
        while temp_stack and temp > temp_list[temp_stack[-1]] : 
            index = temp_stack.pop()
            results[index] = idx - index
        temp_stack.append(idx)
    return results

temperatures = [73,74,75,71,69,72,76,73]
print(f' The input temperature list is : {temperatures}')
print(f' The number of days to wait for a warmer temperature is : {daily_temperature(temperatures)}')