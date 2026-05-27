# Find peak element - which is basically greater than both of its neighbour and any one peak element from the list

def Peak_element(array):
    length = len(array)
    L = 0
    R = length - 1 
    while L <= R :
        middle = L + (R-L)//2
        if middle==0 and array[middle]>array[1]: return f'Index 0'
        elif middle == length-1 and array[middle]>array[middle-1]: return f'Last index - {middle}'
        elif array[middle]>array[middle-1] and array[middle]>array[middle+1]:
            return f"The index is {middle} and element is {array[middle]}"
        else : 
            L+=1 
            R+=1
    return False

print(Peak_element([2,3,4,5,6,6,6,9,5]))