# Assuming the list is sorted
def binary_search(target, given_list):
    length = len(given_list)
    L = 0
    R = length - 1
    while L<=R : 
        middle = L + (R-L)//2
        if given_list[middle] == target : return middle
        elif given_list[middle]<target:
            L = middle + 1
        else : 
            R = middle - 1
    return False


print(binary_search(9, [2,3,4,5,6,6,6,7,9]))
