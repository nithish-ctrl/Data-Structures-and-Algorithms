"""
## Question - car fleet : 
There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.
A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
A car fleet is a single car or a group of cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.
If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
Return the number of car fleets that will arrive at the destination.
"""

# Topics - Monostatic Stack, Sorting

def Car_fleet(target, position, speed) : 
    # Only the cars in the behind can catch up to the cars in front of them. 
    time_stack = [float(target-p)/s for p,s in sorted(zip(position, speed))]
    result = current = 0 
    for time in time_stack[::-1] : 
        if time > current : 
            result += 1 
            current = time
    return result

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(f'The number of car fleets that will arrive at the destination {Car_fleet(target, position, speed)}')
