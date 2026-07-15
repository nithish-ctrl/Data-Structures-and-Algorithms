''' 
Fixed or variable length
Window = (Right-Left)+1

'''

## General Template for sliding window problems 

def Sliding_window(input_string):
    left = 0 
    max_length = 0
    length = len(input_string)
    condition = "The actual condition that needs to be satisfied for the window to be valid"

    for right in range(length):
        while not condition : 
            left += 1
        
        max_length = max(max_length, (right-left+1))
    return max_length
