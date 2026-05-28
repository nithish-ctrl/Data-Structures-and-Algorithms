
def Longest_distinct_substring(input_string):
    left = 0
    longest = 0
    length = len(input_string)
    sett = []
    for r in range(length):
        while input_string[r] in sett : 
            left+=1
            break
        w = (r-left)+1
        longest = max(longest,w)
        sett.append(input_string[r])
    return longest

input_str = "abcdeaa"
print(Longest_distinct_substring(input_str))
