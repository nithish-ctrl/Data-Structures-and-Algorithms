# Shortest Job First 
def Shortest_job_first(array):
    array.sort()
    waiting_time = 0
    time_array = []
    for element in array[:-1]: #Last one does not have to considered since first one has 0 waiting time
        waiting_time = waiting_time + element
        time_array.append(waiting_time)
    average = sum(time_array)/len(array)
    return average

'''
jobs = [3, 1, 4, 2, 5]
print(Shortest_job_first(jobs))

jobs = [4, 3, 7, 1, 2]
print(Shortest_job_first(jobs))
'''
