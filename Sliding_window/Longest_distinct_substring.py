
def Longest_distinct_substring(input_string):
    left = 0
    longest = 0
    length = len(input_string)
    sett = []
    for r in range(length):
        if input_string[r] not in sett:
            sett.append(input_string[r])
            longest = max(longest, r-left+1)
        else : 
            while input_string[r] in sett:
                sett.remove(input_string[left])
                left+=1
            sett.append(input_string[r])
    return longest

input_str = "abcdeaa"
print(Longest_distinct_substring(input_str))
