# Binary Search using recursion
def recursive_binary_search(target, array, L, R):
    while L <= R :
        middle = L + (R-L)//2
        if array[middle] == target : return middle
        elif array[middle] < target : 
            L = middle + 1
            return recursive_binary_search(target, array, L, R)
        else : 
            R = middle - 1
            return recursive_binary_search(target, array, L, R)
        
    return False
    
print(recursive_binary_search(9, [2,3,4,5,6,6,6,7,9], 0, 8))